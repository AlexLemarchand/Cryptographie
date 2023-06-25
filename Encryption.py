import random
from sys import getsizeof

characters = ['O', '?', 'X', '"', 'E', 'M', 'g', '¬', '&', 'a', 'ï', 'c', '‡', '0', '9', 'C', '!', '+', '>', 'l', 'u', '[', 'ù', 'Ù', '2', 'd', '£', 'U', 'e', 'Z', 'è', '(', '3', '<', 'y', 'h', '@', 't', 'J', '®', 'L', 'n', '-', 'w', 'v', ":", 'Y', 'j', 'A', 'S', "ç", 'W', 'k', '%', 's', 'V', "/", 'D', 'T', 'æ', 'B', 'µ', '1', 'Q', 'o', '€', 'P', '5', '|', '∂', 'z', 'ê', 'm', '#', 'K', 'œ', 'Ê', 'À', 'b', '$', '©', '_', 'x', 'p', 'Ç', 'È', 'H', '*', 'r', '†', 'N', 'É', '∏', '.', ')', ',', "'", ' ', '8', '6', ']', 'q', 'i', '=', 'f', 'G', '∑', 'î', 'R', 'ƒ', '™', ';', 'é', '7', '4', 'F', '°', '≈', 'I', "à"]

cryptedCharacters = [['O', '42†B$é&0F£€SN8yLJ‡n$èHMh€'], ['?', '*t5Kq‡C_©?[WJ71‡yz‡"k4F,&'], ['X', "52;jés'£@Ê'2£‡xvÀc@7H,é&É"], ['"', 'SfæyN5*C5ÀàSÇsZNÙa07n≈∏ÉD'], ['E', 'œ©9|TWfP%!tÀzUSx‡U5[°†Ù0o'], ['M', ' h%6m(À_hD1sC>zl+X8] b&F,'], ['g', 'eI[Atæ‡9(µœtzèÀQy[éoh+qC5'], ['¬', 'M#Gww7g>Ù‡∏Xo+PmQµRMyœw;|'], ['&', 'tyù221,Q[†(Cl!A#Bƒ®H5<C=('], ['a', 'k"x£v-b6dHnKdv†|rF6HI$Uv>'], ['c', 'h:Nwt0<Ç®eà∏R,,k940bfK%G='], ['‡', "_:z'aDw2çqQ=#A!pbjf:v'ÉVœ"], ['0', 'Iequx/è?€>Jhj†|oEpÈ™qAç,#'], ['9', 'æù¬Hv®<8q∑j;br-7≈V[a∂3w[H'], ['C', '∂Ê£€È¬\'[#ÙUY.∑ujµ*<zH"™xn'], ['!', '(€X∑µçFs7É≈Nrµi(D+VNHî":S'], ['+', '8-p<∑+gJ/sù 3Wcf5QJnEià_æ'], ['>', '>eµ=°¬£Qg¬N,qY|R∏‡À*¬b<o)'], ['l', 'qæçc€"gk;h%%)U‡∑Vk<>A..M='], ['u', 'Cæ#9îb&.Dàvuw∑Ù(&2dzfÀV¬['], ['[', 'n61wuép-jT$gêkl∏Ww†3(lJ®-'], ['ù', '∑Èa£3t∑Ê::Fx5tq%:XÈbm>,Fr'], ['Ù', '†È£m2,∏Gtge£Hj0çÊ4°0kçC6.'], ['2', '|+ùpqZN/à:h©mx]cAo5À)y¬69'], ['d', '<"U!HµùL6]|≈æé<qzyêéHHyÉ©'], ['£', 'dùsƒ≈çæ4†e;8ÀA≈ƒGÊey"jx\'z'], ['U', 'JiocA]hWTd7‡1Êv∂!®sJ,Q3We'], ['e', '"\'SYd:¬-.F-/J*2‡ÊgqEF†EùK'], ['Z', '%FÇyÀX(c+ÈN:∂†∏|B1Sz∂HG6k'], ['è', '<FÀrF1Z0W*£x(Ml"M/EÇpà. ;'], ['(', ".bnCZPUÙÇo°.1XMÈ°-_nA5*'è"], ['3', 'a‡2:£7 gùtvfs0†E%xJ.êUbCe'], ['<', 'AKfkkE#j4:zhvOgZ™M.2é∏aqK'], ['y', '?Qœ‡°$Tî;ibwHz £PnhçlNÈé9'], ['h', '¬XÙ=%®s27lî|.i®r5èçaœÀQ:œ'], ['@', '%éJRM6sx,/$R[OrGsGMÀ,m©3?'], ['t', '†E90¬"É@)P8jR&éµ∏,s\'3sœvT'], ['J', 'ù†∂©NvL¬ièÀè-†ç_çlsS[∏1;c'], ['®', "'≈!#= ÀœNs=9Lv>∑L;|b'≈Ei."], ['L', '(,2RPja!cR/∂&3=S]ê=V7v?VI'], ['n', 'È≈Kù TN<5< *dYçàêo3€4w©œù'], ['-', '_SœJ¬éQ724Sc[îù"ucæ†w†ƒ™®'], ['w', 'B‡$éEàcu£zsÊ6F9-LafÊAVJæ!'], ['v', '2€us<vSœ°É[7u,UT]†3SævWav'], [':', 'p9Oi!"yaqcM™o∑.C*œWyÙC!6x'], ['Y', ']‡sLu+A_y|AÊhIK;<3îD∏ténh'], ['j', '‡;_ro4iKhÉÙez∑K.;‡Ox≈T>É2'], ['A', "∂OP<;_nù'(æ0N©nUA:Mwz4°Mz"], ['S', '!L<FA"£ƒ P‡_pU3lRl∑/®wU∑µ'], ['ç', 'ùoèi°vHPP∏kÊuÉ™,72Sd/fIV∂'], ['W', '[,ÊE!J|SSèSCr_‡gv∂7®IPzEé'], ['k', 'zCGR#w#"g,$bS"€7< K?!.xa('], ['%', 'PYm™!k]Ù-€wWIYÈ>ÊkNènTÈYq'], ['s', 'aY,%VX∑%*BG≈d0ÙàÀêB°hT G7'], ['V', "<3Y†/]Ly<DC'Oaj1N-à1N()Y;"], ['/', "N7@ÙeGa$'°4©VaO-]ÊéIEc6q("], ['D', 'Sà°àv,PÀn/8,1wb$kè(IèQ6Oæ'], ['T', '#ÊC<N$<‡ÊU2# P)4®8)%,u)kZ'], ['æ', '∑Ymg_*SW_P;3‡1£jeZA!.bùqU'], ['B', 'l6V>êÀ©((XÇ≈°E_MÈXÉh<‡™k '], ['µ', 'À|15 *XçéEµD4Md†l©¬37Fl9>'], ['1', 'G<C=∑î]$jg|ƒ[jU7µKG£‡€o]-'], ['Q', '+KI°H©éNµjHF[†)sutwa4µn™z'], ['o', "(xmd:%'w]Çj&U:Uf≈Ù'@@x)∑6"], ['€', 'Ê5uéRbÉY?ù°|∑èS0êk£ù=*gmê'], ['P', '≈î:>!EàA#2N°1∏èt8ÉdÀ∏s=k:'], ['5', 'Q=/etqbJÈc)©7a@&kPh°>W%wk'], ['|', 'LNih7/urkZ5MYPkrÙDZÀLuƒT_'], ['∂', '+*k.rWW∏Ç6l©NvL&rTheByàÀj'], ['z', '®z*g™b(v°jXf[êê‡%Fg2vd2"j'], ['ê', 'Mqç;ÇçAHCSµ!!0é V?SdV∑+c)'], ['m', '?9-aQ:ÇvYKeF∑[\'_:©\'_="$3®'], ['#', 'xî9IbdY°l,"LîÉ7R7|=wEAWUC'], ['K', 'E6∂6p≈E.w™‡ufUo%€œ/Fy£Ç£Q'], ['œ', 'L[W7A+rrxèfé+©FÉS]p-ç≈,Q>'], ['Ê', '/lÊku3=£è5èkfmài5Dç%hùBU≈'], ['À', 'Bn)Çh0≈#%/%?E8<dAE∂≈fèn+X'], ['b', '!L%n;#RUnVo9E™¬8_(UAtwX£$'], ['$', 'i†&>uÙMIS.°zK*LA=7NK>;>çD'], ['©', "d'©œ7@=<FÙxyUE™-ùÇrMl2£>i"], ['_', '<3LkpT"L‡>fc0)X≈TO4è°6NÉ>'], ['x', '‡[7jæ.8/Uà&#¬q‡<N*Oµl©jV;'], ['p', '!q8[∂∑†0oTuJ≈GmHAÊH!lYSÙF'], ['Ç', 'eeTlAw68mo aza3/cd∂j52¬.6'], ['È', 'Hµ-iJH®àaRê™ƒQt<£9>êÉ,;O='], ['H', 'ÀKKI6S ZGL≈È≈‡+gè∂ededuKQ'], ['*', '&!B?È=gnîvf4(µ5ùQèc8eEÊ]è'], ['r', '¬ll©&rj+lÀ3∂QE#∂!8bsoîFYg'], ['†', '2∂kqM|À9&sênBa?=O6ZBxiLy†'], ['N', '&Uu‡@h9‡àbJYçFtè∏Coæ:*FA1'], ['É', 'Ê*Tµ∑£nor4Rs;ÊP@R?cZZoGN>'], ['∏', 'îxiæé€ƒ[wqHé&;+m:£Mft<JE2'], ['.', 'o=É!p£+%àTo®h0àl¬V∂)@4+©ê'], [')', 'LœÊbæÇI®¬kN:°@J2=H≈ƒ;8®x;'], [',', 'ç&¬v%zsW.|!ùT©∏ƒt#r∂µ.$k€'], ["'", '+µêXys"S?R(w[AMwTAœ®™€èax'], [' ', 'gsÈr∂‡tA=tL)u=*m//D&nQ€(R'], ['8', 'GF£&RJ∂Yg@Ç =è™QX02 œL0h='], ['6', 'vZ6Nz4ÀT∏mà‡2≈EX$qq@-caê9'], [']', '%XGvlx=lCv<∑-|e0¬"1méàBTV'], ['q', '&àZ[<|àE1Uaqd‡<î0z=)EX‡v/'], ['i', 'St:;Éç£œHèp∂kæc@qK XsYIK†'], ['=', '©K™Ub?ƒ,©_:Ù1v°#Ê©Wv_;É03'], ['f', 'CNdJ$6d≈DçÙm∂&!l_x-QÊ_#mU'], ['G', '∏%"qttµGÇ-|/4éƒéCSiRù-S≈î'], ['∑', 'Bx@dusçæ‡d∑è5AI2baÈ5mmN∑x'], ['î', 'hb4††[&gu2lkp∑1a5qb!ri:œM'], ['R', 'IO@,S çES®T¬2à™IdS >®<È5n'], ['ƒ', '%G4*<d™aGzH8e®GM∏Êƒj™pv€à'], ['™', 'iEnàqÊVT∂àP@TÉ†F(BXçYa°∏ '], [';', 'e.S∂WA∂°%dùJlîpù,èXgKB!j&'], ['é', '6O|™OM∏=%bq( 1-k[îMd]5çe['], ['7', "5àN7R'[WDl*mirÙ/†eC9K£aVb"], ['4', 'pKHAœÙ>K]èèlb;Êp#y!3:r9ul'], ['F', "€6oOB°&Gcs'yê<)SJ6ry2è|Ç;"], ['°', 'hx"6s==GMpYylOrzÉ©f€yuS)d'], ['≈', 'wœ(Y;°t7†M/àxjàKq?3WP™£ù"'], ['I', 'Q/ÇD©ÀrƒÙ1eyl.G≈ r9xfzL®*'], ['à', 'ky©2†<ƒ¬I.ê?µ?<nQzq2:∏/îR']]

