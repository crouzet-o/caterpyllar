#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Filename: Caterpyllar/__init__.py
#
#
# Python Module for Speech Perception and Production experiments.
# Copyright Olivier Crouzet - 2010
# olivier.crouzet@univ-nantes.fr


# TODO:
# - So many things...
# - Read XML data file
# - Group items per list in data file and randomize inside lists and between lists
# - and many... many more


##__all__ = ["caterpyllar"]

import sys
import locale
import re
import string
import pygame
#from pygame import event
from pygame.locals import * # events, key names (MOUSEBUTTONDOWN,K_r...)
import time
import scipy
import codecs



# Initialisation de l'affichage
"""
In order to let pygame-based function work, we need to program them
as methods in an object-oriented way (with self. methodology). Because
we need to define an object (e.g. window.) inside the main script
and to alter it within Caterpyllar/_init_.py (e.g. by overlaying window.
with a surface that is defined in the _init_.py Module). Therefore,
display_2AFC() would be a method that is defined for an object wherever
it is defined...

I should text it on a simple Module using a simple script.
"""
black=(0, 0, 0)
white=(250, 250, 250)
red=(255, 0, 0)
green=(0, 255, 0)
lightblue = (105, 160, 170)


bgcolor=lightblue
fgcolor=white

#scale=1
scale=.75
textsize=int(120*scale)

largeur_ecran=int(1280*scale)
hauteur_ecran=int(9*largeur_ecran/16)


# Decreasing display screen size to speed-up processing
#largeur_ecran = int(largeur_ecran/2)
#hauteur_ecran = int(hauteur_ecran/2)

pygame.mixer.pre_init(frequency=44100, size=16, channels=1, buffer=4096)
pygame.mixer.init()
pygame.init()
window = pygame.display.set_mode((largeur_ecran,hauteur_ecran))
#window = pygame.display.set_mode((largeur_ecran,hauteur_ecran),FULLSCREEN)
##pygame.mouse.set_visible(0)
##pygame.event.set_grab(1)
background = pygame.Surface(window.get_size())
background = background.convert()
background.fill(bgcolor)
window.blit(background, (0,0))


fontchoices = 'arial, comicsans, helvetica'
selectedFont = pygame.font.match_font(fontchoices)


#global largeur_ecran,hauteur_ecran,scale

version = '0.0.4'


## General functions

def sayhi():
    print('Hi, this is',__name__,'speaking.')












## Sound specific functions

def play_sound(filename): # Play a sound from disk
    buzz = pygame.mixer.Sound(filename) # Load the sound file (wav format)
    duration = int(buzz.get_length()*1000) # Get its duration in ms
    buzz.play() # Play the file
    pause(duration) # Wait until it's finished playing















## Text files functions

def uconvert(string):
    """ Convert to unicode except if it's already unicode"""    
    try:
        ustring = unicode(string, 'utf8')
    except: 
        ustring = string
    return ustring


def read_data_2D(filepath, sep, header=False, dropg = False):
    """ Function to load the contents of a text file into a 2D table using "sep"
    as a column separator. This function returns the content of the
    file into a 2D table (list of lists) which may be accessed by "
    name_of_table[i][j]
    " (where i = line number, j = column number).

    USAGE: x = read_data_2D(filepath=TEXT, sep=TEXT, header=BOOLEAN, dropg=BOOLEAN)

    EXAMPLE : x = read_data_2D('directory/file.csv',';',1)
    
    """
    table=[] # Create an empty list
    datafile=open(filepath,'r') # Open file for reading
    for line in datafile.readlines(): # For each line in the text file
                                      # This keeps \n at end of line 
        cleandata = line.replace('\n','') # Remove \n at end of line
                                          # (from string.replace)
        if (dropg == True):
            cleandata = cleandata.replace('\"','')
            cleandata = cleandata.replace('\'','')
        oneline = re.split(sep,cleandata) # Split file at commas
        table.append(oneline) # Append the line at end of table
    datafile.close() # Close the file
    if header==1:
        table = table[1:len(table)]
    else:
        table=table
    return table

