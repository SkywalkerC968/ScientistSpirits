# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define narrator = Character(None)
define nvl_n = nvl_narrator
define T = Character("钱学森",color="#de2910",kind=nvl)
define GYH = Character("郭永怀",color="#72baa7",kind=nvl)
define DK = Character("Dan Kimball(美国海军助理次长)",color="4169e1")
define T_US = Character("Professor Tsien",color="#fdb933")
define T_CH = Character("学森同志",color="#de2910")
define CG = Character("陈赓大将",color="#2edfa3")
define NRZ = Character("聂荣臻元帅",color="#f15a22")
define CHPro = Character("中国科研人员",color="#1ba784")
define SUPro = Character("苏联导弹专家",color="#8f4b2e")
define ABPro = Character("原子弹工程专家",color="#005344")
define Trans = Character("中国翻译人员",color="#fab27b")
define XF = Character("小冯",color="ffc20e")
define MZD = Character("毛泽东",color="de2910")
define Meteorologist = Character("气象技术人员",color="#ffc20e")

define T_US_solemn = Character(kind=T_US,image="t us solemn")
define T_US_confident = Character(kind=T_US,image="t us confident.png")
define T_CH_solemn_handdown = Character(kind=T_CH,image="t ch solemn handdown.png")
define T_CH_solemn_handup = Character(kind=T_CH,image="t ch solemn handup.png")
define T_CH_smile = Character(kind=T_CH,image="t ch smile.png")
define T_CH_reflective = Character(kind=T_CH,image="t ch reflective.png")
define T_CH_exhilarated = Character(kind=T_CH,image="t ch exhilarated.png")

#游戏中所需的评判变量。

default credit = 100
default Spirits = set()
default flag = False
default window_flag = False
default V2_flag = False
default SE_flag = False
default HS_flag = False
default EC_flag = False
default Tr_flag = False

#预置背景。
image bg black = "#000000"
image bg white = "#ffffff"

#变换定义。
transform title_show(x=0.93,y=0.9):
    align(x,y) alpha 0.0
    linear 1 alpha 1.0
transform media_show(time=1.0,x=0.5,y=0.2,a=0.3):
    align(x,y) zoom 5.0 alpha a
    linear time zoom 1.0 alpha 1.0


# 游戏在此开始。

label start:

    scene bg black
    pause 1
    scene bg white
    play sound "探照灯.mp3"
    pause 1
    play sound "敲击牢门.mp3"
    scene bg brightprison
    with Dissolve(2.0)
    pause 1
    scene bg black
    pause 1
    scene bg white
    play sound "探照灯.mp3"
    pause 1
    play sound "敲击牢门.mp3"
    scene bg brightprison
    with Dissolve(2.0)
    pause 1

    "呵"

    "美国？{w}怕了？"

    jump Sce0

