import datetime
import tkinter
import csv
import time
import os

root = tkinter.Tk()
root.geometry('605x454')  # ipad/tablet/monitor size


class main:
    """A program which records attendance and deduces if attendee has Covid due to consistence absence\'s
    Features:
    * keyboard for user interface
    * display User Input
    * Suggest possible Options using User Input (Binary Search?)
    * once entered to account Input pincode (Encryption?)
    * mark attendance --> store in csv
    * view previous attendance (with dates)

    Admin Features:
    * Access to attendance records
    * View all attended/not attended
    * Add/Remove attendees
    * Edit attendance records
    * Edit Username\'s
    * Veiw attendees with covid by calculating multiple absences (need to check if this was requested?)
    """

    def __init__(self):
        # configure grid
        root.columnconfigure(0, weight=1)
        # main containers
        self.display_frame = tkinter.Frame(master=root, borderwidth=1, relief='solid')
        self.keyboard_frame = tkinter.Frame(master=root)
        self.pinpad_frame = tkinter.Frame(master=root)

        # layout of main containers
        self.display_frame.grid(row=0, column=0, rowspan=1, sticky='NWNE')
        self.keyboard_frame.grid(row=2, column=0)

        self.display_frame.grid_columnconfigure(1, weight=1)
        self.display_frame.grid_columnconfigure(4, weight=1)
        # unique var display userInput
        self.lbl_str = tkinter.StringVar()
        self.lbl_str.set('Name:')
        self.lbl_value = ''
        # Toggle frame variables
        self.key_frame_off = False
        self.pin_frame_off = True

    def switch_frame(self):
        """ Switches Frames when certain events occur """
        if self.key_frame_off:
            self.keyboard_frame.grid_forget()

            if not self.pin_frame_off:
                self.pinpad_frame.grid(row=2, column=0)
                # runs second frame
                self.pinpad()


        elif not self.key_frame_off:
            self.keyboard_frame.grid(row=2, column=0)

            if self.pin_frame_off:
                self.pinpad_frame.grid_forget()

    def display(self):
        """Display of the Gui Will display User input and
        display list of options which share similaraties with the User Input"""
        # lbl that will display user input
        self.lbl_display_name = tkinter.Label(master=self.display_frame, textvariable=self.lbl_str)

        # second sub_container prompting names using lbl text
        self.frame_name_prompt = tkinter.Frame(master=self.display_frame, borderwidth=1, relief='solid')

        # layout of display frame
        self.lbl_display_name.grid(row=0, column=2, padx=120)
        self.frame_name_prompt.grid(row=0, column=4, columnspan=2, sticky='EW')

    def prompt_one(self, keyboard_pinpad):  # command's for suggestion buttons
        if keyboard_pinpad:
            self.lbl_value = self.lbl_text_one.get()
            self.lbl_str.set(self.lbl_text_one.get())
        else:
            root.quit()

    def prompt_two(self, keyboard_pinpad):  # command's for suggestion buttons
        if keyboard_pinpad:
            self.lbl_value = self.lbl_text_two.get()
            self.lbl_str.set(self.lbl_text_two.get())
        else:
            self.prompt_commands(self.prompt_attendance, True)

    def prompt_three(self, keyboard_pinpad):  # command's for suggestion buttons
        if keyboard_pinpad:
            self.lbl_value = self.lbl_text_three.get()
            self.lbl_str.set(self.lbl_text_three.get())
        else:
            self.prompt_commands(self.prompt_attendance, False)

    def name_prompt(self):
        """Displays all possible user suggestion"""
        # keyboard or pinpad
        self.key_pin_switch = True
        # var determines wether func skip's to suggested name or admit attendance
        self.prompt_attendance = False
        # text variables for bttns
        self.lbl_text_one = tkinter.StringVar()
        self.lbl_text_two = tkinter.StringVar()
        self.lbl_text_three = tkinter.StringVar()

        self.lbl_text_one.set('Suggestion 1')
        self.lbl_text_two.set('Suggestion 2')
        self.lbl_text_three.set('Suggestion 3')

        # creating all prompt labels
        self.lbl_prompt_one = tkinter.Button(master=self.frame_name_prompt, textvariable=self.lbl_text_one,
                                             command=lambda: self.prompt_one(self.key_pin_switch))
        self.lbl_prompt_two = tkinter.Button(master=self.frame_name_prompt, textvariable=self.lbl_text_two,
                                             command=lambda: self.prompt_two(self.key_pin_switch))
        self.lbl_prompt_three = tkinter.Button(master=self.frame_name_prompt, textvariable=self.lbl_text_three,
                                               command=lambda: self.prompt_three(self.key_pin_switch))

        # layout for prompts
        self.lbl_prompt_one.grid(row=0, column=0)
        self.lbl_prompt_two.grid(row=1, column=0)
        self.lbl_prompt_three.grid(row=2, column=0)

    def binary_search(self, sequence_list, item, name_prompt=False):
        start = 0
        end = len(sequence_list) - 1

        while start <= end:
            midpoint = start + (end - start) // 2
            midpoint_value = sequence_list[midpoint]

            if midpoint_value == item:
                return midpoint

            elif midpoint_value > item:
                end = midpoint - 1

            else:
                start = midpoint + 1

        if name_prompt:  # displays sugestions
            prompt_one = str(sequence_list[midpoint - 1]).strip('[]\'')
            prompt_two = str(sequence_list[midpoint]).strip('[]\'')
            prompt_three = str(sequence_list[midpoint + 1]).strip('[]\'')
            self.lbl_text_one.set(prompt_one)
            self.lbl_text_two.set(prompt_two)
            self.lbl_text_three.set(prompt_three)

        return None

    def display_prompts(self):  # displays sugestions
        self.search_name(f'[\'{self.lbl_value}\']', True)

    def prompt_commands(self, pinpad, admit_attendance_YN=None):  # todo name prompts
        '''bttn command either used to skip to suggested name or admit attendance'''
        if not pinpad:  # name prompt
            pass
        else:  # admit attendance
            self.admit_attendance(admit_attendance_YN)

    def search_name(self, name, prompt=False):
        with open('Attendance Record.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            search_list = []
            # get all items to be searched
            for line in csv_reader:
                search_list.append(line['Name'])

        return self.binary_search(search_list, name, prompt)

    def keyboard(self):

        """Key_Board of the GUI modifiable(ForeGround, BackGround, Width, Height)"""

        self.bttn_fg = 'black'
        self.bttn_bg = 'white'
        self.bttn_width = 6  # 605//9
        self.bttn_height = 3  # 20

        # creating all button for keyboard
        bttn_A = tkinter.Button(master=self.keyboard_frame, text='A', fg=self.bttn_fg, bg=self.bttn_bg,
                                width=self.bttn_width, height=self.bttn_height,
                                command=lambda: self.user_input('A'))
        bttn_B = tkinter.Button(master=self.keyboard_frame, text='B', fg=self.bttn_fg, bg=self.bttn_bg,
                                width=self.bttn_width, height=self.bttn_height,
                                command=lambda: self.user_input('B'))
        bttn_C = tkinter.Button(master=self.keyboard_frame, text='C', fg=self.bttn_fg, bg=self.bttn_bg,
                                width=self.bttn_width, height=self.bttn_height,
                                command=lambda: self.user_input('C'))
        bttn_D = tkinter.Button(master=self.keyboard_frame, text='D', fg=self.bttn_fg, bg=self.bttn_bg,
                                width=self.bttn_width, height=self.bttn_height,
                                command=lambda: self.user_input('D'))
        bttn_E = tkinter.Button(master=self.keyboard_frame, text='E', fg=self.bttn_fg, bg=self.bttn_bg,
                                width=self.bttn_width, height=self.bttn_height,
                                command=lambda: self.user_input('E'))
        bttn_F = tkinter.Button(master=self.keyboard_frame, text='F', fg=self.bttn_fg, bg=self.bttn_bg,
                                width=self.bttn_width, height=self.bttn_height,
                                command=lambda: self.user_input('F'))
        bttn_G = tkinter.Button(master=self.keyboard_frame, text='G', fg=self.bttn_fg, bg=self.bttn_bg,
                                width=self.bttn_width, height=self.bttn_height,
                                command=lambda: self.user_input('G'))
        bttn_H = tkinter.Button(master=self.keyboard_frame, text='H', fg=self.bttn_fg, bg=self.bttn_bg,
                                width=self.bttn_width, height=self.bttn_height,
                                command=lambda: self.user_input('H'))
        bttn_I = tkinter.Button(master=self.keyboard_frame, text='I', fg=self.bttn_fg, bg=self.bttn_bg,
                                width=self.bttn_width, height=self.bttn_height,
                                command=lambda: self.user_input('I'))
        bttn_J = tkinter.Button(master=self.keyboard_frame, text='J', fg=self.bttn_fg, bg=self.bttn_bg,
                                width=self.bttn_width, height=self.bttn_height,
                                command=lambda: self.user_input('J'))
        bttn_K = tkinter.Button(master=self.keyboard_frame, text='K', fg=self.bttn_fg, bg=self.bttn_bg,
                                width=self.bttn_width, height=self.bttn_height,
                                command=lambda: self.user_input('K'))
        bttn_L = tkinter.Button(master=self.keyboard_frame, text='L', fg=self.bttn_fg, bg=self.bttn_bg,
                                width=self.bttn_width, height=self.bttn_height,
                                command=lambda: self.user_input('L'))
        bttn_M = tkinter.Button(master=self.keyboard_frame, text='M', fg=self.bttn_fg, bg=self.bttn_bg,
                                width=self.bttn_width, height=self.bttn_height,
                                command=lambda: self.user_input('M'))
        bttn_N = tkinter.Button(master=self.keyboard_frame, text='N', fg=self.bttn_fg, bg=self.bttn_bg,
                                width=self.bttn_width, height=self.bttn_height,
                                command=lambda: self.user_input('N'))
        bttn_O = tkinter.Button(master=self.keyboard_frame, text='O', fg=self.bttn_fg, bg=self.bttn_bg,
                                width=self.bttn_width, height=self.bttn_height,
                                command=lambda: self.user_input('O'))
        bttn_P = tkinter.Button(master=self.keyboard_frame, text='P', fg=self.bttn_fg, bg=self.bttn_bg,
                                width=self.bttn_width, height=self.bttn_height,
                                command=lambda: self.user_input('P'))
        bttn_Q = tkinter.Button(master=self.keyboard_frame, text='Q', fg=self.bttn_fg, bg=self.bttn_bg,
                                width=self.bttn_width, height=self.bttn_height,
                                command=lambda: self.user_input('Q'))
        bttn_R = tkinter.Button(master=self.keyboard_frame, text='R', fg=self.bttn_fg, bg=self.bttn_bg,
                                width=self.bttn_width, height=self.bttn_height,
                                command=lambda: self.user_input('R'))
        bttn_S = tkinter.Button(master=self.keyboard_frame, text='S', fg=self.bttn_fg, bg=self.bttn_bg,
                                width=self.bttn_width, height=self.bttn_height,
                                command=lambda: self.user_input('S'))
        bttn_T = tkinter.Button(master=self.keyboard_frame, text='T', fg=self.bttn_fg, bg=self.bttn_bg,
                                width=self.bttn_width, height=self.bttn_height,
                                command=lambda: self.user_input('T'))
        bttn_U = tkinter.Button(master=self.keyboard_frame, text='U', fg=self.bttn_fg, bg=self.bttn_bg,
                                width=self.bttn_width, height=self.bttn_height,
                                command=lambda: self.user_input('U'))
        bttn_V = tkinter.Button(master=self.keyboard_frame, text='V', fg=self.bttn_fg, bg=self.bttn_bg,
                                width=self.bttn_width, height=self.bttn_height,
                                command=lambda: self.user_input('V'))
        bttn_W = tkinter.Button(master=self.keyboard_frame, text='W', fg=self.bttn_fg, bg=self.bttn_bg,
                                width=self.bttn_width, height=self.bttn_height,
                                command=lambda: self.user_input('W'))
        bttn_X = tkinter.Button(master=self.keyboard_frame, text='X', fg=self.bttn_fg, bg=self.bttn_bg,
                                width=self.bttn_width, height=self.bttn_height,
                                command=lambda: self.user_input('X'))
        bttn_Y = tkinter.Button(master=self.keyboard_frame, text='Y', fg=self.bttn_fg, bg=self.bttn_bg,
                                width=self.bttn_width, height=self.bttn_height,
                                command=lambda: self.user_input('Y'))
        bttn_Z = tkinter.Button(master=self.keyboard_frame, text='Z', fg=self.bttn_fg, bg=self.bttn_bg,
                                width=self.bttn_width, height=self.bttn_height,
                                command=lambda: self.user_input('X'))
        bttn_ENTER = tkinter.Button(master=self.keyboard_frame, text='OK', fg=self.bttn_fg, bg=self.bttn_bg,
                                    width=self.bttn_width, height=self.bttn_height,
                                    command=lambda: self.enter_lbl_text())
        bttn_DELETE = tkinter.Button(master=self.keyboard_frame, text='Delete', fg=self.bttn_fg, bg=self.bttn_bg,
                                     width=self.bttn_width, height=self.bttn_height,
                                     command=lambda: self.delete_chr())
        bttn_SPACE = tkinter.Button(master=self.keyboard_frame, text='SPACE', fg=self.bttn_fg, bg=self.bttn_bg,
                                    width=self.bttn_width * 6, height=self.bttn_height,
                                    command=lambda: self.user_input(' '))
        bttn_CANCEL = tkinter.Button(master=self.keyboard_frame, text='Cancel', fg=self.bttn_fg, bg=self.bttn_bg,
                                     width=self.bttn_width * 3, height=self.bttn_height,
                                     command=lambda: self.cancel())

        # layout for all buttons
        bttn_Q.grid(row=0, column=0)
        bttn_W.grid(row=0, column=1)
        bttn_E.grid(row=0, column=2)
        bttn_R.grid(row=0, column=3)
        bttn_T.grid(row=0, column=4)
        bttn_Y.grid(row=0, column=5)
        bttn_U.grid(row=0, column=6)
        bttn_I.grid(row=0, column=7)
        bttn_O.grid(row=0, column=8)
        bttn_P.grid(row=1, column=0)
        bttn_A.grid(row=1, column=1)
        bttn_S.grid(row=1, column=2)
        bttn_D.grid(row=1, column=3)
        bttn_F.grid(row=1, column=4)
        bttn_G.grid(row=1, column=5)
        bttn_H.grid(row=1, column=6)
        bttn_J.grid(row=1, column=7)
        bttn_K.grid(row=1, column=8)
        bttn_L.grid(row=2, column=0)
        bttn_Z.grid(row=2, column=1)
        bttn_X.grid(row=2, column=2)
        bttn_C.grid(row=2, column=3)
        bttn_V.grid(row=2, column=4)
        bttn_B.grid(row=2, column=5)
        bttn_N.grid(row=2, column=6)
        bttn_M.grid(row=2, column=7)

        bttn_ENTER.grid(row=2, column=8)
        bttn_DELETE.grid(row=3, column=0, columnspan=2, sticky='we')
        bttn_SPACE.grid(row=3, column=0, columnspan=7, sticky='e')
        bttn_CANCEL.grid(row=3, column=6, columnspan=3)

    def user_input(self, user_input, pinpad=False):
        """Receives user input and display's it"""
        if not pinpad:  # if using keyboard
            self.lbl_value += user_input
            self.lbl_value = self.lbl_value.capitalize()
            self.lbl_str.set(self.lbl_value)
            self.display_prompts()

        else:  # if using keyboard
            if len(self.lbl_value) == 4:
                self.lbl_str.set(self.lbl_value)
            else:
                self.lbl_value += user_input
            self.lbl_value = self.lbl_value.capitalize()
            self.lbl_str.set(self.lbl_value)

    def delete_chr(self):
        self.lbl_value = list(self.lbl_value)
        del self.lbl_value[-1]
        self.lbl_value = ''.join(self.lbl_value)
        self.lbl_str.set(self.lbl_value)

    def cancel(self, pinpad=False):
        self.lbl_value = ''  # resets lbl value
        if not pinpad:  # if keyboard
            self.lbl_str.set('Name:')  # display str Name:
        else:  # if pinpad
            self.lbl_str.set('Pin Pad: ')

    def enter_lbl_text(self):
        """
        Search for userInput in csv file
        Switches Frames"""
        # if if user input is in csv file
        self.user_name_loc = self.search_name(f'[\'{self.lbl_value}\']')  # names stored as ['Name']
        if self.user_name_loc is not None:
            # print(self.lbl_value, 'is in database position', self.user_name_loc)

            # delay, to transition into frame switch
            time.sleep(0.2)
            self.key_frame_off = True
            self.pin_frame_off = False
            self.switch_frame()
        else:
            self.lbl_str.set('Name not in file')

    def pinpad(self):
        """PinPad used to secure registration """
        self.key_pin_switch = False

        self.bttn_fg = 'black'
        self.bttn_bg = 'white'
        self.bttn_width = 6  # 605//9
        self.bttn_height = 3  # 20

        # change name prompts to Yes No Questions
        self.lbl_text_one.set('                         ')
        self.lbl_text_two.set('                         ')
        self.lbl_text_three.set('                         ')
        # change lbl str and reset value
        self.lbl_str.set('Pin Code: ')
        self.lbl_value = ''

        # creating buttons for PinPad
        bttn_one = tkinter.Button(master=self.pinpad_frame, text='1', fg=self.bttn_fg, bg=self.bttn_bg,
                                  width=self.bttn_width, height=self.bttn_height,
                                  command=lambda: self.user_input('1', True))
        bttn_two = tkinter.Button(master=self.pinpad_frame, text='2', fg=self.bttn_fg, bg=self.bttn_bg,
                                  width=self.bttn_width, height=self.bttn_height,
                                  command=lambda: self.user_input('2', True))
        bttn_three = tkinter.Button(master=self.pinpad_frame, text='3', fg=self.bttn_fg, bg=self.bttn_bg,
                                    width=self.bttn_width, height=self.bttn_height,
                                    command=lambda: self.user_input('3', True))
        bttn_four = tkinter.Button(master=self.pinpad_frame, text='4', fg=self.bttn_fg, bg=self.bttn_bg,
                                   width=self.bttn_width, height=self.bttn_height,
                                   command=lambda: self.user_input('4', True))
        bttn_five = tkinter.Button(master=self.pinpad_frame, text='5', fg=self.bttn_fg, bg=self.bttn_bg,
                                   width=self.bttn_width, height=self.bttn_height,
                                   command=lambda: self.user_input('5', True))
        bttn_six = tkinter.Button(master=self.pinpad_frame, text='6', fg=self.bttn_fg, bg=self.bttn_bg,
                                  width=self.bttn_width, height=self.bttn_height,
                                  command=lambda: self.user_input('6', True))
        bttn_seven = tkinter.Button(master=self.pinpad_frame, text='7', fg=self.bttn_fg, bg=self.bttn_bg,
                                    width=self.bttn_width, height=self.bttn_height,
                                    command=lambda: self.user_input('7', True))
        bttn_eight = tkinter.Button(master=self.pinpad_frame, text='8', fg=self.bttn_fg, bg=self.bttn_bg,
                                    width=self.bttn_width, height=self.bttn_height,
                                    command=lambda: self.user_input('8', True))
        bttn_nine = tkinter.Button(master=self.pinpad_frame, text='9', fg=self.bttn_fg, bg=self.bttn_bg,
                                   width=self.bttn_width, height=self.bttn_height,
                                   command=lambda: self.user_input('9', True))
        bttn_zero = tkinter.Button(master=self.pinpad_frame, text='0', fg=self.bttn_fg, bg=self.bttn_bg,
                                   width=self.bttn_width, height=self.bttn_height,
                                   command=lambda: self.user_input('0', True))
        bttn_cancel = tkinter.Button(master=self.pinpad_frame, text='Cancel', fg=self.bttn_fg, bg=self.bttn_bg,
                                     width=self.bttn_width, height=self.bttn_height,
                                     command=lambda: self.cancel(True))
        bttn_delete = tkinter.Button(master=self.pinpad_frame, text='Delete', fg=self.bttn_fg, bg=self.bttn_bg,
                                     width=self.bttn_width, height=self.bttn_height,
                                     command=lambda: self.delete_chr())
        bttn_enter = tkinter.Button(master=self.pinpad_frame, text='Enter', fg=self.bttn_fg, bg=self.bttn_bg,
                                    width=self.bttn_width, height=self.bttn_height,
                                    command=lambda: self.pinpad_input_valid())

        # layout for PinPad buttons
        bttn_one.grid(row=0, column=0)
        bttn_two.grid(row=0, column=1)
        bttn_three.grid(row=0, column=2)
        bttn_four.grid(row=1, column=0)
        bttn_five.grid(row=1, column=1)
        bttn_six.grid(row=1, column=2)
        bttn_seven.grid(row=2, column=0)
        bttn_eight.grid(row=2, column=1)
        bttn_nine.grid(row=2, column=2)
        bttn_zero.grid(row=3, column=1)
        bttn_cancel.grid(row=3, column=0)
        bttn_delete.grid(row=3, column=2)
        bttn_enter.grid(row=4, column=1)

    def pinpad_input_valid(self):
        with open('Attendance Record.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            # make csv file list for index
            row = list(csv_reader)
            # user position in list
            user_row = row[self.user_name_loc]
            user_pincode = user_row['PinCode']
            if user_pincode == self.lbl_value:  # is entered pincode valid
                self.prompt_attendance = True  # Allows user to interact with prompts
                self.lbl_text_one.set('Would like to adimit attendance: ')
                self.lbl_text_two.set('YES')
                self.lbl_text_three.set('NO')

    def add_name(self):
        # appends new attendee
        with open('Attendance Record.csv', 'a', newline='') as csvfile:
            Attendance = ['Name', 'Day\'s']
            dict_writer = csv.DictWriter(csvfile, fieldnames=Attendance)
            fileEmpty = os.stat('Attendance Record.csv').st_size == 0  # if file is empty write header
            if fileEmpty:
                dict_writer.writeheader()
            else:  # test_dict = {'Name': [self.lbl_value], 'pincode':12345, 'Day\'s': [1, 2, 3, 4, 5]}

                test_dict = {'Name': [self.lbl_value], 'Day\'s': [1, 2, 3, 4, 5]}
                dict_writer.writerow(test_dict)

    def admit_attendance(self, admit_attendance_YN):
        '''Add's attendance day to csv file converting
         it to a list appending to a value to a key saving it'''
        if admit_attendance_YN:
            # update lbl and buttons
            self.lbl_str.set(f'Attenadance Recorded Date: {datetime.date.today()}')

            with open('Attendance Record.csv', 'r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                attendance_record_dict = list(csv_reader)
                user_record = attendance_record_dict[self.user_name_loc]
                # gets attendance of user and gets the day key then manipulates the string to get desired list
                attendance_record = user_record['Day\'s'].strip('\"[]')
                attendance_record = attendance_record.split(',')
                attendance_record.append(str(datetime.date.today()))  # appends the date
                attendance_record_dict[self.user_name_loc]['Day\'s'] = attendance_record

                Attendance = ['Name', 'PinCode', 'Day\'s']

                with open('Attendance Record.csv', 'w', newline='') as write_file:  # stores attendance
                    csv_writer = csv.DictWriter(write_file, Attendance)
                    csv_writer.writeheader()
                    for line in attendance_record_dict:
                        csv_writer.writerow(line)

            self.lbl_text_one.set('Would You Like To Quit')
            self.lbl_text_two.set('Press Buttun Above')
            self.lbl_text_three.set('Press Buttun Above')

        else:  # todo quit options
            self.lbl_str.set(f'Attenadance Not Recorded Date: {datetime.date.today()}')
            self.lbl_text_one.set('Would You Like To Quit Press')
            self.lbl_text_two.set('Press Buttun Above')
            self.lbl_text_three.set('Press Buttun Above')


# first finished program 2022-03-05
# yes finally after one month of procrastination or like 5 something years
# plans:
# work harder stop using OOP learn Functional
# learn to use OOP properly
# learn machine learning get to advanced stage soon
# get a job

# initialize classes
main_gui = main()
main_gui.display()
main_gui.name_prompt()
main_gui.keyboard()

root.mainloop()