def read_data(filepath, header):
    """ Function to load the contents of a text file into a 1D table
    (list). This function returns the content of the file
    into a list which may be accessed by"name_of_list[i]"
    (where i = line number).

    USAGE: x = read_data(filepath = TEXT, header = BOOLEAN)
    EXAMPLE : x = read_data('directory/file.csv',1)
    
    """
    table=[] # Create an empty list
    datafile=open(filepath,'r') # Open file for reading
    for line in datafile.readlines(): # For each line in the text file
                                      # This keeps \n at end of line
        cleandata = string.replace(line,'\n','') # Remove \n at end of line
                                          # (from string.replace)
        oneline = re.split(",",cleandata) # Split file at commas
        table.append(oneline) # Append the line at end of table
    datafile.close() # Close the file
    if header==True:
        table = table[1:len(table)]
    else:
        table=table
    return table


def cleanup(line):
    data = string.replace(line,'\n','')
    return data

def load_data():
    data = read_data(sys.argv[1])
    return data


# resfile = raw_input("Entrez le nom du fichier de résultats :"
# results = init_resultsfile(resfile)
# runtheexperiment(results)
# results.close()
def init_resultsfile(path):
    """ Initializes a file for appending, argument is the filepath"""
    #results = codecs.open(path,'a','utf-8')
    results = open(path,"a") # a for append (will not overwrite)
    return results









## Image functions

def display_image(filename): # Display an image from disk
    splash = pygame.image.load(filename)
    splashpos = splash.get_rect()
    splashpos.centerx = background.get_rect().centerx
    splashpos.centery = background.get_rect().centery
    blank_bg(bgcolor)
    window.blit(background, (0,0))
    window.blit(splash,splashpos)
    pygame.display.flip()


def draw_button(surface,color,location):
    bwidth = 100 # Set button width
    bheight = 100 # Set button height
    bsize = (bwidth,bheight) # Compute button size

    bsurf = pygame.Surface(bsize) # Create a surface for the button
    bsurf = bsurf.convert() # Convert to same pixel format
    button = pygame.Rect(location,bsize) # Define the button
                                         # coordinates and
                                         # size. Create a "Rectangle"
                                         # coordinate system.
    pygame.draw.rect(surface, color, button, 20) # Draw this rectangle on
                                             # a surface
    #bsurf.blit(bsurf, button) # Put the button on its surface
    #surface.blit(bsurf, location) # Put this surface on the background
                                 # surface
    window.blit(bsurf,location)
    pygame.display.flip() # Flip the display to actually produce the
                          # button
    return bsurf

def draw_2buttons(surface,color):
    bwidth = 100 # Set button width
    bheight = 100 # Set button height
    bsize = (bwidth,bheight) # Compute button size

    location1 = (300-50, 300-50);
    bsurf1 = pygame.Surface(bsize) # Create a surface for the button
    bsurf1 = bsurf1.convert() # Convert to same pixel format
    button1 = pygame.Rect(location1,bsize) # Define the button
                                           # coordinates and type
    pygame.draw.rect(bsurf1, color, button1) # Draw this rectangle on
                                             # a surface
    window.blit(bsurf1, location1) # Set the corresponding surface

    location2 = (500-50, 300-50);
    bsurf2 = pygame.Surface(bsize) # Create a surface for the button
    bsurf2 = bsurf2.convert() # Convert to same pixel format
    button2 = pygame.Rect(location2,bsize) # Define the button
                                           # coordinates and type
    pygame.draw.rect(bsurf2, color, button2) # Draw this rectangle on
                                             # a surface
    window.blit(bsurf2, location2) # Set the corresponding surface

    pygame.display.flip() # Flip the display to actually produce the button
    return location1,location2


def whatdisplay_image(filename,location):
    pygame.image.load(filename, namehint="png")
    








## Screen display functions

def blank_bg(color):
    background.fill(color)
    window.blit(background, (0,0))
    pygame.display.flip()

def blank_screen(color=(0,0,0)):
    window.fill(color)
    window.blit(background, (0, 0))
    pygame.display.flip()

def change_color(color):
    background.fill(color)
    window.blit(background, (0,0))
    pygame.display.flip()

# Clear a rectangular area
def clear_area(coord):
    area = pygame.Surface(coord)
    area.fill(bgcolor)
    window.blit(area,coord)
    pygame.display.flip() # Flip the display to actually produce the
                          # button

# Clear a whole surface
def blank(surface):
    surface.fill(bgcolor)
    window.blit(surface, (0,0))
    pygame.display.flip()

