import tkinter as tk
import tkinter.ttk as ttk
#import ArticleManager
import Article
from Configuration import *
from ArticleManager import *



def clicked(txt, lbl, comboBox,txtHolder):
    res = txt.get()

    '''WAZME - res, czuli txt.get() wyciaga to co jest wpisane w textEditiorze'''
    print(res)

    lbl.configure(text=res)
    txtHolder.delete('1.0', tk.END)
    articleList.clear()
    comboBoxValues.clear()
    comboBox["values"] = comboBoxValues

    '''Pewnie bedziesz chcial wrzucic tekst z textEditora jako argument '''
    addArticleToArticleList(comboBox  )




def addArticleToArticleList(comboBox):
    #TODO: TUTAJ WSADZ SWOJA FUNKCJE KTORA DODAJE ARTYKULY

    valuesInComboBox = len(comboBox["values"])
    newValue = "" + str(valuesInComboBox * 10) + " - " + str((valuesInComboBox * 10) + 9) + ""
    comboBoxValues.append(newValue)
    comboBox["values"] = comboBoxValues

    '''TEN SPOSOB DODAWANIA TRZEBA ZMIENIC'''
    articleList.append(Article("http_reklama_interia_pl"))
    articleList.append(Article("http_reklama_interia_pl_produkty_mobile"))
    articleList.append(Article("http_sport_interia_pl"))
    articleList.append(Article("http_static_tabmo_io_s3_amazonaws_com_privacy_policy_index_html"))
    articleList.append(Article("http_twitter_com_maxmodelspl"))
    articleList.append(Article("http_www_maxmodels_pl_iwa_source_side_menu"))
    articleList.append(Article("http_www_rmfon_pl"))
    articleList.append(Article("http_www_rmfon_pl_play_6_iwa_source_sg_ikona"))
    articleList.append(Article("http_www_xsocialgroup_com_PrivacyPolicy_html"))
    articleList.append(Article("https_e_turysta_pl"))

#c.current(0)
# TODO : tutaj zdefiniuj sposob dodawania nowych artyku³ów
def addNew10Articles(comboBox):
    addArticleToArticleList(comboBox)
    #addArticleToArticleList()

def on_combo_configure(event):
    global fruit
    width = 60
    style = ttk.Style()
    style.configure('TCombobox', postoffset=(0,0,width,0))

def onClickCombobox(comboBoxIndex, txtHolder):

    start = comboBoxIndex * 10
    end = comboBoxIndex*10 + 10
    txtHolder.delete('1.0', tk.END)

    for x in range(start, end):
        txtHolder.insert(tk.INSERT, "\n\n\n====================== " + articleList[x].getDirectoryName()
                         + " ======================\n\n\n")
        txtHolder.insert(tk.INSERT, articleList[x].getTextFromArtile(PATH_FOR_FILES))