simplifiedCryptedCharacters = ['42†B$é&0F£€SN8yLJ‡n$èHMh€', '*t5Kq‡C_©?[WJ71‡yz‡"k4F,&', "52;jés'£@Ê'2£‡xvÀc@7H,é&É", 'SfæyN5*C5ÀàSÇsZNÙa07n≈∏ÉD', 'œ©9|TWfP%!tÀzUSx‡U5[°†Ù0o', ' h%6m(À_hD1sC>zl+X8] b&F,', 'eI[Atæ‡9(µœtzèÀQy[éoh+qC5', 'M#Gww7g>Ù‡∏Xo+PmQµRMyœw;|', 'tyù221,Q[†(Cl!A#Bƒ®H5<C=(', 'k"x£v-b6dHnKdv†|rF6HI$Uv>', '-INfVÀ+Çpw¬†£ÈM/O;µP)™kl7', 'h:Nwt0<Ç®eà∏R,,k940bfK%G=', "_:z'aDw2çqQ=#A!pbjf:v'ÉVœ", 'Iequx/è?€>Jhj†|oEpÈ™qAç,#', 'æù¬Hv®<8q∑j;br-7≈V[a∂3w[H', '∂Ê£€È¬\'[#ÙUY.∑ujµ*<zH"™xn', '(€X∑µçFs7É≈Nrµi(D+VNHî":S', '8-p<∑+gJ/sù 3Wcf5QJnEià_æ', '>eµ=°¬£Qg¬N,qY|R∏‡À*¬b<o)', 'qæçc€"gk;h%%)U‡∑Vk<>A..M=', 'Cæ#9îb&.Dàvuw∑Ù(&2dzfÀV¬[', 'n61wuép-jT$gêkl∏Ww†3(lJ®-', '∑Èa£3t∑Ê::Fx5tq%:XÈbm>,Fr', '†È£m2,∏Gtge£Hj0çÊ4°0kçC6.', '|+ùpqZN/à:h©mx]cAo5À)y¬69', '<"U!HµùL6]|≈æé<qzyêéHHyÉ©', 'dùsƒ≈çæ4†e;8ÀA≈ƒGÊey"jx\'z', 'JiocA]hWTd7‡1Êv∂!®sJ,Q3We', '"\'SYd:¬-.F-/J*2‡ÊgqEF†EùK', '%FÇyÀX(c+ÈN:∂†∏|B1Sz∂HG6k', '<FÀrF1Z0W*£x(Ml"M/EÇpà. ;', ".bnCZPUÙÇo°.1XMÈ°-_nA5*'è", 'a‡2:£7 gùtvfs0†E%xJ.êUbCe', 'AKfkkE#j4:zhvOgZ™M.2é∏aqK', '?Qœ‡°$Tî;ibwHz £PnhçlNÈé9', '¬XÙ=%®s27lî|.i®r5èçaœÀQ:œ', '%éJRM6sx,/$R[OrGsGMÀ,m©3?', '†E90¬"É@)P8jR&éµ∏,s\'3sœvT', 'ù†∂©NvL¬ièÀè-†ç_çlsS[∏1;c', "'≈!#= ÀœNs=9Lv>∑L;|b'≈Ei.", '(,2RPja!cR/∂&3=S]ê=V7v?VI', 'È≈Kù TN<5< *dYçàêo3€4w©œù', '_SœJ¬éQ724Sc[îù"ucæ†w†ƒ™®', 'B‡$éEàcu£zsÊ6F9-LafÊAVJæ!', '2€us<vSœ°É[7u,UT]†3SævWav', 'p9Oi!"yaqcM™o∑.C*œWyÙC!6x', ']‡sLu+A_y|AÊhIK;<3îD∏ténh', '‡;_ro4iKhÉÙez∑K.;‡Ox≈T>É2', "∂OP<;_nù'(æ0N©nUA:Mwz4°Mz", '!L<FA"£ƒ P‡_pU3lRl∑/®wU∑µ', 'ùoèi°vHPP∏kÊuÉ™,72Sd/fIV∂', '[,ÊE!J|SSèSCr_‡gv∂7®IPzEé', 'zCGR#w#"g,$bS"€7< K?!.xa(', 'PYm™!k]Ù-€wWIYÈ>ÊkNènTÈYq', 'aY,%VX∑%*BG≈d0ÙàÀêB°hT G7', "<3Y†/]Ly<DC'Oaj1N-à1N()Y;", "N7@ÙeGa$'°4©VaO-]ÊéIEc6q(", 'Sà°àv,PÀn/8,1wb$kè(IèQ6Oæ', '#ÊC<N$<‡ÊU2# P)4®8)%,u)kZ', '∑Ymg_*SW_P;3‡1£jeZA!.bùqU', 'l6V>êÀ©((XÇ≈°E_MÈXÉh<‡™k ', 'À|15 *XçéEµD4Md†l©¬37Fl9>', 'G<C=∑î]$jg|ƒ[jU7µKG£‡€o]-', '+KI°H©éNµjHF[†)sutwa4µn™z', "(xmd:%'w]Çj&U:Uf≈Ù'@@x)∑6", 'Ê5uéRbÉY?ù°|∑èS0êk£ù=*gmê', '≈î:>!EàA#2N°1∏èt8ÉdÀ∏s=k:', 'Q=/etqbJÈc)©7a@&kPh°>W%wk', 'LNih7/urkZ5MYPkrÙDZÀLuƒT_', '+*k.rWW∏Ç6l©NvL&rTheByàÀj', '®z*g™b(v°jXf[êê‡%Fg2vd2"j', 'Mqç;ÇçAHCSµ!!0é V?SdV∑+c)', '?9-aQ:ÇvYKeF∑[\'_:©\'_="$3®', 'xî9IbdY°l,"LîÉ7R7|=wEAWUC', 'E6∂6p≈E.w™‡ufUo%€œ/Fy£Ç£Q', 'L[W7A+rrxèfé+©FÉS]p-ç≈,Q>', '/lÊku3=£è5èkfmài5Dç%hùBU≈', 'Bn)Çh0≈#%/%?E8<dAE∂≈fèn+X', '!L%n;#RUnVo9E™¬8_(UAtwX£$', 'i†&>uÙMIS.°zK*LA=7NK>;>çD', "d'©œ7@=<FÙxyUE™-ùÇrMl2£>i", '<3LkpT"L‡>fc0)X≈TO4è°6NÉ>', '‡[7jæ.8/Uà&#¬q‡<N*Oµl©jV;', '!q8[∂∑†0oTuJ≈GmHAÊH!lYSÙF', 'eeTlAw68mo aza3/cd∂j52¬.6', 'Hµ-iJH®àaRê™ƒQt<£9>êÉ,;O=', 'ÀKKI6S ZGL≈È≈‡+gè∂ededuKQ', '&!B?È=gnîvf4(µ5ùQèc8eEÊ]è', '¬ll©&rj+lÀ3∂QE#∂!8bsoîFYg', '2∂kqM|À9&sênBa?=O6ZBxiLy†', '&Uu‡@h9‡àbJYçFtè∏Coæ:*FA1', 'Ê*Tµ∑£nor4Rs;ÊP@R?cZZoGN>', 'îxiæé€ƒ[wqHé&;+m:£Mft<JE2', 'o=É!p£+%àTo®h0àl¬V∂)@4+©ê', 'LœÊbæÇI®¬kN:°@J2=H≈ƒ;8®x;', 'ç&¬v%zsW.|!ùT©∏ƒt#r∂µ.$k€', '+µêXys"S?R(w[AMwTAœ®™€èax', 'gsÈr∂‡tA=tL)u=*m//D&nQ€(R', 'GF£&RJ∂Yg@Ç =è™QX02 œL0h=', 'vZ6Nz4ÀT∏mà‡2≈EX$qq@-caê9', '%XGvlx=lCv<∑-|e0¬"1méàBTV', '&àZ[<|àE1Uaqd‡<î0z=)EX‡v/', 'St:;Éç£œHèp∂kæc@qK XsYIK†', '©K™Ub?ƒ,©_:Ù1v°#Ê©Wv_;É03', 'CNdJ$6d≈DçÙm∂&!l_x-QÊ_#mU', '∏%"qttµGÇ-|/4éƒéCSiRù-S≈î', 'Bx@dusçæ‡d∑è5AI2baÈ5mmN∑x', 'hb4††[&gu2lkp∑1a5qb!ri:œM', 'IO@,S çES®T¬2à™IdS >®<È5n', '%G4*<d™aGzH8e®GM∏Êƒj™pv€à', 'iEnàqÊVT∂àP@TÉ†F(BXçYa°∏ ', 'e.S∂WA∂°%dùJlîpù,èXgKB!j&', '6O|™OM∏=%bq( 1-k[îMd]5çe[', "5àN7R'[WDl*mirÙ/†eC9K£aVb", 'pKHAœÙ>K]èèlb;Êp#y!3:r9ul', "€6oOB°&Gcs'yê<)SJ6ry2è|Ç;", 'hx"6s==GMpYylOrzÉ©f€yuS)d', 'wœ(Y;°t7†M/àxjàKq?3WP™£ù"', 'Q/ÇD©ÀrƒÙ1eyl.G≈ r9xfzL®*', 'ky©2†<ƒ¬I.ê?µ?<nQzq2:∏/îR']