# Draw a color on a whole surface
def blank(surface):
    surface.fill(bgcolor)
    window.blit(surface, (0,0))
    pygame.display.flip()












## Text display functions

def splash(text):
    #global largeur_ecran,hauteur_ecran,scale
    #        window.blit(background, (0, 0))
    #        pygame.display.flip()
    #        pygame.time.wait(2000)
    font = pygame.font.Font(selectedFont, int(32*scale)) # Font name and size
    title = font.render(text, 1, fgcolor) # Set text to display, antialiasing and color
    titlepos = title.get_rect() # Get surface size information
    titlepos.centerx = background.get_rect().centerx # set x position
    titlepos.centery = background.get_rect().centery # set y position
    blank_screen()
    window.blit(background, (0,0))
    window.blit(title, titlepos)
    pygame.display.flip()
    waitforkeypress()
    pygame.time.wait(1000)


def display_text(text,color): # Display text
    global largeur_ecran,hauteur_ecran,scale
    font = pygame.font.Font(selectedFont, int(46*scale)) # Font name and size
    text = font.render(text, 1, color) # Set text to display, antialiasing boolean and color
    textpos = text.get_rect() # Get coordinates of the surface needed for text display
    textsize = text.get_size()
    textpos.centerx = background.get_rect().centerx # set text x-position centered
    textpos.centery = background.get_rect().centery # set text y-position centered
    window.blit(background, (0,0)) # Blit it
    window.blit(text, textpos) # Blits the text to the coordinates
    pygame.display.flip() # Flip the display
    
    
    
def whatdisplay_text(text): # Display text
    font = pygame.font.Font(selectedFont, 40*scale) # Font name and size
    text = font.render(text, 1, fgcolor) # Set text to
                                                   # display,
                                                   # antialiasing
                                                   # boolean and color
    textpos = text.get_rect() # Get coordinates of the surface needed
                              # for text display
    textsize = text.get_size()
    textpos.centerx = background.get_rect().centerx # set text
                                                    # x-position
                                                    # centered
    textpos.centery = background.get_rect().centery # set text
                                                    # y-position
                                                    # centered
    background.fill(bgcolor) # Blank the background surface
    window.blit(background, (0,0)) # Blit it
    window.blit(text, textpos) # Blits the text to the coordinates
    pygame.display.flip() # Flip the display


def whatdisplay_text(string):
        font = pygame.font.Font(selectedFont, 46*scale) # set TrueType font to use
                                          # (here default) and size
        text = font.render(string, 1, fgcolor) # Set text to display,
                                             # antialiasing and color
        textpos = text.get_rect() # Get surface size information
        textpos.centerx = background.get_rect().centerx # set x
                                                        # position
        textpos.centery = background.get_rect().centery # set y
                                                        # position
        window.fill(bgcolor)
        window.blit(text, textpos)
        pygame.display.flip()
        pygame.time.wait(5000)

def display_text_pos(text, x, y): # Display text
    global largeur_ecran, hauteur_ecran, scale
    # Text part initialization
    font = pygame.font.Font(selectedFont, int(36*scale)) # Font name and size
    text = font.render(text, 1, fgcolor) # Set text to
                                                   # display,
                                                   # antialiasing
                                                   # boolean and color
    textpos = text.get_rect() # Get coordinates of the surface needed
                              # for text display
    textsize = text.get_size()
    # This part creates "buttons" under the text part
    xbuttonsize = textsize[0] + 10 # Set button x coordinates
    ybuttonsize = textsize[1] + 10 # Set button y coordinates
    bsurface = pygame.Surface((xbuttonsize+200, ybuttonsize)) # Create a dedicated surface
    bsurface.fill(bgcolor) # Fill it with grey
    bx = x - xbuttonsize / 2 # 
    by = y - ybuttonsize / 2
    window.blit(bsurface, (bx, by))
    pygame.display.flip()
    textpos.centerx = x # set text x-position
    textpos.centery = y # set text y-position
    # Then we blit text on this
    window.blit(text, textpos) # Blits the text to the coordinates

