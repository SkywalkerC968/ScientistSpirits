label Sce6:
    image df1missile text = Text("19xx.xx.xx\n东风一号导弹试射场",size=100,font="DaKai.ttf",text_align=1.0)

    play music "<from 40>no time for caution.mp3" fadein 1.0
    scene bg df1missile
    show df1missile text at title_show
    with fade
    pause 3.5
    hide df1missile text with dissolve

    CHPro "报告院长，刚才在检查导弹的时候发现导弹弹体有变形，不知能否进行下一步操作。"
    show t ch solemn handdown at center
    T_CH_solemn_handdown "好，我马上去看"
    CHPro "院长，您看，就在那"
    T_CH_solemn_handdown "这是什么时候出现的？"
    CHPro "就是在准备加注燃料的时候{p}虽然其他指标一切正常，但我们也不敢继续加燃料了"
    CHPro "弹体都变形了，这还能叫一切正常？我看这种情况不能发射"

    $ EC_flag = True

    show screen collection with moveinleft
    menu:
        "是否继续加注燃料并正常发射？"

        "是。":
            hide screen collection with moveoutleft
            jump s6_continue
        "否。":
            hide screen collection with moveoutleft
            jump s6_interrupt

label s6_success:
    $ Spirits.add("追求真理、严谨治学的求实精神")
#闪烁切换两张图片，模拟导弹发射升空
    scene bg df1prepared
    with None
    "{size=50}10 {nw=1.0}9 {nw=1.0}8 {nw=1.0}7 {nw=1.0}6 {nw=1.0}5 {nw=1.0}4 {nw=1.0}3 {nw=1.0}2 {nw=1.0}1 {nw=1.0}{/size}"
    "{size=50}{color=#fdb933}{font=DaKai.ttf}点火，发射！{/font}{/color}{/size}{nw=0.8}"

    play sound "<from 1 to 6>火箭发射.mp3"
    scene bg df1victory
    with Fade(0.5,2.0,1.0,color='#fff')
    pause 3.0

    play sound "胜利欢呼.mp3"
    CHPro "成了，成了！钱院长，成了！！！"
    show t ch exhilarated at center
    T_CH_exhilarated "恭喜恭喜！同志们辛苦了！"
    show t ch smile
    CHPro "钱院长，你是高人啊！我服了！"
    T_CH_smile "不要服我，要服科学！"

    jump Sce7

label s6_continue:
    show t ch solemn handup at left
    T_CH_solemn_handup "我认为{p}加注燃料的时候，由于弹体内部处于真空状态{p}弹体薄，大气压强容易造成这个凹陷"
    T_CH_solemn_handup "如果继续加注燃料，它可以恢复"
    CHPro "可是这样，出了问题谁来负责？这个字谁敢签？"

    show screen collection with moveinleft
    menu:
        "是否坚持正常发射？"

        "顶住压力，坚持继续加注燃料。":
            hide screen collection with moveoutleft
            pass
        "保守一点，还是放弃加注燃料。":
            hide screen collection with moveoutleft
            jump s6_interrupt

    T_CH_solemn_handup "这个字，我来签"

    scene bg addfuelin
    with dissolve
    pause 1
    stop music fadeout 2.0
    CHPro "报告院长，导弹燃料加注完毕。指标一切正常，凹陷亦正常恢复"
    T_CH_solemn_handdown "好，按时发射！"
    CHPro "是！"

    jump s6_success

label s6_interrupt:
    "研究院花费了大量的时间，重新制造了凹陷部分的弹体，再次组装，填充弹药。"
    CHPro "报告院长！" with vpunch
    CHPro "弹体在加注燃料的过程中，{font=DaKai.ttf}再次{/font}出现凹陷！请指示下一步操作！"
#在这里加上credit的判定，
#若高，则有人提出受力，等指标满足要求，不应有误
#若低，则有人质疑钱学森的战略决策，提出就是制造业跟不上
    T_CH_solemn_handup "停止加注燃料，立刻通知全体同志，召开紧集研讨分析会！"

    scene bg smallseminar
    with fade

    T_CH_solemn_handup "请技术人员立刻全面检测我们的弹体和苏联的弹体的各项指标，给出详细检测报告"
    window hide
    show t ch solemn handdown at right:
        linear 2.0 xalign 0.25
    window auto
    CHPro "钱院长，报告出来了"
    T_CH_solemn_handup "发现了什么异常？"
    CHPro "……额……这个……您亲自看看吧！"
    T_CH_solemn_handdown "唉……各项指标都有所欠缺啊……"

    if credit > 70:
        CHPro "材料和工艺等各个方面都和苏联有一定差距，但是我们弹体的各项力学指标都能满足理论计算的阈值"
        CHPro "我们的弹体，绝对足够完成任务！"
        CHPro "但是凹陷的原因，还是毫无头绪……"
    else:
        CHPro "是啊钱院长，我们的工厂制造的产品完全达不到苏联的水平"
        CHPro "现在还只是仿制就问题频出，将来自主研发的时候阻碍会更大"
        CHPro "我认为，只有先聚焦于制造业的技术升级，才能进行下一步的导弹研究"
        CHPro "是啊是啊，我们的制造业太落后了……"

    show screen collection with moveinleft
    menu:
        "中国军工制造业究竟应当何如？"

        "保证单项技术先进性，逐点完善现有工业水平":
            hide screen collection with moveoutleft
            jump s6_ambition
        "求助苏联购买零部件，之后尝试进行仿制生产":
            hide screen collection with moveoutleft
            jump s6_purchase
        "不求单项技术先进性，只求总体设计的合理性":
            hide screen collection with moveoutleft
            jump s6_adaptation

label s6_adaptation:
    T_CH_reflective "弹体凹陷很可疑，但是这一系统应该具有足够的适应性"
    T_CH_reflective "适应……适应……"
    T_CH_reflective "继续加注燃料可以恢复吗……"
    T_CH_reflective "哦！" with vpunch
    T_CH_reflective "加注燃料的时候，由于弹体内部处于真空状态{p}弹体薄，大气压强容易造成这个凹陷！"
    T_CH_solemn_handdown "继续加注燃料！凹陷可以恢复！"

    scene bg addfuelin
    with dissolve
    pause 1
    CHPro "报告院长，导弹燃料加注完毕。指标一切正常，凹陷亦正常恢复"
    T_CH_solemn_handdown "好，按时发射！"
    CHPro "是！"

    jump s6_success

label s6_ambition:
    scene bg tsienhome
    show t ch reflective at center
    with fade

    jump s4_ambition

label s6_purchase:
    scene bg tsienhome
    show t ch reflective at center
    with fade

    jump s4_purchase

