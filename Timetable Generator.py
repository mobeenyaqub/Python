import pandas as pd

# convert pdf to word -> https://www.ilovepdf.com/pdf_to_word
# convert word to excel -> https://online2pdf.com/convert-word-to-excel
# convert excel to csv
def clash_sections(s_dict, df, codes, section, clash_course):
    courses = {key:[False, []] for key in clash_course}
    data_hold = []

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
                    if s == section and code in codes and course_name in clash_course:
                        lab = ' Lab' if 'Lab' in df.iloc[i]['Venue'] and 'Lab' not in course_name else ''
                        lab += f' {s}'
                        if not s_dict[col][day]:
                            courses[course_name][1].append(col)
                            courses[course_name][1].append(day)
                            data_hold.append(course_name + lab)
                        else:
                            courses[course_name][0] = True
                except Exception as e:
                    continue

    new_data = []
    for key, value in courses.items():
        if not courses[key][0]:
            for d in data_hold:
                if key in d:
                    new_data.append(d)

    for key, value in courses.items():
        if not courses[key][0]:
            for v in range(0, len(value[1]), 2):
                s_dict[courses[key][1][v]][courses[key][1][v+1]] = new_data.pop(0)

    return s_dict

def sections(df, codes, section, for_clash=False, combine_section=None, clash_course=None):
    changed = False
    clash_found = False
    clashed_courses = set()
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
                        changed = True
                        lab = ' Lab' if 'Lab' in df.iloc[i]['Venue'] and 'Lab' not in course_name else ''
                        lab += f' {s}'
                        if len(s_dict[col][day]) > 0:
                            clash_found = True
                            clashed_courses.add(course_name)
                        if not for_clash:
                            s_dict[col][day] += course_name + lab + ' & '
                        else:
                            if not s_dict[col][day] and course_name not in clash_course:
                                s_dict[col][day] = course_name + lab

                except Exception as e:
                    continue

    if for_clash:
        s_dict = clash_sections(s_dict, df, codes, combine_section, clash_course)

    if changed:
        for k, v in s_dict.items():
            for value in v:
                if not for_clash:
                    s_dict[k][value] = s_dict[k][value][:-3]

        final_output = pd.DataFrame(s_dict).fillna('-')
        name = f'Section {section[2]}'
        name += f' & Section {combine_section[2]}' if for_clash else ''
        final_output.insert(0, name, days)
        final_output.to_csv(f'{name} Timetable.csv')

    return changed, clash_found, list(clashed_courses)


course_codes = {
    'CS3273': 'Human Computer Interaction',
    'CS4613': 'Machine Learning',
    'CS4623': 'Compiler Construction',
    'HMCS2013': 'Professional Ethics and Legal Issues',
    'MGCS4003': 'Entrepreneurship and Innovation'
}

df = pd.read_csv('TIMETABLE-CS-BSMSMSAI-Fall-23.csv')
df = df.drop(columns=['18:00—19:20', '19:30—20:50'])
df['Day'].fillna(method='ffill', inplace=True)
df.dropna(subset=['Venue'], inplace=True)

for col in df.columns:
    if 'Unnamed' in col:
        df.drop(columns=[col], inplace=True)

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

check_clash = []
course_clash = []

for sec in range(1, 6):
    changed, clash_found, clashed_courses = sections(df, course_codes, f'(S{sec})')
    if changed:
        course_clash.append(clashed_courses)
        check_clash.append(clash_found)

for i in range(len(check_clash)):
    if check_clash[i]:
        for combine_section in range(1, len(check_clash) + 1):
            if i + 1 != combine_section:
                sections(df, course_codes, f'(S{i+1})', True, f'(S{combine_section})', course_clash[i])

print("\nSuccessfully created the timetable.")