def display_info_pos(info, x, y): # Display text
    global largeur_ecran, hauteur_ecran, scale
    # Text part initialization
    font = pygame.font.Font(selectedFont, int(46*scale)) # Font name and size
    text = font.render(info, 1, fgcolor) # Set text to
                                                   # display,
                                                   # antialiasing
                                                   # boolean and color
    textpos = text.get_rect() # Get coordinates of the surface needed
                              # for text display
    textsize = text.get_size()
    # This part creates "buttons" under the text part
    xinfosize = textsize[0] + 50 # Set info x coordinates
    yinfosize = textsize[1] + 50 # Set info y coordinates
    isurface = pygame.Surface((xinfosize, yinfosize)) # Create a dedicated surface
    isurface.fill(bgcolor) # Fill it with grey
    ix = x - xinfosize / 2 # 
    iy = y - yinfosize / 2
    window.blit(isurface, (ix, iy))
    pygame.display.flip()
    textpos.centerx = x # set text x-position
    textpos.centery = y # set text y-position
    # Then we blit text on this
    window.blit(text, textpos) # Blits the text to the coordinates


def display_infoline(info): # Display text
    global largeur_ecran, hauteur_ecran, scale
    # Text part initialization
    font = pygame.font.Font(selectedFont, int(26*scale)) # Font name and size
    text = font.render(info, 1, bgcolor) # Set text to
                                                   # display,
                                                   # antialiasing
                                                   # boolean and color
    textpos = text.get_rect() # Get coordinates of the surface needed
                              # for text display
    textsize = text.get_size()
    print(textpos, textsize, info)
    # This part creates "buttons" under the text part
    xinfosize = textsize[0] + 50 # Set info x coordinates
    yinfosize = textsize[1] + 50 # Set info y coordinates
    isurface = pygame.Surface((largeur_ecran, hauteur_ecran / 10)) # Create a dedicated surface
    isurface.fill(fgcolor) # Fill it with grey
    ix = 0 # x - xinfosize / 2 # 
    iy = 0 #hauteur_ecran - ((hauteur_ecran/10)/2) # y - yinfosize / 2
    window.blit(isurface, (ix, iy))
    textpos.centerx = largeur_ecran/2 #isurface.centerx # set text x-position
    textpos.centery = ((hauteur_ecran/10)/2) # set text y-position
    # Then we blit text on this
    window.blit(text, textpos) # Blits the text to the coordinates
    pygame.display.flip()
    #pygame.display.flip()



## Experimental graghical designs functions

def getanswerfrom_matrix_2_3(x,y,answers):
    global largeur_ecran,hauteur_ecran,scale
    if x <= largeur_ecran/2:
        if y <= 1*hauteur_ecran/3:
            reponse = 'aba'
        elif y <= 2*hauteur_ecran/3:
            reponse = 'ada'
        elif y <= 3*hauteur_ecran/3:
            reponse = 'aga'
    elif x <= 2*largeur_ecran/2:
        if y <= 1*hauteur_ecran/3:
            reponse = 'apa'
        elif y <= 2*hauteur_ecran/3:
            reponse = 'ata'
        elif y <= 3*hauteur_ecran/3:
            reponse = 'aka'
    return reponse

def getanswerfrom_matrix_3_7(x,y,responsematrix):
    global largeur_ecran,hauteur_ecran,scale
    xadd=yresp=0
    if x <= 0.0125*largeur_ecran/(3*2):
        #display_text_pos("Quitter réellement ?",10,10)
        #catchquit()
        sys.exit()
    elif x <= 2*largeur_ecran/(3*2):
        xadd=0
        if y <= 2*hauteur_ecran/(7*2):
            yresp=0
        elif y <= 4*hauteur_ecran/(7*2):
            yresp=1
        elif y <= 6*hauteur_ecran/(7*2):
            yresp=2
        elif y <= 8*hauteur_ecran/(7*2):
            yresp=3
        elif y <= 10*hauteur_ecran/(7*2):
            yresp=4
        elif y <= 12*hauteur_ecran/(7*2):
            yresp=5
        elif y <= 14*hauteur_ecran/(7*2):
            yresp=6
    elif x <= 4*largeur_ecran/(3*2):
        xadd=7
        if y <= 2*hauteur_ecran/(7*2):
            yresp=0
        elif y <= 4*hauteur_ecran/(7*2):
            yresp=1
        elif y <= 6*hauteur_ecran/(7*2):
            yresp=2
        elif y <= 8*hauteur_ecran/(7*2):
            yresp=3
        elif y <= 10*hauteur_ecran/(7*2):
            yresp=4
        elif y <= 12*hauteur_ecran/(7*2):
            yresp=5
        elif y <= 14*hauteur_ecran/(7*2):
            yresp=6
    elif x <= 6*largeur_ecran/(3*2):
        xadd=14
        if y <= 2*hauteur_ecran/(7*2):
            yresp=0
        elif y <= 4*hauteur_ecran/(7*2):
            yresp=1
        elif y <= 6*hauteur_ecran/(7*2):
            yresp=2
        elif y <= 8*hauteur_ecran/(7*2):
            yresp=3
        elif y <= 10*hauteur_ecran/(7*2):
            yresp=4
        elif y <= 12*hauteur_ecran/(7*2):
            yresp=5
        elif y <= 14*hauteur_ecran/(7*2):
            yresp=6
    reponse=responsematrix[xadd+yresp]
    pygame.event.clear()
    return reponse
   