letters = ['O', '?', 'X', '"', 'E', 'M', 'g', '¬', '&', 'a', 'ï', 'c', '‡', 'C', '!', '+', '>', 'l', 'u', '[', 'ù', 'Ù', 'd', '£', 'U', 'e', 'Z', 'è', '(', '<', 'y', 'h', '@', 't', 'J', '®', 'L', 'n', '-', 'w', 'v', ":", 'Y', 'j', 'A', 'S', "ç", 'W', 'k', '%', 's', 'V', "/", 'D', 'T', 'æ', 'B', 'µ', 'Q', 'o', '€', 'P', '|', '∂', 'z', 'ê', 'm', '#', 'K', 'œ', 'Ê', 'À', 'b', '$', '©', '_', 'x', 'p', 'Ç', 'È', 'H', '*', 'r', '†', 'N', 'É', '∏', '.', ')', ',', "'", ' ', ']', 'q', 'i', '=', 'f', 'G', '∑', 'î', 'R', 'ƒ', '™', ';', 'é', 'F', '°', '≈', 'I', "à"]

FullyCryptedMessageForDisplay = ""

""" Noyer le message dans la masse """
def randomCharacters(n: int, text: str, nbChar: int):
   arrText = list(text)
   result = ""
   insertNumber = 0
   appendNumber = 0
   lastCharacter = 0
   for _ in range(1, n+1):
      character = random.randint(0, nbChar - 1)
      while character == lastCharacter:
         character = random.randint(0, nbChar - 1)
      index = random.randint(0, 1)
      if index == 1: 
         appendNumber += 1
         arrText.append(characters[character])
      else:
         insertNumber += 1
         arrText.insert(0, characters[character])
      lastCharacter = character
   result = "".join(arrText)
   result = f"{insertNumber}{checkRandomCharacter(nbChar)}{result}{checkRandomCharacter(nbChar)}{appendNumber}"
   return result

