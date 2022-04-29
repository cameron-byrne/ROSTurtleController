#!/usr/bin/env python
import time

def await_commands():
    '''
    This will be a blocking function meant to take input as it is given from Minecraft.
    '''

    # This is sus! It's dependent on a particular save *and* a particular computer in that save
    path = "C:\\Users\\Cameron\\Documents\\curseforge\\minecraft\\mods\\Instances\\" \
           "ComputerCraftEducational\\saves\\Due Dilligence Test\\computer\\2\\controller_input"

    print(path)

    while True:
        time.sleep(.05)  # 50 ms delay between reads so computercraft actually gets a chance to write to file
        # TODO test with no delay

        # read file contents, continue if none
        file1 = open(path, "r")
        text_input = file1.read()
        file1.close()
        if text_input == "":
            continue

        # delete contents to prep for next message
        file1 = open(path, "w")
        file1.close()

        print(text_input)

def main():
    pass

if __name__ == "__main__":
    main()
