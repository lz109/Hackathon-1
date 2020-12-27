from cmu_112_graphics import *
import datetime
# cmu_112_graphics cited from cmu 15-112 course
class board1(Mode):
    def appStarted(mode):
        mode.image = mode.loadImage('story board1.PNG')
        mode.image2 = mode.scaleImage(mode.image, 2/3)

    def redrawAll(mode, canvas):
        canvas.create_image(400, 300, image=ImageTk.PhotoImage(mode.image2))
        canvas.create_text(245, mode.height/7,
                           text='"人类是隐私和安全链中\n最薄弱的环节"', font='Arial 20 bold', fill='navy')
        canvas.create_text(220, mode.height/3,
                           text='我们又该如何\n保护自己和他人的隐私？', font='Arial 20 bold', fill='navy')
        canvas.create_text(280, mode.height/1.5,
                           text='你是晓娟，\n这里是"你的生活"', font='Arial 30 bold', fill='red')
        canvas.create_text(200, mode.height/1.1,
                           text='点击"S"键，开始游戏',font='Arial 20 bold', fill = 'black')
    def keyPressed(mode, event):
        if event.key == 's':
            mode.app.setActiveMode(mode.app.board2)

class board2(Mode):
    def appStarted(mode):
        mode.image = mode.loadImage('story board2.PNG')
        mode.image2 = mode.scaleImage(mode.image, 1/2)

    def redrawAll(mode, canvas):
        canvas.create_image(100, 300, image=ImageTk.PhotoImage(mode.image2))
        canvas.create_text(3*mode.width/4, 300,
                            text='你是一位20岁的留学生，', font='Arial 20 bold', fill='navy')
        canvas.create_text(2*mode.width/3, 400,
                            text='因为美国爆发的疫情不得不暂停学业，回国。', font='Arial 20 bold', fill='navy')
        canvas.create_text(800, 500,
                            text='点击"S"继续',  font='Arial 20 bold', fill='black')
    def keyPressed(mode, event):
        if event.key == 's':
            mode.app.setActiveMode(mode.app.board3)

class board3(Mode):
    def appStarted(mode):
        mode.image = mode.loadImage('story board3.PNG')
        mode.image2 = mode.scaleImage(mode.image, 1/2)

    def redrawAll(mode, canvas):
        canvas.create_image(350, 300, image=ImageTk.PhotoImage(mode.image2))
        canvas.create_text(mode.width/4, 50,
                            text='下了飞机后，你开始了14天的隔离。', font='Arial 20 bold', fill='navy')
        canvas.create_text(3*mode.width/4,200,
                            text='为了了解当地疫情状况，\n你打开了社交媒体。', font='Arial 20 bold', fill='navy')
        canvas.create_text(mode.width/6.5-15, 220,
                            text='确诊病例详细的个人\n信息成为了\n热搜头条。', font='Arial 20 bold', fill='navy')
        canvas.create_text(4*mode.width/5, 350,
                            text='A: 你大致浏览了确诊病例的信息，\n并且为了让身边的人小心，\n转发了', font='Arial 20 bold', fill='black')
        canvas.create_text(3*mode.width/4, 450,
                            text='B: 无视，去看更有\n趣的娱乐新闻', font='Arial 20 bold', fill='black')

    def keyPressed(mode, event):
        if event.key == 'a' or event.key == 'b':
            mode.app.setActiveMode(mode.app.board4)

class board4(Mode):
    def appStarted(mode):
        mode.image = mode.loadImage('story board16.PNG')
        mode.image2 = mode.scaleImage(mode.image, 1/2)

    def redrawAll(mode, canvas):
            canvas.create_image(650, 280, image=ImageTk.PhotoImage(mode.image2))
            canvas.create_text(mode.width/3, 200,
                            text='你收到了微信消息，以查询行程信息为由，\n要求你把身份证照片和家庭住址发给ta', font='Arial 20 bold', fill='navy')
            canvas.create_text(300, 350,
                            text='A: 无视，不回消息；报警', font='Arial 20 bold', fill='black')
            canvas.create_text(300, 400,
                            text='B: 泄露你的信息', font='Arial 20 bold', fill='black')
    def keyPressed(mode, event):
        if event.key == 'a':
            mode.app.setActiveMode(mode.app.board5)
        if event.key == 'b':
            mode.app.setActiveMode(mode.app.board42)

