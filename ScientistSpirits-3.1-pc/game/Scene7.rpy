label Sce7:
    scene bg nominatelobby
    with fade

    NRZ "我介绍一下啊，吕部长，这是钱部长"
    show t ch smile at right with moveinright
    "你好{nw=.3}你好{nw=.3}你好{nw=0.8}"
    NRZ "吕部长，你拣那个要紧的说一下"
    ABPro "好{nw=.4}"
    ABPro "核弹试验进展顺利，但是在爆轰物理试验的时候遇到一些困难"
    ABPro "我们现在急需一个工程力学方面的专家"
    T_CH_smile "什么层次的？"
    ABPro "当然是最高层次的{p}这个人，除了在{font=DaKai.ttf}技术上{/font}有一定造诣之外，{w}还要有一定{font=DaKai.ttf}领导能力{/font}"
    ABPro "这样，可以担任技术方面的负责人"
    T_CH_smile "我给您推荐一个人，他应该可以胜任"
    ABPro "太好了！你推荐的一定是最好的"

    play music "<from 13>eutopia.mp3" volume 0.8 fadein 3.0
    scene bg yonghuaihome
    with fade

    GYH "不，我不会去的。我绝不会去制造这么大的、毁绝性的武器"
    T "你说过，\"到美国来，是为了将来回去报效祖国。\"永怀，{font=DaKai.ttf}国家现在需要你{/font}"
    GYH "可是，学森，现在全世界有良心的科学家都在禁止它。你是知道的"
    T "如果有一天，原子弹投到中国人的头上，我会后悔的{p}这不是危言耸听，永怀，日本的前车之鉴还不够吗？"
    GYH "学森……你得给我一点时间考虑"
    nvl clear

    menu:
        "是否执意劝说好友？"

        "非他不可。":
            call s7_persuade from _call_s7_persuade
        "尊重选择。":
            call s7_respect from _call_s7_respect
    stop music fadeout 2.0

    jump Sce8

label s7_persuade:
    $ Spirits.add("胸怀祖国、服务人民的爱国精神")
    T """
    我曾经发誓，要用自己的学识改变中国人的命运，你也说过

    我一定要让中国人有自己的原子弹和导弹，哪怕它的存在带来{color=#fdb933}{font=DaKai.ttf}质疑和争论{/font}{/color}

    但是，我认为，这是对抗侵略的准备{p}
    {color=#fdb933}{font=DaKai.ttf}手上没有剑{/font}{/color}和{color=#fdb933}{font=DaKai.ttf}有剑不用{/font}{/color}，是两回事
    """
    GYH "好，我答应你"
    T "以后，我们两个，就是战友了"

    return

label s7_respect:
    T """
    永怀，我理解你
    即使不去研发原子弹，亦还有千千万万的方式报效祖国
    我尊重你考虑之后的选择
    """
    GYH "谢谢你，学森"

    return