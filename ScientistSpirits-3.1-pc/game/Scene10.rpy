label Sce10:
    image USmedia text rotate = Transform(Text("无枪的子弹",size=200,font="DaKai.ttf",color="#ed1941"),rotate=30)

    play music "sunshine.mp3" fadein 1.0 fadeout 1.0
    scene bg abvictorynews
    with Fade(2.0,1.0,2.0)
    pause 1.5
    show USmedia text rotate at media_show
    pause 4.5

    scene bg black
    with dissolve
    MZD "没有导弹，原子弹这个唬人的东西，是吓不住两个超级大国的"
    show t ch reflective at right
    T_CH_reflective "导弹的技术现在还不够成熟，学森并没有把工作做到最好，感到分外有压力"
    MZD "我们不仅要发射导弹，还要发射人造卫星，给导弹加上眼睛"
    MZD "到那个时候，我们才真正有了说话的权力"
    hide t ch reflective
    "经过两年的不懈研究，两弹结合的技术论证已经完毕，准备进行发射实验"

    scene bg sandstorm
    with dissolve
    pause 1.5
    scene bg outdoorchaos
    with dissolve
    pause 1.5
    scene bg indoorchaos
    with dissolve
    pause 1.5
    scene bg centertent
    with fade
    CHPro "今晚22:00起，发射场受冷空气袭击，有风速为20米/秒的大风侵扰"
    CHPro "这么大的风，明天竖装对接会有风险。钱院长，要不要改变一下发射计划？"
    Meteorologist "我认为不必改变发射计划！"
    "（众人侧目）"
    Meteorologist "因为这个气旋移动的速度非常快，它不会影响到27号的发射"
    CHPro "这几个点为什么没有数据？"
    Meteorologist "额，这两个点……通信联系不上，可能是他们的设备被风给刮坏了"
    CHPro "什么话？数据不全，会能保险吗？"
    Meteorologist "气旋的移动，有它自身的规律。就算我们缺少了其中两个点的评测，也并不会影响到，我们对整个气旋轨迹的判断"
    show t ch reflective at left with moveinleft
    T_CH_reflective "那27号的天气有保障吗？"
    Meteorologist "从目前的数据来看，27号无论是发射点还是弹着点，他们的气象条件都是最佳的"
    CHPro "你有把握吗？"
    "（气象技术人员没有回应）"
    if credit > 70:
        pass
    else:
        CHPro "钱院长，应该延后发射！"
        CHPro "这样的极端天气，完全超出了我们理论计算的适用范围"
        CHPro "为了确保成功，应该暂停发射计划，等待天气正常后，择机发射核导弹"

    $ Tr_flag = True

    show screen collection with moveinleft
    menu:
        "是否坚持原计划对接并发射核导弹？"

        "坚持原定计划。":
            hide screen collection with moveoutleft
            call s10_continue from _call_s10_continue
        "延后发射计划。":
            hide screen collection with moveoutleft
            jump s10_interrupt

    play music "<from 41.5>月亮之上（交响乐版）.mp3" fadein 1.0
    scene bg hddprepared
    with fade
    "{size=50}10 {nw=1.0}9 {nw=1.0}8 {nw=1.0}7 {nw=1.0}6 {nw=1.0}5 {nw=1.0}4 {nw=1.0}3 {nw=1.0}2 {nw=1.0}1 {nw=1.0}{/size}"
    "{size=50}{color=#fdb933}{font=DaKai.ttf}点火，发射！{/font}{/color}{/size}{nw=0.8}"

    play sound "<from 1 to 6>火箭发射.mp3"
    scene bg hddthrusting
    with Fade(0.5,2.0,1.0,color='#fff')
    scene bg hddrocketing
    with Fade(0.5,2.0,1.0,color='#fff')
    pause 2
    scene bg hddcruising
    with dissolve
    pause 2
    scene bg hddplunging
    with dissolve
    pause 2
    scene bg mushroomcloud
    pause .5

    jump victory_ending

