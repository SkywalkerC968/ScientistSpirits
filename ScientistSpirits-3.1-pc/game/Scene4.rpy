label Sce4:
    play music "<from 1.5>rise-epic music.mp3" if_changed
    scene bg nieoffice
    with fade

    NRZ "学森同志啊，就目前的这些情况，我们可不可以继续研究啊？"
    show t ch reflective at left
    T_CH_reflective "（面带焦虑）理论上研究是可以的，但制造业跟不上，聂帅"
    show t ch solemn handdown at left with moveinleft
    T_CH_solemn_handdown "国内没有任何一家工厂可以完成我们设计的零部件"
    T_CH_solemn_handdown "单单是一个火箭的发动机，至少需要四千五百个零部件，其他就还不要说了"
    NRZ "你可以提出自己的想法，我们去改造这些工厂"
    T_CH_solemn_handdown "短时间根本没办法做到！" with vpunch
    NRZ "别人做不到，你可以做到"
    NRZ "学森同志，我是晓得你的{p}你是一个{cps=3}可以{font=DaKai.ttf}创造奇迹{/font}的人{/cps}"

    play music "<from 13 to 30>牡丹亭.mp3" volume 0.2 fadein 1.0 fadeout 3.0
    scene bg tsienhome
    show t ch reflective at center
    with fade
    $ SE_flag = True

    show screen collection with moveinleft
    menu:
        "中国军工制造业将向何处去？"

        "保证单项技术先进性\n逐点完善现有工业水平":
            hide screen collection with moveoutleft
            jump s4_ambition
        "求助苏联购买零部件\n之后尝试进行仿制生产":
            hide screen collection with moveoutleft
            jump s4_purchase
        "不求单项技术先进性\n只求总体设计的合理性":
            hide screen collection with moveoutleft
            call s4_adaptation from _call_s4_adaptation

    jump Sce5

label s4_ambition:
    play music "<from 30>no time for caution.mp3" volume 0.8 fadein 1.0
    T_CH_reflective "制造业太落后了，无法生产出符合要求的零部件，导致导弹研制工作受阻"
    T_CH_reflective "国内真就没有一家工厂能生产出合格的零部件了吗？"
    T_CH_reflective "这是在美国喷气动力实验室从来没有遇到过的问题（皱眉沉思）"
    T_CH_reflective "难道去购买这些零件吗？"
    T_CH_reflective "不，导弹技术必须完全自主可控"
    T_CH_reflective "如果在零部件上受制于人，导弹哪怕造出来了也没有任何意义"

    "有了仿制苏联导弹的宝贵经验，研究团队的理论研究稳步推进\n苏联专家援助中国的这几年里，已经基本奠定了我国的工业基础"
    T_CH_reflective "那就着重进行理论攻关，同时根据导弹标准，改造这些工厂！"

    jump deviation_ending


label s4_purchase:
    play music "<from 30>no time for caution.mp3" volume 0.8 fadein 1.0
    T_CH_reflective "以我们目前的工业水平，根本无法造出符合要求的零件"
    T_CH_reflective "我们可以向苏联购买这些零部件，当前的首要任务是理论工作与实际组装工作协调一致，尽快造出第一枚导弹进行试验"
    T_CH_reflective "至于工厂的改造任务，可以与导弹组装试车任务齐头并进"
    T_CH_reflective "完成第一次导弹试车之后，工厂的改造工作应该就完成得差不多了。到时候可以进行零部件国产化替代，真正完成导弹的研制工作"

    scene bg black
    with dissolve
    "苏联当局断然拒绝了我方的购买请求"
    "因事先没有做好制造业升级部署，无法获得零部件，研制工作停滞不前"
    "中国重新开始部署制造业升级，力求达到苏联水平"

    jump deviation_ending


label s4_adaptation:
    $ Spirits.add("力排众议、高瞻远瞩大局观精神")
    play music "<from 33 to 79>rise-epic music.mp3" volume 0.9 fadein 1.0
    pause 1.0
    T_CH_reflective "（恍然大悟）" with hpunch
    T_CH_exhilarated "我明白了一点，要以现有的条件重新制定系统！"
    T_CH_smile "不求单项技术的先进"
    T_CH_smile "只求总体设计的合理性，充分利用仅有资源"
    T_CH_smile "以总体设计，负责对各个分系统的技术协调，提升改造现有的工业技术"
    stop music fadeout 2.0
    return