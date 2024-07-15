label Sce1:
    play music "<loop 13.0>canon in D major.mp3" fadein 3.0
    scene bg centerstadium
    with fade

    CG "（带着一丝担忧）钱先生，我还是要再问你一句，我们到底能不能造出导弹？"

    menu:
        "为什么不能，当然能造出来，中国人难道比美国人矮一头？":
            $ credit -= 10
            $ Spirits.add("胸怀祖国、服务人民的爱国精神")
            call s1_certain from _call_s1_certain
        "研制导弹的现状尚不清楚，应该能造出来，但话不能说死。":
            call s1_hopeso from _call_s1_hopeso

    "{cps=20}周总理指出，{p}我们要尽快造出{font=DaKai.ttf}导弹{/font}并实现{font=DaKai.ttf}双弹合一{/font}，这样国家才能拥有真正的安全{/cps}"

    jump Sce2

label s1_certain:
    show t us solemn at center
    T_US_solemn "陈赓将军，美国人能造出来，我们中国人不比他们少个脑子{p}{cps=20}{color=#fdb933}{font=DaKai.ttf}当然能造出来{/font}{/color}{/cps}"
    CG "（眉头舒展，露出笑容）好！我要的就是你这句话！"
    CG "请，周总理在等你！"
    return

label s1_hopeso:
    show t us solemn at center
    T_US_solemn "（面露难色）嗯……我做最大的努力，应该能造出来"
    CG "（眉头紧锁，作沉思状）好，那就尽我们最大的努力，一定要把导弹造出来！请走这边，周总理在等你"
    return