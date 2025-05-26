import sys
import os
import re
import ast
def add_problem(line_number_loc,problem_number_loc,problem_string_loc):
    global found_problems

    found_problems.update({100*line_number_loc+problem_number_loc: \
    problem_string_loc})

def check_too_long(line_loc,line_number_loc,filename_loc):
    if len(line_loc) > 79:
        problem_string = \
        f'{filename_loc}: Line {line_number_loc}: S001 Too long'
        add_problem(line_number_loc, 1,problem_string)
def check_indentation(line_loc,line_number_loc,filename_loc):
    line_stripped = line_loc.strip()
    if line_stripped:
        index=line_loc.find(line_stripped[0])
        chk_string = line_loc[0:index]
        count = 0
        for c in chk_string:
            if c == "\t":
                count += 4
            elif c == " ":
                count += 1
        if count % 4:
            problem_string = \
            f'{filename_loc}: Line {line_number_loc}: ' + \
            f'S002 Indentation is not a multiple of four'
            add_problem(line_number_loc, 2,problem_string)
def check_unnecessary_semicolon(line_loc,line_number_loc,filename_loc):
    split_at_comment = line_loc.split("#")
    before_comment = split_at_comment[0].strip()
    #print(line_number_loc,before_comment)
    if before_comment and before_comment[-1] == ";":
        problem_string = \
        f'{filename_loc}: Line {line_number_loc}: S003 Unnecessary semicolon'
        add_problem(line_number_loc, 3,problem_string)

def check_spaces_before_inline_comment(line_loc,line_number_loc,filename_loc):
    line_split = line_loc.split("#")
    if len(line_split) > 1:
        if not line_split[0]:
            pass
        elif len(line_split[0]) == 1 and line_split[0][-1] == "\t":
            pass
        elif len(line_split[0])> 1 and \
        (line_split[0][-1] == "\t" or line_split[0][-2] == "\t"):
            pass
        elif len(line_split[0])> 1 and \
        (line_split[0][-1] == " " and line_split[0][-2] == " "):
            pass
        else:
            problem_string = f'{filename_loc}: Line {line_number_loc}: ' + \
            f'S004 At least two spaces required before inline comments'
            add_problem(line_number_loc, 4,problem_string)
def find_to_do(line_loc,line_number_loc,filename_loc):
    line_split = line_loc.split("#")
    if len(line_split) > 1:
        comment = line_loc[len(line_split[0]):].lower()
        if comment.find("todo") != -1:
            problem_string = \
            f'{filename_loc}: Line {line_number_loc}: S005 TODO found'
            add_problem(line_number_loc, 5,problem_string)
def check_to_many_blanklines(empty_line_cnt_loc, line_number_loc,filename_loc):
    if empty_line_cnt_loc > 2:
        problem_string = f'{filename_loc}: Line {line_number_loc}: ' + \
        f'S006 More than two blank lines used before this line'
        add_problem(line_number_loc, 6,problem_string)
def check_too_may_spaces_after_class(line_loc,line_number_loc,filename_loc):
    pat = re.compile(r'class\s.*')
    x = re.search(pat, line_loc)
    if x:
        x = line_loc[x.start():x.end()]
        x=x.lstrip('class')
        y=x.lstrip()
        if len(y) + 1 < len(x):
            problem_string = f'{filename_loc}: Line {line_number_loc}: ' + \
            f'S007 Too many spaces after \'class\''
            add_problem(line_number_loc, 7,problem_string)
    pat = re.compile(r'def\s.*')
    x = re.search(pat, line_loc)
    if x:
        x = line_loc[x.start():x.end()]
        x = x.lstrip('def')
        y = x.lstrip()
        if len(y) + 1 < len(x):
            problem_string = f'{filename_loc}: Line {line_number_loc}: ' + \
            f'S007 Too many spaces after \'def\''
            add_problem(line_number_loc, 7,problem_string)
