label Sce9:
    image df2missile text = Text("19xx.xx.xx\n东风二号导弹试射场",size=100,font="DaKai.ttf",text_align=1.0)

    scene bg df2prepared
    show df2missile text at title_show
    with fade
    pause 3.5
    hide df2missile text with dissolve

    "{size=50}5 {nw=1.0}4 {nw=1.0}3 {nw=1.0}2 {nw=1.0}1 {nw=1.0}{/size}"
    "{size=50}{color=#fdb933}{font=DaKai.ttf}点火，发射！{/font}{/color}{/size}{nw=0.8}"

    play sound "<from 1 to 6>火箭发射.mp3"
    scene bg df2rocketing
    with Fade(0.5,1.0,1.0,color='#fff')
    pause 1.5

    play music "<from 89>on the nature of daylight.mp3" fadein 2.5
    scene bg df2failed
    with Fade(0.5,2.0,1.0,color='#fff')

    "{size=50}东风二号第一次发射 失败{/size}"

    window show
    scene bg df2explosionpit
    with fade
    window auto

    "坠落的东风二号导弹发生巨大爆炸，钱学森深入爆炸坑检查残骸"
    "中国导弹研究人员，第一次经历了惨重的失败"
    "大家沉默地围在钱学森和导弹残骸周围"

    menu:
        "乐观地鼓励工作人员":
            call s9_positive from _call_s9_positive
        "生气地批评工作人员":
            $ credit -= 20
            call s9_negative from _call_s9_negative

    scene bg missileseminar
    with fade

    if credit > 70:
        CHPro "导弹发射八秒，飞行方向就开始出现偏差。我认为，应该从定向仪查起"
        CHPro "钱院长，我是这么想的。弹体在飞行过程中摆动，造成飞行失控"
        T_CH_reflective "（摇头）应该不是……"
        CHPro "钱院长，我有一个想法……"
        CHPro "这导弹在飞行的过程中，弹体经常会出现弹性的震动"
        CHPro "那个……定向陀螺仪，也会随时发生摆动，而造成了一定耦合的现象"
        CHPro "这会不会，就是导弹无法正常飞行的原因呢？"
        T_CH_reflective "哦？！有道理！" with hpunch
    else:
        CHPro "飞行方向出现偏差。或许，应该从定向仪查起？"
        CHPro "是不是弹体在飞行过程中摆动，造成飞行失控？"
        T_CH_reflective "（摇头）不，应该不是。大家还有其他的看法吗？"
        "（众人沉默不语）"

    jump Sce10


label s9_positive:
    $ Spirits.add("集智攻关、团结协作的协同精神")
    show t ch solemn handdown at center
    T_CH_solemn_handdown "怎么了同志们？"
    "（一阵沉默）"
    pause 1.0
    T_CH_solemn_handdown "好，没事！"
    T_CH_solemn_handdown "不就是天上掉下个东二吗。"
    show t ch solemn handup
    T_CH_solemn_handup "明天我们再把它射上去！"
    T_CH_solemn_handup "但今天这个事情，也教会我一点——"
    T_CH_solemn_handup "一定要把一切错误，消灭在地面上。{w}导弹绝对不能带着{font=DaKai.ttf}任何疑点{/font}上天！"
    T_CH_solemn_handup "这个原则，坚决不可以动摇！"
    CHPro "是！" with vpunch
    return

label s9_negative:
    show t ch solemn handdown
    T_CH_solemn_handdown "这次发射是一次惨重的失败！"
    T_CH_solemn_handdown "我之前反复强调过，导弹的制作马虎不得，必须事无巨细"
    T_CH_solemn_handdown "我认为，这次失败，必定与我们某些同事工作上的疏忽有很大关系"
    T_CH_solemn_handdown "我希望，这些同事，能够清醒地认识到自己的错误，不要再拖团队的后腿！"
    "（众人沉默不语）"
    return