""" dcode"""

""" Générer un caractère non-numérique """
def checkRandomCharacter(nbChar: int):
   char = characters[random.randint(0, nbChar - 1)]
   while char.isnumeric():
      char = characters[random.randint(0, nbChar - 1)]
   return char

def checkCompatibility(arrMin, arrExc, text: str):
   arrSolutions = []
   lastValue = 0
   lastMin = 0
   lastExc = 0
   for i in arrMin:
      if lastMin + 1 == i:
         lastMin = i
         arrMin.pop(arrMin.index(lastMin - 1))
      else:
         lastMin = i
   for i in arrExc:
      if lastExc + 1 == i:
         lastExc = i
         arrExc.pop(arrExc.index(lastExc - 1))
      else:
         lastExc = i
   completeArr = arrMin + arrExc
   completeArr.sort()
   for i in completeArr:
      if lastValue + 1 == i and text[lastValue] == "<" and text[i] == "!":
         arrSolutions.append(i + 1)
         lastValue = i
      else:
         lastValue = i
         continue
   if len(arrSolutions) == 1:
      return arrSolutions[0]
   else:
      for i in arrSolutions:
         if checkKey(i, text) or checkKey(i + 1, text) or checkKey(i + 2, text):
            return i

def checkKey(index: int, text: str):
   if text[index + 1] == "?" and text[index + 2] == "<" and text[index + 3] == ")":
      return True
   return False

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def decode(text: str, nbChar: int):

   result = ""
   currentCryptedCharacter = ""
   firstDecryptionText = ""
   for char in text:
     if char != "0" and char != "1":
         """ Repasser en base 10 et utiliser l'index pour trouver le caractère """
         currentCryptedCharacter = int(str(currentCryptedCharacter), 2)

         """ Diviser par 346 == opération inverse de la ligne 183 pour trouver le bon index """
         firstDecryptionText = f"{firstDecryptionText}{characters[round(currentCryptedCharacter / 346)]}"

         """ Réinitialisation """
         currentCryptedCharacter = ""
     else:
        """ Compléter le chiffre en binaire """
        currentCryptedCharacter = f"{currentCryptedCharacter}{char}"
   arrText = list(firstDecryptionText)

   """ Diviser tout le texte en bout de 25 caractères (== longueur d'un caractère allongé [ligne 7]) """

   simpleArrText = chunks(arrText, 25)
   simplifiedArrText = []
   normalText = ""
   for data in simpleArrText:
      complexLetter = "".join(data)
      simplifiedArrText.append(complexLetter)
   for letter in simplifiedArrText:
      normalText = f"{normalText}{characters[simplifiedCryptedCharacters.index(letter)]}"
   arrMin = [i for i, x in enumerate(list(normalText)) if x == "<"]
   arrExc = [i for i, x in enumerate(list(normalText)) if x == "!"]
   arrText = list(normalText)
   index = checkCompatibility(arrMin, arrExc, normalText)
   solution = numberOfInt(normalText, index)

   """ Solution[0] == la clé """
   """ Solution[1] == premier index de la clé """
   """ Solution[2] == dernier index de la clé """

   if solution == [0, 0, 0]:
      print("Jeez")
   elif solution[0] != 0 and normalText[2 + index + len(str(solution[0]))] == ")" and normalText[1 + index + len(str(solution[0]))] == "<" and normalText[index + len(str(solution[0]))] == "?":
      print(f"Passed : {solution[0]}")

      """ Supprimer la clé du texte """

      nbOfDigit = solution[2] - solution[1] # longueur de la clé
      for _ in range(0, nbOfDigit + 1):
         arrText.pop(solution[1])
   numberOfFakeLetters = ""

   """ Lignes 138 à 154 : supprimer les caractères aléatoires générés à la ligne 188 """

   for i in range(0, 3):
      if arrText[i].isnumeric():
         numberOfFakeLetters = f"{numberOfFakeLetters}{arrText[i]}"
      else:
         break
   for index in range(0, int(numberOfFakeLetters) + 3):
      arrText.pop(0)
   numberOfFakeLetters = ""
   arrText.reverse()
   for i in range(0, 3):
      if arrText[i].isnumeric():
         numberOfFakeLetters = f"{arrText[i]}{numberOfFakeLetters}"
      else:
         break
   for index in range(0, int(numberOfFakeLetters) + 3):
      arrText.pop(0)
   arrText.reverse()
   print("Minimized crypted code :", "".join(arrText))

   """ Opération inverse à celle de la ligne ? pour trouver le bon caractère """

   r = max(solution[0], nbChar) % min(solution[0], nbChar)
   for letter in arrText:
      finalIndex = 0
      if characters.index(letter) - r < 0:
         finalIndex = characters.index(letter) - r + nbChar
      else:
         finalIndex = characters.index(letter) - r
      result = f"{result}{characters[finalIndex]}"

   # print("Decrypted result :", result)
   return result

