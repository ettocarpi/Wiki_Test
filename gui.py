
import tkinter as tk
from tkinter import *
from searchWiki import *
from tkhtmlview import HTMLLabel
root = tk.Tk()
label = tk.Label(root,text="Search Wiki")
label.pack()
entry = tk.Entry(root,text="Search Wiki")
entry.pack()

# result = tk.Text(root,height=20, width=100)
# result.pack()



def search_wiki():
    argument = entry.get()
    if argument != '':
        results = search(argument)
        str_output = ''
        for arg in results:
            str_output += '<b>'+arg+'</b>' + "<br>"
            str_output += results[arg]
            str_output += "<br><br>"
        print(str_output)
        html_label = HTMLLabel(root, html=""" {} """.format(str_output))
        html_label.pack(pady=50,padx=100)
        #result.insert(INSERT,str_output)


button_calc = tk.Button(root, text="Search", command=search_wiki)
button_calc.pack()



root.mainloop()











