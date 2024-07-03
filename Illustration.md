Regarding the large scale of the whole project, although the repository has included the entire original codes, 
audio and image resources, to fully illustrate the techniques used in this game, we summarize the technical details
and ultimate outcomes as below.

## 1. plots reference:
   game plots and relative details are based on film, "Xuesen Tsien". In filmmaking, some confidential documents are
   specially allowed to check up, which made the details accurate and correct. Thus, we also use some of the details
   to enhance the difficulty and to improve the enlightenment. The others are based on adequate news resources and interview
   documents from home and abroad, which complements the international background and indicates Tsien's behavioral standards
   In addition, we refine the spirits of scientist behind the right decisions into six in total.
   
## 2. game mechanism:
   We specially add the credit mechanism in this game. It isn't explicitly displayed in the player screen, but the accumulation
   of incorrect choice will lead to slight different in game plots.
   
   In particular, the selections in this game can be mainly divided into two. First is the critical choices. Once you
   choose wrong, you will deviate the main story and veer into the bad ending directly. We design 3 bad ending in total
   which respectively correspond to critical choices in different locations. The other is the normal choices. Once you
   choose wrong, the credit will decrease. Meanwhile the credit will be judged in specific locations. If the credit is
   lower than particular value, it will trigger different plots which are more misleading, but donot change the critical
   choices that player will encounter.

  After some selections, you will collect correspongding spirits and demonstrate later in the settlement screen. Some 
  incorrect normal choices may not influence the victory ending, but will lose some of the spirits. In the final settlement
  screen, it will show in [x/6] to show whether the players have collected all the spirits and guide them to reflect the 
  process, which imprint the valuable spirits into their bones meanwhile.

## 3. clue collection:
   Clue collection mechanism is the special characteristic in the game.
   
   In brief, at every critical choice, there will pop up a column from the side showing some objects to enlighten you.
   Some are sensitive button but others are not. These button will provide some supplementary information on more details
   about the history background or the character statements. Not only will the players be led to right answers, but also
   they can have a better understanding of the international environment and the spiritual strengths. These five objects are 
   particularly selected and embeded to deliver the true meanings of the scientist spirits.

## 4. technical crux: 
### (1) aesthetic design:
    Firstly, the charater design of Xuesen Tsien in different garments, different facial expressions and different gestures.
    For this part, it is our honor to invite the proficient designer in our schoolmate, Sunny Yan, who offered excellent designs.

    Secondly, the multimodal design of every button. A single button includes at least three modes which respectively are
    "Insensitive", "hovered" and "unhovered". Only then, the button will give the players the real sense of clicking.

    In addition, the design of numerous backgrounds. They are partly drawed in AIGC and partly modified from the movie scenes 
    including complicated details and PS process. And finally they are transformed into images with higher definition of 1920*1080.

    Last but not the least, the design of audio clips. These clips include proper background music and verisimilar sound effect.
    For background music, we choose the music appropriate both in tune and volume. Then let the music start in appropriate point.
    For sound effect, we insert the sound like ship horn and loud murmurs to verisimilarize the scenarios and smooth the transition 
    between them.
### (2) script composition:
    Although most of the plots are refered to the film, the detailed catalogues and scenarios are extracted by our studio members 
    carefully. We refined the content to better show the spirits of realism and dedication of the scientists in that era.

    Especially, the reasonable bad ending design are ordeals along the way. Our assumption based on the inner and outer pressure
    at that time, which may make the ending more plausible.

    The last settlement screen refers to the chinese official documents to catagorize the scientist spirits and to summarize the 
    profile of Professor Tsien. The word contents are polished by our members.
### (3) programming skill:
    For this game, we use an engine on the basis of Python called "Ren'py". The group leader in charge of programming learned
    this engine from scratch. What's harder, as the engine is relatively unpopular, the only material is the official documents 
    with limited illustration. The leader even join the forum of the engine to ask for more reference and guidance. Finally, 
    we accomplish this game from trial and error in 15 codes and 362 blocks in total.
   
   
   
