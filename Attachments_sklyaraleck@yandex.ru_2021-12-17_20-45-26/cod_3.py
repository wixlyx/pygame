from pygame import mixer
import pygame
from pygame.transform import scale
import time
import threading
def stakan_size(n, g):
    if int(current_task[n])==max(list(map(int, current_task[0:stakans_amount]))):
        return 125
    elif int(current_task[n])==min(list(map(int, current_task[0:stakans_amount]))):
        return 75
    else:
        return 75 + (int(current_task[n])-min(list(map(int, current_task[0:stakans_amount]))))*(50/(max(list(map(int, current_task[0:stakans_amount]))) - min(list(map(int, current_task[0:stakans_amount])))))
class stakan(pygame.sprite.Sprite):
    def __init__(self, x , y):
        pygame.sprite.Sprite.__init__(self)
        self.imaga = scale(pygame.image.load("feel-trans.png"), (120, 45))
        self.image = scale(pygame.image.load("feel-trans1.png"), (120, 45))
        self.x = x
        self.y = y
    def draw(self,screen):
        if pygame.mouse.get_pos()[0] in range(15, 65) and pygame.mouse.get_pos()[1] in range(85, 135):
            screen.blit(scale(pygame.image.load("restart_grey.png"), (50, 50)),(15, 70))
        else:
            screen.blit(scale(pygame.image.load("restart.png"), (50, 50)),(15, 70))
    def work1(self,size1,size2,size3, size4,mousex,mousey,tap,need):
        global action,have1,have2,have3, have4,chosen,sound, previous_water_1,sound1
        if have1!=0:
             pouring_1 = True
        else:
            pouring_1 = False
        if stakans_amount<4:
            have4 = 0
            size4 = 0
            if stakans_amount<3:
                size3 = 0
                have3 = 0
        if ((mousex > space+stakan1.x//2-60 and mousex < space+stakan1.x//2+60) and (mousey < 479 and mousey > 434 )):
            screen.blit(self.image, (space+stakan1.x//2-60, 434))
        else:
            screen.blit(self.imaga, (space+stakan1.x//2-60, 434))
        screen.blit(scale(pygame.image.load("stakan.png"), (self.x, self.y)), (space, 390-self.y))
        if previous_water_1<round(stakan1.y/size1*have1):
            if round(stakan1.y/size1*have1)-previous_water_1<5:
                previous_water_1=round(stakan1.y/size1*have1)
            else:
                previous_water_1+=5
        elif previous_water_1>round(stakan1.y/size1*have1):
            if previous_water_1-round(stakan1.y/size1*have1)<5:
                previous_water_1=round(stakan1.y/size1*have1)
            else:
                previous_water_1-=5
        if previous_water_1!=0:
            pygame.draw.rect(screen, (64, 128, 255), (space, 390 - previous_water_1, stakan1.x, previous_water_1))
        screen.blit(scale(pygame.image.load("stakan.png"), (self.x, self.y)), (space, 390-self.y))
        if ((mousex > space+stakan1.x//2-60 and mousex < space+stakan1.x//2+60) and (mousey < 537 and mousey > 492 )):
            screen.blit(self.image, (space+stakan1.x//2-60, 492))
        else:
            screen.blit(self.imaga, (space+stakan1.x//2-60, 492))
        if pouring_1 or chosen == 'ограниченный долив':
            screen.blit(pygame.font.SysFont('Nunito-ExtraLight.ttf', 25).render('ВЫЛИТЬ', 1, (1, 1, 1)), (space+stakan1.x//2- 35, 507))
        else:
            screen.blit(pygame.font.SysFont('Nunito-ExtraLight.ttf', 25).render('ЗАПОЛНИТЬ', 1, (1, 1, 1)), (space+stakan1.x//2-52, 507))
        screen.blit(pygame.font.SysFont('Nunito-ExtraLight.ttf', 25).render('ПЕРЕЛИТЬ', 1, (1, 1, 1)), (space+stakan1.x//2-44, 448))
        if chosen == 'ограниченный долив' and (size1 >= size2 and size1 >= size3 and size1>=size4) and hon == 1:
            have1 = size1
            previous_water_1 = stakan1.y
            hon ==2
        if have1 == need:
            if action<= min_motions:
                changer = tasks_texts[task_num-1].split()
                changer[-1] = '1'
                tasks_texts[task_num-1] = ' '.join(changer)
                file = open(chosen+'.txt', 'w', encoding = 'utf-8')
                file.write('\n'.join(tasks_texts))
                file.close()
            if int(tasks_texts[task_num-1].split()[-2])>action or int(tasks_texts[task_num-1].split()[-2])==0:
                record = tasks_texts[task_num-1].split()
                record[-2] = str(action)
                tasks_texts[task_num-1] = ' '.join(record)
                file = open(chosen+'.txt', 'w', encoding = 'utf-8')
                file.write('\n'.join(tasks_texts))
                file.close()
        if (mousex > 15 and mousex < 65) and (mousey < 135 and mousey > 70 ) and tap:
            action = 0
            have1 = 0
            have2 = 0
            hon = 1
            if stakans_amount>2:
                have3 = 0
            if stakans_amount>3:
                have4 = 0
        if ((mousex > space+stakan1.x//2-60 and mousex < space+stakan1.x//2+60) and (mousey < 537 and mousey > 492 )) and tap:
            if pouring_1:
                sound1.stop()
                sound2.stop()
                sound1.play(0)
                have1 = 0
                action+=1
            elif have1!=size1 and chosen == 'бесконечный долив':
                sound1.stop()
                sound2.stop()
                sound1.play(0)
                have1 = size1
                action+=1
        elif ((mousex > space+stakan1.x//2-60 and mousex < space+stakan1.x//2+60) and (mousey < 479 and mousey > 434 )) and tap and have1 != 0 :
            action+=1
            h1=0 
            while h1==0:
                if previous_water_1!=0:
                    pygame.draw.rect(screen, (64, 128, 255), (space, 390 - previous_water_1, stakan1.x, previous_water_1))
                for i in pygame.event.get():
                    if i.type == pygame.MOUSEBUTTONDOWN:
                        if i.button == 1:
                            sound1.stop()
                            sound2.stop()
                            sound.play(0)
                            if (i.pos[0] > space*2+stakan1.x and i.pos[0] < space*2+stakan1.x+stakan2.x) and (i.pos[1] > 390-stakan2.y and i.pos[1] < 390 ) and have2 != size2  :
                                sound1.stop()
                                sound2.stop()
                                sound1.play(0)
                                have2 = have1+have2
                                have1 = 0
                                if have2 > size2 :
                                    have1 = have2-size2
                                    have2 = size2                
                                h1=1
                            if stakans_amount>2:
                                if (i.pos[0] > space*3+stakan1.x+stakan2.x and i.pos[0] < space*3+stakan1.x+stakan2.x+stakan3.x ) and (i.pos[1] > 390-stakan3.y and i.pos[1] < 390 ) and have3 != size3:
                                    sound1.stop()
                                    sound2.stop()
                                    sound1.play(0)
                                    have3 = have1+have3
                                    have1 = 0
                                    if have3 > size3 :
                                        have1 = have3-size3
                                        have3 = size3
                                    h1=1
                                if stakans_amount>3:
                                    if (i.pos[0] > space*4+stakan1.x+stakan2.x+stakan3.x and i.pos[0] < space*4+stakan1.x+stakan2.x+stakan3.x+stakan4.x ) and (i.pos[1] > 390-stakan4.y and i.pos[1] < 390 ) and have4 != size4:
                                        sound1.stop()
                                        sound2.stop()
                                        sound1.play(0)
                                        have4 = have1+have4
                                        have1 = 0
                                        if have4 > size4 :
                                            have1 = have4-size4
                                            have4= size4
                                        h1=1                       
        have1 = str(have1)
        size1 = str(size1)
        text3 = pygame.font.SysFont('Comic Sans MS', 22).render(have1 + '/' + size1, 1, (1, 1, 1))
        screen.blit(text3, (space+stakan1.x//2-13, 395))
        size1 = int (size1)
        have1 = int(have1)
    def work2(self,size1,size2,size3, size4,mousex,mousey,tap,need):
        global action,have1,have2,have3,have4,chosen,sound,previous_water_2,sound1
        if have2!=0:
             pouring_2 = True
        else:
            pouring_2 = False
        if stakans_amount<4:
            have4 = 0
            size4 = 0
            if stakans_amount<3:
                have3 = 0
                size3 = 0
        if ((mousex > space*2+stakan1.x+stakan2.x//2-60 and mousex < space*2+stakan1.x+stakan2.x//2+60) and (mousey < 479 and mousey > 434 )):
            screen.blit(self.image, (space*2+stakan1.x+stakan2.x//2-60, 434))
        else:
            screen.blit(self.imaga, (space*2+stakan1.x+stakan2.x//2-60, 434))
        if previous_water_2<round(stakan2.y/size2*have2):
            if round(stakan2.y/size2*have2)-previous_water_2<5:
                previous_water_2=round(stakan2.y/size2*have2)
            else:
                previous_water_2+=5
        elif previous_water_2>round(stakan2.y/size2*have2):
            if previous_water_2-round(stakan1.y/size2*have2)<5:
                previous_water_2=round(stakan1.y/size2*have2)
            else:
                previous_water_2-=5
        if previous_water_2!=0:
            pygame.draw.rect(screen, (64, 128, 255), (space*2+stakan1.x, 390 - previous_water_2, stakan2.x, previous_water_2))
        screen.blit(scale(pygame.image.load("stakan.png"), (self.x, self.y)), (space*2+stakan1.x, 390-self.y))
        if ((mousex > space*2+stakan1.x+stakan2.x//2-60 and mousex < space*2+stakan1.x+stakan2.x//2+60) and (mousey < 537 and mousey > 492 )):
            screen.blit(self.image, (space*2+stakan1.x+stakan2.x//2-60, 492))
        else:
            screen.blit(self.imaga, (space*2+stakan1.x+stakan2.x//2-60, 492))
        if pouring_2 or chosen == 'ограниченный долив':
            screen.blit(pygame.font.SysFont('Nunito-ExtraLight.ttf', 25).render('ВЫЛИТЬ', 1, (1, 1, 1)), (space*2+stakan1.x+stakan2.x//2-35, 507))
        else:
            screen.blit(pygame.font.SysFont('Nunito-ExtraLight.ttf', 25).render('ЗАПОЛНИТЬ', 1, (1, 1, 1)), (space*2+stakan1.x+stakan2.x//2-52, 507))
        screen.blit(pygame.font.SysFont('Nunito-ExtraLight.ttf', 25).render('ПЕРЕЛИТЬ', 1, (1, 1, 1)), (space*2+stakan1.x+stakan2.x//2-44, 448))
        if chosen == 'ограниченный долив' and (size2 >= size1 and size2 >= size3 and size2>=size4) and hon ==1 :
            hon = 2
            have2 = size2
            previous_water_2 = stakan2.y
        if have2 == need:
            if action<= min_motions:
                changer = tasks_texts[task_num-1].split()
                changer[-1] = '1'
                tasks_texts[task_num-1] = ' '.join(changer)
                file = open(chosen+'.txt', 'w', encoding = 'utf-8')
                file.write('\n'.join(tasks_texts))
                file.close()
            if int(tasks_texts[task_num-1].split()[-2])>action or int(tasks_texts[task_num-1].split()[-2])==0:
                record = tasks_texts[task_num-1].split()
                record[-2] = str(action)
                tasks_texts[task_num-1] = ' '.join(record)
                file = open(chosen+'.txt', 'w', encoding = 'utf-8')
                file.write('\n'.join(tasks_texts))
                file.close()
        if (mousex > 15 and mousex < 65) and (mousey < 135 and mousey > 70 ) and tap:
            action = 0
            have1 = 0
            have2 = 0
            hon = 1
            if stakans_amount>2:
                have3 = 0
            if stakans_amount>3:
                have4 = 0
        if ((mousex > space*2+stakan1.x+stakan2.x//2-60 and mousex < space*2+stakan1.x+stakan2.x//2+60) and (mousey < 537 and mousey > 492 )) and tap:
            if pouring_2:
                sound1.stop()
                sound2.stop()
                sound1.play(0)
                have2 = 0
                action+=1
            elif have2!=size2 and chosen == 'бесконечный долив':
                sound1.stop()
                sound2.stop()
                sound1.play(0)
                have2 = size2
                action+=1
        elif ((mousex > space*2+stakan1.x+stakan2.x//2-60 and mousex < space*2+stakan1.x+stakan2.x//2+60) and (mousey < 479 and mousey > 434 )) and tap and have2 != 0:
            action+=1
            h2=0
            while h2==0:
                for x in pygame.event.get():
                    if x.type == pygame.MOUSEBUTTONDOWN:
                        if x.button == 1:
                            sound1.stop()
                            sound2.stop()
                            sound.play(0)
                            if (x.pos[0] > space and x.pos[0] < space+stakan1.x) and (x.pos[1] < 390 and x.pos[1] > 390-stakan1.y ) and have1 != size1:
                                sound1.stop()
                                sound2.stop()
                                sound1.play(0)
                                have1 = have2+have1
                                have2 = 0
                                if have1 > size1 :
                                    have2 = have1-size1
                                    have1 = size1
                                h2=1
                            if stakans_amount>2:
                                if (x.pos[0] > space*3+stakan1.x+stakan2.x and x.pos[0] < space*3+stakan1.x+stakan2.x+stakan3.x ) and (x.pos[1] > 390-stakan3.y and x.pos[1] < 390 ) and have3 != size3 :
                                    sound1.stop()
                                    sound2.stop()
                                    sound1.play(0)
                                    have3 = have2+have3
                                    have2 = 0
                                    if have3 > size3 :
                                        have2 = have3-size3
                                        have3 = size3
                                    h2=1
                                if stakans_amount>3:
                                    if (x.pos[0] > space*4+stakan1.x+stakan2.x+stakan3.x and x.pos[0] < space*4+stakan1.x+stakan2.x+stakan3.x+stakan4.x ) and (x.pos[1] > 390-stakan4.y and x.pos[1] < 390 ) and have4 != size4:
                                        sound1.stop()
                                        sound2.stop()
                                        sound1.play(0)
                                        have4 = have2+have4
                                        have2 = 0
                                        if have4 > size4 :
                                            have2 = have4-size4
                                            have4= size4
                                        h2=1  
        have2 = str(have2)
        size2 = str(size2)
        text2 = pygame.font.SysFont('Comic Sans MS', 22).render(have2 + '/' + size2, 1, (1, 1, 1))
        screen.blit(text2, (space*2+stakan1.x+stakan2.x//2-13, 395))
        have2 = int (have2)
        size2 = int (size2)
    def work3(self,size1,size2,size3, size4,mousex,mousey,tap,need):
        global action,have1,have2,have3, have4,chosen,hon,sound, previous_water_3
        if have3!=0:
             pouring_3 = True
        else:
            pouring_3 = False
        if stakans_amount<4:
            size4 = 0
        if ((mousex > space*3+stakan1.x+stakan2.x+stakan3.x//2-60 and mousex < space*3+stakan1.x+stakan2.x+stakan3.x//2+60) and (mousey < 479 and mousey > 434 )):
            screen.blit(self.image, (space*3+stakan1.x+stakan2.x+stakan3.x//2-60, 434))
        else:
            screen.blit(self.imaga, (space*3+stakan1.x+stakan2.x+stakan3.x//2-60, 434))
        if previous_water_3<round(stakan3.y/size3*have3):
            if round(stakan3.y/size3*have3)-previous_water_3<5:
                previous_water_3=round(stakan3.y/size3*have3)
            else:
                previous_water_3+=5
        elif previous_water_3>round(stakan3.y/size3*have3):
            if previous_water_3-round(stakan3.y/size3*have3)<5:
                previous_water_3=round(stakan3.y/size3*have3)
            else:
                previous_water_3-=5
        if previous_water_3!=0:
            pygame.draw.rect(screen, (64, 128, 255), (space*3+stakan1.x+stakan2.x, 390 - previous_water_3, stakan3.x, previous_water_3))
        screen.blit(scale(pygame.image.load("stakan.png"), (self.x, self.y)), (space*3+stakan1.x+stakan2.x, 390-self.y))
        if ((mousex > space*3+stakan1.x+stakan2.x+stakan3.x//2-60 and mousex < space*3+stakan1.x+stakan2.x+stakan3.x//2+60) and (mousey < 537 and mousey > 492)):
            screen.blit(self.image, (space*3+stakan1.x+stakan2.x+stakan3.x//2-60, 492))
        else:
            screen.blit(self.imaga, (space*3+stakan1.x+stakan2.x+stakan3.x//2-60, 492))
        if pouring_3 or chosen == 'ограниченный долив':
            screen.blit(pygame.font.SysFont('Nunito-ExtraLight.ttf', 25).render('ВЫЛИТЬ', 1, (1, 1, 1)), (space*3+stakan1.x+stakan2.x+stakan3.x//2-35, 507))
        else:
            screen.blit(pygame.font.SysFont('Nunito-ExtraLight.ttf', 25).render('ЗАПОЛНИТЬ', 1, (1, 1, 1)), (space*3+stakan1.x+stakan2.x+stakan3.x//2-52, 507))
        screen.blit(pygame.font.SysFont('Nunito-ExtraLight.ttf', 25).render('ПЕРЕЛИТЬ', 1, (1, 1, 1)), (space*3+stakan1.x+stakan2.x+stakan3.x//2-44, 448))
        if chosen == 'ограниченный долив' and size3 >= size2 and size3 >= size1 and size3 >= size4 and hon == 1 :
            have3 = size3
            hon = 2
            previous_water_3 = stakan3.y
        if have3 == need:
            if action<= min_motions:
                changer = tasks_texts[task_num-1].split()
                changer[-1] = '1'
                tasks_texts[task_num-1] = ' '.join(changer)
                file = open(chosen+'.txt', 'w', encoding = 'utf-8')
                file.write('\n'.join(tasks_texts))
                file.close()
            if int(tasks_texts[task_num-1].split()[-2])>action or int(tasks_texts[task_num-1].split()[-2])==0:
                record = tasks_texts[task_num-1].split()
                record[-2] = str(action)
                tasks_texts[task_num-1] = ' '.join(record)
                file = open(chosen+'.txt', 'w', encoding = 'utf-8')
                file.write('\n'.join(tasks_texts))
                file.close()
        if (mousex > 15 and mousex < 65) and (mousey < 135 and mousey > 70 ) and tap:
            action = 0
            have1 = 0
            have2 = 0
            have3 =0
            hon = 1
            if stakans_amount>3:
                have4 = 0
        if ((mousex > space*3+stakan1.x+stakan2.x+stakan3.x//2-60 and mousex < space*3+stakan1.x+stakan2.x+stakan3.x//2+60) and (mousey < 537 and mousey > 492)) and tap:
            if pouring_3:
                sound1.stop()
                sound2.stop()
                sound1.play(0)
                have3 = 0
                action+=1
            elif have3!=size3 and chosen == 'бесконечный долив':
                sound1.stop()
                sound2.stop()
                sound1.play(0)
                have3 = size3
                action+=1
        elif ((mousex > space*3+stakan1.x+stakan2.x+stakan3.x//2-60 and mousex < space*3+stakan1.x+stakan2.x+stakan3.x//2+60) and (mousey < 479 and mousey > 434 )) and tap and have3 != 0 :
            action+=1
            h3=0    
            while h3==0:
                for p in pygame.event.get():   
                    if p.type == pygame.MOUSEBUTTONDOWN:
                        if p.button == 1:
                            sound1.stop()
                            sound2.stop()
                            sound.play(0)
                            if (p.pos[0] > space and p.pos[0] < space+stakan1.x) and (p.pos[1] < 390 and p.pos[1] > 390-stakan1.y ) and have1 != size1:
                                sound1.stop()
                                sound2.stop()
                                sound1.play(0)
                                have1 = have3+have1
                                have3 = 0
                                if have1 > size1 :
                                    have3 = have1-size1
                                    have1 = size1
                                h3=1
                            elif (p.pos[0] > space*2+stakan1.x and p.pos[0] < space*2+stakan1.x+stakan2.x) and (p.pos[1] > 390-stakan2.y and p.pos[1] < 390 ) and have2 != size2:
                                sound1.stop()
                                sound2.stop()
                                sound1.play(0)
                                have2 = have3+have2
                                have3 = 0
                                if have2 > size2 :
                                    have3 = have2-size2
                                    have2 = size2
                                h3=1
                            if stakans_amount>3:
                                if (p.pos[0] > space*4+stakan1.x+stakan2.x+stakan3.x and p.pos[0] < space*4+stakan1.x+stakan2.x+stakan3.x+stakan4.x ) and (p.pos[1] > 390-stakan4.y and p.pos[1] < 390 ) and have4 != size4:
                                    sound1.stop()
                                    sound2.stop()
                                    sound1.play(0)
                                    have4 = have3+have4
                                    have3 = 0
                                    if have4 > size4 :
                                        have3 = have4-size4
                                        have4= size4
                                    h3=1
        have3 = str(have3)
        size3 = str(size3)
        text1 = pygame.font.SysFont('Comic Sans MS', 22).render(have3 + '/' + size3, 1, (1, 1, 1))
        screen.blit(text1, (space*3+stakan1.x+stakan2.x+stakan3.x//2-13, 395))
        have3 = int (have3)
        size3 = int (size3)
    def work4(self,size1,size2,size3, size4,mousex,mousey,tap,need):
        global action,have1,have2,have3,have4,chosen,hon,sound, previous_water_4
        if have4!=0:
             pouring_4 = True
        else:
            pouring_4 = False
        if ((mousex > space*4+stakan1.x+stakan2.x+stakan3.x+stakan4.x//2-60 and mousex < space*4+stakan1.x+stakan2.x+stakan3.x+stakan4.x//2+60) and (mousey < 479 and mousey > 434 )):
            screen.blit(self.image, (space*4+stakan1.x+stakan2.x+stakan3.x+stakan4.x//2-60, 434))
        else:
            screen.blit(self.imaga, (space*4+stakan1.x+stakan2.x+stakan3.x+stakan4.x//2-60, 434))
        if previous_water_4<round(stakan4.y/size4*have4):
            if round(stakan4.y/size4*have4)-previous_water_4<5:
                previous_water_4=round(stakan4.y/size4*have4)
            else:
                previous_water_4+=5
        elif previous_water_4>round(stakan4.y/size4*have4):
            if previous_water_4-round(stakan4.y/size4*have4)<5:
                previous_water_4=round(stakan4.y/size4*have4)
            else:
                previous_water_4-=5
        if previous_water_4!=0:
            pygame.draw.rect(screen, (64, 128, 255), (space*4+stakan1.x+stakan2.x+stakan3.x, 390 - previous_water_4, stakan4.x, previous_water_4))
        screen.blit(scale(pygame.image.load("stakan.png"), (self.x, self.y)), (space*4+stakan1.x+stakan2.x+stakan3.x, 390-self.y))
        if ((mousex > space*4+stakan1.x+stakan2.x+stakan3.x+stakan4.x//2-60 and mousex < space*4+stakan1.x+stakan2.x+stakan3.x+stakan4.x//2+60) and (mousey < 537 and mousey > 492)):
            screen.blit(self.image, (space*4+stakan1.x+stakan2.x+stakan3.x+stakan4.x//2-60, 492))
        else:
            screen.blit(self.imaga, (space*4+stakan1.x+stakan2.x+stakan3.x+stakan4.x//2-60, 492))
        if pouring_4 or chosen == 'ограниченный долив':
            screen.blit(pygame.font.SysFont('Nunito-ExtraLight.ttf', 25).render('ВЫЛИТЬ', 1, (1, 1, 1)), (space*4+stakan1.x+stakan2.x+stakan3.x+stakan4.x//2-35, 507))
        else:
            screen.blit(pygame.font.SysFont('Nunito-ExtraLight.ttf', 25).render('ЗАПОЛНИТЬ', 1, (1, 1, 1)), (space*4+stakan1.x+stakan2.x+stakan3.x+stakan4.x//2-52, 507))
        screen.blit(pygame.font.SysFont('Nunito-ExtraLight.ttf', 25).render('ПЕРЕЛИТЬ', 1, (1, 1, 1)), (space*4+stakan1.x+stakan2.x+stakan3.x+stakan4.x//2-44, 448))
        if chosen == 'ограниченный долив' and size4 >= size2 and size4 >= size1 and  size4 >=size3 and hon == 1 :
            have4 = size4
            hon = 2
            previous_water_4 = stakan4.y
        if have4 == need:
            if action<= min_motions:
                changer = tasks_texts[task_num-1].split()
                changer[-1] = '1'
                tasks_texts[task_num-1] = ' '.join(changer)
                file = open(chosen+'.txt', 'w', encoding = 'utf-8')
                file.write('\n'.join(tasks_texts))
                file.close()
            if int(tasks_texts[task_num-1].split()[-2])>action or int(tasks_texts[task_num-1].split()[-2])==0:
                record = tasks_texts[task_num-1].split()
                record[-2] = str(action)
                tasks_texts[task_num-1] = ' '.join(record)
                file = open(chosen+'.txt', 'w', encoding = 'utf-8')
                file.write('\n'.join(tasks_texts))
                file.close()
        if (mousex > 15 and mousex < 65) and (mousey < 135 and mousey > 70 ) and tap:
            action = 0
            have1 = 0
            have2 = 0
            have3 = 0
            have4 = 0
            hon = 1
        if ((mousex > space*4+stakan1.x+stakan2.x+stakan3.x+stakan4.x//2-60 and mousex < space*4+stakan1.x+stakan2.x+stakan3.x+stakan4.x//2+60) and (mousey < 537 and mousey > 492)) and tap:
            if pouring_4:
                sound1.stop()
                sound2.stop()
                sound1.play(0)
                have4 = 0
                action+=1
            elif have4!=size4 and chosen == 'бесконечный долив':
                sound1.stop()
                sound2.stop()
                sound1.play(0)
                have4 = size4
                action+=1
        elif ((mousex > space*4+stakan1.x+stakan2.x+stakan3.x+stakan4.x//2-60 and mousex < space*4+stakan1.x+stakan2.x+stakan3.x+stakan4.x//2+60) and (mousey < 479 and mousey > 434 )) and tap and have4 != 0 :
            action+=1
            h4=0    
            while h4==0:
                for p in pygame.event.get():
                    if p.type == pygame.MOUSEBUTTONDOWN:
                        if p.button == 1:
                            sound1.stop()
                            sound2.stop()
                            sound.play(0)
                            if (p.pos[0] > space and p.pos[0] < space+stakan1.x) and (p.pos[1] < 390 and p.pos[1] > 390-stakan1.y ) and have1 != size1:
                                sound1.stop()
                                sound2.stop()
                                sound1.play(0)
                                have1 = have4+have1
                                have4 = 0
                                if have1 > size1 :
                                    have4 = have1-size1
                                    have1 = size1
                                h4=1
                            elif (p.pos[0] > space*2+stakan1.x and p.pos[0] < space*2+stakan1.x+stakan2.x) and (p.pos[1] > 390-stakan2.y and p.pos[1] < 390 ) and have2 != size2:
                                sound1.stop()
                                sound2.stop()
                                sound1.play(0)
                                have2 = have4+have2
                                have4 = 0
                                if have2 > size2 :
                                    have4 = have2-size2
                                    have2 = size2
                                h4=1
                            elif (p.pos[0] > space*3+stakan1.x+stakan2.x and p.pos[0] < space*3+stakan1.x+stakan2.x+stakan3.x ) and (p.pos[1] > 390-stakan3.y and p.pos[1] < 390 ) and have3 != size3:
                                sound1.stop()
                                sound2.stop()
                                sound1.play(0)
                                have3 = have4+have3
                                have4 = 0
                                if have3 > size3 :
                                    have4 = have3-size3
                                    have3= size3
                                h4=1
        have4 = str(have4)
        size4 = str(size4)
        text1 = pygame.font.SysFont('Comic Sans MS', 22).render(have4 + '/' + size4, 1, (1, 1, 1))
        screen.blit(text1, (space*4+stakan1.x+stakan2.x+stakan3.x+stakan4.x//2-13, 395))
        have4 = int (have4)
        size4 = int (size4)
pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound('zvuk-knopki-myshi.wav')
sound1 = pygame.mixer.Sound('zvuk-chay-letsya-v-kruzhku.wav')
sound2 = pygame.mixer.Sound('den-pobedy-z_uk-1.wav')
screen = pygame.display.set_mode((750, 550))
pygame.display.set_caption("СТАКАНЧИКИ")
fon = scale(pygame.image.load("fon.jpg"), (750, 550))
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 20)
tap = False
ending = ' '
menu = True
aa = 1
bb = 1
switch = False
choice = False
task = False
win = False
MOUSEBUTTONDOWN = False
MOUSEBUTTONDOWN_1 = False
MOUSEBUTTONDOWN_2 = False
MOUSEBUTTONDOWN_3 = False
MOUSEBUTTONDOWN_4 = False
clock = pygame.time.Clock()
while True:
    for e in pygame.event.get():
        if e.type == pygame.MOUSEBUTTONDOWN:
            if e.button == 1:
                sound1.stop()
                sound2.stop()
                sound.play(0)
                tap = True
        if e.type == pygame.QUIT: 
            raise SystemExit("QUIT") 
    screen.blit(fon, (0, 0))
    if task:
        if '&' in current_task:
            stakans_amount = len(current_task[0:-5])
        else:
            stakans_amount = len(current_task[0:-3])
        if need>9 and need<21:
            ending = ' ЛИТРОВ'
        elif need % 10 == 1:
            ending = ' ЛИТР'
        elif need % 10 <= 4 and  need % 10 != 0:
            ending = ' ЛИТРА'
        else:
            ending = ' ЛИТРОВ'
        stakan1 = stakan(round(stakan_size(0, 125)),round(stakan_size(0, 125)*(194/125)))
        stakan2 = stakan(round(stakan_size(1, 125)),round(stakan_size(1, 125)*(194/125)))
        if stakans_amount>2:
            stakan3 = stakan(round(stakan_size(2, 125)),round(stakan_size(2, 125)*(194/125)))
        if stakans_amount>3:
            stakan4 = stakan(round(stakan_size(3, 125)),round(stakan_size(3, 125)*(194/125)))
        space = (750 - (stakan1.x+stakan2.x))//3
        if stakans_amount>2:
            space = (750 - (stakan1.x+stakan2.x+stakan3.x))//4
        if stakans_amount>3:
            space = (750 - (stakan1.x+stakan2.x+stakan3.x+stakan4.x))//5
        stakan1.draw(screen)
        w = pygame.mouse.get_pos()
        stakan1.work1(int(current_task[0]),int(current_task[1]),int(current_task[2]), int(current_task[3]),w[0],w[1],tap,need)
        stakan2.work2(int(current_task[0]),int(current_task[1]),int(current_task[2]), int(current_task[3]),w[0],w[1],tap,need)
        if stakans_amount>2:
            stakan3.work3(int(current_task[0]),int(current_task[1]),int(current_task[2]), int(current_task[3]),w[0],w[1],tap,need)
        if stakans_amount>3:
            stakan4.work4(int(current_task[0]),int(current_task[1]),int(current_task[2]), int(current_task[3]),w[0],w[1],tap,need)
        if have1 == need or have2 == need or have3 == need or have4 == need:
            if not(switch):
                timer = pygame.time.get_ticks()
                action_answer = action
            switch = True
        if switch and pygame.time.get_ticks() - timer > 3300:
            sound1.stop()
            sound2.stop()
            sound2.play(0)
            win = True
            task = False
        tap = False
        action = str(action)
        need = str(need)
        text = pygame.font.SysFont('Comic Sans MS', 22).render('ДЕЙСТВИЕ: '+ action, 1, (1, 1, 1))
        screen.blit(text, (100, 80))
        text7 = pygame.font.Font('8320.ttf', 35).render('ОТМЕРЬТЕ '+ need + str(ending), 1, (1, 1, 1))
        screen.blit(text7, (100, 10))
        action = int(action)
        need = int(need)
        if pygame.mouse.get_pos()[0] in range(15, 65) and pygame.mouse.get_pos()[1] in range(10, 70):
            screen.blit(scale(pygame.image.load("22_grey.png"), (50, 50)), (15, 10))
        else:
            screen.blit(scale(pygame.image.load("22.png"), (50, 50)), (15, 10))
        if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
            MOUSEBUTTONDOWN_4 = True
        if e.type == pygame.MOUSEBUTTONUP and e.button == 1:
            if e.pos[0] in range(15, 65) and e.pos[1] in range(20, 70) and MOUSEBUTTONDOWN_4:
                    task = False
                    choice = True
            MOUSEBUTTONDOWN_4=False
    elif win:
        switch = False
        screen.blit(pygame.font.Font('19363.ttf', 120).render('YOU WIN!', 1, (1,1,1)), (60, 30))
        screen.blit( pygame.font.SysFont('Comic Sans MS', 22).render('ТРЕБОВАЛОСЬ ПОЛУЧИТЬ ЛИТРОВ: '+ str(need), 1, (1, 1, 1)), (160, 290))
        screen.blit( pygame.font.SysFont('Comic Sans MS', 22).render('СКОЛЬКО ХОДОВ ПОТРЕБОВАЛОСЬ: '+ str(action_answer), 1, (1, 1, 1)), (160, 355))
        screen.blit( pygame.font.SysFont('Comic Sans MS', 22).render('РЕКОРД ПО ХОДАМ: '+ str(current_task[-1]), 1, (1, 1, 1)), (240, 420))
        if pygame.mouse.get_pos()[0] in range(340, 410) and pygame.mouse.get_pos()[1] in range(470, 540):
            screen.blit(scale(pygame.image.load("restart_grey.png"), (70, 70)),(340, 470))
            if pygame.mouse.get_pos()[0] in range(340, 410) and pygame.mouse.get_pos()[1] in range(470, 540) and tap:
                sound2.stop()
                win = False
                task = True 
                choice = False
                action = 0
                have1 = 0
                have2 = 0
                have3 = 0
                have4 = 0
                previous_water_1 = 0
                previous_water_2 = 0
                previous_water_3 = 0
                previous_water_4 = 0
        else:
            screen.blit(scale(pygame.image.load("restart.png"), (70, 70)),(340, 470))
        if pygame.mouse.get_pos()[0] in range(15, 65) and pygame.mouse.get_pos()[1] in range(10, 70):
            screen.blit(scale(pygame.image.load("22_grey.png"), (50, 50)), (15, 10))
        else:
            screen.blit(scale(pygame.image.load("22.png"), (50, 50)), (15, 10))
        if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
            MOUSEBUTTONDOWN_5 = True
        if e.type == pygame.MOUSEBUTTONUP and e.button == 1:
            if e.pos[0] in range(15, 65) and e.pos[1] in range(20, 70) and MOUSEBUTTONDOWN_5:
                    sound1.stop()
                    sound2.stop()
                    win = False
                    choice = True
            MOUSEBUTTONDOWN_5=False
    elif menu:
        name = pygame.font.Font('19369.ttf', 100).render('TRANSFUSIONS', False, (1,1,1))
        tasks_type_1 = pygame.font.SysFont('Comic Sans MS', 22).render('БЕСКОНЕЧНЫМ', 1, (1,1,1))
        tasks_type_2 = pygame.font.SysFont('Comic Sans MS', 22).render('ОГРАНИЧЕННЫМ', 1, (1,1,1))
        tasks_type = pygame.font.SysFont('Comic Sans MS', 22).render('ЗАДАЧИ С', 1, (1,1,1))
        tasks_type_ = pygame.font.SysFont('Comic Sans MS', 22).render('ДОЛИВОМ', 1, (1,1,1))
        if pygame.mouse.get_pos()[0] in range(114, 325) and pygame.mouse.get_pos()[1] in range(275, 414):
            screen.blit(scale(pygame.image.load("кнопка_grey.png"), (211, 139)), (114, 275))
        else:
            screen.blit(scale(pygame.image.load("кнопка.png"), (211, 139)), (114, 275))
        if pygame.mouse.get_pos()[0] in range(428, 639) and pygame.mouse.get_pos()[1] in range(275, 414):
            screen.blit(scale(pygame.image.load("кнопка_grey.png"), (211, 139)), (428, 275))
        else:
            screen.blit(scale(pygame.image.load("кнопка.png"), (211, 139)), (428, 275))
        screen.blit(name, (90, 80))
        screen.blit(tasks_type, (160, 295))
        screen.blit(tasks_type, (474, 295))
        screen.blit(tasks_type_1, (130, 330))
        screen.blit(tasks_type_2, (435, 330))
        screen.blit(tasks_type_, (474, 365))
        screen.blit(tasks_type_, (160, 365))
        if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
            MOUSEBUTTONDOWN_3 = True
        if e.type == pygame.MOUSEBUTTONUP and e.button == 1:
            if e.pos[0] in range(114, 325) and e.pos[1] in range(275, 414) and MOUSEBUTTONDOWN_3:
                page=0
                chosen = 'бесконечный долив'
                menu = False
                choice = True
            if e.pos[0] in range(428, 639) and e.pos[1] in range(275, 414) and MOUSEBUTTONDOWN_3:
                page=0
                chosen = 'ограниченный долив'
                menu = False
                choice = True
            MOUSEBUTTONDOWN_3 = False
    elif choice:
        file = open(chosen+'.txt', 'r', encoding = 'utf-8')
        tasks_texts = file.read()
        file.close()
        if tasks_texts!='':
            tasks_texts = tasks_texts.split('\n')
            z = 0
            for i in tasks_texts:
                z+=1
                if '&' not in i:
                    tasks_texts[tasks_texts.index(i)]+=' & 0 0'
            file = open(chosen+'.txt', 'w', encoding = 'utf-8')
            file.write('\n'.join(tasks_texts))
            file.close()
            tasks_amount = len(tasks_texts)
            for i in range(1, 7):
                if page*6+i<=tasks_amount:
                    if i == 1:
                        if pygame.mouse.get_pos()[0] in range(100, 336) and pygame.mouse.get_pos()[1] in range(125, 210):
                            screen.blit(scale(pygame.image.load("level_grey.png"), (236, 85)), (100, 125))
                        else:
                            screen.blit(scale(pygame.image.load("level.png"), (236, 85)), (100, 125))
                        screen.blit(pygame.font.SysFont('Comic Sans MS', 22).render('ЗАДАЧА '+str(page*6+i), 1, (1,1,1)), (105, 130))
                        result_i = page*6+i
                        if tasks_texts[result_i-1][-1]=='0':
                            screen.blit(scale(pygame.image.load("squre.png"), (35, 35)), (280, 150))
                        else:
                            screen.blit(scale(pygame.image.load("squre_tick.png"), (41, 35)), (280, 150))
                        screen.blit(pygame.font.SysFont('Nunito-ExtraLight.ttf', 20).render('ВАШ РЕЗУЛЬТАТ: '+tasks_texts[page*6+i-1].split()[-2], 1, (1,1,1)), (105, 180))
                    elif i ==2:
                        if pygame.mouse.get_pos()[0] in range(100, 336) and pygame.mouse.get_pos()[1] in range(260, 345):
                            screen.blit(scale(pygame.image.load("level_grey.png"), (236, 85)), (100, 260))
                        else:
                            screen.blit(scale(pygame.image.load("level.png"), (236, 85)), (100, 260))
                        screen.blit(pygame.font.SysFont('Comic Sans MS', 22).render('ЗАДАЧА '+str(page*6+i), 1, (1,1,1)), (105, 265))
                        result_i = page*6+i
                        if tasks_texts[result_i-1][-1]=='0':
                            screen.blit(scale(pygame.image.load("squre.png"), (35, 35)), (280, 285))
                        else:
                            screen.blit(scale(pygame.image.load("squre_tick.png"), (41, 35)), (280, 285))
                        screen.blit(pygame.font.SysFont('Nunito-ExtraLight.ttf', 20).render('ВАШ РЕЗУЛЬТАТ: '+tasks_texts[page*6+i-1].split()[-2], 1, (1,1,1)), (105, 315))
                    elif i ==3:
                        if pygame.mouse.get_pos()[0] in range(100, 336) and pygame.mouse.get_pos()[1] in range(395, 480):
                            screen.blit(scale(pygame.image.load("level_grey.png"), (236, 85)), (100, 395))
                        else:
                            screen.blit(scale(pygame.image.load("level.png"), (236, 85)), (100, 395))
                        screen.blit(pygame.font.SysFont('Comic Sans MS', 22).render('ЗАДАЧА '+str(page*6+i), 1, (1,1,1)), (105, 400))
                        result_i = page*6+i
                        if tasks_texts[result_i-1][-1]=='0':
                            screen.blit(scale(pygame.image.load("squre.png"), (35, 35)), (280, 420))
                        else:
                            screen.blit(scale(pygame.image.load("squre_tick.png"), (41, 35)), (280, 420))
                        screen.blit(pygame.font.SysFont('Nunito-ExtraLight.ttf', 20).render('ВАШ РЕЗУЛЬТАТ: '+tasks_texts[page*6+i-1].split()[-2], 1, (1,1,1)), (105, 450))
                    elif i ==4:
                        if pygame.mouse.get_pos()[0] in range(414, 650) and pygame.mouse.get_pos()[1] in range(125, 210):
                            screen.blit(scale(pygame.image.load("level_grey.png"), (236, 85)), (414, 125))
                        else:
                            screen.blit(scale(pygame.image.load("level.png"), (236, 85)), (414, 125))
                        screen.blit(pygame.font.SysFont('Comic Sans MS', 22).render('ЗАДАЧА '+str(page*6+i), 1, (1,1,1)), (419, 130))
                        result_i = page*6+i
                        if tasks_texts[result_i-1][-1]=='0':
                            screen.blit(scale(pygame.image.load("squre.png"), (35, 35)), (594, 150))
                        else:
                            screen.blit(scale(pygame.image.load("squre_tick.png"), (41, 35)), (594, 150))
                        screen.blit(pygame.font.SysFont('Nunito-ExtraLight.ttf', 20).render('ВАШ РЕЗУЛЬТАТ: '+tasks_texts[page*6+i-1].split()[-2], 1, (1,1,1)), (419, 180))
                    elif i == 5:
                        if pygame.mouse.get_pos()[0] in range(414, 650) and pygame.mouse.get_pos()[1] in range(260, 345):
                            screen.blit(scale(pygame.image.load("level_grey.png"), (236, 85)), (414, 260))
                        else:
                            screen.blit(scale(pygame.image.load("level.png"), (236, 85)), (414, 260))
                        screen.blit(pygame.font.SysFont('Comic Sans MS', 22).render('ЗАДАЧА '+str(page*6+i), 1, (1,1,1)), (419, 265))
                        result_i = page*6+i
                        if tasks_texts[result_i-1][-1]=='0':
                            screen.blit(scale(pygame.image.load("squre.png"), (35, 35)), (594, 285))
                        else:
                            screen.blit(scale(pygame.image.load("squre_tick.png"), (41, 35)), (594, 285))
                        screen.blit(pygame.font.SysFont('Nunito-ExtraLight.ttf', 20).render('ВАШ РЕЗУЛЬТАТ: '+tasks_texts[page*6+i-1].split()[-2], 1, (1,1,1)), (419, 315))
                    else:
                        if pygame.mouse.get_pos()[0] in range(414, 650) and pygame.mouse.get_pos()[1] in range(395, 480):
                            screen.blit(scale(pygame.image.load("level_grey.png"), (236, 85)), (414, 395))
                        else:
                            screen.blit(scale(pygame.image.load("level.png"), (236, 85)), (414, 395))
                        screen.blit(pygame.font.SysFont('Comic Sans MS', 22).render('ЗАДАЧА '+str(page*6+i), 1, (1,1,1)), (419, 400))
                        result_i = page*6+i
                        if tasks_texts[result_i-1][-1]=='0':
                            screen.blit(scale(pygame.image.load("squre.png"), (35, 35)), (594, 420))
                        else:
                            screen.blit(scale(pygame.image.load("squre_tick.png"), (41, 35)), (594, 420))
                        screen.blit(pygame.font.SysFont('Nunito-ExtraLight.ttf', 20).render('ВАШ РЕЗУЛЬТАТ: '+tasks_texts[page*6+i-1].split()[-2], 1, (1,1,1)), (419, 450))
            if pygame.mouse.get_pos()[0] in range(310, 360) and pygame.mouse.get_pos()[1] in range(490, 540):
                screen.blit(scale(pygame.image.load("arrow_left_grey.png"), (50, 50)), (310, 490))
            else:
                screen.blit(scale(pygame.image.load("arrow_left.png"), (50, 50)), (310, 490))
            if pygame.mouse.get_pos()[0] in range(390, 440) and pygame.mouse.get_pos()[1] in range(490, 540):
                screen.blit(scale(pygame.image.load("arrow_right_grey.png"), (50, 50)), (390, 490))
            else:
                screen.blit(scale(pygame.image.load("arrow_right.png"), (50, 50)), (390, 490))
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                MOUSEBUTTONDOWN_1 = True
            if e.type == pygame.MOUSEBUTTONUP and e.button == 1:
                if e.pos[0] in range(15, 65) and e.pos[1] in range(20, 70) and MOUSEBUTTONDOWN_1:
                        menu = True
                        choice = False
                elif e.pos[0] in range(100, 336) and e.pos[1] in range(125, 210) and MOUSEBUTTONDOWN_1:
                    if tasks_amount-page*6>0:
                        current_task=tasks_texts[page*6+1-1].split()
                        if '&' in current_task:
                            need = int(current_task[-5])
                            min_motions = int(current_task[-4])
                        else:
                            need = int(current_task[-2])
                            min_motions = int(current_task[-1])
                        task_num = page*6+1
                        action = 0
                        have1 = 0
                        have2 = 0
                        have3 = 0
                        have4 = 0
                        previous_water_1 = 0
                        previous_water_2 = 0
                        previous_water_3 = 0
                        previous_water_4 = 0
                        hon = 1
                        choice = False
                        task = True
                elif e.pos[0] in range(100, 336) and e.pos[1] in range(260, 345) and MOUSEBUTTONDOWN_1:
                    if tasks_amount-page*6>1:
                        current_task=tasks_texts[page*6+2-1].split()
                        if '&' in current_task:
                            need = int(current_task[-5])
                            min_motions = int(current_task[-4])
                        else:
                            need = int(current_task[-2])
                            min_motions = int(current_task[-1])
                        task_num = page*6+2
                        action = 0
                        have1 = 0
                        have2 = 0
                        have3 = 0
                        have4 = 0
                        previous_water_1 = 0
                        previous_water_2 = 0
                        previous_water_3 = 0
                        previous_water_4 = 0
                        hon = 1
                        choice = False
                        task = True
                elif e.pos[0] in range(100, 336) and e.pos[1] in range(395, 480) and MOUSEBUTTONDOWN_1:
                    if tasks_amount-page*6>2:
                        current_task=tasks_texts[page*6+3-1].split()
                        if '&' in current_task:
                         #   need = int(current_task[-5])
                            min_motions = int(current_task[-4])
                        else:
                            need = int(current_task[-2])
                            min_motions = int(current_task[-1])
                        task_num = page*6+3
                        min_hod = int()
                        action = 0
                        have1 = 0
                        have2 = 0
                        have3 = 0 
                        have4 = 0
                        previous_water_1 = 0
                        previous_water_2 = 0
                        previous_water_3 = 0
                        previous_water_4 = 0
                        hon = 1
                        choice = False
                        task = True
                elif e.pos[0] in range(414, 650) and e.pos[1] in range(125, 210) and MOUSEBUTTONDOWN_1:
                    if tasks_amount-page*6>3:
                        current_task=tasks_texts[page*6+4-1].split()
                        if '&' in current_task:
                            need = int(current_task[-5])
                            min_motions = int(current_task[-4])
                        else:
                            need = int(current_task[-2])
                            min_motions = int(current_task[-1])
                        task_num = page*6+4
                        action = 0
                        have1 = 0
                        have2 = 0
                        have3 = 0
                        have4 = 0
                        previous_water_1 = 0
                        previous_water_2 = 0
                        previous_water_3 = 0
                        previous_water_4 = 0
                        hon =1
                        choice = False
                        task = True
                elif e.pos[0] in range(414, 650) and e.pos[1] in range(260, 345) and MOUSEBUTTONDOWN_1:
                    if tasks_amount-page*6>4:
                        current_task=tasks_texts[page*6+5-1].split()
                        if '&' in current_task:
                            need = int(current_task[-5])
                            min_motions = int(current_task[-4])
                        else:
                            need = int(current_task[-2])
                            min_motions = int(current_task[-1])
                        task_num = page*6+5
                        action = 0
                        have1 = 0
                        have2 = 0
                        have3 = 0
                        have4 = 0
                        previous_water_1 = 0
                        previous_water_2 = 0
                        previous_water_3 = 0
                        previous_water_4 = 0
                        hon = 1
                        choice = False
                        task = True
                elif e.pos[0] in range(414, 650) and e.pos[1] in range(395, 480) and MOUSEBUTTONDOWN_1:
                    if tasks_amount-page*6>5:
                        current_task=tasks_texts[page*6+6-1].split()
                        if '&' in current_task:
                            need = int(current_task[-5])
                            min_motions = int(current_task[-4])
                        else:
                            need = int(current_task[-2])
                            min_motions = int(current_task[-1])
                        task_num = page*6+6
                        action = 0
                        have1 = 0
                        have2 = 0
                        have3 = 0
                        have4 = 0
                        previous_water_1 = 0
                        previous_water_2 = 0
                        previous_water_3 = 0
                        previous_water_4 = 0
                        hon = 1
                        choice = False
                        task = True
                MOUSEBUTTONDOWN_1 = False
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                MOUSEBUTTONDOWN_2 = True
            if e.type == pygame.MOUSEBUTTONUP and e.button == 1:
                if e.pos[0] in range(310, 360) and e.pos[1] in range(490, 540) and page!=0 and MOUSEBUTTONDOWN_2:
                    page-=1
                if e.pos[0] in range(390, 440) and e.pos[1] in range(490, 540) and result_i<tasks_amount and MOUSEBUTTONDOWN_2:
                    page+=1
                MOUSEBUTTONDOWN_2 = False
        else:
            screen.blit(pygame.font.SysFont('Nunito-ExtraLight.ttf', 30).render('ЗАДАЧИ ЭТОГО ТИПА ЕЩЁ НЕ ДОБАВЛЕНЫ', 1, (1,1,1)), (145, 295))
        screen.blit(pygame.font.Font('8320.ttf', 35).render('ВЫБЕРИТЕ ЗАДАЧУ, КОТОРУЮ', 1, (1,1,1)), (100, 10))
        screen.blit(pygame.font.Font('8320.ttf', 35).render('БУДЕТЕ РЕШАТЬ', 1, (1,1,1)), (200, 55))
        if pygame.mouse.get_pos()[0] in range(15, 65) and pygame.mouse.get_pos()[1] in range(20, 70):
            screen.blit(scale(pygame.image.load("22_grey.png"), (50, 50)), (15, 10))
        else:
            screen.blit(scale(pygame.image.load("22.png"), (50, 50)), (15, 10))
        if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
            if e.pos[0] in range(15, 65) and e.pos[1] in range(10, 60):
                MOUSEBUTTONDOWN = True
        if e.type == pygame.MOUSEBUTTONUP and e.button == 1:
            if e.pos[0] in range(15, 65) and e.pos[1] in range(10, 60) and MOUSEBUTTONDOWN:
                menu = True
                choice = False
            MOUSEBUTTONDOWN = False
    pygame.display.update()