def display_matrice_2_3(a,b,c,d,e,f): # Usage : displaymatrice_2_3('un','deux','trois','quatre','cinq','six')
    global largeur_ecran,hauteur_ecran,scale
    strings=[[a,b,c],[d,e,f]]
    xpositions=[[1,1,1],[3,3,3]]
    ypositions=[[1,3,5],[1,3,5]]
    zones = [[0,0,0],[0,0,0]]
    for i in range(0,2,1):
        for j in range(0,3,1):
            place_texte_xy(strings[i][j],textsize,xpositions[i][j]/4.0*largeur_ecran,ypositions[i][j]/6.0*hauteur_ecran)


def display_matrice(xsize,ysize):
    global largeur_ecran,hauteur_ecran,scale
    xargs=string.ascii_letters[0:xsize]
    yargs=string.ascii_letters[0:ysize]
    totalargs=string.ascii_letters[0:(xsize*ysize)]
    return totalargs #'abcdefghijklmnopqrstu' need to split


def display_matrice_3_7(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u): # Usage : displaymatrice_2_3('un','deux','trois','quatre','cinq','six')
    #global largeur_ecran,hauteur_ecran,scale,textsize
    strings=[[a,b,c,d,e,f,g],[h,i,j,k,l,m,n],[o,p,q,r,s,t,u]]
    blank_screen()
    xpositions=[1*scipy.ones(7),3*scipy.ones(7),5*scipy.ones(7)] # 1,3,5 = 3 colonnes (indicées 1,3,5)
    ypositions=[range(1,14,2),range(1,14,2),range(1,14,2)] # 7 lignes indicées 1,3,5,7,9,11,13 (centre)
    zones = [[0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0]]
    #print(largeur_ecran, hauteur_ecran, xpositions, ypositions)
    for i in range(0,3,1):
        for j in range(0,7,1):
            place_texte_xy(strings[i][j], textsize, int(xpositions[i][j] * largeur_ecran / 6), int(ypositions[i][j] * hauteur_ecran / 14))
            #print(int(xpositions[i][j] * largeur_ecran/6), int(ypositions[i][j] * hauteur_ecran/14))


def display_2AFC(gauche,droite):
    #global largeur_ecran,hauteur_ecran,scale,textsize
    strings=[gauche,droite]
    blank_screen()
    xpositions=[1,3] # 1,3 = 2 colonnes (indicées 1,3)
    ypositions=[1,1] # 2 lignes centrées
    zones = [0,0]
    #print(largeur_ecran, hauteur_ecran, xpositions, ypositions)
    for i in range(0,2,1):
        for j in range(0,1,1):
            place_texte_xy(strings[i], textsize, int(xpositions[i] * largeur_ecran / 4), int(ypositions[i] * hauteur_ecran / 2))
            #print(int(xpositions[i][j] * largeur_ecran / 6), int(ypositions[i][j] *hauteur_ecran/14))


def getanswerfrom_2AFC(x,y,responsematrix):
    global largeur_ecran,hauteur_ecran,scale
    xadd=0
    if x <= 0.0125*largeur_ecran/(3*2):
        #display_text_pos("Quitter réellement ?",10,10)
        #catchquit()
        sys.exit()
    elif x <= 1*largeur_ecran/2:
        xadd=0
    elif x <= 2*largeur_ecran/2:
        xadd=1
    reponse=responsematrix[xadd]
    pygame.event.clear()
    return reponse


