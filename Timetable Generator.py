import pandas as pd

# convert pdf to word -> https://www.ilovepdf.com/pdf_to_word
# convert word to excel -> https://online2pdf.com/convert-word-to-excel
# convert excel to csv

def sections(df, codes, section):
    s_dict = {k: {d:'' for d in days} for k in df.columns[2:]}
    for i in range(len(df)):
        day = df.iloc[i]['Day']
        if not isinstance(day, float):
            for col in df.columns[2:]:
                try:
                    data = str(df.iloc[i][col]).split('(')
                    code = data[0].strip()
                    s = '(' + data[1]
                    s += ')' if s[-1] != ')' else ''
                    course_name = codes[code]
                    if s == section and code in codes:
                        lab = ' Lab' if 'Lab' in df.iloc[i]['Venue'] and 'Lab' not in course_name else ''
                        s_dict[col][day] += course_name + lab + ' & '
                except:
                    continue

    for k, v in s_dict.items():
        for value in v:
            s_dict[k][value] = s_dict[k][value][:-3]

    final_output = pd.DataFrame(s_dict).fillna('-')
    final_output.to_csv(f'Section {section[2]} Timetable.csv')


course_codes = {
    'CS3433': 'Parallel and Distributed Computing',
    'CS4813': 'Artificial Intelligence',
    'CS4811': 'Artificial Intelligence Lab',
    'ACCS3003': 'Financial Accounting',
    'CS4883': 'Introduction to Data Science',
    'CS3193': 'Web Application Development',
    'CS3833': 'Theory of Programming Languages'
}

df = pd.read_csv('Untitled spreadsheet - Table 1.csv')
df = df.drop(columns=['18:00—19:20', '19:30—20:50'])
df['Day'].fillna(method='ffill', inplace=True)
df.dropna(subset=['Venue'], inplace=True)

for col in df.columns:
    if 'Unnamed' in col:
        df.drop(columns=[col], inplace=True)

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']


for sec in range(1, 6):
    sections(df, course_codes, f'(S{sec})')

print("\nSuccessfully created the timetable.")