def check_class_camel_case(line_loc,line_number_loc,filename_loc):
    pat = re.compile(r'class\s.*')
    x = re.search(pat, line_loc)
    if x:
        x = line_loc[x.start():x.end()].split("(")[0]
        x=x.lstrip('class').strip()
        x = x.rstrip(':')
        if x[0].lower() == x[0]:
            problem_string = f'{filename_loc}: Line {line_number_loc}: ' + \
            f'S008 Class name {x} should use CamelCase'
            add_problem(line_number_loc, 8,problem_string)

def check_def_snake_case(line_loc,line_number_loc,filename_loc):
    pat = re.compile(r'def\s.*')
    x = re.search(pat, line_loc)

    if x:
        x = line_loc[x.start():x.end()].split("(")[0]
        x=x.lstrip('def').strip()
        x = x.rstrip(':')
        if x.lower() != x:
            problem_string = f'{filename_loc}: Line {line_number_loc}: ' + \
            f'S009 Function name {x} should use snake_case'
            add_problem(line_number_loc, 9,problem_string)
def check_problems_of_one_file(file_loc):
    global found_problems
    fp = open(file_loc, 'r')
    lines = fp.readlines()
    # Initialization
    found_problems ={}
    empty_line_cnt = 0
    for count, line in enumerate(lines):
        check_too_long(line.strip('\n'), count + 1,file_loc)  # 1
        check_indentation(line.strip('\n'), count + 1,file_loc)  # 2
        line_content = line.strip()
        if line_content:
            check_unnecessary_semicolon(line_content, count + 1,file_loc)  # 3
            check_spaces_before_inline_comment(line_content, count+1,file_loc)
            find_to_do(line_content, count + 1,file_loc)  # 5
            check_to_many_blanklines(empty_line_cnt, count + 1,file_loc)  #6
            # 7:
            check_too_may_spaces_after_class(line_content, count+1,file_loc)
            check_class_camel_case(line_content, count + 1,file_loc)  # 8
            check_def_snake_case(line_content, count + 1, file_loc)  # 9
            empty_line_cnt = 0
        else:
            empty_line_cnt += 1
    fp.close()
    fp = open(file_loc, 'r')
    script = fp.read()
    tree = ast.parse(script)

    already_mentioned_variables = set()
    already_ment_li_wi_mut_arg = set()

    nodes = ast.walk(tree)
    for node in nodes:
        if isinstance(node, ast.FunctionDef):
            for a in node.args.args:
                if a.arg.lower() != a.arg:
                    line_number = node.lineno
                    problem_string = (f'{file_loc}: Line {line_number}: ' +
                    f'S010 Argument name \'{a.arg}\' should be snake_case')
                    add_problem(line_number, 10,problem_string)

            for a in node.args.defaults:
                if not (node.lineno in already_ment_li_wi_mut_arg) \
                and \
(isinstance(a, ast.List) or isinstance(a, ast.Dict) or isinstance(a, ast.Set)):
                    already_mentioned_variables.add(node.lineno)
                    line_number = node.lineno
                    problem_string = f'{file_loc}: Line {line_number}: ' + \
                    f'S012 Default argument value is mutable'
                    add_problem(line_number, 12,problem_string)

        if isinstance(node, ast.Name):
            if not (node.id in already_mentioned_variables) and \
            node.id.lower() != node.id:
                already_mentioned_variables.add(node.id)
                line_number = node.lineno
                problem_string = f'{file_loc}: Line {line_number}: ' + \
                f'S011 Variable \'{node.id}\' in function should be snake_case'
                add_problem(line_number, 11, problem_string)

    for item in sorted(found_problems.items()):
        print(item[1])
    fp.close()

# The Main Routine


found_problems = {}
if len(sys.argv) == 1:
    print("Not enough arguments")
    sys.exit()
location = sys.argv[1]
filelist = []
if os.path.isdir(location):
    for dirpath, dirnames, filenames in os.walk(location):
        for filename in filenames:
            if filename.endswith(".py"):
                f_name = os.path.join(dirpath, filename)
                filelist.append(f_name)

elif os.path.isfile(location):
    if location.endswith(".py"):
        filelist.append(location)
else:
    sys.exit()
filelist.sort()
for file in filelist:
    check_problems_of_one_file(file)