label deviation_ending:
    play music "<from 30>no time for caution.mp3" if_changed
    scene bg black
    with dissolve
    nvl clear
    nvl_n "时间一天天地过去,工厂的改进速度十分缓慢。马上就要进行导弹的试车工作，导弹实体却连影子都没有见到"
    nvl_n "钱学森为此亲自到工厂进行考察，发现零件制造精度方面的提升十分有限"
    nvl_n "在最先进的工厂中，有部分零件达到了所设计导弹的精度要求，但是大部分的零件工艺还尚未完成改造"
    nvl_n "一个导弹，不得不同时采用这些不同精度等级的零件，在装配导弹时就困难重重"
    nvl_n "以目前的情况来看，这些零件无法造出符合要求的导弹"
    nvl clear
    nvl_n "{size=30}{font=DaKai.ttf}1963年，美、英、苏三国在莫斯科正式签署《关于禁止在大气层、外层空间和水下进行核武器爆炸实验的条约》又称〈部分核禁止条约〉或三家条约{/font}{/size}"
    nvl_n "苏联领导人赫鲁晓夫、勃烈日涅夫出席了签字仪式。联合国秘书长吴丹也应邀出席了签字仪式"
    nvl_n "条约并未禁止地下核试验{p}但是当时只有美苏两国具有进行地下核试验的能力"
    nvl_n "{size=50}{color=#de2910}{cps=6}中国，没有时间了！{/cps}{/color}{/size}"
    nvl_n "点火，发射！"

    scene bg df2failed
    with fade
    pause 1
    scene bg df2explosionpit
    with dissolve
    nvl clear
    nvl_n "仓促的导弹试验，在一声巨响之后，将多年的理论攻关、工厂改造成果化为乌有。短期之内，核导弹实验无法开展"
    nvl_n "导弹坠落炸起的烟尘渐渐散去，烈日之下，万米高空中的一点黑影映入人们视野"
    nvl_n "导弹失败的第二天，外媒铺天盖地地展示出几张戈壁背景的高清照片，照片中央混乱的扬尘，无声地嘲笑着中国的无奈——"
    nvl_n "没有导弹的中国，无法阻止美国高空侦察机的肆意入侵"
    nvl_n "失败的导弹试验催迫着美苏大国加快限制中国的脚步。《全面禁止核试验条约》在三国强暴的核讹诈手段之下，在联合国谈判桌上正式通过"
    nvl clear
    nvl_n "{size=50}{color=#de2910}{cps=6}中国，失去了谈判的能力{/cps}{/color}{/size}"
    nvl_n "{size=66}{color=#de2910}{cps=6}共和国之剑，未能铸成{/cps}{/color}{/size}"
    nvl hide

    scene bg cybernetics
    with dissolve
    "1954年在软禁期间，钱学森写了一本改变历史的著作《工程控制论》"
    "《工程控制论》是系统工程学以及控制论的一本巨著"

    nvl_n "其中第十七章——自行锁定和适应环境的系统，展现了钱学森对于总体系统设计的高瞻远瞩"
    nvl_n "系统越是复杂，那么由于整个系统的装配上的误差，或者因个别元件的损坏而发生失灵现象的可能性也就越大"
    nvl_n "本章里，我们将讨论在系统里建立可靠的和能适应环境的性能的这种可能性，使得整个系统在没有人帮助的情况下，本身能够自动的改正那些设计中偶然的或不能预料到的误差"
    nvl_n "很像生物的适应性机能，这种机能保证生物在周围环境变化的情况下能够生存"
    nvl hide

    scene bg black
    with fade
    "{size=50}中国的发展，需要考虑中国的实际！{/size}"

    jump settlement

label suspension_ending:
    play music "no time for caution.mp3" if_changed

    nvl clear
    nvl_n "核导弹偏出并爆炸，强烈的核辐射席卷了邻近的村庄，由于远离预计着弹地点，中国没有采集到任何爆炸信息"
    nvl_n "苏联媒体：中国对核技术使用不当，应对中国的核科学进行限制"
    nvl_n "{size=30}{font=DaKai.ttf}早在1963年，美、英、苏三国就在莫斯科正式签署《关于禁止在大气层、外层空间和水下进行核武器爆炸实验的条约》{/font}{/size}"
    nvl_n "条约并未禁止地下核试验{p}但是当时只有美苏两国具有进行地下核试验的能力"
    nvl_n "{size=50}{color=#de2910}{cps=6}中国，早已没有时间……{/cps}{/color}{/size}"
    nvl clear
    nvl_n "失败的核导弹试验催迫着美苏大国加快限制中国的脚步"
    nvl_n "《全面禁止核试验条约》在三国强暴的核讹诈手段之下，在联合国谈判桌上正式通过"
    nvl_n "{size=50}{color=#de2910}{cps=6}中国，失去了谈判的能力{/cps}{/color}{/size}"
    nvl_n "{size=66}{color=#de2910}{cps=6}共和国之剑，未能铸成{/cps}{/color}{/size}"
    nvl hide

    scene bg black
    with dissolve
    "{size=50}关键的决断，不是一人之力的预判！{/size}"

    jump settlement

