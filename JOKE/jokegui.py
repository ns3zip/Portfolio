# IMPORT MODULE
import PySimpleGUI as sg

layout = [[sg.Text(text='Why Did the Programmer leave his Job?',
                  font=('Helvetica', 48),
                  expand_x=True,
                  justification='center',)]]

sg.Button('Why?')
text_name = sg.popup('Why did the Programmer leave his Job ?',title='A Joke for Today !')
text_name2 = sg.popup('Because he did not get Arrays')