def display_response_scale(levels):
    blank_bg(bgcolor)

    linewidth = int(3*scale) # Set linewidth in pixels
    linelength = int((levels*largeur_ecran/(levels+2)))
    segmentlength = int(hauteur_ecran/20)

    mainline = (linelength,linewidth) # Compute main line
    mainstart = (int(largeur_ecran-(largeur_ecran/(levels+1))),int(hauteur_ecran/2)) # x,y coordinates
    mainend = (int(largeur_ecran-(largeur_ecran/(levels+1)*levels)),int((hauteur_ecran/2))) # x,y coordinates

    segmentstarty = int((hauteur_ecran/2)-(segmentlength/2)) # Compute segment lines
    segmentendy = segmentstarty + segmentlength # Compute segment lines
    xpositions=[1,2,3,4,5,6,7] # 1,2,3 = n colonnes (indicées 1,2,3...)
    ypositions=[1,1,1,1,1,1,1] # centrées verticalement

    pygame.draw.line(window, fgcolor, mainstart, mainend, linewidth)
    for i in xpositions:
        refsize = int(textsize*.75)
        bigsize = int(refsize*1.25)
        smallsize = int(refsize*.75)
        confidence_level = i
        #segmentstartx = int(largeur_ecran-(largeur_ecran/(levels+1)*i))
        segmentstartx = int((largeur_ecran/(levels+1)*i))
        #print(confidence_level)
        segmentendx = segmentstartx
        pygame.draw.line(window,fgcolor,(segmentstartx,segmentstarty),(segmentendx,segmentendy),linewidth)
        place_texte_xy(str(i),refsize,segmentstartx,segmentstarty+2*segmentlength)
    place_texte_xy("Certain",smallsize, int(largeur_ecran-(largeur_ecran/(levels+1)*1)),segmentstarty+4*segmentlength)
    place_texte_xy("Moyennement certain",smallsize,int(largeur_ecran/2),segmentstarty+4*segmentlength)
    place_texte_xy("Pas du tout certain",smallsize,int(largeur_ecran-(largeur_ecran/(levels+1)*levels)),segmentstarty+4*segmentlength)
    pygame.display.flip() # Flip the display to actually produce the drawing
    return mainline


def getanswerfrom_response_scale(x,levels,responsematrix):
    #global largeur_ecran,hauteur_ecran,scale
    xadd=0
    if x <= 0.0125*largeur_ecran/(3*2):
        #display_text_pos("Quitter réellement ?",10,10)
        #catchquit()
        sys.exit()
    elif x <= 1.5*largeur_ecran/(levels+1):
        xadd=0
    elif x <= 2.5*largeur_ecran/(levels+1):
        xadd=1
    elif x <= 3.5*largeur_ecran/(levels+1):
        xadd=2
    elif x <= 4.5*largeur_ecran/(levels+1):
        xadd=3
    elif x <= 5.5*largeur_ecran/(levels+1):
        xadd=4
    elif x <= 6.5*largeur_ecran/(levels+1):
        xadd=5
    elif x <= 8*largeur_ecran/(levels+1):
        xadd=6
    reponse=responsematrix[xadd]
    pygame.event.clear()
    return reponse
   




## Time functions

def pause(ms):
    pygame.time.delay(ms)













## Keyboard functions

def catchquit():
    pygame.event.pump()
#        tic = pygame.time.get_ticks()
#	toc = tic
    while True:#toc-tic < 3000:
        #toc = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_q:
                    sys.exit()
                else:
                    return
            return
        #print(event.key)
        #sys.exit()
    pygame.event.clear()

def waitforspacekey():
    pygame.event.clear()
    pygame.event.pump()
    while 1:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    pygame.time.wait(10)
                    pygame.event.clear()
            elif event.key == K_ESCAPE:
                sys.exit()
        return
    pygame.event.clear()


def waitforescapekey():
    pygame.event.clear()
    pygame.event.pump()
    while 1:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == 27:
                    pygame.time.wait(10)
                    pygame.event.clear()
                    return
    pygame.event.clear()


