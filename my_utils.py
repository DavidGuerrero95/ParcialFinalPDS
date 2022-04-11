import matplotlib.pyplot as plt
import numpy as np

def plotAxsUnaDimension(dimensionX=1, dimensionY=1, xSize=15, ySize=10, adjust=0.4, dataX=[], dataY=[], title=[], xLabel=[], yLabel=[], fontSize=24, fc=0,linea=False, lineaBw=False, BW=0,linea2=False, fc2 =0,colour=["blue","green","red","black"]):
    fig,axs  = plt.subplots(dimensionX,dimensionY) # Subplots
    fig.set_size_inches((xSize,ySize)) # Tamaño de ventana
    plt.subplots_adjust(hspace=adjust) # Ajuste de ventana
    size = 0
    if dimensionX > 1:
        size = dimensionX
    elif dimensionY > 1:
        size = dimensionY
    for i in range(size):
        axs[i].plot(dataX[i],dataY[i],colour[i]) # Graficas
        if linea == True:
            axs[i].axvline(x=fc,ymin=0,ymax=1.2,color='red',ls='--',label='Fc='+str(fc)+'Hz') # Se grafica linea en fc
            axs[i].legend(loc='upper left')
        if linea2 == True:
            axs[i].axvline(x=fc2,ymin=0,ymax=1.2,color='red',ls='--',label='Fc2='+str(fc2)+'Hz') # Se grafica linea en fc
            axs[i].legend(loc='upper left')
        if lineaBw == True:
            axs[i].axvline(x=fc+BW,ymin=0,ymax=1.2,color='green',ls='-.',label='Fc='+str(fc)+'Hz')
            axs[i].axvline(x=fc-BW,ymin=0,ymax=1.2,color='green',ls='-.',label='Fc='+str(fc)+'Hz')
        axs[i].set_title(title[i], fontsize = fontSize) # Titulo Grafica
        axs[i].set_xlabel(xLabel[i],fontsize = fontSize) # Label X 
        axs[i].set_ylabel(yLabel[i],fontsize=fontSize) # Label Y
        axs[i].grid() # Grid On
    plt.show() # Se muesra la grafica
    
def stemAxs(dimensionX=1, dimensionY=1, xSize=15, ySize=10, adjust=0.4, dataX=[[]], dataY=[[]], title=[[]], xLabel=[[]], yLabel=[[]], fs=0, fontSize=24, fc = 0,cuadro=False, flagFc2=False, fc2=0):
    fig,axs  = plt.subplots(dimensionX,dimensionY) # Subplots
    fig.set_size_inches((xSize,ySize)) # Tamaño de ventana
    plt.subplots_adjust(hspace=adjust) # Ajuste de ventana
    size1 = 0
    size2 = 1
    flagMultidimension = False
    if dimensionX > 1 and dimensionY == 1:
        size1 = dimensionX
    elif dimensionY > 1 and dimensionX == 1:
        size1 = dimensionY
    else:
        flagMultidimension = True
        size1 = dimensionX
        size2 = dimensionY
    if flagMultidimension == False:
        for i in range(size1):
            if i%2 == 0:
                axs[i].stem(dataX[0][i],dataY[0][i],basefmt='b-') # Graficas
            else:
                axs[i].plot(dataX[0][i],dataY[0][i]) # Graficas
                axs[i].axvline(ymin=0,ymax=1.2,color='green',ls='--')
                axs[i].axvline(x=fc,ymin=0,ymax=1.2,color='red',ls='--',label='Fc='+str(fc)+'Hz') # Se grafica linea en fc
                if flagFc2 == True:
                    axs[i].axvline(ymin=0,ymax=1.2,color='green',ls='--')
                    axs[i].axvline(x=fc2,ymin=0,ymax=1.2,color='red',ls='--',label='Fc2='+str(fc2)+'Hz') # Se grafica linea en fc 2
                axs[i].legend(loc='upper left')
                axs[i].axis(xmax=fs/2,xmin=-fs/2)
            axs[i].set_title(title[0][i], fontsize = fontSize) # Titulo Grafica
            axs[i].set_xlabel(xLabel[0][i],fontsize = fontSize) # Label X 
            axs[i].set_ylabel(yLabel[0][i],fontsize=fontSize) # Label Y
            axs[i].grid() # Grid On
    else:
        for i in range(size1):
            for j in range(size2):
                if j%2 == 0:
                    axs[i][j].stem(dataX[i][j],dataY[i][j],basefmt='b-') # Graficas
                else:
                    axs[i][j].plot(dataX[i][j],dataY[i][j]) # Graficas
                    if cuadro == True:
                        axs[i][j].vlines([-fc,fc],0,1,color='g',lw=2.,linestyle='--')
                        axs[i][j].hlines(1,-fc,fc,color='g',lw=2.,linestyle='--')
                    axs[i][j].axvline(ymin=0,ymax=1.2,color='green',ls='--') 
                    axs[i][j].axvline(x=fc,ymin=0,ymax=1.2,color='red',ls='--',label='Fc='+str(fc)+'Hz') # Se grafica linea en fc
                    if flagFc2 == True:
                        axs[i][j].axvline(ymin=0,ymax=1.2,color='green',ls='--')
                        axs[i][j].axvline(x=fc2,ymin=0,ymax=1.2,color='red',ls='--',label='Fc2='+str(fc2)+'Hz') # Se grafica linea en fc 2
                    axs[i][j].legend(loc='upper left')
                    axs[i][j].axis(xmax=fs/2,xmin=-fs/2)
                axs[i][j].set_title(title[i][j], fontsize = fontSize) # Titulo Grafica
                axs[i][j].set_xlabel(xLabel[i][j],fontsize = fontSize) # Label X 
                axs[i][j].set_ylabel(yLabel[i][j],fontsize=fontSize) # Label Y
                axs[i][j].grid() # Grid On
                
    plt.show() # Se muesra la grafica

    
