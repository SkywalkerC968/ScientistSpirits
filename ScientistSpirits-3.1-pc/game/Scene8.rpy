label Sce8:

    scene bg aridland
    with dissolve
    window show
    play music "nightingale.mp3" fadein 1.0
    "严重的自然危害{nw=1.5}"
    scene bg faminepeople
    with dissolve
    "使得大跃进造成的恶果{nw=2.0}"
    scene bg darksky
    with dissolve
    "更加严重地显露出来{nw=1.5}"
    window auto
    scene bg devastatedhouse
    with dissolve
    pause 1.5

    scene bg workerdorm
    with dissolve
    $ Spirits.add("淡泊名利、潜心研究的奉献精神")
    "长期蛋白质的短缺导致研究人员大量出现水肿的问题"
    CHPro "嘿，我这脚怎么就变得这么胖，连鞋子都穿不下了"
    CHPro "你的症状还不算太严重的了，你看我这胳膊，这几天也肿得发亮"
    CHPro "最近啊，院里面这样的人老多了。听说，是因为咱这些日子吃不着肉和蛋，身体补充不到蛋白质，就会水肿，这不就显得‘胖’了"
    CHPro "说得是啊，这都多久没吃上一顿好的了"
    CHPro "唉，也不知道这日子还要熬多久"
    CHPro "我听说，还有人因为营养不良得了色盲"
    CHPro "诶你说，咱这胳膊腿的肿了就肿点，倒也能忍"
    CHPro "可他们得了色盲，那是真影响搞科学工作啊，了不得啊……"

    scene bg tsienoffice
    with dissolve
    CHPro "钱院长，中央派来的食物已经到了"
    show t ch smile at center with moveinright
    T_CH_smile "太好了，来了些什么"
    CHPro "一卡车的猪肉、鸡蛋。还有大米，面粉这些，分量都很足！"
    T_CH_smile "好！那你快去通知食堂，今晚先给大家伙做顿好的"
    T_CH_smile "大家伙都饿的不像样子了"
    CHPro "……"
    CHPro "院长，这些配给品，是发给科技人员的"
    show t ch solemn handdown
    CHPro "凡是部队体系的人，无论军师级干部，还是团级干部，{font=DaKai.ttf}一律都没有{/font}"
    T_CH_solemn_handdown "那些士兵呢？"
    CHPro "也没有"
    CHPro "这是聂帅的命令，必须不折不扣地执行"
    stop music fadeout 2.0

    jump Sce9
