import argparse
import sys

def statistics(dataTypeLoc,sortingTypeLoc,in_file_handle,out_file_handle):

    entries = dict()

    all_count = 0
    while True:
        try:
            data = in_file_handle.readline()

            if not data:
                break
            if dataTypeLoc == "long" or dataTypeLoc == "word":
                data_split = data.split()
            else:
                data_split = [data.strip('\n')]
            for entry_str in data_split:
                if dataTypeLoc == 'long':
                    try:
                        entry_str = int(entry_str)
                    except:
                        out_file_handle.write(f'{entry_str} is not a long and will be skipped.\n')
                        entry_str=""
                if not entries and entry_str:
                    entries = {entry_str: 1}
                    all_count += 1
                elif entry_str:
                    if entries.get(entry_str):
                        entries.update({entry_str: entries[entry_str] + 1})
                    else:
                        entries.update({entry_str: 1})
                    all_count += 1
        except EOFError:
            break
    if dataTypeLoc == 'long':
        out_file_handle.write(f'Total numbers: {all_count} .\n')
        x = sorted(entries.items(), key=lambda item: item[0])
        if sortingTypeLoc == "natural":
            out_string = str(x[0][0])
            for item in x[1:]:
                for i in range(item[1]):
                    out_string = out_string + " " + str(item[0])
            out_file_handle.write(f'Sorted data: {out_string}\n')
        else:
            y = sorted(x, key=lambda z: z[1])
            for item in y:
                out_file_handle.write(f'{item[0]}: {item[1]} time(s), {item[1]*100//all_count,0}%\n')
    elif dataTypeLoc == 'word':
        out_file_handle.write(f'Total words: {all_count}.\n')
        x = sorted(entries.items(), key=lambda item: item[0])
        if sortingTypeLoc == "natural":
            out_string = x[0][0]
            for item in x[1:]:
                for i in range(item[1]):
                    out_string = out_string + " " + item[0]
            out_file_handle.write(f'Sorted data: {out_string}\n')
        else:
            y = sorted(x, key=lambda z: z[1])

            for item in y:
                out_file_handle.write(f'{item[0]}: {item[1]} time(s), {item[1]*100//all_count,0}%\n')
    else:
        out_file_handle.write(f'Total lines: {all_count}.\n')
        x = sorted(entries.items(), key=lambda item: item[0])

        if sortingTypeLoc == "natural":
            out_file_handle.write('Sorted data:\n')
            for item in x:
                for i in range(item[1]):
                    out_file_handle.write(f'{item[0]}\n')
        else:
            y = sorted(x, key=lambda z: z[1])
            for item in y:
                out_file_handle.write(f'{item[0]}: {item[1]} time(s), {item[1] * 100 // all_count, 0}%\n')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Counting ints word or lines"
    )
    parser.add_argument("-dataType",
                        choices=['long', 'word', 'line'],
                        required=False, type=str,nargs = "?")
    parser.add_argument("-sortingType",
                        choices=['natural', 'byCount'],
                        required=False, type=str,nargs = "?")
    parser.add_argument("-inputFile",
                        required=False, type=str, nargs="?")
    parser.add_argument("-outputFile",
                        required=False, type=str, nargs="?")


    args, unknown = parser.parse_known_args()

    if args.inputFile:
        input_file_handle = open(args.inputFile, 'r')
    else:
        input_file_handle = sys.stdin
    if args.outputFile:
        output_file_handle = open(args.outputFile, 'w')
    else:
        output_file_handle = sys.stdout

    if unknown:
        for item in unknown:
            output_file_handle.write(f'{item} is not a valid parameter. It will be skipped.\n')
    if not args.sortingType:
        if '-sortingType' in sys.argv: # Option angegeben aber leer
            output_file_handle.write("No sorting type defined!")
            sys.exit()
        else:
            sortingType = "natural"
    else:
        sortingType = args.sortingType
    if not args.dataType:
        if '-dataType' in sys.argv:  # Option angegeben aber leer
            output_file_handle.write("No data type defined!")
            sys.exit()
        else:
            dataType = "long"
    else:
        dataType = args.dataType

    statistics(dataType,sortingType,input_file_handle,output_file_handle)
    output_file_handle.close()
    input_file_handle.close()