def plotAnalogFilters(dataX=[], dataY=[], title=[], xLabel=[], yLabel=[],fc=0,fc2=0,fontSize=24):
    fig,axs = plt.subplots(1,2)
    fig.set_size_inches((20,5))
    plt.subplots_adjust(hspace=0.6)
    axs[0].plot(dataX[0], dataY[0]) # Grafica temporal del audio
    axs[0].set_title(title[0], fontsize = fontSize)
    axs[0].set_xlabel(xLabel[0],fontsize=fontSize)
    axs[0].set_ylabel(yLabel[0],fontsize=fontSize)
    axs[0].axvline(x=fc,ymin=0,ymax=1.2,color='red',ls='--',label='Fc='+str(fc)+'Hz')
    axs[0].axvline(x=fc2,ymin=0,ymax=1.2,color='red',ls='--',label='Fc2='+str(fc2)+'Hz')
    axs[0].legend(loc='upper left')
    axs[0].grid()
    axs[1].plot(dataX[1], dataY[1])
    axs[1].plot(dataX[2], dataY[2], label='Filtered signal (%g Hz)')
    axs[1].set_title(title[1], fontsize = fontSize)
    axs[1].set_xlabel(xLabel[1],fontsize=fontSize)
    axs[1].set_ylabel(yLabel[1],fontsize=fontSize)
    axs[1].grid(True)
    axs[1].axis('tight')
    axs[1].legend(loc='upper left')
    plt.show()
    plt.figure(figsize=(15,4)) 
    plt.plot(dataX[3], dataY[3], color='purple') # Se grafica en el dominio de la frecuencia.
    plt.xscale('log') # Se ajusta el eje X para que sea escala logarítmica.
    plt.title(title[2]) # Etiqueta título.
    plt.xlabel(xLabel[2],fontsize=fontSize) # Etiqueta eje X.
    plt.ylabel(yLabel[2],fontsize=fontSize) # Etiqueta eje Y.
    plt.grid(which='both', axis='both')
    plt.show()
    
def plot_signal(x,y=None,xlabel=None,ylabel=None,title=None,format=None,size=(15,5),show=True,ret=False,subplots=(1,1),stem=False):
    fig, axs = plt.subplots(*subplots)
    if isinstance(axs,np.ndarray):
        ax = axs[0]
    else:
        ax = axs
    ax.set_aspect('auto')

    if stem:
        foo = ax.stem
    else:
        foo = ax.plot
    if y is not None:
        if format is not None:
            foo(x,y,format)
        else:
            foo(x,y)
    else:
        if format is not None:
            foo(x,format)
        else:
            foo(x)
    if xlabel is not None:
        ax.set_xlabel(xlabel,fontsize=18)
    if ylabel is not None:
        ax.set_ylabel(ylabel,fontsize=18)
    if title is not None:
        ax.set_title(title,fontsize=24)
    if size is not None:
        fig.set_size_inches(size)
    plt.grid()
    plt.tight_layout()
    if show:
        plt.show()
    if ret:
        if subplots == (1,1):
            return fig,ax
        else:
            return fig,axs