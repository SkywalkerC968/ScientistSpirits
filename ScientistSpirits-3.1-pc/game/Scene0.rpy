label Sce0:
    play music "<from 7>river flows in you.mp3" volume 0.5 fadein 3.0 fadeout 1.0
    scene bg kimballoffice
    with dissolve

    DK "Qian, you can't go! You are too valuable to us! Please reconsider"
    show t us solemn
    T_US_solemn "valuable……"

    scene bg awardstage
    show t us confident at left
    with Fade(1.0, 1.0, 1.0, color="#fff")

    T_US_confident "Thank you, thank you..."
    window hide
    show award1 at media_show(1.0,0.7,0.1)
    pause 2
    show award2 at media_show(1.0,0.8,0.3)
    pause 2
    show award3 at media_show(1.0,0.7,0.5)
    pause 2
    show award4 at media_show(1.0,0.8,0.7)
    pause 3
    window auto

    scene bg kimballoffice
    show t us solemn
    with Fade(1.0, 1.0, 1.0, color="#fff")

    T_US_solemn "My mind is made up. Thank you, General"
    hide t us solemn
    "(calling...)" with hpunch
    DK "Professor Qian has had direct access to highly guarded military secrets"
    DK "He is a genius, Sir"
    DK "It's as simple as that, it all started in his head"
    DK "If he returns to {color=#de2910}Communist China{/color}, or {color=de2910}the Soviet{/color} get ahold of him, it will pose a threat to the entire Western Hemisphere"

    play music "<loop 30>heart to courage.mp3" volume 0.6 fadein 2.0 fadeout 2.0
    DK "You can't let him go back to China. {color=#de2910}{b}Absolutely not!{/b}{/color}"
    DK "That man inside can top of 5 divisions, \n{color=#fdb933}{size=50}5 amphibious Navy divisions!{/size}{/color}\n【他一人能顶五个师！】"

    scene bg tsienstudy
    with dissolve

    "钱学森从此被软禁在美国家中，每个月需到移民局报到"
    "在漫长的软禁期间中，钱学森开始对全新科学的研究"
    "1954年，{color=#fdb933}{size=50}《工程控制论》{/size}{/color}完成"

#地图上标注箭头，标记各个位置，给出背景知识，在日内瓦可以走向下一个场景
    call screen worldmap with dissolve

    play sound "汽笛.mp3"
    scene bg largeliner
    with dissolve
    "1955.9.17 钱学森从洛杉矶踏上归途"


    play music "<from 31>春节序曲.mp3" fadein 3.0
    scene bg trainfield
    with dissolve
    $ window_flag = True
    "1955.10.8 钱学森全家回到祖国"

    jump Sce1