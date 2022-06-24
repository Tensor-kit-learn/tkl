import matplotlib.pyplot as plt
import os
from tkinter import *
from PIL import Image, ImageTk

#prepars data to be rendered

def init(inputs,neurons,outputs):
    out = []
    new_out = []
    for i in inputs:out.extend(i)
    for n in neurons:out.extend(n[0])
    
    out.extend(outputs[1:-1])
    def filter():
        for objects in out:
            if objects != 'nan':
                new_out.append(objects)
            
        else:
             pass
        
    fil = filter()
    del out[:]
    for vals in new_out:
        out.append(vals)
    
    return[out,[len(inputs),len(neurons),len(outputs)]]

   
    
#renders your neural-network and requires the `tklearn.tkboard.init()` function[DOES NOT SOUPPORT `tklearn.koala()` yet]
def render(init,base='T.NN()',theme='#4CAF50'):
    def __board__(title):
        try:
            #config
            app = Tk()
            x = app.winfo_screenwidth()
            y = app.winfo_screenheight()
            data = list(init[1])   
            app.state('zoomed')
            app.title(str(title))

            
            def chart(init):
                plt.plot(init)
                plt.savefig('chart.png',facecolor='None')
                plt.show()
                plt.close('all')
                return('chart.png')
               
            def delete_file(file):
                if os.path.exists(file):
                  os.remove(file)
                else:pass
            
            def NN_chart(inputs,neurons,output):
                def draw_neural_net(ax,layer_sizes):
                    left = .1
                    right = .9
                    bottom = .1
                    top = .9
                    v_spacing = (top - bottom)/float(max(layer_sizes))
                    h_spacing = (right - left)/float(len(layer_sizes) - 1)
                    for n, layer_size in enumerate(layer_sizes):
                        layer_top = v_spacing*(layer_size - 1)/2. + (top + bottom)/2.
                        for m in range(layer_size):
                            circle = plt.Circle((n*h_spacing + left, layer_top - m*v_spacing), v_spacing/4.,
                                                color='w', ec='k', zorder=4)
                            ax.add_artist(circle)
                    for n, (layer_size_a, layer_size_b) in enumerate(zip(layer_sizes[:-1], layer_sizes[1:])):
                        layer_top_a = v_spacing*(layer_size_a - 1)/2. + (top + bottom)/2.
                        layer_top_b = v_spacing*(layer_size_b - 1)/2. + (top + bottom)/2.
                        for m in range(layer_size_a):
                            for o in range(layer_size_b):
                                line = plt.Line2D([n*h_spacing + left, (n + 1)*h_spacing + left],
                                                  [layer_top_a - m*v_spacing, layer_top_b - o*v_spacing], c='k')
                                ax.add_artist(line)
                                
                fig = plt.figure(figsize=(5, 5))
                plt.close(fig)
                ax = fig.gca()
                ax.axis('off')
                draw_neural_net(ax,[inputs,neurons,output])
                fig.savefig('nn.png',facecolor='None')
                return('nn.png')
            

            #Graph
            graph = chart(init[0])
            
            
            file1 = Image.open(graph)
            new_img = file1.resize((640,480),Image.ANTIALIAS)
            graph_img = ImageTk.PhotoImage(new_img)
            graph_frame = Label(image=graph_img)
            graph_frame.place(x=20,y=90) 
            
            #NN
            NN_graph = NN_chart(data[0],data[1],data[2])
            file2 = Image.open(NN_graph)
            new_img2 = file2.resize((500,500),Image.ANTIALIAS)
            graph_img2 = ImageTk.PhotoImage(new_img2)
            graph_frame2 = Label(image=graph_img2)
            graph_frame2.place(x=x-600,y=70) 
            
            
            #NN data graph
            df = Frame(bg='#808080',width=310,height=220)
            df.place(x=x-480,y=y-395)
            
            inp_text = Label(app,text=('inputs: '+str(data[0])),bg='#808080',fg='#FFFFFF')
            inp_text.config(font=("bold", 30))
            inp_text.place(x=x-400,y=y-369)
            
            ner_text = Label(app,text=('neurons: '+str(data[1])),bg='#808080',fg='#FFFFFF')
            ner_text.config(font=("bold", 30))
            ner_text.place(x=x-400,y=y-308)
                            
            out_text = Label(app,text=('outputs: '+str(data[2])),bg='#808080',fg='#FFFFFF')
            out_text.config(font=("bold", 30))
            out_text.place(x=x-400,y=y-250)
            
            #Headder
            Frame(app,bg=theme,width=x,height=70).place(x=0,y=0)
            top_text = Label(text='Tkboard',bg=theme,fg='#FFFFFF')
            top_text.place(x=x//2-100,y=10)
            top_text.config(font=("Helvetica", 30))            
            
            
            close_btn = Button(app,text='X',width=5,height=1,bg='red',fg='white',borderwidth=0,command=app.destroy)
            close_btn.place(x=x-41,y=0)
            
            
            app.bind("<F11>", lambda event: app.attributes("-fullscreen",not app.attributes("-fullscreen")))
            app.bind("<Escape>", lambda event: app.attributes("-fullscreen", False))
            
            app.mainloop()
            delete_file('chart.png')
            delete_file('nn.png')
            
        except (RuntimeError, TypeError, NameError,Exception) as e:
            print(e)
    
    base = base.lower()
    if 't' in base:__board__('Tkboard-@'+str(os.environ.get('USERNAME')))
    
    else:raise ImportWarning('Tkboard is only supported for "tkl.nn()"')