class board42(Mode):
    def appStarted(mode):
        mode.image = mode.loadImage('story board4.PNG')
        mode.image2 = mode.scaleImage(mode.image, 1/2)

    def redrawAll(mode, canvas):
            canvas.create_image(750, 300, image=ImageTk.PhotoImage(mode.image2))
            canvas.create_text(mode.width/3, 300,
                            text='你获得一次重新选择的机会，\n记住在提供个人信息前，\n要验证对方身份，\n了解信息采集的具体目的', font='Arial 20 bold', fill='green')
            canvas.create_text(150,500,
                            text='点击"S"重新选择', font='Arial 20 bold', fill='black')
    def keyPressed(mode, event):
        if event.key == 's':
            mode.app.setActiveMode(mode.app.board4)

class board5(Mode):
    def appStarted(mode):
        mode.image = mode.loadImage('story board5.PNG')
        mode.image2 = mode.scaleImage(mode.image, 1/2)

    def redrawAll(mode, canvas):
        canvas.create_image(350, 300, image=ImageTk.PhotoImage(mode.image2))
        canvas.create_text(mode.width/5-50, 100,
                            text='漫长隔离结束后，\n你开始了正常的生活，\n包括频繁的网上购物。', font='Arial 20 bold', fill='navy')
        canvas.create_text(mode.width/5-50 ,300,
                            text='有一天，\n你接到快递电话后\n下楼至快递柜领取\n你的物品。', font='Arial 20 bold', fill='navy')
        canvas.create_text(4*mode.width/5+50, 350,
                            text='A: 取出快递后\n直接将包装盒丢弃', font='Arial 20 bold', fill='black')
        canvas.create_text(4*mode.width/5+50, 450,
                            text='B: 将快递单上的\n个人信息抹去', font='Arial 20 bold', fill='black')

    def keyPressed(mode, event):
        if event.key == 'a':
            mode.app.setActiveMode(mode.app.board52)
        if event.key == 'b':
            mode.app.setActiveMode(mode.app.board6)

class board52(Mode):
    def appStarted(mode):
        mode.image = mode.loadImage('story board7.PNG')
        mode.image2 = mode.scaleImage(mode.image, 2/3)

    def redrawAll(mode, canvas):
        canvas.create_image(350, 300, image=ImageTk.PhotoImage(mode.image2))
        canvas.create_text(370, 400,
                            text='你的姓名联系方式\n和住址被泄漏...\n你发现之后的几天晚上\n好像有人尾随', font='Arial 20 bold', fill='black')
        canvas.create_text(4*mode.width/5+20,400,
                            text='你获得一次重新选择的机会，\n记住在提供个人信息前，\n要验证对方身份和\n了解信息采集的具体目的', font='Arial 20 bold', fill='white')
        canvas.create_text(4*mode.width/5, 550,
                            text='点击"S"重新选择', font='Arial 20 bold', fill='white')

    def keyPressed(mode, event):
        if event.key == 's':
            mode.app.setActiveMode(mode.app.board5)

class board6(Mode):
    def appStarted(mode):
        mode.image = mode.loadImage('story board8.PNG')
        mode.image2 = mode.scaleImage(mode.image, 1/2)

    def redrawAll(mode, canvas):
        canvas.create_image(350, 300, image=ImageTk.PhotoImage(mode.image2))
        canvas.create_text(3*mode.width/5+50, 30,
                            text='国内的疫情受到了控制后，你决定继续你的DJ兼职。', font='Arial 20 bold', fill='navy')
        canvas.create_text(3*mode.width/4-50,200,
                            text='周六晚上，你连轴转，一下子去了8家酒吧。', font='Arial 20 bold', fill='navy')
        canvas.create_text(4*mode.width/5, 550,
                            text='点击"S"继续', font='Arial 20 bold', fill='black')

    def keyPressed(mode, event):
        if event.key == 's':
            mode.app.setActiveMode(mode.app.board7)