label foolhardiness_ending:
    play music "on the nature of daylight.mp3" fadein 1.0

    nvl clear
    nvl_n "客观现实是:{w}没有风洞，{w}没有试车台，{w}没有设计导弹最基本的参数"
    nvl_n "在自主设计导弹的过程中，因为缺乏参数，同时缺少风洞试验，走了许多弯路，耽误了很多时间"
    nvl_n "导弹外形的气动参数设计，因为缺少数据，不得不进行大量的实验"
    nvl_n "缺少整体设计中各部分设计之间的调度经验，无法协调高效推进"
    nvl clear
    nvl_n "{size=30}{font=DaKai.ttf}1963年，美、英、苏三国在莫斯科正式签署《关于禁止在大气层、外层空间和水下进行核武器爆炸实验的条约》又称〈部分核禁止条约〉或三家条约{/font}{/size}"
    nvl_n "条约并未禁止地下核试验{p}但是当时只有美苏两国具有进行地下核试验的能力"
    nvl_n "{size=50}{color=#de2910}{cps=6}中国，没有时间了！{/cps}{/color}{/size}"
    nvl_n "点火，发射！"
    scene bg df2explosionpit
    with fade
    nvl clear
    nvl_n "仓促的导弹试验，在一声巨响之后，将多年的理论攻关、工厂改造成果化为乌有。短期之内，核导弹实验无法开展"
    nvl_n "导弹坠落炸起的烟尘渐渐散去，烈日之下，万米高空中的一点黑影映入人们视野"
    nvl_n "导弹失败的第二天，外媒铺天盖地地展示出几张戈壁背景的高清照片，照片中央混乱的扬尘，无声地嘲笑着中国的无奈——"
    nvl_n "没有导弹的中国，无法阻止美国高空侦察机的肆意入侵"
    nvl_n "失败的导弹试验催迫着美苏大国加快限制中国的脚步。《全面禁止核试验条约》在三国强暴的核讹诈手段之下，在联合国谈判桌上正式通过"
    nvl clear
    nvl_n "{size=50}{color=#de2910}{cps=6}中国，失去了谈判的能力{/cps}{/color}{/size}"
    nvl_n "{size=66}{color=#de2910}{cps=6}共和国之剑，未能铸成{/cps}{/color}{/size}"
    nvl hide
    scene bg black
    with fade
    "{size=50}必要的仿制，决定弯道超车的效率！{/size}"

    jump settlement

label victory_ending:
    $ flag = True
    play music "<from 41.5>月亮之上（交响乐版）.mp3" if_changed
    image slogan1 text = Text("五年归国路，十年两弹成",size=150,font="DaKai.ttf")
    image slogan2 text = Text("尊严只在剑锋之上！",size=150,font="DaKai.ttf")

    nvl clear
    nvl_n "{size=50}{color=#de2910}{b}罗布泊上的一声巨响，是东方雄狮苏醒的怒吼！{/b}{/color}{/size}"
    nvl_n "{size=50}{color=#de2910}{b}冉冉升起的一朵巨云，是中华民族挺起的脊梁！{/b}{/color}{/size}"
    nvl_n "无穷的远方，无数的人们"
    nvl_n "无数的抉择，唯一的机遇"
    nvl clear
    nvl_n "{size=37}一位超群绝伦的科学家{/size}"
    nvl_n "{size=37}一位高瞻远瞩的战略家{/size}"
    nvl_n "{size=37}一位鞠躬尽瘁的爱国者{/size}"
    nvl_n "{size=37}一位浪漫不渝的好丈夫{/size}"
    nvl hide
    show slogan1 text at title_show(0.5,0.08)

    jump settlement

label settlement:
    if flag:
        "恭喜你，成功了！"
        hide slogan1 text with dissolve
        show slogan2 text at title_show(0.5,0.08)
        "两弹研发中的点点滴滴，全面体现了科学家精神的真正内涵"
        "看看其中体现的各种精神内涵吧~"
        window hide
    else:
        "很遗憾，失败了。"
        "两弹研发中的点点滴滴，依然体现了许多科学家精神的内涵"
        "看看你所收集到的科学家精神吧~"
        window hide

    show screen Spirits
    pause 3.0

    window auto
    "游戏到这里就结束了~"
    hide screen Spirits

    if(flag):
        "你步步为营，成功走过了各个生死攸关的关键决策"
        hide slogan2 text with dissolve
        show wishes at title_show(0.5,0.4)
        "愿你铭记这历史的光辉，赓续前人的灯火"
        "回到日常的生活时，将科学家精神落实于一言一行之中"
    else:
        "两弹一星这样伟大工程的成功，需要前瞻洞见生死攸关的关键决策"
        "虽然你不慎失误未能成功，不过好在只是游戏一场"
        "且看这太平的国度，这纷乱的时局。两弹一星成功的国人底气历久弥坚"
        show wishes at title_show(0.5,0.4)
        "愿你铭记这历史的光辉，赓续前人的灯火"
        "回到日常的生活时，将科学家精神落实于一言一行之中"

    scene bg black with dissolve
    scene bg acknowledgement at media_show(x=0,y=0,a=1.0)
    pause 5.0

    return