label s10_continue:
    $ Spirits.add("集智攻关、团结协作的协同精神")
    T_CH_solemn_handdown "我认为，可以按照原计划，完成对接"
    CHPro "可是，钱院长……"
    T_CH_reflective "我知道，再这样的天气条件下，竖装导弹有一定的难度。"
    show t ch solemn handdown
    T_CH_solemn_handdown "但是，我们没有时间了"
    T_CH_solemn_handdown "我的建议是，{color=#fdb933}{font=DaKai.ttf}明天，竖装导弹{/font}{/color}"

    scene bg centertent
    with Fade(1.0,2.0,1.0)
    Meteorologist "钱院长，钱院长！"
    Meteorologist "是风！是风停了！明天是个好天！"
    show t ch smile at right with moveinright
    T_CH_smile "好，好，那弹着点的天气呢？"
    Meteorologist "弹着点亦是好天！"
    T_CH_exhilarated "好啊好啊，明天的试验，{color=#fbd933}{size=30}一定成功！{/size}{/color}"
    return

label s10_interrupt:
    T_CH_solemn_handdown "周总理对这次核试验下达了明确的命令"
    T_CH_solemn_handdown "这次热试只许成功，不许失败，要周到细致，做到万无一失！"
    T_CH_solemn_handdown "这样极端的天气，确实不满足既定发射条件。在没有十足把握的情况下，应当延后发射计划"

    play music "no time for caution.mp3" fadein 1.0
    scene bg centertent
    with fade
    Meteorologist "钱院长，钱院长！"
    Meteorologist "风停了，明天会是个好天！"
    T_CH_reflective "可是现在两弹尚未竖装对接，赶不到明天发射了……之后的天气呢？"
    Meteorologist "钱院长……罗布泊的气候极端多变，恐怕难以预测何时会出现一个连续三天的好天气"
    Meteorologist "不过我将持续跟踪观测，一旦有好的情况出现，立即向您汇报！"
    T_CH_reflective "嗯……你先去吧……"

    T_CH_reflective "这是我的失误啊……"
    T_CH_reflective "这样再拖下去，恐怕会有意外……"

#外媒报道中国将要进行和导弹试验的照片，天气不良，点火失败，功亏一篑。美国加苏联共同核讹诈。
    scene bg black
    with dissolve
    "几天后，聂荣臻元帅突然来电"
    NRZ "学森啊，两弹结合，能不能搞提前一点？"
    T_CH_solemn_handdown "报告聂帅，这边的沙尘暴还在持续，可能还需要一些时间"
    NRZ "学森同志，现在情况十分紧急。我们得到消息，苏联决定对我国的战略核设施进行打击"
    T_CH_solemn_handdown "聂帅……您确定吗（失语）"
    NRZ "这个情报，我们已经确认。但我们不确定，苏联人有没有胆子真打。所以，中央希望能够早一点实现两弹结合，用于震慑苏联。这很重要"
    T_CH_solemn_handdown "……聂帅，我明白了"
    "迫于外部压力，两弹结合在沙尘暴天气强行推进"

    scene bg hddprepared
    with fade
    "10{nw=1.0}9{nw=1.0}8{nw=1.0}7{nw=1.0}6{nw=1.0}5{nw=1.0}4{nw=1.0}3{nw=1.0}2{nw=1.0}1{nw=1.0}"
    "{size=50}{color=#fdb933}{b}点火，发射！{/b}{/color}{/size}{fast}"
    play sound "<from 1 to 6>火箭发射.mp3"
    scene bg hddthrusting
    with Fade(0.5,2.0,1.0,color='#fff')
    scene bg hddrocketing
    with Fade(0.5,2.0,1.0,color='#fff')
    pause 1
    scene bg hddcruising
    with dissolve
    CHPro "遥测信号追踪异常！遥测信号追踪异常！" with vpunch
    T_CH_solemn_handdown "什么情况？"
    CHPro "遥测信号丢失了，我们追踪不到导弹的位置了！有可能是沙尘暴导致传感器里进了沙子导致传感器失灵了"
    T_CH_solemn_handdown "坏了，坏了……"

    jump suspension_ending