class board7(Mode):
    def appStarted(mode):
        mode.image = mode.loadImage('story board9.PNG')
        mode.image2 = mode.scaleImage(mode.image, 1/2)

    def redrawAll(mode, canvas):
        canvas.create_image(600, 300, image=ImageTk.PhotoImage(mode.image2))
        canvas.create_text(mode.width/5+50, 100,
                            text='凌晨才回到家的你，\n为了安全考虑结束了一整套洗漱', font='Arial 20 bold', fill='navy')
        canvas.create_text(1*mode.width/4,200,
                            text='在昏昏入睡时收到了陌生的来电', font='Arial 20 bold', fill='navy')
        canvas.create_text(1*mode.width/5+80, 350,
                            text='"请问是晓娟吗？\n您今晚去过的酒吧有一位人员刚刚确诊，\n为了您和他人安全的考虑，\n需要你的配合......"'
                            , font='Arial 20 bold', fill='navy')
        canvas.create_text(mode.width/8, 550,
                            text='点击"S"继续', font='Arial 20 bold', fill='black')

    def keyPressed(mode, event):
        if event.key == 's':
            mode.app.setActiveMode(mode.app.board8)

class board8(Mode):
    def appStarted(mode):
        mode.image = mode.loadImage('story board10.PNG')
        mode.image2 = mode.scaleImage(mode.image, 1/2)

    def redrawAll(mode, canvas):
        canvas.create_image(600, 300, image=ImageTk.PhotoImage(mode.image2))
        canvas.create_text(mode.width/3, 300,
                            text='在医院你如实上报了行程，\n做了核酸检测', font='Arial 20 bold', fill='navy')
        canvas.create_text(4*mode.width/5, 570,
                            text='点击"S"继续', font='Arial 20 bold', fill='black')

    def keyPressed(mode, event):
        if event.key == 's':
            mode.app.setActiveMode(mode.app.board9)

class board9(Mode):
    def appStarted(mode):
        mode.image = mode.loadImage('story board11.PNG')
        mode.image2 = mode.scaleImage(mode.image, 1.8/3)

    def redrawAll(mode, canvas):
        canvas.create_image(350, 300, image=ImageTk.PhotoImage(mode.image2))
        canvas.create_text(mode.width/5-100, 100,
                            text='在医院里\n你静静地\n刷着朋友圈\n等待结果', font='Arial 20 bold', fill='navy')
        canvas.create_text(mode.width/5-70, 400,
                            text='却看到自己的名字\n赫然出现在\n推文的标题上，\n你赶紧点开', font='Arial 20 bold', fill='navy')
        canvas.create_text(4*mode.width/5+100, 580,
                            text='点击"S"继续', font='Arial 20 bold', fill='black')

    def keyPressed(mode, event):
        if event.key == 's':
            mode.app.setActiveMode(mode.app.board10)

class board10(Mode):
    def appStarted(mode):
        mode.image = mode.loadImage('story board12.PNG')
        mode.image2 = mode.scaleImage(mode.image, 1/2)

    def redrawAll(mode, canvas):
        canvas.create_image(600 , 300, image=ImageTk.PhotoImage(mode.image2))
        canvas.create_text(mode.width/3-50, 300,
                            text='无论你向警察寻求帮助，\n还是通过法律维权，\n你逐渐意识到这一切都是不可逆的：\n你的手机号码，住址，姓名，\n甚至你的家人仍然暴露在公众的目光下', font='Arial 20 bold', fill='black')
        canvas.create_text(4*mode.width/5, 570,
                            text='点击"S"继续', font='Arial 20 bold', fill='black')

    def keyPressed(mode, event):
        if event.key == 's':
            mode.app.setActiveMode(mode.app.board12)

