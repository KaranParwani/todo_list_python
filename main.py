from tkinter import *

class Todo:
    
    def __init__(self, root: object) -> None:
        
        self.root = root

        self.title = Label(self.root, text='Todo List Application', font='ariel, 20 bold', 
                           width=10, bd=5, bg='yellow', fg='black')
        self.title.pack(side='top', fill=BOTH)

        self.add_task_title = Label(self.root, text='Add Task', font='ariel, 20 bold', 
                                    width=10, bd=5, bg='yellow', fg='black')
        self.add_task_title.place(x=70 , y=54)

        self.tasks = Label(self.root, text='Task List', font='ariel, 20 bold', 
                                    width=10, bd=5, bg='yellow', fg='black')
        self.tasks.place(x=400 , y=54)

        self.completed_tasks = Label(self.root, text='Completed Task', font='ariel, 20 bold', 
                                    width=15, bd=5, bg='yellow', fg='black') 
        self.completed_tasks.place(x=700 , y=54)

        self.comp_task_list = Listbox(self.root, height=9, bd=5, width=20, font='ariel, 20 italic bold')
        self.comp_task_list.place(x=670, y=100)

        self.task_list = Listbox(self.root, height=9, bd=5, width=20, font='ariel, 20 italic bold')
        self.task_list.place(x=350, y=100)

        self.text_box = Text(self.root, height=1, bd=5, width=20, font='ariel, 20 bold')
        self.text_box.place(x=20, y=100)


        def add():
            '''
            Method is to add the entered text to the task_list file.
            Parameters:
                None
            '''

            # get the data from the text box #1.0 means starting from index 1 and END means till the end
            context = self.text_box.get(1.0, END)

            # add the context to the listbox
            self.task_list.insert(END, context)

            # write the context data to the file which can be displayed in the listbox box under Task list
            with open('task_list.txt', 'a') as file:
                file.write(context)
                file.seek(0)

            # textbox content is added to the listbox and then delete from the textbox 
            self.text_box.delete(1.0, END)

        def mark_complete():
            '''
            Method is to mark task as completed and append it to file called completed task.
            Parameters:
                None
            '''

            # select the to list item
            selected_task = self.task_list.curselection()
        
            # append task to task_list file
            with open('task_list.txt', 'r+') as file:
                read_lines = file.readlines()
                file.seek(0)
                for line in read_lines:
                    file.write(line)

            # delete the task from task list
            self.task_list.delete(selected_task)
            
            # copying one file content to another
            with open('completed_task.txt', 'w') as completed_task_file, open('task_list.txt', 'r+') as file:
                read_lines = file.readlines()
                file.seek(0)
                for line in read_lines:
                    completed_task_file.write(line)

                    # insert the completed task to completed_task_list
                    self.comp_task_list.insert(END, line)

        
        self.add_button = Button(self.root, text='ADD', font='sarif, 10 bold italic', 
                                 width=10, bd=5, bg='yellow', fg='black', command=add)
        self.add_button.place(x=40, y=150)

        self.done_button = Button(self.root, text='MARK AS COMPLETED', font='sarif, 10 bold italic', 
                                  width=20, bd=5, bg='yellow', fg='black', command=mark_complete) 
        self.done_button.place(x=30, y=200)

def main():
    root = Tk()
    
    root.title('Todo List')
    root.geometry('1000x410+300+150')
    
    Todo(root)
    root.mainloop()

if __name__ == "__main__":
    main()