label Sce2:
    image nieoffice text = Text("聂荣臻元帅办公室",size=100,font="DaKai.ttf")

    play music "<from 106.5>time.mp3" volume 0.6 fadein 3.0
    scene bg nieoffice
    show nieoffice text at title_show

    with fade
    pause 1.5
    hide nieoffice with dissolve

    NRZ "（眉头紧皱）学森同志，你告诉我，目前工作上最迫切的是啥子？"
    show t ch solemn handdown at left
    T_CH_solemn_handdown "聂帅，两个方面。{p}{font=DaKai.ttf}一，人{/font}"

    scene bg armyarrival
    with dissolve
    T_CH_solemn_handdown "国防航空工业需要大批有专业知识的骨干力量"
    NRZ "那第二件事呢？"
    scene bg nieoffice
    show t ch solemn handdown at left
    with Dissolve(.2)
    T_CH_solemn_handdown "（坚定）我需要一个{font=DaKai.ttf}大一点的地方！{/font}"

    scene bg vastworld1
    with dissolve
    pause 1.7
    scene bg vastworld2
    with dissolve
    pause 1
    NRZ "学森同志啊……"
    scene bg nieoffice
    show t ch solemn handdown at left
    with Dissolve(.2)
    NRZ "目前我们的国家还是很穷，朝鲜战争把我们的家底打光了。{p}但是，我们会竭尽全力，满足你的要求！"
    NRZ "你晓不晓得为啥子？"
    NRZ "因为你在为国家，铸造一把锋利的宝剑！"
    NRZ "这把宝剑在手，国家才会有尊严，人民才会有和平"
    T_CH_solemn_handdown "聂帅，请您放心，学森就是为了{cps=3}{font=DaKai.ttf}报效祖国{/font}回来的，我一定竭尽全力！{/cps}"
    window auto
    stop music fadeout 3.0

    jump Sce3

