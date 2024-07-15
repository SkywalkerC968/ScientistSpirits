label Sce3:
    image chsuborder text = Text("中苏边境 满洲里",size=100,font="DaKai.ttf")
    image missilecenter text = Text("国防部导弹研究所",size=100,font="DaKai.ttf")
    image termination text = Text("单方面撕毁协定",size=200,font="DaKai.ttf",color="#de2910")

    scene bg chsuborder
    show chsuborder text at title_show
    with fade
    pause 2.5

    scene bg missilecenter
    show missilecenter text at title_show
    with fade
    pause 2.5
    play sound "打开厂门.mp3"
    hide missilecenter with dissolve

    "（苏联专家正在讲授导弹知识）"
    "叮！叮叮！" with vpunch
    "Время вышло!（时间到了！）"

    menu:
        "是否继续追问？"

        "是。":
            pass

    play sound "众人议论.mp3"
    CHPro "这里还没讲完啊"
    CHPro "（转向翻译）你跟他们说等他们下班以后，我们能不能留下来再研究一下？"
    Trans "Можем ли мы остаться после работы и продолжить работу над ракетами?\n（请问下班以后，我们能留下来继续研究导弹吗）"
    SUPro "В соглашении прописано, что нельзя подходить к ракетам без присутствия советских специалистов\n（协议规定，苏联专家不在场的情况下，你们不能接近导弹）"
    Trans "他说协议规定，在苏联专家不在场的情况下我们是不能接近导弹的"
    "（……不满……难以接受……无奈……隐忍……）"

    scene bg smallseminar
    with dissolve
    $ V2_flag = True

    show t ch solemn handup at center
    T_CH_solemn_handup "这些导弹，德国V-2导弹演变过来的，苏联的第一代导弹，没有制导系统，属于淘汰产品"

    play music "<from 1.5>rise-epic music.mp3"
    CHPro "淘汰产品？"
    "（愤怒，砸桌子）{nw=1}" with vpunch
    CHPro "真拿自己当上帝了。{nw=1.5}老大哥还是老大哥。{nw=1.5}太过分了！……{nw=2}"

    show screen collection with moveinleft

    menu:
        "下一步导弹研制方向何如？"

        "仿制苏联\"淘汰产品\"。":
            hide screen collection with moveoutleft
            call s3_imitation from _call_s3_imitation
        "导弹系统\"完全自主\"。":
            hide screen collection with moveoutleft
            jump s3_independence

    hide t ch solemn handdown
    show termination text at media_show(0.2)
    play sound "低频撞击.mp3"

    "{size=45}{cps=10}苏联单方面撕毁了《十月十五号协定》撤走了{font=DaKai.ttf}全部{/font}专家{/cps}{/size}"
    "导弹研究院的科学家在钱学森的领导下，夜以继日，讨论研究"
    stop music fadeout 2.0

    jump Sce4

label s3_imitation:

    show t ch solemn handdown at center
    T_CH_solemn_handdown "看人脸色的日子是不好过……"
    show t ch solemn handup at center
    T_CH_solemn_handup "所以我们更应该加紧把自己的导弹研制出来！"
    T_CH_solemn_handup "客观现实是什么？"
    T_CH_solemn_handup "{w}一，我们没有风洞{p}二，没有试车台{p}三，连设计最基本的参数我们都没有"
    T_CH_solemn_handdown "难道干等吗？"
    show t ch solemn handdown at center
    T_CH_solemn_handdown "所以仿制是必须的，少走很多弯路，积蓄一些经验"
    T_CH_solemn_handdown "如果大伙受点气，我认为应该的，别往心里去"
    CHPro "嗯{nw=.4}嗯对{nw=.4}没错{nw=.4}是啊{nw=1.4}"
    return

label s3_independence:
    T_CH_solemn_handdown "苏联专家还是靠不住，保不准哪天他们就不帮助我们了"
    T_CH_solemn_handdown "还是得靠我们自己，现在研制不出来，那我们就再加把劲"
    T_CH_solemn_handdown "依我看，为了节省时间，我们就不用管这个淘汰产品了"
    T_CH_solemn_handdown "应该直接开始研制我们自己的导弹！"

    hide t ch solemn handdown
    show termination text at media_show(0.2)
    play sound "低频撞击.mp3"
    "{size=45}{cps=10}苏联单方面撕毁了《十月十五号协定》撤走了{font=DaKai.ttf}全部{/font}专家{/cps}{/size}"
    "导弹研究院的科学家在钱学森的领导下，夜以继日，讨论研究"
    hide termination text

    jump foolhardiness_ending