class board12(Mode):
    def appStarted(mode):
        mode.image = mode.loadImage('story board13.PNG')
        mode.image2 = mode.scaleImage(mode.image, 1/2)

    def redrawAll(mode, canvas):
        canvas.create_image(350, 400, image=ImageTk.PhotoImage(mode.image2))
        canvas.create_text(mode.width/4+300, 100,
                            text='这种歧视不止于网络，甚至在你出门时别人也会投来异样的目光。', font='Arial 20 bold', fill='navy')
        canvas.create_text(mode.width/4+300, 200,
                            text='你的生活被改变了...', font='Arial 20 bold', fill='navy')
        canvas.create_text(4*mode.width/5, 350,
                            text='点击"S"继续', font='Arial 20 bold', fill='black')

    def keyPressed(mode, event):
        if event.key == 's':
            mode.app.setActiveMode(mode.app.board13)

class board13(Mode):
    def appStarted(mode):
        mode.image = mode.loadImage('story board14.PNG')
        mode.image2 = mode.scaleImage(mode.image, 1/2)

    def redrawAll(mode, canvas):
        canvas.create_image(350, 300, image=ImageTk.PhotoImage(mode.image2))
        canvas.create_text(550, 80,
                            text='你回想起曾经在热搜上看到的确诊病人信息……', font='Arial 20 bold', fill='navy')
        canvas.create_text(4*mode.width/5, 350,
                            text='点击"S"继续', font='Arial 20 bold', fill='black')

    def keyPressed(mode, event):
        if event.key == 's':
            mode.app.setActiveMode(mode.app.board14)

class board14(Mode):
    def appStarted(mode):
        mode.image = mode.loadImage('story board15.PNG')
        mode.image2 = mode.scaleImage(mode.image, 1/2)

    def redrawAll(mode, canvas):
        canvas.create_image(350, 200, image=ImageTk.PhotoImage(mode.image2))
        canvas.create_text(500, 350,
                            text='疫情之下，个人信息泄露已经成为了常态。\n个人信息可以是帮助抗疫的武器，却也可以是伤害我们的利刃。\n作为个人，我们能做的就是保护好自己，\n同时不成为信息泄露的帮凶。', font='Arial 20 bold', fill='navy')
        canvas.create_text(4*mode.width/5, 500,
                            text='点击"S"继续', font='Arial 30 bold', fill='black')
    def keyPressed(mode, event):
        if event.key == 's':
            mode.app.setActiveMode(mode.app.board15)

class board15(Mode):
    def appStarted(mode):
        mode.storeTime()
    def storeTime(mode):
        time = datetime.datetime.now()
        current_time = time.strftime("%Y-%m-%d %H:%M:%S")
        f = open("historyTime.txt","a+")
        f.write(f'{current_time}\n')
        f.close()

        read = open("historyTime.txt", "r")
        mode.app.time = read.readlines()[-1]
        print()
    def redrawAll(mode, canvas):
        canvas.create_text(500, 350,
                            text=f'您在{mode.app.time}完成了游戏，\n恭喜您在个人信息保护的路上更进一步！', font='Arial 20 bold', fill='red')

class MyModalApp(ModalApp):
    def appStarted(app):
        app.time = 0
        app.board2 = board2()
        app.board1 = board1()
        app.board3 = board3()
        app.board4 = board4()
        app.board42 = board42()
        app.board5 = board5()
        app.board52 = board52()
        app.board6 = board6()
        app.board7 = board7()
        app.board8 = board8()
        app.board9 = board9()
        app.board10 = board10()
        app.board12 = board12()
        app.board13 = board13()
        app.board14 = board14()
        app.board15 = board15()
        app.setActiveMode(app.board1)
        app.timerDelay = 700

def main():
    MyModalApp(width=1000, height=600)

if __name__ == '__main__':
    main()