def waitforkeypress():
    #pygame.event.set_blocked(None) # Re-enable all events
    pygame.event.set_allowed([MOUSEMOTION,MOUSEBUTTONUP,MOUSEBUTTONDOWN,KEYDOWN,KEYUP]) # Block
    pygame.event.clear()
    pygame.event.pump()
    while 1:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit()
                else:
                    pygame.time.wait(10)
                    pygame.event.clear()
                    return
    pygame.event.clear()


## Mouse functions
def catchmouseOrQuit():
    """ Wait for mouse click and return x,y coordinates and button id in a [x,y,button] list.
    
    x and y are scalars.
    button is a list [1,0,0] = left.
    
    QUIT if (x, y) button == (0, 0)

    """
    done = False
    quitnow = False
    pygame.event.set_blocked([MOUSEMOTION,MOUSEBUTTONUP]) # Block
                                                          # specific
                                                          # events
    pygame.event.clear() # Clear the event buffer from the queue
    pygame.event.pump() # Update the event buffer
    #pygame.event.set_blocked([MOUSEMOTION,MOUSEBUTTONUP,KEYDOWN,KEYUP]) # Block
    #pygame.event.wait() # Wait for an event
    while not done:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                quitnow = True
                #if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    #sys.exit()
                    #quitnow = True
                    #pygame.quit()
            elif event.type == MOUSEBUTTONDOWN: # If a mouse button is pressed
                (x, y) = pygame.mouse.get_pos() # Get the current coordinates of the mouse
                print((x,y)); # Print these coordinates on the output
                button = pygame.mouse.get_pressed()
                done = True
    pygame.event.set_allowed([MOUSEMOTION, MOUSEBUTTONUP, KEYUP]) # Block
    #pygame.event.set_blocked(None) # Re-enable all events
    pygame.event.clear()
    if done == True:
        if (x, y) == (0, 0):
            pygame.quit()
        else:
            return(x, y, button)
    #elif quitnow == True:
    #    pygame.quit()



def catchmouse():
    """ Wait for mouse click and return x,y coordinates and button id in a [x,y,button] list.
    
    x and y are scalars.
    button is a list [1,0,0] = left.

    """
    pygame.event.set_blocked([MOUSEMOTION,MOUSEBUTTONUP,KEYDOWN,KEYUP]) # Block
                                                          # specific
                                                          # events
    pygame.event.clear() # Clear the event buffer from the queue
    pygame.event.pump() # Update the event buffer
    #pygame.event.set_blocked([MOUSEMOTION,MOUSEBUTTONUP,KEYDOWN,KEYUP]) # Block
    pygame.event.wait() # Wait for an event
    if pygame.mouse.get_pressed(): # If a mouse button is pressed
        (x,y) = pygame.mouse.get_pos() # Get the current coordinates of the mouse
            ##print((x,y)); # Print these coordinates on the output
        button = pygame.mouse.get_pressed()
    pygame.event.set_allowed([MOUSEMOTION,MOUSEBUTTONUP,MOUSEBUTTONDOWN,KEYDOWN,KEYUP]) # Block
    #pygame.event.set_blocked(None) # Re-enable all events
    pygame.event.clear()
    return(x,y,button)


def catchmouseleft():
    """ Wait for left mouse click and return x,y coordinates and button id (always "left") in a [x,y,button] list."""
    pygame.event.clear() # Clear the event buffer from the queue
    pygame.event.pump() # Update the event buffer
    pygame.event.set_blocked([MOUSEMOTION,MOUSEBUTTONUP,KEYDOWN,KEYUP]) # Block
                                                          # specific
                                                          # events
    pygame.event.wait() # Wait for an event
    if pygame.mouse.get_pressed() == (1,0,0): # If a mouse button is pressed
        (x,y) = pygame.mouse.get_pos() # Get the current coordinates of the mouse
        button = "left"
        #print(pygame.mouse.get_pressed())
    pygame.event.set_allowed() # Re-enable all events
    pygame.event.clear()
    return(x,y,button)






















def main2():
    #   window.blit(background, (0, 0))
    #   pygame.display.flip()
    #change_color(fgcolor)
    #pygame.time.wait(2000)
    #splash()
    draw_button(background, fgcolor, (200-50,300-50))
    loc = draw_button(background, fgcolor, (600-50,300-50))
    pygame.time.wait(2000)
    blank(loc)
    pygame.time.wait(2000)
    blank(background)
    draw_2buttons(background, fgcolor)
    pygame.time.wait(2000)
    blank(background)
    pygame.time.wait(2000)
    pygame.display.quit()