def encode(text: str, nbChar: int):
  global FullyCryptedMessageForDisplay
  firstEncryptionResult = ""
  """ Clé aléatoire entre 2 et 999 """
  byte = random.randint(2, 999)
  while byte % nbChar == 0:
    byte = random.randint(2, 999)
  r = max(byte, nbChar) % min(byte, nbChar)
  for letter in text:
    finalIndex = 0
    """ Récupérer le caractère equivalent si on ajoute r à l'index du caractère """
    if r + characters.index(letter) >= nbChar:
       finalIndex = characters.index(letter) + r - nbChar
    else:
       finalIndex = characters.index(letter) + r
    firstEncryptionResult = f"{firstEncryptionResult}{characters[finalIndex]}"
  """ Mettre la clé aléatoirement dans le message """
  ByteIndex = random.randint(0, len(firstEncryptionResult) - 1)
  longByte = f"<!{byte}?<)"
  arrResult = list(firstEncryptionResult)
  arrResult.insert(ByteIndex, longByte)
  firstEncryptionResult = "".join(arrResult)
  """ Mettre avant et après des caractères aléatoires """
  firstEncryptionResult = randomCharacters(random.randint(90, 150), firstEncryptionResult, nbChar)

  print("First Encryption result :", firstEncryptionResult)
  secondEncryptionResult = ""
  fullResult = ""
  for letter0 in firstEncryptionResult:
     """ Prendre l'équivalent de la lettre en chaine de 25 caractères (à complexifier pour avoir plusiquers chaines de caractères possibles) """
     secondEncryptionResult = f"{secondEncryptionResult}{simplifiedCryptedCharacters[characters.index(letter0)]}"
     for letter1 in simplifiedCryptedCharacters[characters.index(letter0)]:
        """ Prendre l'index de 'letter1' dans 'characters' pour le multiplier par 346 et le mettre en binaire """
        """ Séparation de chaque nombre en binaire par un chiffre aléatoire entre 2 et 9 avec 'randomIntWithout0and1(10)' """
        fullResult = f"{fullResult}{int(format(round(characters.index(letter1) * 346), 'b'))}{randomIntWithout0and1(10)}"
     fullResult = f"{fullResult}"
  print("Second Encryption result :", secondEncryptionResult)
  print("Fully Encrypted result :", fullResult)

  FullyCryptedMessageForDisplay = fullResult
  return fullResult


""" Renvoie le nombre de caractère dans la clé """
def numberOfInt(text: str, index: int):
   numbers = 0
   strNumber = ""
   for index0 in range(index, len(text)):
      if text[index0].isnumeric():
         numbers += 1
      else:
         break
   if numbers != 0 and text[index + numbers] == "?" and text[index + 1 + numbers] == "<" and text[index + 2 + numbers] == ")":
      for index1 in range(index, index + numbers):
        strNumber = f"{strNumber}{text[index1]}"
      return [int(strNumber), index - 2, index + 2 + numbers]
   else:
      return [0, 0, 0]
   
def randomIntWithout0and1(endInt: int):
   randomInt = random.randint(2, endInt - 1)
   return randomInt

char = ""
for i in range(25):
   char = f'{char}{characters[random.randint(0, len(characters) - 1)]}'
print(char)
   

""" Boucle """
while True: 
 Message = input(str("Enter : "))
 if Message == "break":
    break
 else:
    decryptedMessage = decode(encode(Message, len(characters)), len(characters))
    print("Decrypted result :", decryptedMessage)
    print(getsizeof(FullyCryptedMessageForDisplay))

