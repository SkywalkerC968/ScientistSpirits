label Sce5:
    scene bg missilelecture
    show t ch smile at center
    with fade
    "（钱学森向工作人员讲授导弹知识）"
    show t ch smile at center
    T_CH_smile "（放下粉笔，长舒一口气）都明白了吗？"
    CHPro "……都明白了……"
    play sound "众人起身.mp3"
    "（钱学森如释重负，环视一周，发现有一位大学生面露难色）"
    T_CH_smile "小冯啊，你明白了吗？"
    XF "还行还行（心虚）"
    T_CH_smile "哪部分不明白，你就可以直接提出来，我马上给你再讲一遍"
    XF "钱院长，其实我……全都没有弄明白"
    CHPro "是{nw=.3}是{nw=.3}其实{nw=0.7}"
    CHPro "其实我们大伙都没弄明白"

    $ HS_flag = True

    show screen collection with moveinleft
    menu:
        "是否重新再讲一遍？"

        "算了。":
            $ credit -= 30
            hide screen collection with moveoutleft
            show t ch solemn handdown at center
            T_CH_solemn_handdown "今天的课就上到这吧，有什么不懂的地方下去复习复习"
            T_CH_solemn_handdown "我的任务还很重，现在没有时间细细解答了"
        "必须。":
            $ Spirits.add("甘为人梯、奖掖后学的育人精神")
            hide screen collection with moveoutleft
            window hide
            pause 1.5
            window auto
            T_CH_smile "好，来{nw=.8}"
            T_CH_smile "来，我们再讲一遍"
            T_CH_smile "帮我把黑板搬过来"
            play sound "黑板放下.mp3"
            T_CH_smile "咱们重新再来一次！"
            hide t ch smile

    jump Sce6