def runtheexperiment(results):
    material = read_data("text-file-2.txt")
    for i in range(0,len(material)):
        # Puts the mouse cursor at # the center of the screen.
        pygame.mouse.set_pos((background.get_rect().centerx,background.get_rect().centery))
        blank_bg(red)
        bpygame.time.delay(ISI)
        background.fill(bgcolor) # Blank the background surface
        window.blit(background, (0,0)) # Blit it
        
        display_text_pos("[b]",width/4,height/2)
        display_text_pos("[p]",3*width/4,height/2)
        pygame.display.flip() # Flip the display
        (x,y,button) = catchmouse()
        if button == (1,0,0):
            button = "left"
        elif button == (0,1,0):
            button = "right"
        print(x)
        if x < width/2:
            answer = "b"
        else:
            answer = "p"
        data = (str(i+1)+";"+material[i][0]+";"+material[i][1]+";"+str(x)+";"+str(y)+";"+str(button)+";"+answer+"\n")
        #results.write(str(data)+"\n")
        #data = (str(i+1)+";"+nom+";"+nb+"\n")
        results.write(data)
        results.flush # Actually write data after each trial (so no data is lost)


    
def whatpause(ms):
    pygame.time.delay(ms)

def whatread_data(filepath): # Function to load the contents of a text
                         # file into a 2D table
    table=[] # Create an empty list
    datafile=open(filepath,'r') # Open file for reading
    for line in datafile.readlines(): # For each line in the text file
                                      # This keeps \n at end of line
        cleandata = string.replace(line,'\n','') # Remove \n at end of line
                                          # (from string.replace)
        oneline = re.split(",",cleandata) # Split file at commas
        table.append(oneline) # Append the line at end of table
    datafile.close() # Close the file
    return table


def whatcleanup(line):
    data = string.replace(line,'\n','')
    return data

def whatload_data():
    data = read_data(sys.argv[1])
    return data


def place_texte_xy(string,size,x,y): # Usage : place_texte_xy('texte',32,200,300)
    font = pygame.font.Font(selectedFont, int(size*scale))
    text = font.render(string, 1, fgcolor)
    textpos = text.get_rect()
    textsize = text.get_size()
    textpos.centerx = x
    textpos.centery = y
    window.blit(text, textpos) # Blits the text to the coordinates
    pygame.display.flip() # Flip the display
    
    
def whatblank_bg(color):
    background.fill(color)
    window.blit(background, (0,0))
    pygame.display.flip()


def whatpause(ms):
    pygame.time.delay(ms)

def quitthegame():
	sys.exit('\ninterrupted by the user !!!')

def whatcatchmouse(): # Usage : (xcoord,ycoord,bouton) = catchmouse()
    pygame.event.clear() # Clear the event buffer from the queue
    pygame.event.pump() # Update the event buffer
    pygame.event.set_blocked([MOUSEMOTION,MOUSEBUTTONUP,KEYDOWN,KEYUP]) # Block specific events
    pygame.event.wait() # Wait for an event
    if pygame.mouse.get_pressed(): # If a mouse button is pressed
        (x,y) = pygame.mouse.get_pos() # Get the current coordinates of the mouse
        #print((x,y)); # Print these coordinates on the output
        button = pygame.mouse.get_pressed()
    #pygame.event.set_allowed() # Re-enable all events
    pygame.event.clear()
    return x,y,button


def whatblank_screen():
    window.fill(bgcolor)
    window.blit(background, (0, 0))


def whatread_data_2D(filepath): # Function to load the contents of a text
                        # file into a 2D table
    table=[] # Create an empty list
    datafile=open(filepath,'r') # Open file for reading
    for line in datafile.readlines(): # For each line in the text file
                                    # This keeps \n at end of line
        cleandata = string.replace(line,'\n','') # Remove \n at end of line
                                        # (from string.replace)
        oneline = re.split(";",cleandata) # Split file at commas
        table.append(oneline) # Append the line at end of table
    datafile.close() # Close the file
    return table


def whatcleanup(line):
    data = string.replace(line,'\n','')
    return data






# End of caterpyllar.py
