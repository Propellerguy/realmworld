import pygame
pygame.init()
import console
import random
import greetz
from qg import qg
import qnet2
import hasher

screen = pygame.display.set_mode((640,480))
pygame.display.set_caption('WORLD')

con = console.TextConsole(screen,console.ConFont())

con.printf('+'+chr(196)*28+'+\n')
con.printf(chr(179)+' (C) 2017 Propellerguy      '+chr(179)+'\n')
con.printf(chr(179)+' MIT Licensed               '+chr(179)+'\n')
con.printf('+'+chr(196)*28+'+\n')
con.printf('\n')
con.printf(greetz.greetz())
con.printf('\n\n')

# if con.yesno('Would you like to update today (y/n)? '):
#     mirror = qg('mirror')
#     con.printf('Using '+mirror+'\n')
#     con.printf('Connecting...\n\n')
#     connection = qnet2.Connection(mirror,9875)
#     connected = False
#     try:
#         connection.converse('who')
#         connected = True
#     except:
#         con.printf( 'Unable to connect.\n\n')
#
#     if connected: 
#         con.printf(connection.converse('who')+': '+connection.converse('motd')+'\n\n')
#         con.printf('Computing hashes recursively...')
#         hashes = hasher.all_hashes()