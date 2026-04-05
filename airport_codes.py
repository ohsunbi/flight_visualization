from __future__ import annotations

from typing import Optional


# Generated from OurAirports airports.csv
# Includes large_airport and medium_airport entries with both ICAO and IATA codes.
ICAO_TO_IATA = {
    "AGGH": "HIR",  # large_airport | Honiara International Airport
    "AGGM": "MUA",  # medium_airport | Munda Airport
    "ANYN": "INU",  # medium_airport | Nauru International Airport
    "AYBA": "VMU",  # medium_airport | Baimuru Airport
    "AYBK": "BUA",  # medium_airport | Buka Airport
    "AYBM": "OPU",  # medium_airport | Balimo Airport
    "AYCH": "CMU",  # medium_airport | Chimbu Airport
    "AYDU": "DAU",  # medium_airport | Daru Airport
    "AYGA": "GKA",  # medium_airport | Goroka Airport
    "AYGN": "GUR",  # medium_airport | Gurney Airport
    "AYGR": "PNP",  # medium_airport | Girua Airport
    "AYHK": "HKN",  # medium_airport | Hoskins Airport
    "AYKM": "KMA",  # medium_airport | Kerema Airport
    "AYKV": "KVG",  # medium_airport | Kavieng Airport
    "AYMD": "MAG",  # medium_airport | Madang Airport
    "AYMH": "HGU",  # medium_airport | Mount Hagen Kagamuga Airport
    "AYMN": "MDU",  # medium_airport | Mendi Airport
    "AYMO": "MAS",  # medium_airport | Momote Airport
    "AYNZ": "LAE",  # large_airport | Nadzab Tomodachi International Airport
    "AYPY": "POM",  # large_airport | Port Moresby Jacksons International Airport
    "AYTK": "RAB",  # medium_airport | Tokua Airport
    "AYVN": "VAI",  # medium_airport | Vanimo Airport
    "AYWD": "WBM",  # medium_airport | Wapenamanda Airport
    "AYWK": "WWK",  # medium_airport | Wewak International Airport
    "BGAA": "JEG",  # medium_airport | Aasiaat Airport
    "BGBW": "UAK",  # medium_airport | Narsarsuaq Airport
    "BGCO": "CNP",  # medium_airport | Neerlerit Inaat Airport
    "BGGH": "GOH",  # large_airport | Nuuk International Airport
    "BGJN": "JAV",  # medium_airport | Ilulissat Airport
    "BGKK": "KUS",  # medium_airport | Kulusuk Airport
    "BGQQ": "NAQ",  # medium_airport | Qaanaaq Airport
    "BGSF": "SFJ",  # large_airport | Kangerlussuaq International Airport
    "BGSS": "JHS",  # medium_airport | Sisimiut Airport
    "BGTL": "THU",  # large_airport | Pituffik Space Base
    "BIAR": "AEY",  # large_airport | Akureyri International Airport
    "BIBD": "BIU",  # medium_airport | Bildudalur Airport
    "BIEG": "EGS",  # medium_airport | Egilsstaðir Airport
    "BIGR": "GRY",  # medium_airport | Grímsey Airport
    "BIHN": "HFN",  # medium_airport | Hornafjörður Airport
    "BIHU": "HZK",  # medium_airport | Húsavík Airport
    "BIIS": "IFJ",  # medium_airport | Ísafjörður Airport
    "BIKF": "KEF",  # large_airport | Keflavik International Airport
    "BIRK": "RKV",  # medium_airport | Reykjavík Domestic Airport
    "BIRL": "MVA",  # medium_airport | Mývatn Airport
    "BISI": "SIJ",  # medium_airport | Siglufjörður Airport
    "BIVM": "VEY",  # medium_airport | Vestmannaeyjar Airport
    "BIVO": "VPN",  # medium_airport | Vopnafjörður Airport
    "BKPR": "PRN",  # large_airport | Priština Adem Jashari International Airport
    "CBBC": "ZEL",  # medium_airport | Bella Bella (Campbell Island) Airport
    "CYAG": "YAG",  # medium_airport | Fort Frances Municipal Airport
    "CYAH": "YAH",  # medium_airport | La Grande-4 Airport
    "CYAM": "YAM",  # medium_airport | Sault Ste Marie Airport
    "CYAQ": "XKS",  # medium_airport | Kasabonika Airport
    "CYAY": "YAY",  # medium_airport | St. Anthony Airport
    "CYAZ": "YAZ",  # medium_airport | Tofino / Long Beach Airport
    "CYBC": "YBC",  # medium_airport | Baie-Comeau Airport
    "CYBD": "QBC",  # medium_airport | Bella Coola Airport
    "CYBF": "YBY",  # medium_airport | Bonnyville Airport
    "CYBG": "YBG",  # medium_airport | Saguenay-Bagotville Airport
    "CYBK": "YBK",  # medium_airport | Baker Lake Airport
    "CYBL": "YBL",  # medium_airport | Campbell River Airport
    "CYBR": "YBR",  # medium_airport | Brandon Municipal Airport
    "CYBX": "YBX",  # medium_airport | Lourdes-de-Blanc-Sablon Airport
    "CYCB": "YCB",  # medium_airport | Cambridge Bay Airport
    "CYCC": "YCC",  # medium_airport | Cornwall Regional Airport
    "CYCD": "YCD",  # medium_airport | Nanaimo Airport
    "CYCE": "YCE",  # medium_airport | Centralia / James T. Field Memorial Aerodrome
    "CYCG": "YCG",  # medium_airport | Castlegar/West Kootenay Regional Airport
    "CYCH": "YCH",  # medium_airport | Miramichi Airport
    "CYCL": "YCL",  # medium_airport | Charlo Airport
    "CYCN": "YCN",  # medium_airport | Cochrane Airport
    "CYCQ": "YCQ",  # medium_airport | Chetwynd Airport
    "CYDA": "YDA",  # medium_airport | Dawson City Airport
    "CYDB": "YDB",  # medium_airport | Burwash Airport
    "CYDF": "YDF",  # medium_airport | Deer Lake Airport
    "CYDM": "XRR",  # medium_airport | Ross River Airport
    "CYDN": "YDN",  # medium_airport | Dauphin Barker Airport
    "CYDO": "YDO",  # medium_airport | Dolbeau-Saint-Felicien Airport
    "CYDQ": "YDQ",  # medium_airport | Dawson Creek Airport
    "CYEG": "YEG",  # large_airport | Edmonton International Airport
    "CYEL": "YEL",  # medium_airport | Elliot Lake Municipal Airport
    "CYEM": "YEM",  # medium_airport | Manitoulin East Municipal Airport
    "CYEN": "YEN",  # medium_airport | Estevan Airport
    "CYET": "YET",  # medium_airport | Edson Airport
    "CYEV": "YEV",  # medium_airport | Inuvik Mike Zubko Airport
    "CYEY": "YEY",  # medium_airport | Amos/Magny Airport
    "CYFB": "YFB",  # medium_airport | Iqaluit Airport
    "CYFC": "YFC",  # medium_airport | Fredericton International Airport
    "CYFE": "YFE",  # medium_airport | Forestville Airport
    "CYFJ": "YTM",  # medium_airport | Mont-Tremblant International Airport
    "CYFR": "YFR",  # medium_airport | Fort Resolution Airport
    "CYFS": "YFS",  # medium_airport | Fort Simpson Airport
    "CYGK": "YGK",  # medium_airport | Kingston Norman Rogers Airport
    "CYGL": "YGL",  # medium_airport | La Grande Rivière Airport
    "CYGM": "YGM",  # medium_airport | Gimli Industrial Park Airport
    "CYGP": "YGP",  # medium_airport | Michel-Pouliot Gaspé Airport
    "CYGQ": "YGQ",  # medium_airport | Geraldton Greenstone Regional Airport
    "CYGR": "YGR",  # medium_airport | Îles-de-la-Madeleine Airport
    "CYGV": "YGV",  # medium_airport | Havre-Saint-Pierre Airport
    "CYGW": "YGW",  # medium_airport | Kuujjuarapik Airport
    "CYHD": "YHD",  # medium_airport | Dryden Regional Airport
    "CYHF": "YHF",  # medium_airport | Hearst René Fontaine Municipal Airport
    "CYHM": "YHM",  # medium_airport | John C. Munro Hamilton International Airport
    "CYHN": "YHN",  # medium_airport | Hornepayne Municipal Airport
    "CYHT": "YHT",  # medium_airport | Haines Junction Airport
    "CYHU": "YHU",  # medium_airport | Montréal / Saint-Hubert Metropolitan Airport
    "CYHY": "YHY",  # medium_airport | Hay River / Merlyn Carter Airport
    "CYHZ": "YHZ",  # large_airport | Halifax / Stanfield International Airport
    "CYIB": "YIB",  # medium_airport | Atikokan Municipal Airport
    "CYID": "YDG",  # medium_airport | Digby / Annapolis Regional Airport
    "CYIF": "YIF",  # medium_airport | St Augustin Airport
    "CYIV": "YIV",  # medium_airport | Island Lake Airport
    "CYJF": "YJF",  # medium_airport | Fort Liard Airport
    "CYJN": "YJN",  # medium_airport | St Jean Airport
    "CYJT": "YJT",  # medium_airport | Stephenville Dymond International Airport
    "CYKA": "YKA",  # medium_airport | Kamloops John Moose Fulton Field Regional Airport
    "CYKF": "YKF",  # medium_airport | Region of Waterloo International Airport
    "CYKJ": "YKJ",  # medium_airport | Key Lake Airport
    "CYKL": "YKL",  # medium_airport | Schefferville Airport
    "CYKM": "YKD",  # medium_airport | Kincardine Municipal Airport
    "CYKX": "YKX",  # medium_airport | Kirkland Lake Airport
    "CYKY": "YKY",  # medium_airport | Kindersley Airport
    "CYLD": "YLD",  # medium_airport | Chapleau Airport
    "CYLJ": "YLJ",  # medium_airport | Meadow Lake Airport
    "CYLL": "YLL",  # medium_airport | Lloydminster Airport
    "CYLR": "YLR",  # medium_airport | Leaf Rapids Airport
    "CYLS": "YLK",  # medium_airport | Barrie-Lake Simcoe Regional Airport
    "CYLT": "YLT",  # medium_airport | Alert Airport
    "CYLW": "YLW",  # large_airport | Kelowna International Airport
    "CYMA": "YMA",  # medium_airport | Mayo Airport
    "CYME": "YME",  # medium_airport | Matane Airport
    "CYMG": "YMG",  # medium_airport | Manitouwadge Airport
    "CYMJ": "YMJ",  # medium_airport | Moose Jaw Air Vice Marshal C. M. McEwen Airport
    "CYML": "YML",  # medium_airport | Charlevoix Airport
    "CYMM": "YMM",  # medium_airport | Fort McMurray International Airport
    "CYMO": "YMO",  # medium_airport | Moosonee Airport
    "CYMT": "YMT",  # medium_airport | Chapais Airport
    "CYMX": "YMX",  # medium_airport | Montreal Mirabel International Airport
    "CYNA": "YNA",  # medium_airport | Natashquan Airport
    "CYND": "YND",  # medium_airport | Ottawa / Gatineau Airport
    "CYNJ": "YLY",  # medium_airport | Langley Airport
    "CYNL": "YNL",  # medium_airport | Points North Landing Airport
    "CYNM": "YNM",  # medium_airport | Matagami Airport
    "CYOA": "YOA",  # medium_airport | Ekati Airport
    "CYOD": "YOD",  # medium_airport | CFB Cold Lake
    "CYOJ": "YOJ",  # medium_airport | High Level Airport
    "CYOO": "YOO",  # medium_airport | Oshawa Executive Airport
    "CYOP": "YOP",  # medium_airport | Rainbow Lake Airport
    "CYOS": "YOS",  # medium_airport | Owen Sound / Billy Bishop Regional Airport
    "CYOW": "YOW",  # large_airport | Ottawa Macdonald-Cartier International Airport
    "CYPA": "YPA",  # medium_airport | Prince Albert Glass Field
    "CYPD": "YPS",  # medium_airport | Port Hawkesbury Airport
    "CYPE": "YPE",  # medium_airport | Peace River Airport
    "CYPG": "YPG",  # medium_airport | Portage-la-Prairie / Southport Airport
    "CYPL": "YPL",  # medium_airport | Pickle Lake Airport
    "CYPN": "YPN",  # medium_airport | Port-Menier Airport
    "CYPQ": "YPQ",  # medium_airport | Peterborough Regional Airport
    "CYPR": "YPR",  # medium_airport | Prince Rupert Airport
    "CYPW": "YPW",  # medium_airport | Powell River Airport
    "CYPX": "YPX",  # medium_airport | Puvirnituq Airport
    "CYPY": "YPY",  # medium_airport | Fort Chipewyan Airport
    "CYPZ": "YPZ",  # medium_airport | Burns Lake Airport
    "CYQA": "YQA",  # medium_airport | Muskoka Airport
    "CYQB": "YQB",  # large_airport | Quebec Jean Lesage International Airport
    "CYQD": "YQD",  # medium_airport | The Pas Airport
    "CYQF": "YQF",  # medium_airport | Red Deer Regional Airport
    "CYQG": "YQG",  # medium_airport | Windsor International Airport
    "CYQH": "YQH",  # medium_airport | Watson Lake Airport
    "CYQI": "YQI",  # medium_airport | Yarmouth Airport
    "CYQK": "YQK",  # medium_airport | Kenora Airport
    "CYQL": "YQL",  # medium_airport | Lethbridge County Airport
    "CYQM": "YQM",  # medium_airport | Greater Moncton Roméo LeBlanc International Airport
    "CYQN": "YQN",  # medium_airport | Nakina Airport
    "CYQQ": "YQQ",  # medium_airport | Comox Valley International Airport / CFB Comox
    "CYQR": "YQR",  # medium_airport | Regina International Airport
    "CYQS": "YQS",  # medium_airport | St Thomas Municipal Airport
    "CYQT": "YQT",  # medium_airport | Thunder Bay International Airport
    "CYQU": "YQU",  # medium_airport | Grande Prairie Airport
    "CYQV": "YQV",  # medium_airport | Yorkton Municipal Airport
    "CYQW": "YQW",  # medium_airport | North Battleford Airport
    "CYQX": "YQX",  # medium_airport | Gander International Airport
    "CYQY": "YQY",  # medium_airport | Sydney / J.A. Douglas McCurdy Airport
    "CYQZ": "YQZ",  # medium_airport | Quesnel Airport
    "CYRB": "YRB",  # medium_airport | Resolute Bay Airport
    "CYRI": "YRI",  # medium_airport | Rivière-du-Loup Airport
    "CYRJ": "YRJ",  # medium_airport | Roberval Airport
    "CYRL": "YRL",  # medium_airport | Red Lake Airport
    "CYRO": "YRO",  # medium_airport | Ottawa / Rockcliffe Airport
    "CYRQ": "YRQ",  # medium_airport | Trois-Rivières Airport
    "CYRT": "YRT",  # medium_airport | Rankin Inlet Airport
    "CYRV": "YRV",  # medium_airport | Revelstoke Airport
    "CYSB": "YSB",  # medium_airport | Sudbury Airport
    "CYSC": "YSC",  # medium_airport | Sherbrooke Airport
    "CYSF": "YSF",  # medium_airport | Stony Rapids Airport
    "CYSH": "YSH",  # medium_airport | Smiths Falls-Montague (Russ Beach) Airport
    "CYSJ": "YSJ",  # medium_airport | Saint John Airport
    "CYSL": "YSL",  # medium_airport | Saint-Léonard Airport
    "CYSM": "YSM",  # medium_airport | Fort Smith Airport
    "CYSN": "YCM",  # medium_airport | Niagara District Airport
    "CYSP": "YSP",  # medium_airport | Marathon Airport
    "CYSU": "YSU",  # medium_airport | Summerside Airport
    "CYTA": "YTA",  # medium_airport | Pembroke Airport
    "CYTF": "YTF",  # medium_airport | Alma Airport
    "CYTH": "YTH",  # medium_airport | Thompson Airport
    "CYTR": "YTR",  # medium_airport | CFB Trenton
    "CYTS": "YTS",  # medium_airport | Timmins/Victor M. Power
    "CYTZ": "YTZ",  # medium_airport | Billy Bishop Toronto City Airport
    "CYUL": "YUL",  # large_airport | Montreal / Pierre Elliott Trudeau International Airport
    "CYUX": "YUX",  # medium_airport | Hall Beach Airport
    "CYUY": "YUY",  # medium_airport | Rouyn Noranda Airport
    "CYVB": "YVB",  # medium_airport | Bonaventure Airport
    "CYVC": "YVC",  # medium_airport | La Ronge Airport
    "CYVK": "YVE",  # medium_airport | Vernon Regional Airport
    "CYVO": "YVO",  # medium_airport | Val-d'Or Airport
    "CYVP": "YVP",  # medium_airport | Kuujjuaq Airport
    "CYVQ": "YVQ",  # medium_airport | Norman Wells Airport
    "CYVR": "YVR",  # large_airport | Vancouver International Airport
    "CYVV": "YVV",  # medium_airport | Wiarton Airport
    "CYWG": "YWG",  # large_airport | Winnipeg / James Armstrong Richardson International Airport
    "CYWK": "YWK",  # medium_airport | Wabush Airport
    "CYWL": "YWL",  # medium_airport | Williams Lake Airport
    "CYWY": "YWY",  # medium_airport | Wrigley Airport
    "CYXC": "YXC",  # medium_airport | Cranbrook/Canadian Rockies International Airport
    "CYXE": "YXE",  # large_airport | Saskatoon John G. Diefenbaker International Airport
    "CYXH": "YXH",  # medium_airport | Medicine Hat Regional Airport
    "CYXJ": "YXJ",  # medium_airport | Fort St John / North Peace Regional Airport
    "CYXK": "YXK",  # medium_airport | Rimouski Airport
    "CYXL": "YXL",  # medium_airport | Sioux Lookout Airport
    "CYXQ": "YXQ",  # medium_airport | Beaver Creek Airport
    "CYXR": "YXR",  # medium_airport | Earlton (Timiskaming Regional) Airport
    "CYXS": "YXS",  # medium_airport | Prince George (International) Airport
    "CYXT": "YXT",  # medium_airport | Northwest Regional Airport Terrace-Kitimat
    "CYXU": "YXU",  # medium_airport | London International Airport
    "CYXX": "YXX",  # medium_airport | Abbotsford International Airport
    "CYXY": "YXY",  # medium_airport | Whitehorse / Erik Nielsen International Airport
    "CYXZ": "YXZ",  # medium_airport | Wawa Airport
    "CYYB": "YYB",  # medium_airport | North Bay Jack Garland Airport
    "CYYC": "YYC",  # large_airport | Calgary International Airport
    "CYYD": "YYD",  # medium_airport | Smithers Airport
    "CYYE": "YYE",  # medium_airport | Fort Nelson Airport
    "CYYF": "YYF",  # medium_airport | Penticton Airport
    "CYYG": "YYG",  # medium_airport | Charlottetown Airport
    "CYYJ": "YYJ",  # large_airport | Victoria International Airport
    "CYYL": "YYL",  # medium_airport | Lynn Lake Airport
    "CYYN": "YYN",  # medium_airport | Swift Current Airport
    "CYYQ": "YYQ",  # medium_airport | Churchill Airport
    "CYYR": "YYR",  # medium_airport | Goose Bay Airport
    "CYYT": "YYT",  # large_airport | St. John's International Airport
    "CYYU": "YYU",  # medium_airport | Kapuskasing Airport
    "CYYW": "YYW",  # medium_airport | Armstrong Airport
    "CYYY": "YYY",  # medium_airport | Mont Joli Airport
    "CYYZ": "YYZ",  # large_airport | Toronto Pearson International Airport
    "CYZE": "YZE",  # medium_airport | Gore Bay Manitoulin Airport
    "CYZF": "YZF",  # medium_airport | Yellowknife International Airport
    "CYZH": "YZH",  # medium_airport | Slave Lake Airport
    "CYZP": "YZP",  # medium_airport | Sandspit Airport
    "CYZR": "YZR",  # medium_airport | Chris Hadfield Airport
    "CYZS": "YZS",  # medium_airport | Coral Harbour Airport
    "CYZT": "YZT",  # medium_airport | Port Hardy Airport
    "CYZU": "YZU",  # medium_airport | Whitecourt Airport
    "CYZV": "YZV",  # medium_airport | Sept-Îles Airport
    "CYZW": "YZW",  # medium_airport | Teslin Airport
    "CYZX": "YZX",  # medium_airport | CFB Greenwood
    "CZAM": "YSN",  # medium_airport | Shuswap Regional Airport
    "CZBB": "YDT",  # medium_airport | Boundary Bay Airport
    "CZBF": "ZBF",  # medium_airport | Bathurst Airport
    "CZBM": "ZBM",  # medium_airport | Bromont (Roland Désourdy) Airport
    "CZEE": "KES",  # medium_airport | Kelsey Airport
    "CZFA": "ZFA",  # medium_airport | Faro Airport
    "CZGF": "ZGF",  # medium_airport | Grand Forks Airport
    "CZJG": "ZJG",  # medium_airport | Jenpeg Airport
    "CZJN": "ZJN",  # medium_airport | Swan River Airport
    "CZLQ": "YTD",  # medium_airport | Thicket Portage Airport
    "CZMN": "PIW",  # medium_airport | Pikwitonei Airport
    "CZMT": "ZMT",  # medium_airport | Masset Airport
    "CZPC": "WPC",  # medium_airport | Pincher Creek Airport
    "CZSJ": "ZSJ",  # medium_airport | Sandy Lake Airport
    "CZST": "ZST",  # medium_airport | Stewart Airport
    "CZUC": "ZUC",  # medium_airport | Ignace Municipal Airport
    "DAAD": "BUJ",  # medium_airport | Bou Saada Airport
    "DAAE": "BJA",  # large_airport | Soummam–Abane Ramdane Airport
    "DAAG": "ALG",  # large_airport | Houari Boumediene Airport
    "DAAJ": "DJG",  # large_airport | Tiska Djanet Airport
    "DAAP": "VVZ",  # medium_airport | Illizi Takhamalt Airport
    "DAAS": "QSF",  # medium_airport | Ain Arnat Airport
    "DAAT": "TMR",  # large_airport | Aguenar – Hadj Bey Akhamok Airport
    "DAAV": "GJL",  # large_airport | Jijel Ferhat Abbas Airport
    "DAAY": "MZW",  # medium_airport | Mecheria Airport
    "DABB": "AAE",  # large_airport | Annaba Rabah Bitat Airport
    "DABC": "CZL",  # large_airport | Mohamed Boudiaf International Airport
    "DABS": "TEE",  # medium_airport | Cheikh Larbi Tébessi Airport
    "DABT": "BLJ",  # large_airport | Batna Mostefa Ben Boulaid Airport
    "DAFH": "HRM",  # medium_airport | Hassi R'Mel Airport
    "DAOB": "TID",  # medium_airport | Abdelhafid Boussouf Bou Chekif Airport
    "DAOF": "TIN",  # medium_airport | Tindouf Airport
    "DAOI": "CFK",  # large_airport | Chlef Aboubakr Belkaid International Airport
    "DAOL": "TAF",  # medium_airport | Oran Tafraoui Airport
    "DAON": "TLM",  # large_airport | Zenata – Messali El Hadj Airport
    "DAOO": "ORN",  # large_airport | Oran Es-Sénia (Ahmed Ben Bella) International Airport
    "DAOR": "CBH",  # medium_airport | Béchar Boudghene Ben Ali Lotfi Airport
    "DAOV": "MUW",  # medium_airport | Ghriss Airport
    "DAUA": "AZR",  # medium_airport | Touat-Cheikh Sidi Mohamed Belkebir Airport
    "DAUB": "BSK",  # large_airport | Biskra - Mohamed Khider Airport
    "DAUE": "ELG",  # medium_airport | El Golea Airport
    "DAUG": "GHA",  # medium_airport | Noumérat - Moufdi Zakaria Airport
    "DAUH": "HME",  # medium_airport | Hassi Messaoud-Oued Irara Krim Belkacem Airport
    "DAUI": "INZ",  # medium_airport | In Salah Airport
    "DAUK": "TGR",  # medium_airport | Touggourt Sidi Madhi Airport
    "DAUL": "LOO",  # medium_airport | Laghouat - Molay Ahmed Medeghri Airport
    "DAUO": "ELU",  # medium_airport | Guemar Airport - مطار قمار بالوادي
    "DAUT": "TMX",  # medium_airport | Timimoun Airport
    "DAUU": "OGX",  # medium_airport | Ain Beida Airport
    "DAUZ": "IAM",  # medium_airport | Zarzaitine - In Aménas Airport
    "DBBB": "COO",  # large_airport | Cotonou Cadjehoun International Airport
    "DFFD": "OUA",  # large_airport | Ouagadougou Thomas Sankara International Airport
    "DFOO": "BOY",  # large_airport | Bobo Dioulasso Airport
    "DGAA": "ACC",  # large_airport | Kotoka International Airport
    "DGLE": "TML",  # large_airport | Yakubu Tali International Airport
    "DGSI": "KMS",  # large_airport | Prempeh I International Airport
    "DGSN": "NYI",  # medium_airport | Sunyani Airport
    "DGTK": "TKD",  # medium_airport | Takoradi Airport
    "DIAP": "ABJ",  # large_airport | Félix-Houphouët-Boigny International Airport
    "DIBK": "BYK",  # medium_airport | Bouaké Airport
    "DIDL": "DJO",  # medium_airport | Daloa Airport
    "DIKO": "HGO",  # medium_airport | Korhogo Airport
    "DIMN": "MJC",  # medium_airport | Man Airport
    "DISP": "SPY",  # medium_airport | San Pedro Airport
    "DIYO": "ASK",  # large_airport | Yamoussoukro International Airport
    "DNAA": "ABV",  # large_airport | Nnamdi Azikiwe International Airport
    "DNAI": "QUO",  # medium_airport | Akwa Ibom International Airport
    "DNAK": "AKR",  # medium_airport | Akure Airport
    "DNAS": "ABB",  # large_airport | Asaba International Airport
    "DNBC": "BCU",  # large_airport | Sir Abubakar Tafawa Balewa Bauchi State International Airport
    "DNBE": "BNI",  # medium_airport | Benin Airport
    "DNCA": "CBQ",  # medium_airport | Margaret Ekpo International Airport
    "DNEN": "ENU",  # large_airport | Akanu Ibiam International Airport
    "DNGO": "GMO",  # medium_airport | Gombe Lawanti International Airport
    "DNIB": "IBA",  # medium_airport | Ibadan Airport
    "DNIL": "ILR",  # large_airport | General Tunde Idiagbon International Airport
    "DNIM": "QOW",  # medium_airport | Sam Mbakwe International Cargo Airport
    "DNJO": "JOS",  # medium_airport | Yakubu Gowon Airport
    "DNKA": "KAD",  # large_airport | Kaduna International Airport
    "DNKN": "KAN",  # large_airport | Mallam Aminu Kano International Airport
    "DNMA": "MIU",  # large_airport | Maiduguri International Airport
    "DNMK": "MDI",  # medium_airport | Makurdi Airport
    "DNMM": "LOS",  # large_airport | Murtala Muhammed International Airport
    "DNMN": "MXJ",  # medium_airport | Minna Airport
    "DNPO": "PHC",  # large_airport | Port Harcourt International Airport
    "DNSO": "SKO",  # large_airport | Sadiq Abubakar III International Airport
    "DNSU": "QRW",  # medium_airport | Warri Airport
    "DNYO": "YOL",  # medium_airport | Yola Airport
    "DNZA": "ZAR",  # medium_airport | Zaria Airport
    "DRRM": "MFQ",  # medium_airport | Maradi Airport
    "DRRN": "NIM",  # large_airport | Diori Hamani International Airport
    "DRRT": "THZ",  # medium_airport | Tahoua Airport
    "DRZA": "AJY",  # medium_airport | Mano Dayak International Airport
    "DRZR": "ZND",  # medium_airport | Zinder Airport
    "DTKA": "TBJ",  # medium_airport | Tabarka-Aïn Draham International Airport
    "DTMB": "MIR",  # medium_airport | Monastir Habib Bourguiba International Airport
    "DTNH": "NBE",  # medium_airport | Enfidha - Hammamet International Airport
    "DTTA": "TUN",  # large_airport | Tunis Carthage International Airport
    "DTTF": "GAF",  # medium_airport | Gafsa Ksar International Airport
    "DTTG": "GAE",  # medium_airport | Gabès Matmata International Airport
    "DTTJ": "DJE",  # large_airport | Djerba Zarzis International Airport
    "DTTR": "EBM",  # medium_airport | El Borma Airport
    "DTTX": "SFA",  # large_airport | Sfax Thyna International Airport
    "DTTZ": "TOE",  # medium_airport | Tozeur Nefta International Airport
    "DXNG": "LRL",  # large_airport | Niamtougou International Airport
    "DXXX": "LFW",  # large_airport | Lomé–Tokoin International Airport
    "EBAW": "ANR",  # medium_airport | Antwerp International Airport (Deurne)
    "EBBR": "BRU",  # large_airport | Brussels Airport
    "EBCI": "CRL",  # large_airport | Brussels South Charleroi Airport
    "EBKT": "KJK",  # medium_airport | Flanders International Airport Kortrijk-Wevelgem
    "EBLG": "LGG",  # medium_airport | Liège Airport
    "EBOS": "OST",  # large_airport | Ostend-Bruges International Airport
    "EDAC": "AOC",  # medium_airport | Leipzig–Altenburg Airport
    "EDAH": "HDF",  # medium_airport | Heringsdorf Airport
    "EDBN": "FNB",  # medium_airport | Neubrandenburg Trollenhagen Airport
    "EDDB": "BER",  # large_airport | Berlin Brandenburg Airport
    "EDDC": "DRS",  # large_airport | Dresden Airport
    "EDDE": "ERF",  # large_airport | Erfurt-Weimar Airport
    "EDDF": "FRA",  # large_airport | Frankfurt Main Airport
    "EDDG": "FMO",  # large_airport | Münster Osnabrück Airport
    "EDDH": "HAM",  # large_airport | Hamburg Helmut Schmidt Airport
    "EDDK": "CGN",  # large_airport | Cologne Bonn Airport
    "EDDL": "DUS",  # large_airport | Düsseldorf Airport
    "EDDM": "MUC",  # large_airport | Munich Airport
    "EDDN": "NUE",  # large_airport | Nuremberg Airport
    "EDDP": "LEJ",  # large_airport | Leipzig/Halle Airport
    "EDDR": "SCN",  # medium_airport | Saarbrücken Airport
    "EDDS": "STR",  # large_airport | Stuttgart Airport
    "EDDV": "HAJ",  # large_airport | Hannover Airport
    "EDDW": "BRE",  # large_airport | Bremen Airport
    "EDFH": "HHN",  # large_airport | Frankfurt-Hahn Airport
    "EDFM": "MHG",  # medium_airport | Mannheim-City Airport
    "EDGE": "EIB",  # medium_airport | Eisenach-Kindel Airport
    "EDGS": "SGE",  # medium_airport | Siegerland Airport
    "EDHI": "XFW",  # medium_airport | Hamburg-Finkenwerder Airport
    "EDHK": "KEL",  # medium_airport | Kiel-Holtenau Airport
    "EDHL": "LBC",  # medium_airport | Lübeck Blankensee Airport
    "EDJA": "FMM",  # large_airport | Memmingen Allgau Airport
    "EDLI": "BFE",  # medium_airport | Bielefeld Airport
    "EDLN": "MGL",  # medium_airport | Mönchengladbach Airport
    "EDLP": "PAD",  # large_airport | Paderborn Lippstadt Airport
    "EDLV": "NRN",  # large_airport | Weeze (Niederrhein) Airport
    "EDLW": "DTM",  # large_airport | Dortmund Airport
    "EDMA": "AGB",  # medium_airport | Augsburg Airport
    "EDML": "QLG",  # medium_airport | Landshut Airfield
    "EDMO": "OBF",  # medium_airport | Oberpfaffenhofen Airport
    "EDNY": "FDH",  # large_airport | Bodensee Airport Friedrichshafen
    "EDQD": "BYU",  # medium_airport | Bayreuth Airport
    "EDQM": "HOQ",  # medium_airport | Hof-Plauen Airport
    "EDSB": "FKB",  # large_airport | Karlsruhe Baden-Baden Airport
    "EDTL": "LHA",  # medium_airport | Lahr Airport
    "EDVE": "BWE",  # medium_airport | Braunschweig-Wolfsburg Airport
    "EDVK": "KSF",  # large_airport | Kassel Airport
    "EDXW": "GWT",  # medium_airport | Westerland Sylt Airport
    "EEKA": "KDL",  # medium_airport | Kärdla Airport
    "EEKE": "URE",  # medium_airport | Kuressaare Airport
    "EEPU": "EPU",  # medium_airport | Pärnu Airport
    "EETN": "TLL",  # large_airport | Lennart Meri Tallinn Airport
    "EETU": "TAY",  # medium_airport | Tartu Airport
    "EFET": "ENF",  # medium_airport | Enontekio Airport
    "EFHA": "KEV",  # medium_airport | Halli Airport
    "EFHK": "HEL",  # large_airport | Helsinki Vantaa Airport
    "EFIT": "KTQ",  # medium_airport | Kitee Airport
    "EFIV": "IVL",  # large_airport | Ivalo Airport
    "EFJO": "JOE",  # medium_airport | Joensuu Airport
    "EFJY": "JYV",  # medium_airport | Jyväskylä Airport
    "EFKA": "KAU",  # medium_airport | Kauhava Airfield
    "EFKE": "KEM",  # medium_airport | Kemi-Tornio Airport
    "EFKI": "KAJ",  # medium_airport | Kajaani Airport
    "EFKJ": "KHJ",  # medium_airport | Kauhajoki Airfield
    "EFKK": "KOK",  # medium_airport | Kokkola-Pietarsaari Airport
    "EFKS": "KAO",  # medium_airport | Kuusamo Airport
    "EFKT": "KTT",  # large_airport | Kittilä International Airport
    "EFKU": "KUO",  # large_airport | Kuopio Airport
    "EFLP": "LPP",  # large_airport | Lappeenranta Airport
    "EFMA": "MHQ",  # large_airport | Mariehamn Airport
    "EFMI": "MIK",  # medium_airport | Mikkeli Airport
    "EFOU": "OUL",  # large_airport | Oulu Airport
    "EFPO": "POR",  # medium_airport | Pori Airport
    "EFRO": "RVN",  # large_airport | Rovaniemi Airport
    "EFSA": "SVL",  # medium_airport | Savonlinna Airport
    "EFSI": "SJY",  # medium_airport | Seinäjoki Airport
    "EFSO": "SOT",  # medium_airport | Sodankyla Airport
    "EFTP": "TMP",  # large_airport | Tampere-Pirkkala Airport
    "EFTU": "TKU",  # large_airport | Turku Airport
    "EFUT": "UTI",  # medium_airport | Utti Air Base
    "EFVA": "VAA",  # large_airport | Vaasa Airport
    "EFVR": "VRK",  # medium_airport | Varkaus Airport
    "EFYL": "YLI",  # medium_airport | Ylivieska Airfield
    "EGAA": "BFS",  # large_airport | Belfast International Airport
    "EGAB": "ENK",  # medium_airport | Enniskillen/St Angelo Airport
    "EGAC": "BHD",  # medium_airport | George Best Belfast City Airport
    "EGAE": "LDY",  # medium_airport | City of Derry Airport
    "EGBB": "BHX",  # large_airport | Birmingham Airport
    "EGBE": "CVT",  # medium_airport | Coventry Airport
    "EGBJ": "GLO",  # medium_airport | Gloucestershire Airport
    "EGBN": "NQT",  # medium_airport | Nottingham City Airport
    "EGCC": "MAN",  # large_airport | Manchester Airport
    "EGDY": "YEO",  # medium_airport | RNAS Yeovilton
    "EGEC": "CAL",  # medium_airport | Campbeltown Airport
    "EGED": "EOI",  # medium_airport | Eday Airport
    "EGFE": "HAW",  # medium_airport | Haverfordwest Airport
    "EGFF": "CWL",  # large_airport | Cardiff International Airport
    "EGFH": "SWS",  # medium_airport | Swansea Airport
    "EGGD": "BRS",  # large_airport | Bristol Airport
    "EGGP": "LPL",  # large_airport | Liverpool John Lennon Airport
    "EGGW": "LTN",  # large_airport | London Luton Airport
    "EGHH": "BOH",  # medium_airport | Bournemouth Airport
    "EGHI": "SOU",  # medium_airport | Southampton Airport
    "EGHQ": "NQY",  # medium_airport | Cornwall Airport Newquay
    "EGJA": "ACI",  # medium_airport | Alderney Airport
    "EGJB": "GCI",  # medium_airport | Guernsey Airport
    "EGJJ": "JER",  # medium_airport | Jersey Airport
    "EGKA": "ESH",  # medium_airport | Brighton City Airport
    "EGKB": "BQH",  # medium_airport | London Biggin Hill Airport
    "EGKK": "LGW",  # large_airport | London Gatwick Airport
    "EGLC": "LCY",  # medium_airport | London City Airport
    "EGLF": "FAB",  # medium_airport | Farnborough Airport
    "EGLK": "BBS",  # medium_airport | Blackbushe Airport
    "EGLL": "LHR",  # large_airport | London Heathrow Airport
    "EGMC": "SEN",  # medium_airport | London Southend Airport
    "EGMD": "LYX",  # medium_airport | Lydd London Ashford Airport
    "EGNC": "CAX",  # medium_airport | Carlisle Lake District Airport
    "EGNH": "BLK",  # medium_airport | Blackpool Airport
    "EGNJ": "HUY",  # medium_airport | Humberside Airport
    "EGNL": "BWF",  # medium_airport | Barrow Walney Island Airport
    "EGNM": "LBA",  # large_airport | Leeds Bradford Airport
    "EGNO": "WRT",  # medium_airport | Warton Aerodrome
    "EGNR": "CEG",  # medium_airport | Hawarden Airport
    "EGNS": "IOM",  # large_airport | Isle of Man Airport
    "EGNT": "NCL",  # large_airport | Newcastle International Airport
    "EGNV": "MME",  # medium_airport | Teesside International Airport
    "EGNX": "EMA",  # large_airport | East Midlands Airport
    "EGOV": "VLY",  # medium_airport | Anglesey Airport
    "EGPA": "KOI",  # medium_airport | Kirkwall Airport
    "EGPB": "LSI",  # medium_airport | Sumburgh Airport
    "EGPC": "WIC",  # medium_airport | Wick John O'Groats Airport
    "EGPD": "ABZ",  # large_airport | Aberdeen International Airport
    "EGPE": "INV",  # medium_airport | Inverness Airport
    "EGPF": "GLA",  # large_airport | Glasgow Airport
    "EGPH": "EDI",  # large_airport | Edinburgh Airport
    "EGPI": "ILY",  # medium_airport | Islay Airport
    "EGPK": "PIK",  # large_airport | Glasgow Prestwick Airport
    "EGPL": "BEB",  # medium_airport | Benbecula Airport
    "EGPN": "DND",  # medium_airport | Dundee Airport
    "EGPO": "SYY",  # medium_airport | Stornoway Airport
    "EGPR": "BRR",  # medium_airport | Barra Airport
    "EGPU": "TRE",  # medium_airport | Tiree Airport
    "EGQL": "ADX",  # medium_airport | Leuchars Station Airfield
    "EGQS": "LMO",  # medium_airport | RAF Lossiemouth
    "EGSC": "CBG",  # medium_airport | Cambridge City Airport
    "EGSH": "NWI",  # medium_airport | Norwich Airport
    "EGSS": "STN",  # large_airport | London Stansted Airport
    "EGTE": "EXT",  # medium_airport | Exeter International Airport
    "EGTK": "OXF",  # medium_airport | London Oxford Airport
    "EGUB": "BEX",  # medium_airport | RAF Benson
    "EGUL": "LKZ",  # medium_airport | RAF Lakenheath
    "EGUN": "MHZ",  # medium_airport | RAF Mildenhall
    "EGVA": "FFD",  # medium_airport | RAF Fairford
    "EGVN": "BZZ",  # medium_airport | RAF Brize Norton
    "EGVO": "ODH",  # medium_airport | RAF Odiham
    "EGWU": "NHT",  # medium_airport | RAF Northolt
    "EGXC": "QCY",  # medium_airport | RAF Coningsby
    "EGXH": "BEQ",  # medium_airport | RAF Honington
    "EGXW": "WTN",  # medium_airport | RAF Waddington
    "EGYM": "KNF",  # medium_airport | RAF Marham
    "EGYP": "MPN",  # large_airport | Mount Pleasant Airport / RAF Mount Pleasant
    "EHAM": "AMS",  # large_airport | Amsterdam Airport Schiphol
    "EHBK": "MST",  # large_airport | Maastricht Aachen Airport
    "EHEH": "EIN",  # large_airport | Eindhoven Airport
    "EHGG": "GRQ",  # large_airport | Groningen Airport Eelde
    "EHGR": "GLZ",  # medium_airport | Gilze Rijen Air Base
    "EHKD": "DHR",  # medium_airport | De Kooy Airfield / Den Helder Naval Air Station
    "EHLE": "LEY",  # medium_airport | Lelystad Airport
    "EHLW": "LWR",  # medium_airport | Leeuwarden Air Base
    "EHRD": "RTM",  # large_airport | Rotterdam The Hague Airport
    "EHTW": "ENS",  # medium_airport | Twente Airport
    "EHVK": "UDE",  # medium_airport | Volkel Air Base
    "EHWO": "WOE",  # medium_airport | Woensdrecht Air Base
    "EICK": "ORK",  # large_airport | Cork International Airport
    "EIDL": "CFN",  # medium_airport | Donegal Airport
    "EIDW": "DUB",  # large_airport | Dublin Airport
    "EIKN": "NOC",  # large_airport | Ireland West Airport Knock
    "EIKY": "KIR",  # medium_airport | Kerry Airport
    "EINN": "SNN",  # large_airport | Shannon Airport
    "EISG": "SXL",  # medium_airport | Sligo Airport
    "EIWF": "WAT",  # medium_airport | Waterford Airport
    "EKAH": "AAR",  # large_airport | Aarhus Airport
    "EKBI": "BLL",  # large_airport | Billund Airport
    "EKCH": "CPH",  # large_airport | Copenhagen Kastrup Airport
    "EKEB": "EBJ",  # medium_airport | Esbjerg Airport
    "EKKA": "KRP",  # medium_airport | Midtjyllands Airport / Air Base Karup
    "EKMB": "MRW",  # medium_airport | Lolland Falster Maribo Airport
    "EKOD": "ODE",  # large_airport | Odense Hans Christian Andersen Airport
    "EKRK": "RKE",  # medium_airport | Copenhagen Roskilde Airport
    "EKRN": "RNN",  # medium_airport | Bornholm Airport
    "EKSB": "SGD",  # medium_airport | Sønderborg Airport
    "EKSN": "CNL",  # medium_airport | Sindal Airport
    "EKSP": "SKS",  # medium_airport | Skrydstrup Air Base
    "EKSV": "SQW",  # medium_airport | Skive Airport
    "EKTS": "TED",  # medium_airport | Thisted Airport
    "EKVG": "FAE",  # large_airport | Vágar Airport
    "EKVJ": "STA",  # medium_airport | Stauning Vestjylland  Airport
    "EKYT": "AAL",  # large_airport | Aalborg Airport
    "ELLX": "LUX",  # large_airport | Luxembourg-Findel International Airport
    "ENAL": "AES",  # large_airport | Ålesund Airport
    "ENAN": "ANX",  # medium_airport | Andøya Airport, Andenes
    "ENAT": "ALF",  # medium_airport | Alta Airport
    "ENBN": "BNN",  # medium_airport | Brønnøysund Airport, Brønnøy
    "ENBO": "BOO",  # large_airport | Bodø Airport
    "ENBR": "BGO",  # large_airport | Bergen Airport, Flesland
    "ENBS": "BJF",  # medium_airport | Båtsfjord Airport
    "ENBV": "BVG",  # medium_airport | Berlevåg Airport
    "ENCN": "KRS",  # large_airport | Kristiansand Airport
    "ENDU": "BDU",  # medium_airport | Bardufoss Airport
    "ENEV": "EVE",  # large_airport | Harstad/Narvik Airport
    "ENFL": "FRO",  # medium_airport | Florø Airport
    "ENGM": "OSL",  # large_airport | Oslo-Gardermoen International Airport
    "ENHD": "HAU",  # medium_airport | Haugesund Airport, Karmøy
    "ENHF": "HFT",  # medium_airport | Hammerfest Airport
    "ENHV": "HVG",  # medium_airport | Honningsvåg Airport, Valan
    "ENKB": "KSU",  # medium_airport | Kristiansund Airport, Kvernberget
    "ENKR": "KKN",  # medium_airport | Kirkenes Airport, Høybuktmoen
    "ENLK": "LKN",  # medium_airport | Leknes Airport
    "ENMH": "MEH",  # medium_airport | Mehamn Airport
    "ENML": "MOL",  # medium_airport | Molde Airport, Årø
    "ENMS": "MJF",  # medium_airport | Mosjøen Airport, Kjærstad
    "ENNA": "LKL",  # medium_airport | Lakselv Airport, Banak
    "ENNO": "NTB",  # medium_airport | Notodden Airport
    "ENOL": "OLA",  # medium_airport | Ørland Airport
    "ENOV": "HOV",  # medium_airport | Ørsta-Volda Airport, Hovden
    "ENRA": "MQN",  # medium_airport | Mo i Rana Airport, Røssvoll
    "ENRM": "RVK",  # medium_airport | Rørvik Airport, Ryum
    "ENRO": "RRS",  # medium_airport | Røros Airport
    "ENSB": "LYR",  # medium_airport | Svalbard Airport, Longyear
    "ENSH": "SVJ",  # medium_airport | Svolvær Airport, Helle
    "ENSK": "SKN",  # medium_airport | Stokmarknes Airport, Skagen
    "ENSO": "SRP",  # medium_airport | Stord Airport, Sørstokken
    "ENSR": "SOJ",  # medium_airport | Sørkjosen Airport
    "ENSS": "VAW",  # medium_airport | Vardø Airport, Svartnes
    "ENST": "SSJ",  # medium_airport | Sandnessjøen Airport, Stokka
    "ENTC": "TOS",  # large_airport | Tromsø Airport
    "ENTO": "TRF",  # large_airport | Sandefjord Airport, Torp
    "ENVA": "TRD",  # large_airport | Trondheim Airport, Værnes
    "ENVD": "VDS",  # medium_airport | Vadsø Airport
    "ENZV": "SVG",  # large_airport | Stavanger Airport, Sola
    "EPBY": "BZG",  # medium_airport | Ignacy Jan Paderewski Bydgoszcz Airport
    "EPGD": "GDN",  # large_airport | Gdańsk Lech Wałęsa Airport
    "EPKK": "KRK",  # large_airport | Kraków John Paul II International Airport
    "EPKT": "KTW",  # large_airport | Katowice Wojciech Korfanty International Airport
    "EPLB": "LUZ",  # large_airport | Lublin Airport
    "EPLL": "LCJ",  # large_airport | Łódź Władysław Reymont Airport
    "EPMO": "WMI",  # large_airport | Warsaw Modlin Airport
    "EPPO": "POZ",  # large_airport | Poznań-Ławica Airport
    "EPRA": "RDO",  # medium_airport | Warsaw Radom Airport
    "EPRZ": "RZE",  # large_airport | Rzeszów-Jasionka Airport
    "EPSC": "SZZ",  # large_airport | Solidarity Szczecin–Goleniów Airport
    "EPSY": "SZY",  # medium_airport | Olsztyn-Mazury Airport
    "EPWA": "WAW",  # large_airport | Warsaw Chopin Airport
    "EPWR": "WRO",  # large_airport | Copernicus Wrocław Airport
    "EPZG": "IEG",  # medium_airport | Zielona Góra-Babimost Airport
    "ESDF": "RNB",  # medium_airport | Ronneby Airport
    "ESGG": "GOT",  # large_airport | Göteborg Landvetter Airport
    "ESGJ": "JKG",  # medium_airport | Jönköping Airport
    "ESGP": "GSE",  # medium_airport | Säve Airport
    "ESGR": "KVB",  # medium_airport | Skövde Airport
    "ESGT": "THN",  # medium_airport | Trollhättan-Vänersborg Airport
    "ESKK": "KSK",  # medium_airport | Karlskoga Airport
    "ESKM": "MXX",  # medium_airport | Mora Airport
    "ESKN": "NYO",  # large_airport | Stockholm Skavsta Airport
    "ESKS": "SCR",  # large_airport | Scandinavian Mountains Airport
    "ESMK": "KID",  # medium_airport | Kristianstad Airport
    "ESMQ": "KLR",  # medium_airport | Kalmar Airport
    "ESMS": "MMX",  # large_airport | Malmö Sturup Airport
    "ESMT": "HAD",  # medium_airport | Halmstad Airport
    "ESMX": "VXO",  # medium_airport | Växjö Kronoberg Airport
    "ESNG": "GEV",  # medium_airport | Gällivare Airport
    "ESNK": "KRF",  # medium_airport | Kramfors-Sollefteå Höga Kusten Airport
    "ESNL": "LYC",  # medium_airport | Lycksele Airport
    "ESNN": "SDL",  # medium_airport | Sundsvall-Härnösand Airport
    "ESNO": "OER",  # medium_airport | Örnsköldsvik Airport
    "ESNQ": "KRN",  # large_airport | Kiruna Airport
    "ESNS": "SFT",  # medium_airport | Skellefteå Airport
    "ESNU": "UME",  # large_airport | Umeå Airport
    "ESNV": "VHM",  # medium_airport | Vilhelmina South Lapland Airport
    "ESNX": "AJR",  # medium_airport | Arvidsjaur Airport
    "ESNY": "SOO",  # medium_airport | Söderhamn Airport
    "ESNZ": "OSD",  # large_airport | Åre Östersund Airport
    "ESOE": "ORB",  # medium_airport | Örebro Airport
    "ESOK": "KSD",  # medium_airport | Karlstad Airport
    "ESOW": "VST",  # large_airport | Stockholm Västerås Airport
    "ESPA": "LLA",  # large_airport | Luleå Airport
    "ESSA": "ARN",  # large_airport | Stockholm-Arlanda Airport
    "ESSB": "BMA",  # medium_airport | Stockholm-Bromma Airport
    "ESSD": "BLE",  # medium_airport | Dala Airport
    "ESSK": "GVX",  # medium_airport | Gävle Sandviken Airport
    "ESSL": "LPI",  # large_airport | Linköping City Airport
    "ESSP": "NRK",  # medium_airport | Norrköping Airport
    "ESST": "TYF",  # medium_airport | Torsby Airport
    "ESSU": "EKT",  # medium_airport | Eskilstuna Airport
    "ESSV": "VBY",  # large_airport | Visby Airport
    "ESTA": "AGH",  # medium_airport | Ängelholm-Helsingborg Airport
    "ESUD": "SQO",  # medium_airport | Storuman Airport
    "ETAD": "SPM",  # medium_airport | Spangdahlem Air Base
    "ETAR": "RMS",  # medium_airport | Ramstein Air Base
    "ETHF": "FRZ",  # medium_airport | Fritzlar Army Airfield
    "ETMN": "FCN",  # medium_airport | Sea-Airport Cuxhaven/Nordholz / Nordholz Naval Airbase
    "ETNG": "GKE",  # medium_airport | Geilenkirchen Air Base
    "ETNL": "RLG",  # medium_airport | Rostock-Laage Airport
    "ETNS": "WBG",  # medium_airport | Schleswig Air Base
    "ETOU": "WIE",  # medium_airport | Wiesbaden Army Airfield
    "ETSI": "IGS",  # medium_airport | Ingolstadt Manching Airport
    "EVLA": "LPX",  # large_airport | Liepāja International Airport
    "EVRA": "RIX",  # large_airport | Riga International Airport
    "EYKA": "KUN",  # large_airport | Kaunas International Airport
    "EYPA": "PLQ",  # large_airport | Palanga International Airport
    "EYPP": "PNV",  # medium_airport | Panevėžys Air Base
    "EYSA": "SQQ",  # medium_airport | Šiauliai International Airport
    "EYVI": "VNO",  # large_airport | Vilnius International Airport
    "FAAB": "ALJ",  # medium_airport | Alexander Bay Airport
    "FAAG": "AGZ",  # medium_airport | Aggeneys Airport
    "FABE": "BIY",  # medium_airport | Bisho Airport
    "FABL": "BFN",  # large_airport | Bram Fischer International Airport
    "FACT": "CPT",  # large_airport | Cape Town International Airport
    "FAEL": "ELS",  # large_airport | King Phalo Airport
    "FAFB": "FCB",  # medium_airport | Ficksburg Sentraoes Airport
    "FAGC": "GCJ",  # medium_airport | Grand Central Airport
    "FAGG": "GRJ",  # large_airport | George Airport
    "FAGM": "QRA",  # medium_airport | Rand Airport
    "FAHR": "HRS",  # medium_airport | Harrismith Airport
    "FAHT": "HDS",  # medium_airport | Eastgate Airport / Air Force Base Hoedspruit
    "FAKD": "KXE",  # medium_airport | P C Pelser Airport
    "FAKM": "KIM",  # large_airport | Kimberley Airport
    "FAKN": "MQP",  # large_airport | Kruger Mpumalanga International Airport
    "FAKU": "KMH",  # medium_airport | Johan Pienaar Airport
    "FAKZ": "KLZ",  # medium_airport | Kleinsee Airport
    "FALA": "HLA",  # large_airport | Lanseria International Airport
    "FALC": "LMR",  # medium_airport | Lime Acres Finsch Mine Airport
    "FALE": "DUR",  # large_airport | King Shaka International Airport
    "FALW": "SDB",  # medium_airport | Langebaanweg Airport
    "FALY": "LAY",  # medium_airport | Ladysmith Airport
    "FAMD": "AAM",  # medium_airport | Malamala Airport
    "FAMG": "MGH",  # medium_airport | Margate Airport
    "FAMM": "MBD",  # medium_airport | Mmabatho International Airport
    "FAMU": "MZQ",  # medium_airport | Mkuze Airport
    "FANC": "NCS",  # medium_airport | Newcastle Airport
    "FAOH": "OUH",  # medium_airport | Oudtshoorn Airport
    "FAOR": "JNB",  # large_airport | O.R. Tambo International Airport
    "FAPE": "PLZ",  # large_airport | Chief Dawid Stuurman International Airport
    "FAPG": "PBZ",  # medium_airport | Plettenberg Bay Airport
    "FAPH": "PHW",  # medium_airport | Hendrik Van Eck Airport
    "FAPJ": "JOH",  # medium_airport | Port St Johns Airport
    "FAPM": "PZB",  # medium_airport | Pietermaritzburg Airport
    "FAPN": "NTY",  # medium_airport | Pilanesberg International Airport
    "FAPP": "PTG",  # large_airport | Polokwane International Airport
    "FAPS": "PCF",  # medium_airport | Potchefstroom Airport
    "FAQT": "UTW",  # medium_airport | Queenstown Airport
    "FARB": "RCB",  # medium_airport | Richards Bay Airport
    "FARS": "ROD",  # medium_airport | Robertson Airport
    "FASB": "SBU",  # medium_airport | Springbok Airport
    "FASC": "ZEC",  # medium_airport | Secunda Airport
    "FASS": "SIS",  # medium_airport | Sishen Airport
    "FASZ": "SZK",  # medium_airport | Skukuza Airport
    "FATZ": "LTA",  # medium_airport | Tzaneen Airport
    "FAUL": "ULD",  # medium_airport | Prince Mangosuthu Buthelezi Airport
    "FAUP": "UTN",  # medium_airport | Upington Airport
    "FAUT": "UTT",  # medium_airport | K. D. Matanzima Airport
    "FAVB": "VRU",  # medium_airport | Vryburg Airport
    "FAVG": "VIR",  # medium_airport | Virginia Airport
    "FAVR": "VRE",  # medium_airport | Vredendal Airport
    "FAWB": "PRY",  # medium_airport | Wonderboom Airport
    "FAWK": "WKF",  # medium_airport | Waterkloof Air Force Base
    "FBFT": "FRW",  # large_airport | Phillip Gaonwe Matante International Airport
    "FBJW": "JWA",  # medium_airport | Jwaneng Airport
    "FBKE": "BBK",  # large_airport | Kasane International Airport
    "FBMN": "MUB",  # large_airport | Maun International Airport
    "FBSK": "GBE",  # large_airport | Sir Seretse Khama International Airport
    "FBSN": "SXN",  # medium_airport | Sua Pan Airport
    "FBSP": "PKW",  # medium_airport | Selebi Phikwe Airport
    "FCBB": "BZV",  # large_airport | Maya-Maya International Airport
    "FCOD": "OLL",  # medium_airport | Oyo Ollombo Airport
    "FCOO": "FTX",  # medium_airport | Owando Airport
    "FCOU": "OUE",  # medium_airport | Ouesso Airport
    "FCPL": "DIS",  # medium_airport | Ngot Nzoungou Airport
    "FCPP": "PNR",  # large_airport | Antonio Agostinho-Neto International Airport
    "FDMS": "MTS",  # large_airport | Matsapha International Airport
    "FDSK": "SHO",  # large_airport | King Mswati III International Airport
    "FEFF": "BGF",  # large_airport | Bangui M'Poko International Airport
    "FEFT": "BBT",  # medium_airport | Berbérati Airport
    "FGBT": "BSG",  # large_airport | Bata International Airport
    "FGMY": "GEM",  # large_airport | President Obiang Nguema International Airport
    "FGSL": "SSG",  # large_airport | Malabo International Airport
    "FHAW": "ASI",  # medium_airport | RAF Ascension Island
    "FHSH": "HLE",  # medium_airport | Saint Helena International Airport
    "FIMP": "MRU",  # large_airport | Sir Seewoosagur Ramgoolam International Airport
    "FIMR": "RRG",  # medium_airport | Sir Charles Gaetan Duval Airport
    "FJDG": "NKW",  # medium_airport | Naval Support Facility Diego Garcia
    "FKKC": "TKC",  # medium_airport | Tiko Airport
    "FKKD": "DLA",  # large_airport | Douala International Airport
    "FKKL": "MVR",  # medium_airport | Salak Airport
    "FKKM": "FOM",  # medium_airport | Foumban Nkounja Airport
    "FKKN": "NGE",  # medium_airport | N'Gaoundéré Airport
    "FKKR": "GOU",  # large_airport | Garoua International Airport
    "FKKU": "BFX",  # medium_airport | Bafoussam Airport
    "FKKV": "BPC",  # medium_airport | Bamenda Airport
    "FKKY": "YAO",  # medium_airport | Yaoundé Ville Airport
    "FKYS": "NSI",  # large_airport | Yaoundé Nsimalen International Airport
    "FLKE": "CGJ",  # medium_airport | Kasompe Airport
    "FLLI": "LVI",  # large_airport | Harry Mwanga Nkumbula International Airport
    "FLLS": "LUN",  # large_airport | Kenneth Kaunda International Airport
    "FLMF": "MFU",  # large_airport | Mfuwe International Airport
    "FLMG": "MNR",  # medium_airport | Mongu Airport
    "FLSK": "NLA",  # large_airport | Simon Mwansa Kapwepwe International Airport
    "FLSO": "KIW",  # medium_airport | Southdowns Airport
    "FMCH": "HAH",  # large_airport | Prince Said Ibrahim International Airport
    "FMCI": "NWA",  # medium_airport | Mohéli Bandar Es Eslam Airport
    "FMCV": "AJN",  # medium_airport | Ouani Airport
    "FMCZ": "DZA",  # large_airport | Dzaoudzi Pamandzi International Airport
    "FMEE": "RUN",  # large_airport | Roland Garros Airport
    "FMEP": "ZSE",  # large_airport | Saint-Pierre Pierrefonds Airport
    "FMMI": "TNR",  # large_airport | Ivato International Airport
    "FMMN": "ZVA",  # medium_airport | Miandrivazo Airport
    "FMMS": "SMS",  # medium_airport | Sainte Marie Airport
    "FMMT": "TMM",  # large_airport | Toamasina Ambalamanasy Airport
    "FMMV": "MOQ",  # medium_airport | Morondava Airport
    "FMNA": "DIE",  # medium_airport | Arrachart Airport
    "FMNC": "WMR",  # medium_airport | Mananara Nord Airport
    "FMND": "ZWA",  # medium_airport | Andapa Airport
    "FMNH": "ANM",  # medium_airport | Antsirabe Airport
    "FMNL": "HVA",  # medium_airport | Analalava Airport
    "FMNM": "MJN",  # large_airport | Amborovy Airport
    "FMNN": "NOS",  # medium_airport | Nosy Be-Fascene International Airport
    "FMNQ": "BPY",  # medium_airport | Besalampy Airport
    "FMNR": "WMN",  # medium_airport | Maroantsetra Airport
    "FMNS": "SVB",  # medium_airport | Sambava Airport
    "FMNV": "VOH",  # medium_airport | Vohemar Airport
    "FMNW": "WAI",  # medium_airport | Ambalabe Airport
    "FMSD": "FTU",  # medium_airport | Tôlanaro Airport
    "FMSF": "WFI",  # medium_airport | Fianarantsoa Airport
    "FMSK": "WVK",  # medium_airport | Manakara Airport
    "FMSM": "MNJ",  # medium_airport | Mananjary Airport
    "FMSR": "MXM",  # medium_airport | Morombe Airport
    "FMST": "TLE",  # medium_airport | Toliara Airport
    "FNBC": "SSY",  # medium_airport | Mbanza Congo Airport
    "FNBG": "BUG",  # medium_airport | Benguela Airport
    "FNBJ": "NBJ",  # large_airport | Dr. Antonio Agostinho Neto International Airport
    "FNCA": "CAB",  # medium_airport | Cabinda Airport
    "FNCT": "CBT",  # medium_airport | Catumbela Airport
    "FNDU": "DUE",  # medium_airport | Dundo Airport
    "FNGI": "VPE",  # medium_airport | Ngjiva Pereira Airport
    "FNHU": "NOV",  # medium_airport | Albano Machado Airport
    "FNKU": "SVP",  # medium_airport | Kuito Airport
    "FNLU": "LAD",  # large_airport | Quatro de Fevereiro International Airport
    "FNMA": "MEG",  # medium_airport | Malanje Airport
    "FNME": "SPP",  # medium_airport | Menongue Airport
    "FNMO": "MSZ",  # medium_airport | Welwitschia Mirabilis International Airport
    "FNNG": "GXG",  # medium_airport | Negage Airport
    "FNPA": "PBN",  # medium_airport | Porto Amboim Airport
    "FNSA": "VHC",  # medium_airport | Saurimo Airport
    "FNSO": "SZA",  # medium_airport | Soyo Airport
    "FNSU": "NDD",  # medium_airport | Sumbe Airport
    "FNUB": "SDD",  # medium_airport | Lubango Mukanka International Airport
    "FNUE": "LUO",  # medium_airport | Luena Airport
    "FNUG": "UGO",  # medium_airport | Uige Airport
    "FNXA": "XGN",  # medium_airport | Xangongo Airport
    "FOGK": "KOU",  # medium_airport | Koulamoutou Mabimbi Airport
    "FOGM": "MJL",  # medium_airport | Mouilla Ville Airport
    "FOGO": "OYE",  # medium_airport | Oyem Airport
    "FOGQ": "OKN",  # medium_airport | Okondja Airport
    "FOGR": "LBQ",  # medium_airport | Lambarene Airport
    "FOOB": "BMM",  # medium_airport | Bitam Airport
    "FOOG": "POG",  # large_airport | Port Gentil International Airport
    "FOOH": "OMB",  # medium_airport | Omboue Hospital Airport
    "FOOK": "MKU",  # medium_airport | Makokou Airport
    "FOOL": "LBV",  # large_airport | Libreville Leon M'ba International Airport
    "FOON": "MVB",  # large_airport | M'Vengue El Hadj Omar Bongo Ondimba International Airport
    "FPPR": "PCP",  # medium_airport | Principe Airport
    "FPST": "TMS",  # large_airport | São Tomé International Airport
    "FQBR": "BEW",  # large_airport | Beira International Airport
    "FQCH": "VPY",  # medium_airport | Chimoio Airport
    "FQIN": "INH",  # medium_airport | Inhambane Airport
    "FQLC": "VXC",  # medium_airport | Lichinga Airport
    "FQMA": "MPM",  # large_airport | Maputo Airport
    "FQMD": "MUD",  # medium_airport | Mueda Airport
    "FQMP": "MZB",  # medium_airport | Mocímboa da Praia Airport
    "FQNC": "MNC",  # medium_airport | Nacala International Airport
    "FQNP": "APL",  # large_airport | Nampula Airport
    "FQPB": "POL",  # medium_airport | Pemba Airport
    "FQQL": "UEL",  # medium_airport | Quelimane Airport
    "FQTT": "TET",  # large_airport | Tete Airport
    "FQVL": "VNX",  # medium_airport | Vilankulo Airport
    "FSIA": "SEZ",  # large_airport | Seychelles International Airport
    "FSPP": "PRI",  # medium_airport | Praslin Island Airport
    "FTTC": "AEH",  # medium_airport | Abeche Airport
    "FTTD": "MQQ",  # medium_airport | Moundou Airport
    "FTTJ": "NDJ",  # large_airport | N'Djamena International Airport
    "FTTY": "FYT",  # medium_airport | Faya-Largeau Airport
    "FVBU": "BUQ",  # large_airport | Joshua Mqabuko Nkomo International Airport
    "FVCZ": "BFO",  # medium_airport | Buffalo Range Airport
    "FVFA": "VFA",  # large_airport | Victoria Falls International Airport
    "FVHA": "HRE",  # large_airport | Robert Gabriel Mugabe International Airport
    "FVKB": "KAB",  # medium_airport | Kariba Airport
    "FVMV": "MVZ",  # medium_airport | Masvingo International Airport
    "FVTL": "GWE",  # medium_airport | Josiah Tungamirai Air Force Base
    "FVWN": "HWN",  # medium_airport | Hwange National Park Airport
    "FWCL": "BLZ",  # large_airport | Chileka International Airport
    "FWDW": "DWA",  # medium_airport | Dwangwa Airport
    "FWKA": "KGJ",  # medium_airport | Karonga Airport
    "FWKI": "LLW",  # large_airport | Kamuzu International Airport
    "FWUU": "ZZU",  # medium_airport | Mzuzu Airport
    "FXMM": "MSU",  # large_airport | Moshoeshoe I International Airport
    "FYAR": "ADI",  # medium_airport | Arandis Airport
    "FYGF": "GFY",  # medium_airport | Grootfontein Airport
    "FYKM": "MPA",  # medium_airport | Katima Mulilo Airport
    "FYKT": "KMP",  # medium_airport | Keetmanshoop Airport
    "FYLZ": "LUD",  # medium_airport | Luderitz Airport
    "FYOA": "OND",  # medium_airport | Ondangwa Airport
    "FYOG": "OMD",  # medium_airport | Oranjemund Airport
    "FYRU": "NDU",  # medium_airport | Rundu Airport
    "FYTM": "TSB",  # medium_airport | Tsumeb Airport
    "FYWB": "WVB",  # large_airport | Walvis Bay International Airport
    "FYWE": "ERS",  # medium_airport | Eros Airport
    "FYWH": "WDH",  # large_airport | Hosea Kutako International Airport
    "FZAA": "FIH",  # large_airport | Ndjili International Airport
    "FZAB": "NLO",  # medium_airport | Ndolo Airport
    "FZBO": "FDU",  # medium_airport | Bandundu Airport
    "FZCA": "KKW",  # medium_airport | Kikwit Airport
    "FZEA": "MDK",  # medium_airport | Mbandaka Airport
    "FZFD": "BDT",  # medium_airport | Gbadolite Airport
    "FZFK": "GMA",  # medium_airport | Gemena Airport
    "FZGA": "LIQ",  # medium_airport | Lisala Airport
    "FZIC": "FKI",  # large_airport | Bangoka International Airport
    "FZJH": "IRP",  # medium_airport | Matari Airport
    "FZKA": "BUX",  # medium_airport | Bunia Airport
    "FZKJ": "BZU",  # medium_airport | Buta Zega Airport
    "FZMA": "BKY",  # medium_airport | Bukavu Kavumu Airport
    "FZNA": "GOM",  # large_airport | Goma International Airport
    "FZOA": "KND",  # medium_airport | Kindu Airport
    "FZQA": "FBM",  # large_airport | Lubumbashi International Airport
    "FZQM": "KWZ",  # medium_airport | Kolwezi Airport
    "FZRF": "FMI",  # medium_airport | Kalemie Airport
    "FZUA": "KGA",  # medium_airport | Kananga Airport
    "FZWA": "MJM",  # medium_airport | Mbuji Mayi Airport
    "GABS": "BKO",  # large_airport | Modibo Keita International Airport
    "GAGO": "GAQ",  # medium_airport | Gao International Airport
    "GAKY": "KYS",  # medium_airport | Kayes Dag Dag Airport
    "GAMB": "MZI",  # medium_airport | Mopti Airport
    "GATB": "TOM",  # large_airport | Tombouktou Airport
    "GBYD": "BJL",  # large_airport | Banjul International Airport
    "GCFV": "FUE",  # large_airport | Fuerteventura Airport
    "GCHI": "VDE",  # medium_airport | El Hierro Airport
    "GCLA": "SPC",  # medium_airport | La Palma Airport
    "GCLP": "LPA",  # large_airport | Gran Canaria Airport
    "GCRR": "ACE",  # large_airport | César Manrique-Lanzarote Airport
    "GCTS": "TFS",  # large_airport | Tenerife Sur Airport
    "GCXO": "TFN",  # large_airport | Tenerife Norte-Ciudad de La Laguna Airport
    "GEML": "MLN",  # medium_airport | Melilla Airport
    "GFBO": "KBS",  # medium_airport | Bo Airport
    "GFKE": "KEN",  # medium_airport | Kenema Airport
    "GFLL": "FNA",  # large_airport | Lungi International Airport
    "GFYE": "WYE",  # medium_airport | Yengema Airport
    "GGOV": "OXB",  # large_airport | Osvaldo Vieira International Airport
    "GLGE": "SNI",  # medium_airport | Greenville/Sinoe Airport
    "GLMR": "MLW",  # medium_airport | Spriggs Payne Airport
    "GLRB": "ROB",  # large_airport | Roberts International Airport
    "GMAD": "AGA",  # large_airport | Al Massira Airport
    "GMAT": "TTA",  # medium_airport | Tan Tan Airport
    "GMAZ": "OZG",  # large_airport | Zagora Airport
    "GMFB": "UAR",  # medium_airport | Bouarfa Airport
    "GMFF": "FEZ",  # large_airport | Fes Saïss International Airport
    "GMFK": "ERH",  # medium_airport | Moulay Ali Cherif Airport
    "GMFM": "MEK",  # medium_airport | Bassatine Airport
    "GMFO": "OUD",  # large_airport | Oujda Angads Airport
    "GMMA": "SMW",  # large_airport | Smara Airport
    "GMMD": "BEM",  # large_airport | Beni Mellal Airport
    "GMME": "RBA",  # large_airport | Rabat-Salé Airport
    "GMMH": "VIL",  # large_airport | Dakhla Airport
    "GMMI": "ESU",  # medium_airport | Essaouira-Mogador Airport
    "GMML": "EUN",  # large_airport | Laayoune Hassan I International Airport
    "GMMN": "CMN",  # large_airport | Mohammed V International Airport
    "GMMW": "NDR",  # large_airport | Nador Al Aaroui International Airport
    "GMMX": "RAK",  # large_airport | Marrakesh Menara Airport
    "GMMY": "NNA",  # medium_airport | Kenitra Air Base
    "GMMZ": "OZZ",  # large_airport | Ouarzazate International Airport
    "GMTA": "AHU",  # medium_airport | Cherif Al Idrissi Airport
    "GMTN": "TTU",  # large_airport | Sania Ramel Airport
    "GMTT": "TNG",  # large_airport | Tangier Ibn Battuta Airport
    "GOBD": "DSS",  # large_airport | Blaise Diagne International Airport
    "GOGG": "ZIG",  # medium_airport | Ziguinchor Airport
    "GOGS": "CSK",  # medium_airport | Cap Skirring Airport
    "GOOK": "KLC",  # medium_airport | Kaolack Airport
    "GOOY": "DKR",  # large_airport | Léopold Sédar Senghor International Airport
    "GOSM": "MAX",  # medium_airport | Ouro Sogui Airport
    "GOSS": "XLS",  # medium_airport | Saint Louis Airport
    "GOTB": "BXE",  # medium_airport | Bakel Airport
    "GOTK": "KGG",  # medium_airport | Kédougou Airport
    "GOTT": "TUD",  # medium_airport | Tambacounda Airport
    "GQNO": "NKC",  # large_airport | Nouakchott–Oumtounsy International Airport
    "GQPA": "ATR",  # large_airport | Atar International Airport
    "GQPP": "NDB",  # large_airport | Nouadhibou International Airport
    "GUCY": "CKY",  # large_airport | Ahmed Sékou Touré International Airport
    "GVAC": "SID",  # large_airport | Amílcar Cabral International Airport
    "GVBA": "BVC",  # large_airport | Aristides Pereira International Airport
    "GVMA": "MMO",  # medium_airport | Maio Airport
    "GVNP": "RAI",  # large_airport | Nelson Mandela International Airport
    "GVSN": "SNE",  # medium_airport | Preguiça Airport
    "GVSV": "VXE",  # large_airport | Cesaria Evora International Airport
    "HAAB": "ADD",  # large_airport | Addis Ababa Bole International Airport
    "HAAM": "AMH",  # medium_airport | Arba Minch Airport
    "HAAX": "AXU",  # medium_airport | Axum Airport
    "HABD": "BJR",  # medium_airport | Bahir Dar Airport
    "HADR": "DIR",  # large_airport | Aba Tenna Dejazmach Yilma International Airport
    "HAGM": "GMB",  # medium_airport | Gambela Airport
    "HAGN": "GDQ",  # medium_airport | Gondar Airport
    "HAGO": "GDE",  # medium_airport | Gode Airport
    "HAHM": "QHR",  # medium_airport | Harar Meda Airport
    "HAJJ": "JIJ",  # large_airport | Gerad Wilwal International Airport
    "HAJK": "BCO",  # medium_airport | Baco Airport
    "HAJM": "JIM",  # medium_airport | Jimma Airport
    "HAKD": "ABK",  # medium_airport | Kebri Dahar Airport
    "HALA": "AWA",  # large_airport | Hawassa International Airport
    "HAMK": "MQX",  # medium_airport | Mekele Alula Aba Nega Airport
    "HASO": "ASO",  # medium_airport | Asosa Airport
    "HBBA": "BJM",  # large_airport | Bujumbura Melchior Ndadaye International Airport
    "HBBE": "GID",  # medium_airport | Gitega Airport
    "HCMF": "BSA",  # large_airport | Bender Qassim International Airport
    "HCMH": "HGA",  # large_airport | Egal International Airport
    "HCMI": "BBO",  # medium_airport | Berbera Airport
    "HCMK": "KMU",  # medium_airport | Kismayo Airport
    "HCMM": "MGQ",  # large_airport | Aden Adde International Airport
    "HDAM": "JIB",  # large_airport | Djibouti-Ambouli Airport
    "HEAL": "DBB",  # large_airport | El Alamein International Airport
    "HEAR": "AAC",  # large_airport | El Arish International Airport
    "HEAT": "ATZ",  # large_airport | Asyut International Airport
    "HEBA": "HBE",  # large_airport | Alexandria International Airport
    "HEBL": "ABS",  # medium_airport | Abu Simbel Airport
    "HECA": "CAI",  # large_airport | Cairo International Airport
    "HECP": "CCE",  # medium_airport | Capital International Airport
    "HEGN": "HRG",  # large_airport | Hurghada International Airport
    "HEGR": "EGH",  # medium_airport | El Jora Airport
    "HELX": "LXR",  # large_airport | Luxor International Airport
    "HEMA": "RMF",  # large_airport | Marsa Alam International Airport
    "HEMM": "MUH",  # large_airport | Mersa Matruh International Airport
    "HEPS": "PSD",  # large_airport | Port Said International Airport
    "HESC": "SKV",  # medium_airport | Saint Catherine International Airport
    "HESG": "HMB",  # large_airport | Sohag International Airport
    "HESH": "SSH",  # large_airport | Sharm El Sheikh International Airport
    "HESN": "ASW",  # large_airport | Aswan International Airport
    "HESX": "SPX",  # large_airport | Sphinx International Airport
    "HETB": "TCP",  # medium_airport | Taba International Airport
    "HHAS": "ASM",  # large_airport | Asmara International Airport
    "HHMS": "MSW",  # medium_airport | Massawa International Airport
    "HHSB": "ASA",  # medium_airport | Assab International Airport
    "HJJJ": "JUB",  # large_airport | Juba International Airport
    "HKAM": "ASV",  # medium_airport | Amboseli Airport
    "HKEL": "EDL",  # large_airport | Eldoret International Airport
    "HKJK": "NBO",  # large_airport | Jomo Kenyatta International Airport
    "HKKI": "KIS",  # large_airport | Kisumu International Airport
    "HKKT": "KTL",  # medium_airport | Kitale Airport
    "HKLK": "LKG",  # medium_airport | Lokichogio Airport
    "HKLO": "LOK",  # medium_airport | Lodwar Airport
    "HKLU": "LAU",  # medium_airport | Manda Airport
    "HKML": "MYD",  # medium_airport | Malindi International Airport
    "HKMO": "MBA",  # large_airport | Moi International Airport
    "HKMS": "MRE",  # medium_airport | Mara Serena Lodge Airstrip
    "HKNK": "NUU",  # medium_airport | Lanet Military Airstrip
    "HKNL": "NYK",  # medium_airport | Nanyuki Airport
    "HKNW": "WIL",  # medium_airport | Nairobi Wilson Airport
    "HKWJ": "WJR",  # medium_airport | Wajir Airport
    "HLGD": "SRX",  # large_airport | Sirt International Airport / Ghardabiya Airbase
    "HLGT": "GHT",  # medium_airport | Ghat Airport
    "HLKF": "AKF",  # medium_airport | Kufra Airport
    "HLLB": "BEN",  # large_airport | Benina International Airport
    "HLLM": "MJI",  # large_airport | Mitiga International Airport
    "HLLQ": "LAQ",  # large_airport | Al Abraq International Airport
    "HLLS": "SEB",  # medium_airport | Sabha Airport
    "HLMB": "LMQ",  # medium_airport | Marsa al Brega Airport
    "HLTD": "LTD",  # medium_airport | Ghadames Airport
    "HRYG": "GYI",  # medium_airport | Gisenyi Airport
    "HRYR": "KGL",  # large_airport | Kigali International Airport
    "HRZA": "KME",  # medium_airport | Kamembe Airport
    "HSDN": "DOG",  # medium_airport | Dongola Airport
    "HSFS": "ELF",  # medium_airport | El Fasher Airport
    "HSKA": "KSL",  # medium_airport | Kassala Airport
    "HSMN": "MWE",  # medium_airport | Merowe Airport
    "HSNN": "UYL",  # medium_airport | Nyala Airport
    "HSOB": "EBD",  # medium_airport | El-Obeid Airport
    "HSPN": "PZU",  # large_airport | Port Sudan New International Airport
    "HSSK": "KRT",  # large_airport | Khartoum International Airport
    "HSSM": "MAK",  # medium_airport | Malakal International Airport
    "HSWW": "WUU",  # medium_airport | Wau Airport
    "HTAR": "ARK",  # medium_airport | Arusha Airport
    "HTDA": "DAR",  # large_airport | Julius Nyerere International Airport
    "HTDO": "DOD",  # medium_airport | Dodoma Airport
    "HTGW": "MBI",  # medium_airport | Songwe Airport
    "HTIR": "IRI",  # medium_airport | Iringa Airport
    "HTKJ": "JRO",  # large_airport | Kilimanjaro International Airport
    "HTLM": "LKY",  # medium_airport | Lake Manyara Airport
    "HTMT": "MYW",  # medium_airport | Mtwara Airport
    "HTMW": "MWZ",  # large_airport | Mwanza International Airport
    "HTPE": "PMA",  # medium_airport | Pemba Airport
    "HTTG": "TGT",  # medium_airport | Tanga Airport
    "HTZA": "ZNZ",  # large_airport | Abeid Amani Karume International Airport
    "HUAR": "RUA",  # medium_airport | Arua Airport
    "HUEN": "EBB",  # large_airport | Entebbe International Airport
    "HUGU": "ULU",  # medium_airport | Gulu Airport
    "HUSO": "SRT",  # medium_airport | Soroti Airport
    "KABE": "ABE",  # medium_airport | Lehigh Valley International Airport
    "KABI": "ABI",  # medium_airport | Abilene Regional Airport
    "KABQ": "ABQ",  # large_airport | Albuquerque International Sunport
    "KABR": "ABR",  # medium_airport | Aberdeen Regional Airport
    "KABY": "ABY",  # medium_airport | Southwest Georgia Regional Airport
    "KACK": "ACK",  # medium_airport | Nantucket Memorial Airport
    "KACT": "ACT",  # medium_airport | Waco Regional Airport
    "KACV": "ACV",  # medium_airport | California Redwood Coast-Humboldt County Airport
    "KACY": "ACY",  # medium_airport | Atlantic City International Airport
    "KADH": "ADT",  # medium_airport | Ada Regional Airport
    "KADW": "ADW",  # medium_airport | Joint Base Andrews
    "KAEX": "AEX",  # medium_airport | Alexandria International Airport
    "KAFW": "AFW",  # medium_airport | Perot Field/Fort Worth Alliance Airport
    "KAGC": "AGC",  # medium_airport | Allegheny County Airport
    "KAGS": "AGS",  # medium_airport | Augusta Regional At Bush Field
    "KAHN": "AHN",  # medium_airport | Athens Ben Epps Airport
    "KAIA": "AIA",  # medium_airport | Alliance Municipal Airport
    "KAKR": "AKC",  # medium_airport | Akron Fulton International Airport
    "KALB": "ALB",  # large_airport | Albany International Airport
    "KALI": "ALI",  # medium_airport | Alice International Airport
    "KALM": "ALM",  # medium_airport | Alamogordo White Sands Regional Airport
    "KALN": "ALN",  # medium_airport | St Louis Regional Airport
    "KALO": "ALO",  # medium_airport | Waterloo Regional Airport
    "KALS": "ALS",  # medium_airport | San Luis Valley Regional Airport/Bergman Field
    "KALW": "ALW",  # medium_airport | Walla Walla Regional Airport
    "KAMA": "AMA",  # medium_airport | Rick Husband Amarillo International Airport
    "KANB": "ANB",  # medium_airport | Anniston Regional Airport
    "KAND": "AND",  # medium_airport | Anderson Regional Airport
    "KAOO": "AOO",  # medium_airport | Altoona Blair County Airport
    "KAPA": "APA",  # medium_airport | Centennial Airport
    "KAPF": "APF",  # medium_airport | Naples Municipal Airport
    "KAPG": "APG",  # medium_airport | Phillips Army Air Field
    "KAPN": "APN",  # medium_airport | Alpena County Regional Airport
    "KARA": "ARA",  # medium_airport | Acadiana Regional Airport
    "KART": "ART",  # medium_airport | Watertown International Airport
    "KASE": "ASE",  # medium_airport | Aspen-Pitkin County Airport (Sardy Field)
    "KAST": "AST",  # medium_airport | Astoria Regional Airport
    "KATL": "ATL",  # large_airport | Hartsfield Jackson Atlanta International Airport
    "KATW": "ATW",  # medium_airport | Appleton International Airport
    "KATY": "ATY",  # medium_airport | Watertown Regional Airport
    "KAUG": "AUG",  # medium_airport | Augusta State Airport
    "KAUS": "AUS",  # large_airport | Austin Bergstrom International Airport
    "KAUW": "AUW",  # medium_airport | Wausau Downtown Airport
    "KAVL": "AVL",  # medium_airport | Asheville Regional Airport
    "KAVP": "AVP",  # medium_airport | Wilkes-Barre/Scranton International Airport
    "KAXN": "AXN",  # medium_airport | Chandler Field
    "KAZO": "AZO",  # medium_airport | Kalamazoo/Battle Creek International Airport
    "KBAB": "BAB",  # medium_airport | Beale Air Force Base
    "KBAD": "BAD",  # medium_airport | Barksdale Air Force Base
    "KBAF": "BAF",  # medium_airport | Westfield-Barnes Regional Airport
    "KBAK": "CLU",  # medium_airport | Columbus Municipal Airport
    "KBBD": "BBD",  # medium_airport | Curtis Field
    "KBBG": "BKG",  # medium_airport | Branson Airport
    "KBCE": "BCE",  # medium_airport | Bryce Canyon Airport
    "KBCT": "BCT",  # medium_airport | Boca Raton Airport
    "KBDE": "BDE",  # medium_airport | Baudette International Airport
    "KBDL": "BDL",  # large_airport | Bradley International Airport
    "KBDR": "BDR",  # medium_airport | Igor I Sikorsky Memorial Airport
    "KBED": "BED",  # medium_airport | Laurence G Hanscom Field
    "KBFD": "BFD",  # medium_airport | Bradford Regional Airport
    "KBFF": "BFF",  # medium_airport | Western Neb. Rgnl/William B. Heilig Airport
    "KBFI": "BFI",  # medium_airport | King County International Airport - Boeing Field
    "KBFL": "BFL",  # medium_airport | Meadows Field
    "KBFM": "BFM",  # medium_airport | Mobile Downtown Airport
    "KBGM": "BGM",  # medium_airport | Greater Binghamton/Edwin A Link field
    "KBGR": "BGR",  # medium_airport | Bangor International Airport
    "KBHB": "BHB",  # medium_airport | Hancock County-Bar Harbor Airport
    "KBHM": "BHM",  # large_airport | Birmingham-Shuttlesworth International Airport
    "KBIF": "BIF",  # medium_airport | Biggs Army Air Field (Fort Bliss)
    "KBIH": "BIH",  # medium_airport | Eastern Sierra Regional Airport
    "KBIL": "BIL",  # medium_airport | Billings Logan International Airport
    "KBIS": "BIS",  # medium_airport | Bismarck Municipal Airport
    "KBIX": "BIX",  # medium_airport | Keesler Air Force Base
    "KBJC": "BJC",  # medium_airport | Rocky Mountain Metropolitan Airport
    "KBJI": "BJI",  # medium_airport | Bemidji Regional Airport
    "KBKE": "BKE",  # medium_airport | Baker City Municipal Airport
    "KBKF": "BFK",  # medium_airport | Buckley Space Force Base
    "KBKL": "BKL",  # medium_airport | Burke Lakefront Airport
    "KBKW": "BKW",  # medium_airport | Raleigh County Memorial Airport
    "KBLF": "BLF",  # medium_airport | Mercer County Airport
    "KBLH": "BLH",  # medium_airport | Blythe Airport
    "KBLI": "BLI",  # medium_airport | Bellingham International Airport
    "KBLV": "BLV",  # medium_airport | Scott AFB/Midamerica Airport
    "KBMG": "BMG",  # medium_airport | Monroe County Airport
    "KBMI": "BMI",  # medium_airport | Central Illinois Regional Airport at Bloomington-Normal
    "KBNA": "BNA",  # large_airport | Nashville International Airport
    "KBNO": "BNO",  # medium_airport | Burns Municipal Airport
    "KBOI": "BOI",  # large_airport | Boise Air Terminal/Gowen Field
    "KBOS": "BOS",  # large_airport | Boston Logan International Airport
    "KBPI": "BPI",  # medium_airport | Miley Memorial Field
    "KBPK": "WMH",  # medium_airport | Ozark Regional Airport
    "KBPT": "BPT",  # medium_airport | Jack Brooks Regional Airport
    "KBQK": "BQK",  # medium_airport | Brunswick Golden Isles Airport
    "KBRD": "BRD",  # medium_airport | Brainerd Lakes Regional Airport
    "KBRL": "BRL",  # medium_airport | Southeast Iowa Regional Airport
    "KBRO": "BRO",  # medium_airport | Brownsville South Padre Island International Airport
    "KBTL": "BTL",  # medium_airport | Battle Creek Executive Airport at Kellogg Field
    "KBTM": "BTM",  # medium_airport | Bert Mooney Airport
    "KBTR": "BTR",  # medium_airport | Baton Rouge Metropolitan Airport
    "KBTV": "BTV",  # medium_airport | Patrick Leahy Burlington International Airport
    "KBUF": "BUF",  # large_airport | Buffalo Niagara International Airport
    "KBUR": "BUR",  # large_airport | Hollywood Burbank Airport
    "KBVI": "BFP",  # medium_airport | Beaver County Airport
    "KBVY": "BVY",  # medium_airport | Beverly Regional Airport
    "KBWG": "BWG",  # medium_airport | Bowling Green Warren County Regional Airport
    "KBWI": "BWI",  # large_airport | Baltimore/Washington International Thurgood Marshall Airport
    "KBXM": "NHZ",  # medium_airport | Brunswick Executive Airport
    "KBYH": "BYH",  # medium_airport | Arkansas International Airport
    "KBYI": "BYI",  # medium_airport | Burley Municipal Airport
    "KBYS": "BYS",  # medium_airport | Bicycle Lake Army Air Field
    "KBZN": "BZN",  # medium_airport | Bozeman Yellowstone International Airport
    "KCAE": "CAE",  # medium_airport | Columbia Metropolitan Airport
    "KCAK": "CAK",  # medium_airport | Akron Canton Regional Airport
    "KCAR": "CAR",  # medium_airport | Caribou Municipal Airport
    "KCBM": "CBM",  # medium_airport | Columbus Air Force Base
    "KCCR": "CCR",  # medium_airport | Buchanan Field
    "KCCY": "CCY",  # medium_airport | Northeast Iowa Regional Airport
    "KCDC": "CDC",  # medium_airport | Cedar City Regional Airport
    "KCDR": "CDR",  # medium_airport | Chadron Municipal Airport
    "KCDS": "CDS",  # medium_airport | Childress Municipal Airport
    "KCEC": "CEC",  # medium_airport | Jack Mc Namara Field Airport
    "KCEF": "CEF",  # medium_airport | Westover Metropolitan Airport / Westover Air Reserve Base
    "KCEW": "CEW",  # medium_airport | Bob Sikes Airport
    "KCEZ": "CEZ",  # medium_airport | Cortez Municipal Airport
    "KCGF": "CGF",  # medium_airport | Cuyahoga County Airport
    "KCGI": "CGI",  # medium_airport | Cape Girardeau Regional Airport
    "KCHA": "CHA",  # medium_airport | Chattanooga Metropolitan Airport (Lovell Field)
    "KCHO": "CHO",  # medium_airport | Charlottesville Albemarle Airport
    "KCHS": "CHS",  # large_airport | Charleston International Airport
    "KCID": "CID",  # medium_airport | The Eastern Iowa Airport
    "KCIU": "CIU",  # medium_airport | Chippewa County International Airport
    "KCKB": "CKB",  # medium_airport | North Central West Virginia Airport
    "KCLE": "CLE",  # large_airport | Cleveland Hopkins International Airport
    "KCLL": "CLL",  # medium_airport | Easterwood Field
    "KCLM": "CLM",  # medium_airport | William R Fairchild International Airport
    "KCLT": "CLT",  # large_airport | Charlotte Douglas International Airport
    "KCMH": "CMH",  # large_airport | John Glenn Columbus International Airport
    "KCMI": "CMI",  # medium_airport | University of Illinois Willard Airport
    "KCMX": "CMX",  # medium_airport | Houghton County Memorial Airport
    "KCNM": "CNM",  # medium_airport | Cavern City Air Terminal
    "KCNU": "CNU",  # medium_airport | Chanute Martin Johnson Airport
    "KCNY": "CNY",  # medium_airport | Canyonlands Regional Airport
    "KCOD": "COD",  # medium_airport | Yellowstone Regional Airport
    "KCOE": "COE",  # medium_airport | Coeur D'Alene Airport - Pappy Boyington Field
    "KCOF": "COF",  # medium_airport | Patrick Space Force Base
    "KCON": "CON",  # medium_airport | Concord Municipal Airport
    "KCOS": "COS",  # large_airport | City of Colorado Springs Municipal Airport
    "KCOU": "COU",  # medium_airport | Columbia Regional Airport
    "KCPR": "CPR",  # medium_airport | Casper-Natrona County International Airport
    "KCRE": "CRE",  # medium_airport | Grand Strand Airport
    "KCRG": "CRG",  # medium_airport | Jacksonville Executive at Craig Airport
    "KCRP": "CRP",  # medium_airport | Corpus Christi International Airport
    "KCRQ": "CLD",  # medium_airport | McClellan-Palomar Airport
    "KCRW": "CRW",  # medium_airport | Yeager Airport
    "KCSG": "CSG",  # medium_airport | Columbus Airport
    "KCSV": "CSV",  # medium_airport | Crossville Memorial Airport Whitson Field
    "KCTB": "CTB",  # medium_airport | Cut Bank International Airport
    "KCUB": "CUB",  # medium_airport | Jim Hamilton L.B. Owens Airport
    "KCVG": "CVG",  # large_airport | Cincinnati Northern Kentucky International Airport
    "KCVN": "CVN",  # medium_airport | Clovis Municipal Airport
    "KCVO": "CVO",  # medium_airport | Corvallis Municipal Airport
    "KCVS": "CVS",  # medium_airport | Cannon Air Force Base
    "KCWA": "CWA",  # medium_airport | Central Wisconsin Airport
    "KCXO": "CXO",  # medium_airport | Conroe-North Houston Regional Airport
    "KCXP": "CSN",  # medium_airport | Carson Airport
    "KCYS": "CYS",  # medium_airport | Cheyenne Regional Jerry Olson Field
    "KDAA": "DAA",  # medium_airport | Davison Army Air Field
    "KDAB": "DAB",  # medium_airport | Daytona Beach International Airport
    "KDAG": "DAG",  # medium_airport | Barstow Daggett Airport
    "KDAL": "DAL",  # large_airport | Dallas Love Field
    "KDAN": "DAN",  # medium_airport | Danville Regional Airport
    "KDAY": "DAY",  # medium_airport | James M. Cox Dayton International Airport
    "KDBQ": "DBQ",  # medium_airport | Dubuque Regional Airport
    "KDCA": "DCA",  # large_airport | Ronald Reagan Washington National Airport
    "KDDC": "DDC",  # medium_airport | Dodge City Regional Airport
    "KDEC": "DEC",  # medium_airport | Decatur Airport
    "KDEN": "DEN",  # large_airport | Denver International Airport
    "KDET": "DET",  # medium_airport | Coleman A. Young Municipal Airport
    "KDFW": "DFW",  # large_airport | Dallas Fort Worth International Airport
    "KDHN": "DHN",  # medium_airport | Dothan Regional Airport
    "KDHT": "DHT",  # medium_airport | Dalhart Municipal Airport
    "KDIK": "DIK",  # medium_airport | Dickinson Theodore Roosevelt Regional Airport
    "KDLF": "DLF",  # medium_airport | Laughlin Air Force Base
    "KDLH": "DLH",  # medium_airport | Duluth International Airport
    "KDLS": "DLS",  # medium_airport | Columbia Gorge Regional Airport
    "KDMA": "DMA",  # medium_airport | Davis Monthan Air Force Base
    "KDMN": "DMN",  # medium_airport | Deming Municipal Airport
    "KDNL": "DNL",  # medium_airport | Daniel Field
    "KDOV": "DOV",  # medium_airport | Dover Civil Air Terminal/Dover Air Force Base
    "KDPA": "DPA",  # medium_airport | Dupage Airport
    "KDRA": "DRA",  # medium_airport | Desert Rock Airport
    "KDRI": "DRI",  # medium_airport | Beauregard Regional Airport
    "KDRO": "DRO",  # medium_airport | Durango La Plata County Airport
    "KDRT": "DRT",  # medium_airport | Del Rio International Airport
    "KDSM": "DSM",  # large_airport | Des Moines International Airport
    "KDTS": "DSI",  # medium_airport | Destin Executive Airport
    "KDTW": "DTW",  # large_airport | Detroit Metropolitan Wayne County Airport
    "KDUA": "DUA",  # medium_airport | Durant Regional Airport - Eaker Field
    "KDUG": "DUG",  # medium_airport | Bisbee Douglas International Airport
    "KDUJ": "DUJ",  # medium_airport | DuBois Regional Airport
    "KDVL": "DVL",  # medium_airport | Devils Lake Regional Airport
    "KDXR": "DXR",  # medium_airport | Danbury Municipal Airport
    "KDYS": "DYS",  # medium_airport | Dyess Air Force Base
    "KEAR": "EAR",  # medium_airport | Kearney Regional Airport
    "KEAT": "EAT",  # medium_airport | Pangborn Memorial Airport
    "KEAU": "EAU",  # medium_airport | Chippewa Valley Regional Airport
    "KECG": "ECG",  # medium_airport | Elizabeth City Regional Airport & Coast Guard Air Station
    "KECP": "ECP",  # medium_airport | Northwest Florida Beaches International Airport
    "KEDW": "EDW",  # medium_airport | Edwards Air Force Base
    "KEED": "EED",  # medium_airport | Needles Airport
    "KEEN": "EEN",  # medium_airport | Dillant Hopkins Airport
    "KEFD": "EFD",  # medium_airport | Ellington Airport
    "KEGE": "EGE",  # medium_airport | Eagle County Regional Airport
    "KEGI": "EGI",  # medium_airport | Duke Field
    "KEKA": "EKA",  # medium_airport | Murray Field
    "KEKN": "EKN",  # medium_airport | Elkins-Randolph County Regional Airport
    "KEKO": "EKO",  # medium_airport | Elko Regional Airport
    "KELD": "ELD",  # medium_airport | South Arkansas Regional Airport at Goodwin Field
    "KELM": "ELM",  # medium_airport | Elmira Corning Regional Airport
    "KELO": "LYU",  # medium_airport | Ely Municipal Airport
    "KELP": "ELP",  # large_airport | El Paso International Airport
    "KELY": "ELY",  # medium_airport | Ely Airport Yelland Field
    "KEND": "END",  # medium_airport | Vance Air Force Base
    "KENV": "ENV",  # medium_airport | Wendover Airport
    "KENW": "ENW",  # medium_airport | Kenosha Regional Airport
    "KERI": "ERI",  # medium_airport | Erie International Tom Ridge Field
    "KESC": "ESC",  # medium_airport | Delta County Airport
    "KESF": "ESF",  # medium_airport | Esler Army Airfield / Esler Regional Airport
    "KEUG": "EUG",  # medium_airport | Eugene Airport
    "KEVV": "EVV",  # medium_airport | Evansville Regional Airport
    "KEVW": "EVW",  # medium_airport | Evanston-Uinta County Airport-Burns Field
    "KEWB": "EWB",  # medium_airport | New Bedford Regional Airport
    "KEWN": "EWN",  # medium_airport | Coastal Carolina Regional Airport
    "KEWR": "EWR",  # large_airport | Newark Liberty International Airport
    "KEYW": "EYW",  # medium_airport | Key West International Airport
    "KFAF": "FAF",  # medium_airport | Felker Army Air Field
    "KFAR": "FAR",  # medium_airport | Hector International Airport
    "KFAT": "FAT",  # large_airport | Fresno Yosemite International Airport
    "KFAY": "FAY",  # medium_airport | Fayetteville Regional Airport - Grannis Field
    "KFBG": "FBG",  # medium_airport | Simmons Army Air Field
    "KFCS": "FCS",  # medium_airport | Butts AAF (Fort Carson) Air Field
    "KFDY": "FDY",  # medium_airport | Findlay Airport
    "KFFO": "FFO",  # medium_airport | Wright-Patterson Air Force Base
    "KFHR": "FRD",  # medium_airport | Friday Harbor Airport
    "KFHU": "FHU",  # medium_airport | Sierra Vista Municipal Airport / Libby Army Air Field
    "KFKL": "FKL",  # medium_airport | Venango Regional Airport
    "KFLG": "FLG",  # medium_airport | Flagstaff Pulliam Airport
    "KFLL": "FLL",  # large_airport | Fort Lauderdale Hollywood International Airport
    "KFLO": "FLO",  # medium_airport | Florence Regional Airport
    "KFME": "FME",  # medium_airport | Fort Meade Executive Airport
    "KFMN": "FMN",  # medium_airport | Four Corners Regional Airport
    "KFMY": "FMY",  # medium_airport | Page Field
    "KFNL": "FNL",  # medium_airport | Northern Colorado Regional Airport
    "KFNT": "FNT",  # medium_airport | Bishop International Airport
    "KFOD": "FOD",  # medium_airport | Fort Dodge Regional Airport
    "KFOE": "FOE",  # medium_airport | Topeka Regional Airport
    "KFPR": "FPR",  # medium_airport | Treasure Coast International Airport
    "KFRG": "FRG",  # medium_airport | Republic Airport
    "KFRI": "FRI",  # medium_airport | Marshall Army Air Field
    "KFSD": "FSD",  # medium_airport | Sioux Falls Regional Airport
    "KFSI": "FSI",  # medium_airport | Henry Post Army Air Field
    "KFSM": "FSM",  # medium_airport | Fort Smith Regional Airport
    "KFST": "FST",  # medium_airport | Fort Stockton Pecos County Airport
    "KFTK": "FTK",  # medium_airport | Godman Army Air Field
    "KFTW": "FTW",  # medium_airport | Fort Worth Meacham International Airport
    "KFTY": "FTY",  # medium_airport | Fulton County Airport Brown Field
    "KFWA": "FWA",  # medium_airport | Fort Wayne International Airport
    "KFXE": "FXE",  # medium_airport | Fort Lauderdale Executive Airport
    "KFYV": "FYV",  # medium_airport | Drake Field
    "KGCC": "GCC",  # medium_airport | Northeast Wyoming Regional Airport
    "KGCK": "GCK",  # medium_airport | Garden City Regional Airport
    "KGCN": "GCN",  # medium_airport | Grand Canyon National Park Airport
    "KGDV": "GDV",  # medium_airport | Dawson Community Airport
    "KGEG": "GEG",  # large_airport | Spokane International Airport
    "KGFK": "GFK",  # medium_airport | Grand Forks International Airport
    "KGFL": "GFL",  # medium_airport | Floyd Bennett Memorial Airport
    "KGGG": "GGG",  # medium_airport | East Texas Regional Airport
    "KGGW": "GGW",  # medium_airport | Glasgow Valley County Airport Wokal Field
    "KGJT": "GJT",  # medium_airport | Grand Junction Regional Airport
    "KGLD": "GLD",  # medium_airport | Goodland Municipal Airport
    "KGLH": "GLH",  # medium_airport | Mid Delta Regional Airport
    "KGLS": "GLS",  # medium_airport | Scholes International At Galveston Airport
    "KGMU": "GMU",  # medium_airport | Greenville Downtown Airport
    "KGNV": "GNV",  # medium_airport | Gainesville Regional Airport
    "KGON": "GON",  # medium_airport | Groton New London Airport
    "KGPI": "FCA",  # medium_airport | Glacier Park International Airport
    "KGPT": "GPT",  # medium_airport | Gulfport Biloxi International Airport
    "KGRB": "GRB",  # medium_airport | Austin Straubel International Airport
    "KGRF": "GRF",  # medium_airport | Gray Army Air Field
    "KGRI": "GRI",  # medium_airport | Central Nebraska Regional Airport
    "KGRK": "GRK",  # medium_airport | Killeen Regional Airport / Robert Gray Army Airfield
    "KGRR": "GRR",  # large_airport | Gerald R. Ford International Airport
    "KGSB": "GSB",  # medium_airport | Seymour Johnson Air Force Base
    "KGSO": "GSO",  # large_airport | Piedmont Triad International Airport
    "KGSP": "GSP",  # medium_airport | Greenville-Spartanburg International Airport
    "KGTF": "GTF",  # medium_airport | Great Falls International Airport
    "KGTR": "GTR",  # medium_airport | Golden Triangle Regional Airport
    "KGUC": "GUC",  # medium_airport | Gunnison Crested Butte Regional Airport
    "KGUP": "GUP",  # medium_airport | Gallup Municipal Airport
    "KGUS": "GUS",  # medium_airport | Grissom Air Reserve Base
    "KGUY": "GUY",  # medium_airport | Guymon Municipal Airport
    "KGWO": "GWO",  # medium_airport | Greenwood–Leflore Airport
    "KGYI": "PNX",  # medium_airport | North Texas Regional Airport Perrin Field
    "KGYY": "GYY",  # medium_airport | Gary/Chicago International Airport
    "KHBG": "HBG",  # medium_airport | Hattiesburg Bobby L Chain Municipal Airport
    "KHBR": "HBR",  # medium_airport | Hobart Regional Airport
    "KHDN": "HDN",  # medium_airport | Yampa Valley Airport
    "KHEF": "MNZ",  # medium_airport | Manassas Regional Airport/Harry P. Davis Field
    "KHFD": "HFD",  # medium_airport | Hartford Brainard Airport
    "KHGR": "HGR",  # medium_airport | Hagerstown Regional Richard A Henson Field
    "KHHR": "HHR",  # medium_airport | Jack Northrop Field Hawthorne Municipal Airport
    "KHIB": "HIB",  # medium_airport | Range Regional Airport
    "KHIF": "HIF",  # medium_airport | Hill Air Force Base
    "KHII": "HII",  # medium_airport | Lake Havasu City Airport
    "KHIO": "HIO",  # medium_airport | Portland Hillsboro Airport
    "KHKY": "HKY",  # medium_airport | Hickory Regional Airport
    "KHLG": "HLG",  # medium_airport | Wheeling Ohio County Airport
    "KHLN": "HLN",  # medium_airport | Helena Regional Airport
    "KHMN": "HMN",  # medium_airport | Holloman Air Force Base
    "KHOB": "HOB",  # medium_airport | Lea County Regional Airport
    "KHON": "HON",  # medium_airport | Huron Regional Airport
    "KHOP": "HOP",  # medium_airport | Campbell Army Airfield (Fort Campbell)
    "KHOT": "HOT",  # medium_airport | Memorial Field Airport
    "KHOU": "HOU",  # large_airport | William P. Hobby Airport
    "KHPN": "HPN",  # medium_airport | Westchester County Airport
    "KHQM": "HQM",  # medium_airport | Bowerman Airport
    "KHRL": "HRL",  # medium_airport | Valley International Airport
    "KHRO": "HRO",  # medium_airport | Boone County Airport
    "KHST": "HST",  # medium_airport | Homestead Air Reserve Base
    "KHSV": "HSV",  # medium_airport | Huntsville International Airport
    "KHTS": "HTS",  # medium_airport | Tri-State Airport / Milton J. Ferguson Field
    "KHUA": "HUA",  # medium_airport | Redstone Army Air Field
    "KHUF": "HUF",  # medium_airport | Terre Haute Regional Airport, Hulman Field
    "KHUL": "HUL",  # medium_airport | Houlton International Airport
    "KHUT": "HUT",  # medium_airport | Hutchinson Municipal Airport
    "KHVN": "HVN",  # medium_airport | Tweed New Haven Airport
    "KHVR": "HVR",  # medium_airport | Havre City County Airport
    "KHWO": "HWO",  # medium_airport | North Perry Airport
    "KHXD": "HHH",  # medium_airport | Hilton Head Airport
    "KHYA": "HYA",  # medium_airport | Cape Cod Gateway Airport
    "KHYR": "HYR",  # medium_airport | Sawyer County Airport
    "KHYS": "HYS",  # medium_airport | Hays Regional Airport
    "KHZY": "JFN",  # medium_airport | Northeast Ohio Regional Airport
    "KIAB": "IAB",  # medium_airport | McConnell Air Force Base
    "KIAD": "IAD",  # large_airport | Washington Dulles International Airport
    "KIAG": "IAG",  # medium_airport | Niagara Falls International Airport
    "KIAH": "IAH",  # large_airport | George Bush Intercontinental Airport
    "KICT": "ICT",  # medium_airport | Wichita Dwight D. Eisenhower National Airport
    "KIDA": "IDA",  # medium_airport | Idaho Falls Regional Airport
    "KIFP": "IFP",  # medium_airport | Laughlin Bullhead International Airport
    "KIGM": "IGM",  # medium_airport | Kingman Airport
    "KIKK": "IKK",  # medium_airport | Greater Kankakee Airport
    "KILG": "ILG",  # medium_airport | Wilmington Airport
    "KILM": "ILM",  # medium_airport | Wilmington International Airport
    "KILN": "ILN",  # medium_airport | Wilmington Airpark
    "KIMT": "IMT",  # medium_airport | Ford Airport
    "KIND": "IND",  # large_airport | Indianapolis International Airport
    "KINK": "INK",  # medium_airport | Winkler County Airport
    "KINL": "INL",  # medium_airport | Falls International Airport
    "KINT": "INT",  # medium_airport | Smith Reynolds Airport
    "KINW": "INW",  # medium_airport | Winslow Lindbergh Regional Airport
    "KIPL": "IPL",  # medium_airport | Imperial County Airport
    "KIPT": "IPT",  # medium_airport | Williamsport Regional Airport
    "KIRK": "IRK",  # medium_airport | Kirksville Regional Airport
    "KISM": "ISM",  # medium_airport | Kissimmee Gateway Airport
    "KISO": "ISO",  # medium_airport | Kinston Regional Jetport At Stallings Field
    "KISP": "ISP",  # medium_airport | Long Island MacArthur Airport
    "KITH": "ITH",  # medium_airport | Ithaca Tompkins Regional Airport
    "KIWA": "AZA",  # medium_airport | Mesa Gateway Airport
    "KJAC": "JAC",  # medium_airport | Jackson Hole Airport
    "KJAN": "JAN",  # medium_airport | Jackson-Medgar Wiley Evers International Airport
    "KJAX": "JAX",  # large_airport | Jacksonville International Airport
    "KJBR": "JBR",  # medium_airport | Jonesboro Municipal Airport
    "KJCT": "JCT",  # medium_airport | Kimble County Airport
    "KJFK": "JFK",  # large_airport | John F. Kennedy International Airport
    "KJHW": "JHW",  # medium_airport | Chautauqua County-Jamestown Airport
    "KJLN": "JLN",  # medium_airport | Joplin Regional Airport
    "KJMS": "JMS",  # medium_airport | Jamestown Regional Airport
    "KJQF": "USA",  # medium_airport | Concord-Padgett Regional Airport
    "KJST": "JST",  # medium_airport | John Murtha Johnstown Cambria County Airport
    "KJXN": "JXN",  # medium_airport | Jackson County Airport/Reynolds Field
    "KKLS": "KLS",  # medium_airport | Southwest Washington Regional Airport
    "KLAA": "LAA",  # medium_airport | Southeast Colorado Regional Airport
    "KLAF": "LAF",  # medium_airport | Purdue University Airport
    "KLAL": "LAL",  # medium_airport | Lakeland Linder International Airport
    "KLAN": "LAN",  # medium_airport | Capital Region International Airport
    "KLAR": "LAR",  # medium_airport | Laramie Regional Airport
    "KLAS": "LAS",  # large_airport | Harry Reid International Airport
    "KLAW": "LAW",  # medium_airport | Lawton Fort Sill Regional Airport
    "KLAX": "LAX",  # large_airport | Los Angeles International Airport
    "KLBB": "LBB",  # medium_airport | Lubbock Preston Smith International Airport
    "KLBE": "LBE",  # medium_airport | Arnold Palmer Regional Airport
    "KLBF": "LBF",  # medium_airport | North Platte Regional Airport Lee Bird Field
    "KLBL": "LBL",  # medium_airport | Liberal Mid-America Regional Airport
    "KLBT": "LBT",  # medium_airport | Lumberton Regional Airport
    "KLBX": "LJN",  # medium_airport | Texas Gulf Coast Regional Airport
    "KLCH": "LCH",  # medium_airport | Lake Charles Regional Airport
    "KLCK": "LCK",  # medium_airport | Rickenbacker International Airport
    "KLEB": "LEB",  # medium_airport | Lebanon Municipal Airport
    "KLEE": "LEE",  # medium_airport | Leesburg International Airport
    "KLEX": "LEX",  # medium_airport | Blue Grass Airport
    "KLFI": "LFI",  # medium_airport | Langley Air Force Base
    "KLFK": "LFK",  # medium_airport | Angelina County Airport
    "KLFT": "LFT",  # medium_airport | Lafayette Regional Airport
    "KLGA": "LGA",  # large_airport | LaGuardia Airport
    "KLGB": "LGB",  # large_airport | Long Beach International Airport
    "KLGU": "LGU",  # medium_airport | Logan-Cache Airport
    "KLIT": "LIT",  # medium_airport | Bill & Hillary Clinton National Airport/Adams Field
    "KLMT": "LMT",  # medium_airport | Crater Lake-Klamath Regional Airport
    "KLND": "LND",  # medium_airport | Hunt Field
    "KLNK": "LNK",  # medium_airport | Lincoln Airport
    "KLNS": "LNS",  # medium_airport | Lancaster Airport
    "KLOL": "LOL",  # medium_airport | Derby Field
    "KLOU": "LOU",  # medium_airport | Bowman Field
    "KLOZ": "LOZ",  # medium_airport | London-Corbin Airport/Magee Field
    "KLRD": "LRD",  # medium_airport | Laredo International Airport
    "KLRF": "LRF",  # medium_airport | Little Rock Air Force Base
    "KLRU": "LRU",  # medium_airport | Las Cruces International Airport
    "KLSE": "LSE",  # medium_airport | La Crosse Regional Airport
    "KLSF": "LSF",  # medium_airport | Lawson Army Air Field
    "KLSV": "LSV",  # medium_airport | Nellis Air Force Base
    "KLTS": "LTS",  # medium_airport | Altus Air Force Base
    "KLUF": "LUF",  # medium_airport | Luke Air Force Base
    "KLUK": "LUK",  # medium_airport | Cincinnati Municipal Airport Lunken Field
    "KLVM": "LVM",  # medium_airport | Mission Field
    "KLVS": "LVS",  # medium_airport | Las Vegas Municipal Airport
    "KLWB": "LWB",  # medium_airport | Greenbrier Valley Airport
    "KLWM": "LWM",  # medium_airport | Lawrence Municipal Airport
    "KLWS": "LWS",  # medium_airport | Lewiston Nez Perce County Airport
    "KLWT": "LWT",  # medium_airport | Lewistown Municipal Airport
    "KLYH": "LYH",  # medium_airport | Lynchburg Regional Airport - Preston Glenn Field
    "KMAF": "MAF",  # medium_airport | Midland International Air and Space Port
    "KMBG": "MBG",  # medium_airport | Mobridge Municipal Airport
    "KMBS": "MBS",  # medium_airport | MBS International Airport
    "KMCB": "MCB",  # medium_airport | McComb-Pike County Airport / John E Lewis Field
    "KMCC": "MCC",  # medium_airport | McClellan Airfield
    "KMCE": "MCE",  # medium_airport | Merced Regional Macready Field
    "KMCF": "MCF",  # medium_airport | MacDill Air Force Base
    "KMCI": "MCI",  # large_airport | Kansas City International Airport
    "KMCK": "MCK",  # medium_airport | McCook Ben Nelson Regional Airport
    "KMCN": "MCN",  # medium_airport | Middle Georgia Regional Airport
    "KMCO": "MCO",  # large_airport | Orlando International Airport
    "KMCW": "MCW",  # medium_airport | Mason City Municipal Airport
    "KMDH": "MDH",  # medium_airport | Southern Illinois Airport
    "KMDT": "MDT",  # medium_airport | Harrisburg International Airport
    "KMDW": "MDW",  # large_airport | Chicago Midway International Airport
    "KMEI": "MEI",  # medium_airport | Key Field / Meridian Regional Airport
    "KMEM": "MEM",  # large_airport | Memphis International Airport
    "KMER": "MER",  # medium_airport | Castle Airport
    "KMFD": "MFD",  # medium_airport | Mansfield Lahm Regional Airport
    "KMFE": "MFE",  # medium_airport | McAllen Miller International Airport
    "KMFR": "MFR",  # medium_airport | Rogue Valley International-Medford Airport
    "KMGC": "MGC",  # medium_airport | Michigan City Municipal Airport
    "KMGE": "MGE",  # medium_airport | Dobbins Air Reserve Base
    "KMGM": "MGM",  # medium_airport | Montgomery Regional (Dannelly Field) Airport
    "KMGW": "MGW",  # medium_airport | Morgantown Municipal Airport Walter L. (Bill) Hart Field
    "KMHK": "MHK",  # medium_airport | Manhattan Regional Airport
    "KMHR": "MHR",  # medium_airport | Sacramento Mather Airport
    "KMHT": "MHT",  # medium_airport | Manchester-Boston Regional Airport
    "KMHV": "MHV",  # medium_airport | Mojave Air &  Space Port
    "KMIA": "MIA",  # large_airport | Miami International Airport
    "KMIB": "MIB",  # medium_airport | Minot Air Force Base
    "KMIE": "MIE",  # medium_airport | Delaware County Johnson Field
    "KMIV": "MIV",  # medium_airport | Millville Municipal Airport
    "KMKC": "MKC",  # medium_airport | Charles B. Wheeler Downtown Airport
    "KMKE": "MKE",  # large_airport | General Mitchell International Airport
    "KMKG": "MKG",  # medium_airport | Muskegon County Airport
    "KMKL": "MKL",  # medium_airport | McKellar-Sipes Regional Airport
    "KMLB": "MLB",  # medium_airport | Melbourne Orlando International Airport
    "KMLC": "MLC",  # medium_airport | Mc Alester Regional Airport
    "KMLI": "MLI",  # medium_airport | Quad City International Airport
    "KMLS": "MLS",  # medium_airport | Miles City Airport - Frank Wiley Field
    "KMLU": "MLU",  # medium_airport | Monroe Regional Airport
    "KMMT": "MMT",  # medium_airport | Mc Entire Joint National Guard Base
    "KMMU": "MMU",  # medium_airport | Morristown Municipal Airport
    "KMOB": "MOB",  # medium_airport | Mobile Regional Airport
    "KMOD": "MOD",  # medium_airport | Modesto City Co-Harry Sham Field
    "KMOT": "MOT",  # medium_airport | Minot International Airport
    "KMPV": "MPV",  # medium_airport | Edward F Knapp State Airport
    "KMQY": "MQY",  # medium_airport | Smyrna Airport
    "KMRB": "MRB",  # medium_airport | Eastern WV Regional Airport/Shepherd Field
    "KMRY": "MRY",  # medium_airport | Monterey Regional Airport
    "KMSL": "MSL",  # medium_airport | Northwest Alabama Regional Airport
    "KMSN": "MSN",  # medium_airport | Dane County Regional Truax Field
    "KMSO": "MSO",  # medium_airport | Missoula Montana Airport
    "KMSP": "MSP",  # large_airport | Minneapolis–Saint Paul International Airport / Wold–Chamberlain Field
    "KMSS": "MSS",  # medium_airport | Massena International Airport Richards Field
    "KMSY": "MSY",  # large_airport | Louis Armstrong New Orleans International Airport
    "KMTC": "MTC",  # medium_airport | Selfridge Air National Guard Base Airport
    "KMTH": "MTH",  # medium_airport | Florida Keys Marathon International Airport
    "KMTJ": "MTJ",  # medium_airport | Montrose Regional Airport
    "KMTN": "MTN",  # medium_airport | Martin State Airport
    "KMUI": "MUI",  # medium_airport | Muir Army Air Field (Fort Indiantown Gap) Airport
    "KMUO": "MUO",  # medium_airport | Mountain Home Air Force Base
    "KMWA": "MWA",  # medium_airport | Veterans Airport of Southern Illinois
    "KMWH": "MWH",  # medium_airport | Grant County International Airport
    "KMWL": "MWL",  # medium_airport | Mineral Wells Regional Airport
    "KMXF": "MXF",  # medium_airport | Maxwell Air Force Base
    "KMYL": "MYL",  # medium_airport | McCall Municipal Airport
    "KMYR": "MYR",  # large_airport | Myrtle Beach International Airport
    "KMYV": "MYV",  # medium_airport | Yuba County Airport
    "KNBG": "NBG",  # medium_airport | New Orleans NAS JRB/Alvin Callender Field
    "KNEL": "NEL",  # medium_airport | Lakehurst Maxfield Field Airport
    "KNEW": "NEW",  # medium_airport | Lakefront Airport
    "KNFL": "NFL",  # medium_airport | Fallon Naval Air Station
    "KNFW": "FWH",  # medium_airport | NAS Fort Worth JRB / Carswell Field
    "KNGP": "NGP",  # medium_airport | Naval Air Station Corpus Christi Truax Field
    "KNGU": "NGU",  # medium_airport | Norfolk Naval Station (Chambers Field)
    "KNHK": "NHK",  # medium_airport | Patuxent River Naval Air Station (Trapnell Field)
    "KNIP": "NIP",  # medium_airport | Jacksonville Naval Air Station (Towers Field)
    "KNJK": "NJK",  # medium_airport | El Centro NAF Airport (Vraciu Field)
    "KNKX": "NKX",  # medium_airport | Miramar Marine Corps Air Station - Mitscher Field
    "KNLC": "NLC",  # medium_airport | Lemoore Naval Air Station (Reeves Field) Airport
    "KNPA": "NPA",  # medium_airport | Naval Air Station Pensacola Forrest Sherman Field
    "KNQA": "NQA",  # medium_airport | Millington-Memphis Airport
    "KNQI": "NQI",  # medium_airport | Kingsville Naval Air Station
    "KNQX": "NQX",  # medium_airport | Naval Air Station Key West/Boca Chica Field
    "KNRB": "NRB",  # medium_airport | Naval Station Mayport / Admiral David L McDonald Field
    "KNSE": "NSE",  # medium_airport | Whiting Field Naval Air Station - North
    "KNTD": "NTD",  # medium_airport | Point Mugu Naval Air Station (Naval Base Ventura Co)
    "KNTU": "NTU",  # medium_airport | Oceana Naval Air Station
    "KNUQ": "NUQ",  # medium_airport | Moffett Federal Airfield
    "KNUW": "NUW",  # medium_airport | Whidbey Island Naval Air Station (Ault Field)
    "KNYG": "NYG",  # medium_airport | Quantico Marine Corps Airfield / Turner Field
    "KNYL": "YUM",  # medium_airport | Yuma International Airport / Marine Corps Air Station Yuma
    "KNZY": "NZY",  # medium_airport | North Island Naval Air Station-Halsey Field
    "KOAJ": "OAJ",  # medium_airport | Albert J Ellis Airport
    "KOAK": "OAK",  # large_airport | San Francisco Bay Oakland International Airport
    "KOFF": "OFF",  # medium_airport | Offutt Air Force Base
    "KOFK": "OFK",  # medium_airport | Karl Stefan Memorial Airport
    "KOGB": "OGB",  # medium_airport | Orangeburg Municipal Airport
    "KOGD": "OGD",  # medium_airport | Ogden Hinckley Airport
    "KOGS": "OGS",  # medium_airport | Ogdensburg International Airport
    "KOKB": "OCN",  # medium_airport | Oceanside Municipal Airport
    "KOKC": "OKC",  # large_airport | OKC Will Rogers World Airport
    "KOLF": "OLF",  # medium_airport | L M Clayton Airport
    "KOLM": "OLM",  # medium_airport | Olympia Regional Airport
    "KOLS": "OLS",  # medium_airport | Nogales International Airport
    "KOLU": "OLU",  # medium_airport | Columbus Municipal Airport
    "KOMA": "OMA",  # large_airport | Eppley Airfield
    "KONO": "ONO",  # medium_airport | Ontario Municipal Airport
    "KONP": "ONP",  # medium_airport | Newport Municipal Airport
    "KONT": "ONT",  # large_airport | Ontario International Airport
    "KOPF": "OPF",  # medium_airport | Miami-Opa Locka Executive Airport
    "KOQU": "NCO",  # medium_airport | Quonset State Airport
    "KORD": "ORD",  # large_airport | Chicago O'Hare International Airport
    "KORF": "ORF",  # large_airport | Norfolk International Airport
    "KORH": "ORH",  # medium_airport | Worcester Regional Airport
    "KORL": "ORL",  # medium_airport | Orlando Executive Airport
    "KORS": "ESD",  # medium_airport | Orcas Island Airport
    "KOSH": "OSH",  # medium_airport | Wittman Regional Airport
    "KOSU": "OSU",  # medium_airport | The Ohio State University Airport - Don Scott Field
    "KOTH": "OTH",  # medium_airport | Southwest Oregon Regional Airport
    "KOTM": "OTM",  # medium_airport | Ottumwa Regional Airport
    "KOWB": "OWB",  # medium_airport | Owensboro Daviess County Airport
    "KOWD": "OWD",  # medium_airport | Norwood Memorial Airport
    "KOXB": "OCE",  # medium_airport | Ocean City Municipal Airport
    "KOXR": "OXR",  # medium_airport | Oxnard Airport
    "KOZR": "OZR",  # medium_airport | Cairns AAF (Fort Rucker) Air Field
    "KPAE": "PAE",  # medium_airport | Seattle Paine Field International Airport
    "KPAH": "PAH",  # medium_airport | Barkley Regional Airport
    "KPAM": "PAM",  # medium_airport | Tyndall Air Force Base
    "KPAO": "PAO",  # medium_airport | Palo Alto Airport
    "KPBF": "PBF",  # medium_airport | Pine Bluff Regional Airport, Grider Field
    "KPBG": "PBG",  # medium_airport | Plattsburgh International Airport
    "KPBI": "PBI",  # large_airport | Palm Beach International Airport
    "KPDK": "PDK",  # medium_airport | DeKalb Peachtree Airport
    "KPDT": "PDT",  # medium_airport | Eastern Oregon Regional Airport at Pendleton
    "KPDX": "PDX",  # large_airport | Portland International Airport
    "KPGA": "PGA",  # medium_airport | Page Municipal Airport
    "KPGD": "PGD",  # medium_airport | Punta Gorda Airport
    "KPGV": "PGV",  # medium_airport | Pitt-Greenville Airport
    "KPHF": "PHF",  # medium_airport | Newport News Williamsburg International Airport
    "KPHL": "PHL",  # large_airport | Philadelphia International Airport
    "KPHX": "PHX",  # large_airport | Phoenix Sky Harbor International Airport
    "KPIA": "PIA",  # medium_airport | General Wayne A. Downing Peoria International Airport
    "KPIB": "PIB",  # medium_airport | Hattiesburg Laurel Regional Airport
    "KPIE": "PIE",  # large_airport | St. Petersburg Clearwater International Airport
    "KPIH": "PIH",  # medium_airport | Pocatello Regional Airport
    "KPIR": "PIR",  # medium_airport | Pierre Regional Airport
    "KPIT": "PIT",  # large_airport | Pittsburgh International Airport
    "KPKB": "PKB",  # medium_airport | Mid Ohio Valley Regional Airport
    "KPLN": "PLN",  # medium_airport | Pellston Regional Airport of Emmet County Airport
    "KPMD": "PMD",  # medium_airport | Palmdale Regional Airport / USAF Plant 42 Airport
    "KPNA": "PWY",  # medium_airport | Ralph Wenz Field
    "KPNC": "PNC",  # medium_airport | Ponca City Regional Airport
    "KPNE": "PNE",  # medium_airport | Northeast Philadelphia Airport
    "KPNS": "PNS",  # large_airport | Pensacola International Airport
    "KPOB": "POB",  # medium_airport | Pope Field
    "KPOE": "POE",  # medium_airport | Polk Army Air Field
    "KPOU": "POU",  # medium_airport | Dutchess County Airport
    "KPQI": "PQI",  # medium_airport | Presque Isle International Airport
    "KPRB": "PRB",  # medium_airport | Paso Robles Municipal Airport
    "KPRC": "PRC",  # medium_airport | Prescott Regional Airport - Ernest A. Love Field
    "KPRX": "PRX",  # medium_airport | Cox Field
    "KPSC": "PSC",  # medium_airport | Tri Cities Airport
    "KPSM": "PSM",  # medium_airport | Portsmouth International Airport at Pease
    "KPSP": "PSP",  # large_airport | Palm Springs International Airport
    "KPTK": "PTK",  # medium_airport | Oakland County International Airport
    "KPUB": "PUB",  # medium_airport | Pueblo Memorial Airport
    "KPUW": "PUW",  # medium_airport | Pullman-Moscow Regional Airport
    "KPVD": "PVD",  # large_airport | Rhode Island T. F. Green International Airport
    "KPVU": "PVU",  # medium_airport | Provo Municipal Airport
    "KPWK": "PWK",  # medium_airport | Chicago Executive Airport
    "KPWM": "PWM",  # large_airport | Portland International Jetport
    "KPWT": "PWT",  # medium_airport | Bremerton National Airport
    "KRAL": "RAL",  # medium_airport | Riverside Municipal Airport
    "KRAP": "RAP",  # medium_airport | Rapid City Regional Airport
    "KRBL": "RBL",  # medium_airport | Red Bluff Municipal Airport
    "KRCA": "RCA",  # medium_airport | Ellsworth Air Force Base
    "KRDD": "RDD",  # medium_airport | Redding Municipal Airport
    "KRDG": "RDG",  # medium_airport | Reading Regional Airport (Carl A Spaatz Field)
    "KRDM": "RDM",  # medium_airport | Roberts Field
    "KRDR": "RDR",  # medium_airport | Grand Forks Air Force Base
    "KRDU": "RDU",  # large_airport | Raleigh-Durham International Airport
    "KRFD": "RFD",  # medium_airport | Chicago Rockford International Airport
    "KRHI": "RHI",  # medium_airport | Rhinelander Oneida County Airport
    "KRIC": "RIC",  # large_airport | Richmond International Airport
    "KRIL": "RIL",  # medium_airport | Garfield County Regional Airport
    "KRIV": "RIV",  # medium_airport | March Air Reserve Base
    "KRIW": "RIW",  # medium_airport | Central Wyoming Regional Airport
    "KRKD": "RKD",  # medium_airport | Knox County Regional Airport
    "KRKS": "RKS",  # medium_airport | Southwest Wyoming Regional Airport
    "KRME": "RME",  # medium_airport | Griffiss International Airport
    "KRMG": "RMG",  # medium_airport | Richard B Russell Airport
    "KRND": "RND",  # medium_airport | Randolph Air Force Base
    "KRNH": "RNH",  # medium_airport | New Richmond Regional Airport
    "KRNO": "RNO",  # large_airport | Reno Tahoe International Airport
    "KROA": "ROA",  # medium_airport | Roanoke–Blacksburg Regional Airport
    "KROC": "ROC",  # large_airport | Frederick Douglass Greater Rochester International Airport
    "KROW": "ROW",  # medium_airport | Roswell Air Center Airport
    "KRSL": "RSL",  # medium_airport | Russell Municipal Airport
    "KRST": "RST",  # medium_airport | Rochester International Airport
    "KRSW": "RSW",  # large_airport | Southwest Florida International Airport
    "KRUT": "RUT",  # medium_airport | Rutland - Southern Vermont Regional Airport
    "KRVS": "RVS",  # medium_airport | Tulsa Riverside Airport
    "KRWF": "RWF",  # medium_airport | Redwood Falls Municipal Airport
    "KRWI": "RWI",  # medium_airport | Rocky Mount Wilson Regional Airport
    "KRWL": "RWL",  # medium_airport | Rawlins Municipal Airport/Harvey Field
    "KSAC": "SAC",  # medium_airport | Sacramento Executive Airport
    "KSAF": "SAF",  # medium_airport | Santa Fe Municipal Airport
    "KSAN": "SAN",  # large_airport | San Diego International Airport
    "KSAT": "SAT",  # large_airport | San Antonio International Airport
    "KSAV": "SAV",  # large_airport | Savannah Hilton Head International Airport
    "KSAW": "MQT",  # medium_airport | Marquette/Sawyer International Airport
    "KSBA": "SBA",  # medium_airport | Santa Barbara Municipal Airport
    "KSBD": "SBD",  # large_airport | San Bernardino International Airport
    "KSBN": "SBN",  # medium_airport | South Bend International Airport
    "KSBP": "SBP",  # medium_airport | San Luis County Regional Airport
    "KSBY": "SBY",  # medium_airport | Salisbury Ocean City Wicomico Regional Airport
    "KSCH": "SCH",  # medium_airport | Schenectady County Airport
    "KSCK": "SCK",  # medium_airport | Stockton Metropolitan Airport
    "KSDF": "SDF",  # large_airport | Louisville Muhammad Ali International Airport
    "KSDM": "SDM",  # medium_airport | Brown Field Municipal Airport
    "KSDY": "SDY",  # medium_airport | Sidney - Richland Regional Airport
    "KSEA": "SEA",  # large_airport | Seattle–Tacoma International Airport
    "KSFB": "SFB",  # large_airport | Orlando Sanford International Airport
    "KSFF": "SFF",  # medium_airport | Felts Field
    "KSFO": "SFO",  # large_airport | San Francisco International Airport
    "KSGF": "SGF",  # medium_airport | Springfield Branson National Airport
    "KSGH": "SGH",  # medium_airport | Springfield-Beckley Municipal Airport
    "KSGJ": "UST",  # medium_airport | Northeast Florida Regional Airport
    "KSGR": "SGR",  # medium_airport | Sugar Land Regional Airport
    "KSGU": "SGU",  # medium_airport | St George Regional Airport
    "KSHD": "SHD",  # medium_airport | Shenandoah Valley Regional Airport
    "KSHR": "SHR",  # medium_airport | Sheridan County Airport
    "KSHV": "SHV",  # medium_airport | Shreveport Regional Airport
    "KSJC": "SJC",  # large_airport | Norman Y. Mineta San Jose International Airport
    "KSJT": "SJT",  # medium_airport | San Angelo Regional Mathis Field
    "KSKA": "SKA",  # medium_airport | Fairchild Air Force Base
    "KSKF": "SKF",  # medium_airport | Lackland Air Force Base
    "KSKX": "TSM",  # medium_airport | Taos Regional Airport
    "KSLC": "SLC",  # large_airport | Salt Lake City International Airport
    "KSLE": "SLE",  # medium_airport | Salem-Willamette Valley Airport/McNary Field
    "KSLK": "SLK",  # medium_airport | Adirondack Regional Airport
    "KSLN": "SLN",  # medium_airport | Salina Municipal Airport
    "KSME": "SME",  # medium_airport | Lake Cumberland Regional Airport
    "KSMF": "SMF",  # large_airport | Sacramento International Airport
    "KSMN": "SMN",  # medium_airport | Lemhi County Airport
    "KSMO": "SMO",  # medium_airport | Santa Monica Municipal Airport
    "KSMX": "SMX",  # medium_airport | Santa Maria Public Airport Captain G Allan Hancock Field
    "KSNA": "SNA",  # large_airport | John Wayne Orange County International Airport
    "KSNS": "SNS",  # medium_airport | Salinas Municipal Airport
    "KSNY": "SNY",  # medium_airport | Sidney Municipal Airport Lloyd W Carr Field
    "KSOW": "SOW",  # medium_airport | Show Low Regional Airport
    "KSPI": "SPI",  # medium_airport | Abraham Lincoln Capital Airport
    "KSPS": "SPS",  # medium_airport | Wichita Falls Municipal Airport / Sheppard Air Force Base
    "KSQL": "SQL",  # medium_airport | San Carlos Airport
    "KSRQ": "SRQ",  # large_airport | Sarasota Bradenton International Airport
    "KSRR": "RUI",  # medium_airport | Sierra Blanca Regional Airport
    "KSSC": "SSC",  # medium_airport | Shaw Air Force Base
    "KSSF": "SSF",  # medium_airport | Stinson Municipal Airport
    "KSSI": "SSI",  # medium_airport | St Simons Island Airport
    "KSTC": "STC",  # medium_airport | Saint Cloud Regional Airport
    "KSTJ": "STJ",  # medium_airport | Rosecrans Memorial Airport
    "KSTL": "STL",  # large_airport | St. Louis Lambert International Airport
    "KSTP": "STP",  # medium_airport | Saint Paul Downtown Holman Field
    "KSTS": "STS",  # medium_airport | Charles M. Schulz Sonoma County Airport
    "KSUN": "SUN",  # medium_airport | Friedman Memorial Airport
    "KSUS": "SUS",  # medium_airport | Spirit of St Louis Airport
    "KSUU": "SUU",  # medium_airport | Travis Air Force Base
    "KSUX": "SUX",  # medium_airport | Sioux Gateway Airport / Brigadier General Bud Day Field
    "KSVC": "SVC",  # medium_airport | Grant County Airport
    "KSVN": "SVN",  # medium_airport | Hunter Army Air Field
    "KSWF": "SWF",  # medium_airport | New York Stewart International Airport
    "KSWO": "SWO",  # medium_airport | Stillwater Regional Airport
    "KSYR": "SYR",  # large_airport | Syracuse Hancock International Airport
    "KSZL": "SZL",  # medium_airport | Whiteman Air Force Base
    "KTBN": "TBN",  # medium_airport | Waynesville-St. Robert Regional Airport-Forney Field
    "KTCC": "TCC",  # medium_airport | Tucumcari Municipal Airport
    "KTCL": "TCL",  # medium_airport | Tuscaloosa National Airport
    "KTCM": "TCM",  # medium_airport | McChord Air Force Base
    "KTCS": "TCS",  # medium_airport | Truth or Consequences Municipal Airport
    "KTEB": "TEB",  # medium_airport | Teterboro Airport
    "KTEX": "TEX",  # medium_airport | Telluride Regional Airport
    "KTIK": "TIK",  # medium_airport | Tinker Air Force Base
    "KTIW": "TIW",  # medium_airport | Tacoma Narrows Airport
    "KTIX": "TIX",  # medium_airport | Space Coast Regional Airport
    "KTLH": "TLH",  # medium_airport | Tallahassee International Airport
    "KTMB": "TMB",  # medium_airport | Miami Executive Airport
    "KTOI": "TOI",  # medium_airport | Troy Municipal Airport at N Kenneth Campbell Field
    "KTOL": "TOL",  # medium_airport | Eugene F. Kranz Toledo Express Airport
    "KTOP": "TOP",  # medium_airport | Philip Billard Municipal Airport
    "KTPA": "TPA",  # large_airport | Tampa International Airport
    "KTPH": "TPH",  # medium_airport | Tonopah Airport
    "KTPL": "TPL",  # medium_airport | Draughon Miller Central Texas Regional Airport
    "KTRI": "TRI",  # medium_airport | Tri-Cities Regional TN/VA Airport
    "KTRK": "TKF",  # medium_airport | Truckee Tahoe Airport
    "KTRM": "TRM",  # medium_airport | Jacqueline Cochran Regional Airport
    "KTTD": "TTD",  # medium_airport | Portland Troutdale Airport
    "KTTN": "TTN",  # medium_airport | Trenton Mercer Airport
    "KTUL": "TUL",  # large_airport | Tulsa International Airport
    "KTUP": "TUP",  # medium_airport | Tupelo Regional Airport
    "KTUS": "TUS",  # large_airport | Tucson International Airport
    "KTVC": "TVC",  # medium_airport | Cherry Capital Airport
    "KTVF": "TVF",  # medium_airport | Thief River Falls Regional Airport
    "KTVL": "TVL",  # medium_airport | Lake Tahoe Airport
    "KTWF": "TWF",  # medium_airport | Joslin Field Magic Valley Regional Airport
    "KTXK": "TXK",  # medium_airport | Texarkana Regional Airport (Webb Field)
    "KTYR": "TYR",  # medium_airport | Tyler Pounds Regional Airport
    "KTYS": "TYS",  # large_airport | McGhee Tyson Airport
    "KUIN": "UIN",  # medium_airport | Quincy Regional Airport Baldwin Field
    "KUKI": "UKI",  # medium_airport | Ukiah Municipal Airport
    "KUNV": "SCE",  # medium_airport | State College Regional Airport
    "KUOX": "UOX",  # medium_airport | University Oxford Airport
    "KUTS": "HTV",  # medium_airport | Huntsville Regional Airport
    "KUUU": "NPT",  # medium_airport | Newport State Airport
    "KVAD": "VAD",  # medium_airport | Moody Air Force Base
    "KVBG": "VBG",  # medium_airport | Vandenberg Space Force Base
    "KVCT": "VCT",  # medium_airport | Victoria Regional Airport
    "KVEL": "VEL",  # medium_airport | Vernal Regional Airport
    "KVGT": "VGT",  # medium_airport | North Las Vegas Airport
    "KVIS": "VIS",  # medium_airport | Visalia Municipal Airport
    "KVLD": "VLD",  # medium_airport | Valdosta Regional Airport
    "KVNY": "VNY",  # large_airport | Van Nuys Airport
    "KVOK": "VOK",  # medium_airport | Volk Field
    "KVPS": "VPS",  # medium_airport | Destin-Fort Walton Beach Airport
    "KVPZ": "VPZ",  # medium_airport | Porter County Municipal Airport
    "KVQQ": "VQQ",  # medium_airport | Cecil Airport
    "KVRB": "VRB",  # medium_airport | Vero Beach Regional Airport
    "KVTN": "VTN",  # medium_airport | Miller Field
    "KWJF": "WJF",  # medium_airport | General William J Fox Airfield
    "KWMC": "WMC",  # medium_airport | Winnemucca Municipal Airport
    "KWRB": "WRB",  # medium_airport | Robins Air Force Base
    "KWRI": "WRI",  # medium_airport | Mc Guire Air Force Base
    "KWRL": "WRL",  # medium_airport | Worland Municipal Airport
    "KWST": "WST",  # medium_airport | Westerly State Airport
    "KWWD": "WWD",  # medium_airport | Cape May County Airport
    "KWWR": "WWR",  # medium_airport | West Woodward Airport
    "KWYS": "WYS",  # medium_airport | Yellowstone Airport
    "KXNA": "XNA",  # medium_airport | Northwest Arkansas National Airport
    "KXWA": "XWA",  # medium_airport | Williston Basin International Airport
    "KYIP": "YIP",  # medium_airport | Willow Run Airport
    "KYKM": "YKM",  # medium_airport | Yakima Air Terminal McAllister Field
    "KYKN": "YKN",  # medium_airport | Chan Gurney Municipal Airport
    "KYNG": "YNG",  # medium_airport | Youngstown Warren Regional Airport
    "KZZV": "ZZV",  # medium_airport | Zanesville Municipal Airport
    "LAKU": "KFZ",  # medium_airport | Kukës International Airport
    "LATI": "TIA",  # large_airport | Tirana International Airport Mother Teresa
    "LBBG": "BOJ",  # large_airport | Burgas Airport
    "LBGO": "GOZ",  # medium_airport | Gorna Oryahovitsa Airport
    "LBPD": "PDV",  # large_airport | Plovdiv International Airport
    "LBSF": "SOF",  # large_airport | Sofia Airport
    "LBWN": "VAR",  # large_airport | Varna Airport
    "LCEN": "ECN",  # large_airport | Ercan International Airport
    "LCGK": "GEC",  # medium_airport | Lefkoniko Airport / Geçitkale Air Base
    "LCLK": "LCA",  # large_airport | Larnaca International Airport
    "LCPH": "PFO",  # large_airport | Paphos International Airport
    "LCRA": "AKT",  # medium_airport | RAF Akrotiri
    "LDDU": "DBV",  # large_airport | Dubrovnik Ruđer Bošković Airport
    "LDOS": "OSI",  # medium_airport | Osijek Airport
    "LDPL": "PUY",  # large_airport | Pula Airport
    "LDRI": "RJK",  # large_airport | Rijeka Airport
    "LDSB": "BWK",  # medium_airport | Brač Airport
    "LDSP": "SPU",  # large_airport | Split Saint Jerome Airport
    "LDZA": "ZAG",  # large_airport | Zagreb Franjo Tuđman International Airport
    "LDZD": "ZAD",  # large_airport | Zadar Airport
    "LEAB": "ABC",  # medium_airport | Albacete Airport / Los Llanos Air Base
    "LEAL": "ALC",  # large_airport | Alicante-Elche Miguel Hernández Airport
    "LEAM": "LEI",  # medium_airport | Almería Airport
    "LEAS": "OVD",  # large_airport | Asturias Airport
    "LEBA": "ODB",  # medium_airport | Córdoba Airport
    "LEBB": "BIO",  # large_airport | Bilbao Airport
    "LEBG": "RGS",  # medium_airport | Burgos Airport
    "LEBL": "BCN",  # large_airport | Josep Tarradellas Barcelona-El Prat Airport
    "LEBZ": "BJZ",  # medium_airport | Badajoz Airport
    "LECH": "CDT",  # medium_airport | Castellón-Costa Azahar Airport
    "LECO": "LCG",  # medium_airport | A Coruña Airport
    "LEDA": "ILD",  # medium_airport | Lleida-Alguaire Airport
    "LEGE": "GRO",  # large_airport | Girona-Costa Brava Airport
    "LEGR": "GRX",  # medium_airport | F.G.L. Airport Granada-Jaén Airport
    "LEIB": "IBZ",  # large_airport | Ibiza Airport
    "LEJR": "XRY",  # medium_airport | Jerez Airport
    "LELN": "LEN",  # large_airport | León Int'l Airport
    "LELO": "RJL",  # medium_airport | Logroño-Agoncillo Airport
    "LEMD": "MAD",  # large_airport | Adolfo Suárez Madrid–Barajas Airport
    "LEMG": "AGP",  # large_airport | Málaga-Costa del Sol Airport
    "LEMH": "MAH",  # large_airport | Menorca Airport
    "LEMI": "RMU",  # large_airport | Region of Murcia International Airport
    "LEMO": "OZP",  # medium_airport | Moron Air Base
    "LEPA": "PMI",  # large_airport | Palma de Mallorca Airport
    "LEPP": "PNA",  # medium_airport | Pamplona Airport
    "LERL": "CQM",  # medium_airport | Ciudad Real International Airport
    "LERS": "REU",  # large_airport | Reus Airport
    "LERT": "ROZ",  # medium_airport | Rota Naval Station Airport
    "LESA": "SLM",  # medium_airport | Salamanca Airport
    "LESO": "EAS",  # medium_airport | San Sebastián Airport
    "LEST": "SCQ",  # large_airport | Santiago-Rosalía de Castro Airport
    "LESU": "LEU",  # medium_airport | Pirineus - la Seu d'Urgel Airport
    "LETL": "TEV",  # medium_airport | Teruel Airport
    "LETO": "TOJ",  # medium_airport | Madrid–Torrejón Airport / Torrejón Air Base
    "LEVC": "VLC",  # large_airport | Valencia Airport
    "LEVD": "VLL",  # medium_airport | Valladolid Airport
    "LEVT": "VIT",  # medium_airport | Vitoria Airport
    "LEVX": "VGO",  # medium_airport | Vigo Airport
    "LEXJ": "SDR",  # medium_airport | Seve Ballesteros-Santander Airport
    "LEZG": "ZAZ",  # large_airport | Zaragoza Airport
    "LEZL": "SVQ",  # large_airport | Seville Airport
    "LFAC": "CQF",  # medium_airport | Calais Marck Airport
    "LFAT": "LTQ",  # medium_airport | Le Touquet-Côte d'Opale Airport
    "LFBA": "AGF",  # medium_airport | Agen La Garenne airport
    "LFBD": "BOD",  # large_airport | Bordeaux–Mérignac Airport
    "LFBE": "EGC",  # medium_airport | Bergerac Dordogne-Périgord airport
    "LFBG": "CNG",  # medium_airport | Cognac-Châteaubernard (BA 709) Air Base
    "LFBH": "LRH",  # medium_airport | La Rochelle Île de Ré Airport
    "LFBI": "PIS",  # medium_airport | Poitiers-Biard Airport
    "LFBK": "MCU",  # medium_airport | Montluçon-Guéret Airport
    "LFBL": "LIG",  # medium_airport | Limoges Airport
    "LFBN": "NIT",  # medium_airport | Niort - Marais Poitevin Airport
    "LFBO": "TLS",  # large_airport | Toulouse-Blagnac Airport
    "LFBP": "PUF",  # medium_airport | Pau Pyrénées Airport
    "LFBT": "LDE",  # medium_airport | Tarbes-Lourdes-Pyrénées Airport
    "LFBU": "ANG",  # medium_airport | Angoulême Brie-Champniers airport
    "LFBX": "PGX",  # medium_airport | Périgueux-Bassillac Airport
    "LFBZ": "BIQ",  # medium_airport | Biarritz Pays Basque airport
    "LFCC": "ZAO",  # medium_airport | Cahors Lalbenque airport
    "LFCI": "LBI",  # medium_airport | Albi Le Sequestre airport
    "LFCK": "DCM",  # medium_airport | Castres Mazamet Airport
    "LFCR": "RDZ",  # medium_airport | Rodez–Aveyron Airport
    "LFCY": "RYN",  # medium_airport | Royan-Médis Airport
    "LFDN": "RCO",  # medium_airport | Rochefort-Saint-Agnant (BA 721) Airport
    "LFGA": "CMR",  # medium_airport | Colmar Houssen airport
    "LFGJ": "DLE",  # medium_airport | Dole Tavaux Airport
    "LFHO": "OBS",  # medium_airport | Aubenas-South Ardèche Airport
    "LFJL": "ETZ",  # medium_airport | Metz-Nancy-Lorraine Airport
    "LFJR": "ANE",  # medium_airport | Angers Marcé airport
    "LFKB": "BIA",  # large_airport | Bastia-Poretta International airport
    "LFKC": "CLY",  # medium_airport | Calvi Sainte Catherine Airport
    "LFKF": "FSC",  # large_airport | Figari Sud-Corse Airport
    "LFKJ": "AJA",  # medium_airport | Ajaccio Napoléon Bonaparte airport
    "LFKS": "SOZ",  # medium_airport | Solenzara (BA 126) Air Base
    "LFLA": "AUF",  # medium_airport | Auxerre Branches airport
    "LFLB": "CMF",  # medium_airport | Chambéry Aix les Bains airport
    "LFLC": "CFE",  # large_airport | Clermont-Ferrand Auvergne airport
    "LFLD": "BOU",  # medium_airport | Bourges airport
    "LFLL": "LYS",  # large_airport | Lyon Saint-Exupéry Airport
    "LFLN": "SYT",  # medium_airport | Saint-Yan Airport
    "LFLO": "RNE",  # medium_airport | Roanne-Renaison Airport
    "LFLP": "NCY",  # medium_airport | Annecy Meythet airport
    "LFLS": "GNB",  # medium_airport | Grenoble Alpes Isère Airport
    "LFLU": "VAF",  # medium_airport | Valence-Chabeuil Airport
    "LFLV": "VHY",  # medium_airport | Vichy-Charmeil Airport
    "LFLW": "AUR",  # medium_airport | Aurillac airport
    "LFLX": "CHR",  # medium_airport | Châteauroux Déols airport
    "LFLY": "LYN",  # medium_airport | Lyon Bron Airport
    "LFMD": "CEQ",  # medium_airport | Cannes Mandelieu Airport
    "LFMH": "EBU",  # medium_airport | Saint-Étienne-Bouthéon Airport
    "LFMK": "CCF",  # medium_airport | Carcassonne Salvaza Airport
    "LFML": "MRS",  # large_airport | Marseille Provence Airport
    "LFMN": "NCE",  # large_airport | Nice-Côte d'Azur Airport
    "LFMP": "PGF",  # medium_airport | Perpignan-Rivesaltes (Llabanère) Airport
    "LFMQ": "CTT",  # medium_airport | Le Castellet Airport
    "LFMT": "MPL",  # large_airport | Montpellier-Méditerranée Airport
    "LFMU": "BZR",  # medium_airport | Béziers Vias airport
    "LFMV": "AVN",  # medium_airport | Avignon Caumont airport
    "LFNB": "MEN",  # medium_airport | Mende-Brenoux Airfield
    "LFOB": "BVA",  # large_airport | Beauvais-Tillé airport
    "LFOE": "EVX",  # medium_airport | Évreux-Fauville (BA 105) Air Base
    "LFOH": "LEH",  # medium_airport | Le Havre-Octeville Airport
    "LFOK": "XCR",  # medium_airport | Chalons Vatry airport
    "LFOP": "URO",  # medium_airport | Rouen Vallée de Seine Airport
    "LFOT": "TUF",  # medium_airport | Tours Val de Loire Airport
    "LFOV": "LVA",  # medium_airport | Laval-Entrammes Airport
    "LFPB": "LBG",  # large_airport | Paris-Le Bourget International Airport
    "LFPC": "CSF",  # medium_airport | Creil Air Base
    "LFPG": "CDG",  # large_airport | Charles de Gaulle International Airport
    "LFPN": "TNF",  # medium_airport | Toussus-le-Noble Airport
    "LFPO": "ORY",  # large_airport | Paris-Orly Airport
    "LFPT": "POX",  # medium_airport | Pontoise-Cormeilles Aerodrome
    "LFPV": "VIY",  # medium_airport | Vélizy-Villacoublay Air Base
    "LFQG": "NVS",  # medium_airport | Nevers-Fourchambault Airport
    "LFQQ": "LIL",  # large_airport | Lille Airport
    "LFQT": "HZB",  # medium_airport | Merville-Calonne Airport
    "LFRB": "BES",  # large_airport | Brest Bretagne airport
    "LFRC": "CER",  # medium_airport | Cherbourg Manche airport
    "LFRD": "DNR",  # medium_airport | Dinard Pleurtuit Saint-Malo airport
    "LFRE": "LBY",  # medium_airport | La Baule-Escoublac Airport
    "LFRF": "GFR",  # medium_airport | Granville Airport
    "LFRG": "DOL",  # medium_airport | Deauville Normandie airport
    "LFRH": "LRT",  # medium_airport | Lorient South Brittany (Bretagne Sud) Airport
    "LFRI": "EDM",  # medium_airport | La Roche-sur-Yon Les Ajoncs Airport
    "LFRJ": "LDV",  # medium_airport | Landivisiau Air Base
    "LFRK": "CFR",  # medium_airport | Caen Carpiquet airport
    "LFRM": "LME",  # medium_airport | Le Mans-Arnage Airport
    "LFRN": "RNS",  # medium_airport | Rennes-Saint-Jacques Airport
    "LFRO": "LAI",  # medium_airport | Lannion Airport
    "LFRQ": "UIP",  # medium_airport | Quimper-Cornouaille Airport
    "LFRS": "NTE",  # medium_airport | Nantes Atlantique Airport
    "LFRT": "SBK",  # medium_airport | Saint-Brieuc-Armor Airport
    "LFRU": "MXN",  # medium_airport | Morlaix-Ploujean Airport
    "LFRV": "VNE",  # medium_airport | Vannes-Meucon Airport
    "LFRZ": "SNR",  # medium_airport | Saint-Nazaire-Montoir Airport
    "LFSB": "BSL",  # large_airport | EuroAirport Basel–Mulhouse–Freiburg
    "LFSD": "DIJ",  # medium_airport | Dijon Longvic airport
    "LFSG": "EPL",  # medium_airport | Épinal Mirecourt Airport
    "LFSL": "BVE",  # medium_airport | Brive Souillac airport
    "LFSN": "ENC",  # medium_airport | Nancy-Essey Airport
    "LFST": "SXB",  # large_airport | Strasbourg Airport
    "LFTH": "TLN",  # medium_airport | Toulon-Hyères Airport
    "LFTW": "FNI",  # medium_airport | Nîmes-Arles-Camargue Airport
    "LFVP": "FSP",  # medium_airport | Saint-Pierre Pointe-Blanche Airport
    "LGAD": "PYR",  # medium_airport | Andravida Air Base
    "LGAL": "AXD",  # medium_airport | Alexandroupoli Democritus Airport
    "LGAV": "ATH",  # large_airport | Athens Eleftherios Venizelos International Airport
    "LGBL": "VOL",  # medium_airport | Nea Anchialos National Airport
    "LGHI": "JKH",  # medium_airport | Chios Island National Airport
    "LGIO": "IOA",  # medium_airport | Ioannina King Pyrrhus National Airport
    "LGIR": "HER",  # large_airport | Heraklion International Nikos Kazantzakis Airport
    "LGKF": "EFL",  # medium_airport | Kefallinia Airport
    "LGKL": "KLX",  # medium_airport | Kalamata Airport
    "LGKO": "KGS",  # large_airport | Kos International Airport \"Ippokratis\"
    "LGKP": "AOK",  # medium_airport | Karpathos Airport
    "LGKR": "CFU",  # large_airport | Corfu Ioannis Kapodistrias International Airport
    "LGKV": "KVA",  # large_airport | Kavala Alexander the Great International Airport
    "LGKZ": "KZI",  # medium_airport | Kozani National Airport Filippos
    "LGMK": "JMK",  # medium_airport | Mykonos Island National Airport
    "LGMT": "MJT",  # medium_airport | Mytilene International Airport
    "LGPZ": "PVK",  # medium_airport | Aktion National Airport
    "LGRP": "RHO",  # large_airport | Rhodes International Airport \"Diagoras\"
    "LGRX": "GPA",  # medium_airport | Patras Araxos Agamemnon Airport
    "LGSA": "CHQ",  # large_airport | Chania International Airport
    "LGSK": "JSI",  # medium_airport | Skiathos Island National Airport
    "LGSM": "SMI",  # medium_airport | Samos Airport
    "LGSR": "JTR",  # large_airport | Santorini International Airport
    "LGST": "JSH",  # medium_airport | Sitia Airport
    "LGTS": "SKG",  # large_airport | Thessaloniki Macedonia International Airport
    "LGZA": "ZTH",  # medium_airport | Zakynthos International Airport Dionysios Solomos
    "LHBP": "BUD",  # large_airport | Budapest Liszt Ferenc International Airport
    "LHDC": "DEB",  # large_airport | Debrecen International Airport
    "LHPP": "PEV",  # large_airport | Pécs-Pogány International Airport
    "LHPR": "QGY",  # medium_airport | Győr-Pér Airport
    "LHSM": "SOB",  # medium_airport | Hévíz–Balaton Airport
    "LIBC": "CRV",  # medium_airport | Crotone Sant'Anna Pythagoras Airport
    "LIBD": "BRI",  # large_airport | Bari Karol Wojtyła International Airport
    "LIBF": "FOG",  # medium_airport | Foggia Gino Lisa Airport
    "LIBG": "TAR",  # medium_airport | Taranto-Grottaglie Marcello Arlotta Airport
    "LIBN": "LCC",  # medium_airport | Lecce Galatina Air Base / Galatina Fortunato Cesari Airport
    "LIBP": "PSR",  # large_airport | Abruzzo Airport
    "LIBR": "BDS",  # large_airport | Brindisi Airport
    "LICA": "SUF",  # large_airport | Lamezia Terme Sant'Eufemia International Airport
    "LICB": "CIY",  # medium_airport | Comiso Airport
    "LICC": "CTA",  # large_airport | Catania-Fontanarossa Airport
    "LICD": "LMP",  # medium_airport | Lampedusa Airport
    "LICG": "PNL",  # medium_airport | Pantelleria Airport
    "LICJ": "PMO",  # large_airport | Falcone–Borsellino Airport
    "LICR": "REG",  # medium_airport | Reggio Calabria Airport
    "LICT": "TPS",  # medium_airport | Vincenzo Florio Airport Trapani-Birgi
    "LIEA": "AHO",  # medium_airport | Alghero-Fertilia Airport
    "LIED": "DCI",  # medium_airport | Decimomannu Air Base
    "LIEE": "CAG",  # large_airport | Cagliari Elmas Airport
    "LIEO": "OLB",  # large_airport | Olbia Costa Smeralda Airport
    "LIMC": "MXP",  # large_airport | Milan Malpensa International Airport
    "LIME": "BGY",  # large_airport | Il Caravaggio International Airport
    "LIMF": "TRN",  # large_airport | Turin Airport
    "LIMJ": "GOA",  # large_airport | Genoa Cristoforo Colombo Airport
    "LIML": "LIN",  # large_airport | Milano Linate Airport
    "LIMP": "PMF",  # medium_airport | Parma Airport
    "LIMW": "AOT",  # medium_airport | Aosta Corrado Gex Airport
    "LIMZ": "CUF",  # medium_airport | Cuneo International Airport
    "LIPA": "AVB",  # medium_airport | Aviano Air Base
    "LIPB": "BZO",  # medium_airport | Bolzano Airport
    "LIPE": "BLQ",  # large_airport | Bologna Guglielmo Marconi Airport
    "LIPH": "TSF",  # large_airport | Treviso Airport
    "LIPK": "FRL",  # medium_airport | Forlì-Luigi Ridolfi International Airport
    "LIPO": "VBS",  # medium_airport | Brescia Gabriele d'Annunzio Airport
    "LIPQ": "TRS",  # large_airport | Trieste Airport
    "LIPR": "RMI",  # large_airport | Federico Fellini International Airport
    "LIPX": "VRN",  # large_airport | Verona Villafranca Valerio Catullo Airport
    "LIPY": "AOI",  # medium_airport | Marche Airport
    "LIPZ": "VCE",  # large_airport | Venice Marco Polo Airport
    "LIRA": "CIA",  # large_airport | Ciampino–G. B. Pastine International Airport
    "LIRF": "FCO",  # large_airport | Rome–Fiumicino Leonardo da Vinci International Airport
    "LIRI": "QSR",  # medium_airport | Salerno Costa d'Amalfi Airport
    "LIRJ": "EBA",  # medium_airport | Marina di Campo Airport
    "LIRN": "NAP",  # large_airport | Naples International Airport
    "LIRP": "PSA",  # large_airport | Pisa International Airport
    "LIRQ": "FLR",  # large_airport | Florence Airport, Peretola
    "LIRS": "GRS",  # medium_airport | Grosseto Corrado Baccarini Air Base / Grosseto Airport
    "LIRZ": "PEG",  # large_airport | Perugia San Francesco d'Assisi – Umbria International Airport
    "LJLJ": "LJU",  # large_airport | Ljubljana Jože Pučnik Airport
    "LJMB": "MBX",  # medium_airport | Maribor Edvard Rusjan Airport
    "LJPZ": "POW",  # medium_airport | Portorož Airport
    "LKCS": "JCL",  # large_airport | České Budějovice South Bohemian Airport
    "LKKU": "UHE",  # medium_airport | Kunovice Airport
    "LKKV": "KLV",  # large_airport | Karlovy Vary Airport
    "LKMT": "OSR",  # large_airport | Leoš Janáček Airport Ostrava
    "LKPD": "PED",  # large_airport | Pardubice Airport
    "LKPO": "PRV",  # medium_airport | Přerov Air Base
    "LKPR": "PRG",  # large_airport | Václav Havel Airport Prague
    "LKTB": "BRQ",  # medium_airport | Brno-Tuřany Airport
    "LKVO": "VOD",  # medium_airport | Vodochody Airport
    "LLBG": "TLV",  # large_airport | Ben Gurion International Airport
    "LLER": "ETM",  # large_airport | Ramon International Airport
    "LLHA": "HFA",  # medium_airport | Uri Michaeli Haifa International Airport
    "LLIB": "RPN",  # medium_airport | Rosh Pina Airport
    "LLMZ": "MTZ",  # medium_airport | Bar Yehuda Airfield
    "LLNV": "VTM",  # medium_airport | Nevatim Air Base
    "LMML": "MLA",  # large_airport | Malta International Airport
    "LOWG": "GRZ",  # large_airport | Graz Airport
    "LOWI": "INN",  # large_airport | Innsbruck Airport
    "LOWK": "KLU",  # large_airport | Klagenfurt Airport
    "LOWL": "LNZ",  # large_airport | Linz-Hörsching Airport
    "LOWS": "SZG",  # large_airport | Salzburg Airport
    "LOWW": "VIE",  # large_airport | Vienna International Airport
    "LPAZ": "SMA",  # medium_airport | Santa Maria Airport
    "LPBG": "BGC",  # medium_airport | Bragança Airport
    "LPBJ": "BYJ",  # medium_airport | Beja Airport / Airbase
    "LPCS": "CAT",  # medium_airport | Cascais Airport
    "LPFL": "FLW",  # medium_airport | Flores Airport
    "LPFR": "FAO",  # large_airport | Faro - Gago Coutinho International Airport
    "LPGR": "GRW",  # medium_airport | Graciosa Airport
    "LPHR": "HOR",  # medium_airport | Horta Airport
    "LPLA": "TER",  # medium_airport | Lajes Airport
    "LPMA": "FNC",  # large_airport | Cristiano Ronaldo International Airport
    "LPPD": "PDL",  # large_airport | João Paulo II Airport
    "LPPI": "PIX",  # medium_airport | Pico Airport
    "LPPM": "PRM",  # medium_airport | Portimão Airport
    "LPPR": "OPO",  # large_airport | Francisco de Sá Carneiro Airport
    "LPPS": "PXO",  # medium_airport | Porto Santo Airport
    "LPPT": "LIS",  # large_airport | Lisbon Humberto Delgado Airport
    "LPSJ": "SJZ",  # medium_airport | São Jorge Airport
    "LPVR": "VRL",  # medium_airport | Vila Real Airport
    "LPVZ": "VSE",  # medium_airport | Aerodromo Goncalves Lobato (Viseu Airport)
    "LQBK": "BNX",  # large_airport | Banja Luka International Airport
    "LQMO": "OMO",  # large_airport | Mostar International Airport
    "LQSA": "SJJ",  # large_airport | Sarajevo International Airport
    "LQTZ": "TZL",  # large_airport | Tuzla International Airport
    "LRAR": "ARW",  # medium_airport | Arad International Airport
    "LRBC": "BCM",  # large_airport | Bacău George Enescu International  Airport
    "LRBM": "BAY",  # medium_airport | Maramureș International Airport
    "LRBS": "BBU",  # large_airport | Bucharest Băneasa Aurel Vlaicu International Airport
    "LRBV": "GHV",  # large_airport | Brașov-Ghimbav International Airport
    "LRCK": "CND",  # large_airport | Mihail Kogălniceanu International Airport
    "LRCL": "CLJ",  # large_airport | Avram Iancu Cluj International Airport
    "LRCS": "CSB",  # medium_airport | Caransebeş Airport
    "LRCV": "CRA",  # large_airport | Craiova International Airport
    "LRIA": "IAS",  # large_airport | Iaşi International Airport
    "LROD": "OMR",  # large_airport | Oradea International Airport
    "LROP": "OTP",  # large_airport | Bucharest Henri Coandă International Airport
    "LRSB": "SBZ",  # large_airport | Sibiu International Airport
    "LRSM": "SUJ",  # medium_airport | Satu Mare International Airport
    "LRSV": "SCV",  # large_airport | Suceava Ștefan cel Mare International Airport
    "LRTC": "TCE",  # medium_airport | Tulcea Danube Delta Airport
    "LRTM": "TGM",  # medium_airport | Târgu Mureş Transilvania International Airport
    "LRTR": "TSR",  # large_airport | Timișoara Traian Vuia International Airport
    "LSGG": "GVA",  # large_airport | Geneva International Airport
    "LSGS": "SIR",  # medium_airport | Sion Airport
    "LSME": "EML",  # medium_airport | Emmen Air Base
    "LSMP": "VIP",  # medium_airport | Payerne Air Base
    "LSZA": "LUG",  # medium_airport | Lugano Airport
    "LSZB": "BRN",  # medium_airport | Bern Airport
    "LSZH": "ZRH",  # large_airport | Zürich Airport
    "LSZR": "ACH",  # medium_airport | Sankt Gallen Altenrhein Airport
    "LSZS": "SMV",  # medium_airport | Engadin Airport
    "LTAC": "ESB",  # large_airport | Esenboğa International Airport
    "LTAD": "ANK",  # medium_airport | Etimesgut Air Base
    "LTAF": "ADA",  # large_airport | Adana Şakirpaşa Airport
    "LTAG": "UAB",  # medium_airport | İncirlik Air Base
    "LTAH": "AFY",  # medium_airport | Afyon Air Base
    "LTAI": "AYT",  # large_airport | Antalya International Airport
    "LTAJ": "GZT",  # large_airport | Gaziantep Oğuzeli International Airport
    "LTAL": "KFS",  # medium_airport | Kastamonu Airport
    "LTAN": "KYA",  # large_airport | Konya Airport
    "LTAS": "ONQ",  # medium_airport | Zonguldak Çaycuma Airport
    "LTAT": "MLX",  # medium_airport | Malatya Erhaç Airport
    "LTAU": "ASR",  # large_airport | Kayseri Erkilet International Airport
    "LTAW": "TJK",  # medium_airport | Tokat Airport
    "LTAY": "DNZ",  # medium_airport | Çardak Airport
    "LTAZ": "NAV",  # large_airport | Nevşehir Kapadokya Airport
    "LTBA": "ISL",  # large_airport | İstanbul Atatürk Airport
    "LTBF": "BZI",  # medium_airport | Balıkesir Airport
    "LTBG": "BDM",  # medium_airport | Bandırma Airport
    "LTBH": "CKZ",  # medium_airport | Çanakkale Airport
    "LTBI": "ESK",  # medium_airport | Eskişehir Air Base
    "LTBJ": "ADB",  # large_airport | Adnan Menderes International Airport
    "LTBL": "IGL",  # medium_airport | Çiğli Airbase
    "LTBO": "USQ",  # medium_airport | Uşak Airport
    "LTBQ": "KCO",  # medium_airport | Cengiz Topel Airport
    "LTBR": "YEI",  # medium_airport | Bursa Yenişehir Airport
    "LTBS": "DLM",  # large_airport | Dalaman International Airport
    "LTBU": "TEQ",  # medium_airport | Tekirdağ Çorlu Airport
    "LTBY": "AOE",  # large_airport | Hasan Polatkan Airport
    "LTCA": "EZS",  # medium_airport | Elazığ Airport
    "LTCB": "OGU",  # medium_airport | Ordu–Giresun Airport
    "LTCC": "DIY",  # medium_airport | Diyarbakır Airport
    "LTCD": "ERC",  # medium_airport | Erzincan Airport
    "LTCE": "ERZ",  # medium_airport | Erzurum International Airport
    "LTCF": "KSY",  # medium_airport | Kars Airport
    "LTCG": "TZX",  # medium_airport | Trabzon International Airport
    "LTCI": "VAN",  # medium_airport | Van Ferit Melen Airport
    "LTCJ": "BAL",  # medium_airport | Batman Airport
    "LTCK": "MSR",  # medium_airport | Muş Airport
    "LTCL": "SXZ",  # medium_airport | Siirt Airport
    "LTCM": "NOP",  # medium_airport | Sinop Airport
    "LTCN": "KCM",  # medium_airport | Kahramanmaraş Airport
    "LTCO": "AJI",  # medium_airport | Ağrı Airport
    "LTCP": "ADF",  # medium_airport | Adıyaman Airport
    "LTCR": "MQM",  # medium_airport | Mardin Airport
    "LTCS": "GNY",  # large_airport | Şanlıurfa GAP Airport
    "LTCT": "IGD",  # medium_airport | Iğdır Airport
    "LTCV": "NKT",  # medium_airport | Şırnak Şerafettin Elçi Airport
    "LTCW": "YKO",  # medium_airport | Hakkari Yüksekova Airport
    "LTDA": "HTY",  # medium_airport | Hatay Airport
    "LTDB": "COV",  # large_airport | Çukurova International Airport
    "LTFC": "ISE",  # medium_airport | Süleyman Demirel International Airport
    "LTFD": "EDO",  # large_airport | Balıkesir Koca Seyit Airport
    "LTFE": "BJV",  # large_airport | Milas Bodrum International Airport
    "LTFG": "GZP",  # medium_airport | Gazipaşa-Alanya Airport
    "LTFH": "SZF",  # medium_airport | Samsun-Çarşamba Airport
    "LTFJ": "SAW",  # large_airport | Istanbul Sabiha Gökçen International Airport
    "LTFM": "IST",  # large_airport | İstanbul Airport
    "LTFO": "RZV",  # large_airport | Rize–Artvin Airport
    "LUBL": "BZY",  # medium_airport | Bălți-Leadoveni International Airport
    "LUKK": "RMO",  # large_airport | Chişinău International Airport
    "LWOH": "OHD",  # large_airport | Ohrid St. Paul the Apostle Airport
    "LWSK": "SKP",  # large_airport | Skopje International Airport
    "LXGB": "GIB",  # large_airport | Gibraltar Airport
    "LYBE": "BEG",  # large_airport | Belgrade Nikola Tesla Airport
    "LYBT": "BJY",  # medium_airport | Batajnica Air Base
    "LYKV": "KVO",  # medium_airport | Morava Airport
    "LYNI": "INI",  # large_airport | Niš Constantine the Great Airport
    "LYPG": "TGD",  # large_airport | Podgorica Airport / Podgorica Golubovci Airbase
    "LYTV": "TIV",  # medium_airport | Tivat Airport
    "LYUZ": "UZC",  # medium_airport | Ponikve Airport
    "LZIB": "BTS",  # large_airport | M. R. Štefánik Airport
    "LZKZ": "KSC",  # medium_airport | Košice International Airport
    "LZPP": "PZY",  # medium_airport | Piešťany Airport
    "LZSL": "SLD",  # medium_airport | Sliač Airport
    "LZTT": "TAT",  # medium_airport | Poprad-Tatry Airport
    "LZZI": "ILZ",  # medium_airport | Žilina-Dolný Hričov Airport
    "MBGT": "GDT",  # medium_airport | JAGS McCartney International Airport
    "MBNC": "NCA",  # medium_airport | North Caicos Airport
    "MBPV": "PLS",  # large_airport | Providenciales International Airport
    "MBSC": "XSC",  # medium_airport | South Caicos Airport
    "MDBH": "BRX",  # medium_airport | Maria Montez International Airport
    "MDCR": "CBJ",  # medium_airport | Cabo Rojo Airport
    "MDCY": "AZS",  # medium_airport | Samaná El Catey International Airport
    "MDJB": "JBQ",  # medium_airport | La Isabela International Airport
    "MDLR": "LRM",  # large_airport | Casa De Campo International Airport
    "MDPC": "PUJ",  # large_airport | Punta Cana International Airport
    "MDPP": "POP",  # medium_airport | Gregorio Luperon International Airport
    "MDSD": "SDQ",  # large_airport | Las Américas International Airport
    "MDST": "STI",  # large_airport | Cibao International Airport
    "MGCB": "CBV",  # medium_airport | Coban Airport
    "MGGT": "GUA",  # large_airport | La Aurora International Airport
    "MGPB": "PBR",  # medium_airport | Puerto Barrios Airport
    "MGRB": "RUV",  # medium_airport | Rubelsanto Airport
    "MGRT": "RER",  # medium_airport | Retalhuleu Airport
    "MGSJ": "GSJ",  # medium_airport | San José Airport
    "MGTK": "FRS",  # medium_airport | Mundo Maya International Airport
    "MHLC": "LCE",  # medium_airport | Golosón International Airport
    "MHLM": "SAP",  # large_airport | Ramón Villeda Morales International Airport
    "MHNJ": "GJA",  # medium_airport | La Laguna Airport
    "MHRO": "RTB",  # large_airport | Juan Manuel Gálvez International Airport
    "MHSC": "XPL",  # large_airport | Palmerola International Airport
    "MHTE": "TEA",  # medium_airport | Tela Airport
    "MHTG": "TGU",  # medium_airport | Toncontín Airport
    "MHTJ": "TJI",  # medium_airport | Trujillo Airport
    "MKBS": "OCJ",  # medium_airport | Ian Fleming International Airport
    "MKJP": "KIN",  # large_airport | Norman Manley International Airport
    "MKJS": "MBJ",  # large_airport | Sangster International Airport
    "MKKJ": "POT",  # medium_airport | Ken Jones Airport
    "MKTP": "KTP",  # medium_airport | Tinson Pen Airport
    "MMAA": "ACA",  # large_airport | General Juan N. Álvarez International Airport
    "MMAN": "NTR",  # medium_airport | Del Norte International Airport
    "MMAS": "AGU",  # large_airport | Aguascalientes International Airport
    "MMBT": "HUX",  # large_airport | Bahías de Huatulco International Airport
    "MMCB": "CVJ",  # medium_airport | General Mariano Matamoros International Airport
    "MMCC": "ACN",  # medium_airport | Ciudad Acuña International Airport
    "MMCE": "CME",  # medium_airport | Ciudad del Carmen International Airport
    "MMCL": "CUL",  # large_airport | Bachigualato Federal International Airport
    "MMCM": "CTM",  # medium_airport | Chetumal International Airport
    "MMCN": "CEN",  # medium_airport | Ciudad Obregón International Airport
    "MMCP": "CPE",  # medium_airport | Ingeniero Alberto Acuña Ongay International Airport
    "MMCS": "CJS",  # large_airport | Abraham González International Airport
    "MMCU": "CUU",  # large_airport | General Roberto Fierro Villalobos International Airport
    "MMCV": "CVM",  # medium_airport | General Pedro Jose Mendez International Airport
    "MMCY": "CYW",  # medium_airport | Captain Rogelio Castillo National Airport
    "MMCZ": "CZM",  # large_airport | Cozumel International Airport
    "MMDO": "DGO",  # medium_airport | General Guadalupe Victoria International Airport
    "MMEP": "TPQ",  # medium_airport | Amado Nervo National Airport
    "MMES": "ESE",  # medium_airport | Ensenada International Airport / El Ciprés Air Base
    "MMGL": "GDL",  # large_airport | Guadalajara International Airport
    "MMGM": "GYM",  # medium_airport | General José María Yáñez International Airport
    "MMHO": "HMO",  # large_airport | General Ignacio L. Pesqueira International Airport
    "MMIA": "CLQ",  # medium_airport | Licenciado Miguel de la Madrid International Airport
    "MMIO": "SLW",  # medium_airport | Plan De Guadalupe International Airport
    "MMIT": "IZT",  # medium_airport | General Antonio Cárdenas Rodríguez National Airport / Ixtepec Air Base
    "MMJA": "JAL",  # medium_airport | El Lencero Airport
    "MMLC": "LZC",  # medium_airport | Lázaro Cárdenas Airport
    "MMLM": "LMM",  # medium_airport | Valle del Fuerte International Airport
    "MMLO": "BJX",  # large_airport | Guanajuato International Airport
    "MMLP": "LAP",  # medium_airport | Manuel Márquez de León International Airport
    "MMLT": "LTO",  # large_airport | Loreto International Airport
    "MMMA": "MAM",  # medium_airport | General Servando Canales International Airport
    "MMMD": "MID",  # large_airport | Manuel Crescencio Rejón International Airport
    "MMML": "MXL",  # medium_airport | General Rodolfo Sánchez Taboada International Airport
    "MMMM": "MLM",  # large_airport | General Francisco J. Mujica International Airport
    "MMMT": "MTT",  # medium_airport | Minatitlán/Coatzacoalcos International Airport
    "MMMV": "LOV",  # medium_airport | Monclova International Airport
    "MMMX": "MEX",  # large_airport | Mexico City Benito Juárez International Airport
    "MMMY": "MTY",  # large_airport | Monterrey International Airport
    "MMMZ": "MZT",  # large_airport | General Rafael Buelna International Airport
    "MMNG": "NOG",  # medium_airport | Nogales International Airport
    "MMNL": "NLD",  # medium_airport | Quetzalcóatl International Airport
    "MMOX": "OAX",  # large_airport | Xoxocotlán International Airport
    "MMPA": "PAZ",  # medium_airport | El Tajín National Airport
    "MMPB": "PBC",  # large_airport | Hermanos Serdán International Airport
    "MMPG": "PDS",  # medium_airport | Piedras Negras International Airport
    "MMPN": "UPN",  # medium_airport | Uruapan - Licenciado y General Ignacio Lopez Rayon International Airport
    "MMPR": "PVR",  # large_airport | Puerto Vallarta International Airport
    "MMPS": "PXM",  # medium_airport | Puerto Escondido International Airport
    "MMQT": "QRO",  # large_airport | Querétaro Intercontinental Airport
    "MMRX": "REX",  # medium_airport | General Lucio Blanco International Airport
    "MMSD": "SJD",  # large_airport | Los Cabos International Airport
    "MMSL": "CSW",  # medium_airport | Cabo San Lucas International Airport
    "MMSM": "NLU",  # large_airport | Felipe Ángeles International Airport
    "MMSP": "SLP",  # medium_airport | Ponciano Arriaga International Airport
    "MMTC": "TRC",  # medium_airport | Francisco Sarabia Tinoco International Airport
    "MMTG": "TGZ",  # medium_airport | Angel Albino Corzo International Airport
    "MMTJ": "TIJ",  # large_airport | General Abelardo L. Rodriguez International Airport
    "MMTL": "TQO",  # large_airport | Felipe Carrillo Puerto International Airport Tulum
    "MMTM": "TAM",  # medium_airport | General Francisco Javier Mina International Airport
    "MMTO": "TLC",  # large_airport | Adolfo López Mateos International Airport
    "MMTP": "TAP",  # medium_airport | Tapachula International Airport
    "MMUN": "CUN",  # large_airport | Cancún International Airport
    "MMVA": "VSA",  # large_airport | Carlos Rovirosa Pérez International Airport
    "MMVR": "VER",  # large_airport | General Heriberto Jara International Airport
    "MMZC": "ZCL",  # medium_airport | General Leobardo C. Ruiz International Airport
    "MMZH": "ZIH",  # large_airport | Ixtapa-Zihuatanejo International Airport
    "MMZO": "ZLO",  # medium_airport | Playa de Oro International Airport
    "MNBL": "BEF",  # medium_airport | Bluefields Airport
    "MNMG": "MGA",  # large_airport | Augusto C. Sandino (Managua) International Airport
    "MNPC": "PUZ",  # medium_airport | Puerto Cabezas Airport
    "MPBO": "BOC",  # medium_airport | Bocas del Toro \"Isla Colón\" International Airport
    "MPCE": "CTD",  # medium_airport | Alonso Valderrama Airport
    "MPCH": "CHX",  # medium_airport | Changuinola Captain Manuel Niño International Airport
    "MPDA": "DAV",  # medium_airport | Enrique Malek International Airport
    "MPEJ": "ONX",  # medium_airport | Enrique Adolfo Jimenez Airport
    "MPMG": "PAC",  # medium_airport | Marcos A. Gelabert International Airport
    "MPSA": "SYP",  # medium_airport | Ruben Cantu Airport
    "MPTO": "PTY",  # large_airport | Tocumen International Airport
    "MRAN": "FON",  # medium_airport | La Fortuna Arenal Airport
    "MRBA": "BAI",  # medium_airport | Buenos Aires Airport
    "MRBC": "BCL",  # medium_airport | Barra del Colorado Airport
    "MRCC": "OTR",  # medium_airport | Coto 47 Airport
    "MRGF": "GLF",  # medium_airport | Golfito Airport
    "MRGP": "GPL",  # medium_airport | Guapiles Airport
    "MRLB": "LIR",  # large_airport | Daniel Oduber Quirós International Airport
    "MRLC": "LSL",  # medium_airport | Los Chiles Airport
    "MRLM": "LIO",  # medium_airport | Limón International Airport
    "MRNS": "NOB",  # medium_airport | Nosara Airport
    "MROC": "SJO",  # large_airport | Juan Santamaría International Airport
    "MRPJ": "PJM",  # medium_airport | Puerto Jimenez Airport
    "MRPM": "PMZ",  # medium_airport | Palmar Sur Airport
    "MRPV": "SYQ",  # medium_airport | Tobías Bolaños International Airport
    "MRQP": "XQP",  # medium_airport | Quepos Managua Airport
    "MRUP": "UPL",  # medium_airport | Upala Airport
    "MSLP": "SAL",  # large_airport | El Salvador International Airport Saint Óscar Arnulfo Romero y Galdámez
    "MSSS": "ILS",  # medium_airport | Ilopango International Airport
    "MTCA": "CYA",  # medium_airport | Antoine-Simon International Airport
    "MTCH": "CAP",  # large_airport | Cap Haitien International Airport
    "MTJA": "JAK",  # medium_airport | Jacmel Airport
    "MTJE": "JEE",  # medium_airport | Jérémie Airport
    "MTPP": "PAP",  # large_airport | Toussaint Louverture International Airport
    "MTPX": "PAX",  # medium_airport | Port-de-Paix Airport
    "MUBA": "BCA",  # medium_airport | Gustavo Rizo Airport
    "MUBY": "BYM",  # medium_airport | Carlos Manuel de Cespedes Airport
    "MUCA": "AVI",  # medium_airport | Máximo Gómez Airport
    "MUCC": "CCC",  # medium_airport | Jardines Del Rey Airport
    "MUCF": "CFG",  # medium_airport | Jaime Gonzalez Airport
    "MUCL": "CYO",  # medium_airport | Vilo Acuña International Airport
    "MUCM": "CMW",  # large_airport | Ignacio Agramonte International Airport
    "MUCU": "SCU",  # large_airport | Antonio Maceo International Airport
    "MUGM": "NBW",  # medium_airport | Leeward Point Field
    "MUGT": "GAO",  # medium_airport | Mariana Grajales Airport
    "MUHA": "HAV",  # large_airport | José Martí International Airport
    "MUHG": "HOG",  # large_airport | Frank Pais International Airport
    "MUKW": "VRO",  # medium_airport | Kawama Airport
    "MUMO": "MOA",  # medium_airport | Orestes Acosta Airport
    "MUMZ": "MZO",  # medium_airport | Sierra Maestra International Airport
    "MUNG": "GER",  # medium_airport | Rafael Cabrera Airport
    "MUPB": "UPB",  # medium_airport | Playa Baracoa Airport
    "MUSC": "SNU",  # large_airport | Abel Santamaria International Airport
    "MUSJ": "SNJ",  # medium_airport | San Julián Air Base
    "MUSN": "SZJ",  # medium_airport | Siguanea Airport
    "MUTD": "TND",  # medium_airport | Alberto Delgado Airport
    "MUVR": "VRA",  # large_airport | Juan Gualberto Gomez International Airport
    "MUVT": "VTU",  # medium_airport | Hermanos Ameijeiras Airport
    "MWCB": "CYB",  # medium_airport | Charles Kirkconnell International Airport
    "MWCL": "LYB",  # medium_airport | Edward Bodden Little Cayman Airfield
    "MWCR": "GCM",  # large_airport | Owen Roberts International Airport
    "MYAB": "MAY",  # medium_airport | Clarence A. Bain Airport
    "MYAF": "ASD",  # medium_airport | Andros Town Airport
    "MYAK": "TZN",  # medium_airport | Congo Town Airport
    "MYAM": "MHH",  # medium_airport | Leonard M. Thompson International Airport
    "MYAN": "SAQ",  # medium_airport | San Andros Airport
    "MYAP": "AXP",  # medium_airport | Spring Point Airport
    "MYAT": "TCB",  # medium_airport | Treasure Cay Airport
    "MYBC": "CCZ",  # medium_airport | Chub Cay Airport
    "MYBG": "GHC",  # medium_airport | Great Harbour Cay Airport
    "MYBS": "BIM",  # medium_airport | South Bimini Airport
    "MYCA": "ATC",  # medium_airport | Arthur's Town Airport
    "MYCB": "TBI",  # medium_airport | New Bight Airport
    "MYCI": "CRI",  # medium_airport | Colonel Hill Airport
    "MYEF": "GGT",  # medium_airport | Exuma International Airport
    "MYEH": "ELH",  # medium_airport | North Eleuthera Airport
    "MYEM": "GHB",  # medium_airport | Governor's Harbour Airport
    "MYEN": "NMC",  # medium_airport | Normans Cay Airport
    "MYER": "RSD",  # medium_airport | Rock Sound International Airport
    "MYES": "TYM",  # medium_airport | Staniel Cay Airport
    "MYGF": "FPO",  # large_airport | Grand Bahama International Airport
    "MYIG": "IGA",  # medium_airport | Inagua Airport
    "MYLD": "LGI",  # medium_airport | Deadman's Cay Airport
    "MYLS": "SML",  # medium_airport | Stella Maris Airport
    "MYMM": "MYG",  # medium_airport | Mayaguana Airport
    "MYNN": "NAS",  # large_airport | Lynden Pindling International Airport
    "MYRD": "DCT",  # medium_airport | Duncan Town Airport
    "MYSM": "ZSA",  # large_airport | San Salvador International Airport
    "MZBZ": "BZE",  # large_airport | Philip S. W. Goldson International Airport
    "MZPL": "PLJ",  # medium_airport | Placencia Airport
    "NCRG": "RAR",  # large_airport | Rarotonga International Airport
    "NFFN": "NAN",  # large_airport | Nadi International Airport
    "NFNA": "SUV",  # large_airport | Nausori International Airport
    "NFNL": "LBS",  # medium_airport | Labasa Airport
    "NFTF": "TBU",  # large_airport | Fua'amotu International Airport
    "NFTL": "HPA",  # medium_airport | Lifuka Island Airport
    "NFTV": "VAV",  # large_airport | Vava'u International Airport
    "NGFU": "FUN",  # medium_airport | Funafuti International Airport
    "NGTA": "TRW",  # large_airport | Bonriki International Airport
    "NGTE": "TBF",  # medium_airport | Tabiteuea North Airport
    "NIUE": "IUE",  # medium_airport | Niue International Airport
    "NLWW": "WLS",  # large_airport | Hihifo Airport
    "NSFA": "APW",  # large_airport | Faleolo International Airport
    "NSTU": "PPG",  # large_airport | Pago Pago International Airport
    "NTAA": "PPT",  # large_airport | Fa'a'ā International Airport
    "NTAR": "RUR",  # medium_airport | Rurutu Airport
    "NTAT": "TUB",  # medium_airport | Tubuai Airport
    "NTGA": "AAA",  # medium_airport | Anaa Airport
    "NTGB": "FGU",  # medium_airport | Fangatau Airport
    "NTGC": "TIH",  # medium_airport | Tikehau Airport
    "NTGE": "REA",  # medium_airport | Reao Airport
    "NTGF": "FAV",  # medium_airport | Fakarava Airport
    "NTGI": "XMH",  # medium_airport | Manihi Airport
    "NTGJ": "GMR",  # medium_airport | Totegegie Airport
    "NTGK": "KKR",  # medium_airport | Kaukura Airport
    "NTGM": "MKP",  # medium_airport | Makemo Airport
    "NTGT": "TKP",  # medium_airport | Takapoto Airport
    "NTGU": "AXR",  # medium_airport | Arutua Airport
    "NTGV": "MVT",  # medium_airport | Mataiva Airport
    "NTHE": "AHE",  # medium_airport | Ahe Airport
    "NTKR": "TKX",  # medium_airport | Takaroa Airport
    "NTMD": "NHV",  # medium_airport | Nuku Hiva Airport
    "NTMN": "AUQ",  # medium_airport | Hiva Oa-Atuona Airport
    "NTTB": "BOB",  # medium_airport | Bora Bora Airport
    "NTTG": "RGI",  # medium_airport | Rangiroa Airport
    "NTTH": "HUH",  # medium_airport | Huahine-Fare Airport
    "NTTM": "MOZ",  # medium_airport | Moorea Temae Airport
    "NTTO": "HOI",  # medium_airport | Hao Airport
    "NTTP": "MAU",  # medium_airport | Maupiti Airport
    "NTTR": "RFP",  # medium_airport | Raiatea Airport
    "NVSQ": "ZGU",  # medium_airport | Gaua Island Airport
    "NVSS": "SON",  # medium_airport | Santo Pekoa International Airport
    "NVVV": "VLI",  # large_airport | Bauerfield International Airport
    "NVVW": "TAH",  # medium_airport | Whitegrass Airport
    "NWWA": "TGJ",  # medium_airport | Tiga Airport
    "NWWD": "KNQ",  # medium_airport | Koné Airport
    "NWWE": "ILP",  # medium_airport | Île des Pins Airport
    "NWWL": "LIF",  # medium_airport | Lifou Airport
    "NWWM": "GEA",  # medium_airport | Nouméa Magenta Airport
    "NWWR": "MEE",  # medium_airport | Maré Airport
    "NWWU": "TOU",  # medium_airport | Touho Airport
    "NWWV": "UVE",  # medium_airport | Ouvéa Airport
    "NWWW": "NOU",  # large_airport | La Tontouta International Airport
    "NZAA": "AKL",  # large_airport | Auckland International Airport
    "NZAP": "TUO",  # medium_airport | Taupo Airport
    "NZAR": "AMZ",  # medium_airport | Ardmore Airport
    "NZCH": "CHC",  # large_airport | Christchurch International Airport
    "NZCI": "CHT",  # medium_airport | Inia William Tuuta Memorial Airport
    "NZDN": "DUD",  # medium_airport | Dunedin International Airport
    "NZGS": "GIS",  # medium_airport | Gisborne Airport
    "NZGT": "GTN",  # medium_airport | Glentanner Airport
    "NZHK": "HKK",  # medium_airport | Hokitika Airfield
    "NZHN": "HLZ",  # medium_airport | Hamilton International Airport
    "NZKK": "KKE",  # medium_airport | Kerikeri Airport
    "NZKT": "KAT",  # medium_airport | Kaitaia Airport
    "NZLX": "ALR",  # medium_airport | Alexandra Aerodrome
    "NZMC": "MON",  # medium_airport | Mount Cook Airport
    "NZMO": "TEU",  # medium_airport | Manapouri Airport
    "NZMS": "MRO",  # medium_airport | Hood Airport
    "NZNP": "NPL",  # medium_airport | New Plymouth Airport
    "NZNR": "NPE",  # medium_airport | Hawke's Bay Airport
    "NZNS": "NSN",  # medium_airport | Nelson Airport
    "NZNV": "IVC",  # medium_airport | Invercargill Airport
    "NZOH": "OHA",  # medium_airport | RNZAF Base Ohakea
    "NZOU": "OAM",  # medium_airport | Oamaru Airport
    "NZPM": "PMR",  # medium_airport | Palmerston North Airport
    "NZPP": "PPQ",  # medium_airport | Paraparaumu Airport
    "NZQN": "ZQN",  # large_airport | Queenstown Airport
    "NZRO": "ROT",  # medium_airport | Rotorua Regional Airport
    "NZTG": "TRG",  # medium_airport | Tauranga Airport
    "NZTU": "TIU",  # medium_airport | Timaru Airport
    "NZUK": "TWZ",  # medium_airport | Pukaki Airport
    "NZWB": "BHE",  # medium_airport | Woodbourne Airport
    "NZWF": "WKA",  # medium_airport | Wanaka Airport
    "NZWK": "WHK",  # medium_airport | Whakatāne Airport
    "NZWN": "WLG",  # large_airport | Wellington International Airport
    "NZWO": "WIR",  # medium_airport | Wairoa Airport
    "NZWR": "WRE",  # medium_airport | Whangarei Airport
    "NZWS": "WSZ",  # medium_airport | Westport Airport
    "NZWU": "WAG",  # medium_airport | Wanganui Airport
    "OAHR": "HEA",  # large_airport | Herat - Khwaja Abdullah Ansari International Airport
    "OAIX": "OAI",  # medium_airport | Bagram Airfield
    "OAJL": "JAA",  # medium_airport | Jalalabad Airport
    "OAKB": "KBL",  # large_airport | Kabul International Airport
    "OAKN": "KDH",  # large_airport | Ahmad Shah Baba International Airport
    "OAKS": "KHT",  # medium_airport | Khost International Airport
    "OAMN": "MMZ",  # medium_airport | Maymana Zahiraddin Faryabi Airport
    "OAMS": "MZR",  # large_airport | Mazar-i-Sharif International Airport
    "OAUZ": "UND",  # medium_airport | Kunduz Airport
    "OBBI": "BAH",  # large_airport | Bahrain International Airport
    "OEAB": "AHB",  # large_airport | Abha International Airport
    "OEAH": "HOF",  # large_airport | Al-Ahsa International Airport
    "OEAO": "ULH",  # large_airport | Al-Ula International Airport
    "OEBA": "ABT",  # medium_airport | King Saud Bin Abdulaziz (Al Baha) Airport
    "OEBH": "BHH",  # medium_airport | Bisha Airport
    "OEDF": "DMM",  # large_airport | King Fahd International Airport
    "OEDM": "DWD",  # medium_airport | Dawadmi Domestic Airport
    "OEDR": "DHA",  # large_airport | King Abdulaziz Air Base
    "OEGN": "GIZ",  # medium_airport | Jizan Regional Airport / King Abdullah bin Abdulaziz Airport
    "OEGS": "ELQ",  # large_airport | Prince Naif bin Abdulaziz International Airport
    "OEGT": "URY",  # medium_airport | Gurayat Domestic Airport
    "OEHL": "HAS",  # large_airport | Hail International Airport
    "OEJN": "JED",  # large_airport | King Abdulaziz International Airport
    "OEKK": "KMC",  # medium_airport | King Khaled Military City Airport
    "OEKM": "KMX",  # medium_airport | King Khalid Air Base
    "OEMA": "MED",  # large_airport | Prince Mohammad Bin Abdulaziz Airport
    "OENG": "EAM",  # medium_airport | Najran Domestic Airport
    "OENN": "NUM",  # large_airport | Neom Bay Airport
    "OEPA": "AQI",  # large_airport | Qaisumah–Hafar Al-Batin International Airport
    "OEPS": "AKH",  # medium_airport | Prince Sultan Air Base
    "OERF": "RAH",  # medium_airport | Rafha Domestic Airport
    "OERK": "RUH",  # large_airport | King Khalid International Airport
    "OERR": "RAE",  # medium_airport | Arar Domestic Airport
    "OESH": "SHW",  # medium_airport | Sharurah Domestic Airport
    "OESK": "AJF",  # large_airport | Al-Jawf International Airport
    "OETB": "TUU",  # large_airport | Prince Sultan bin Abdulaziz International Airport
    "OETF": "TIF",  # large_airport | Taif International Airport
    "OETR": "TUI",  # medium_airport | Turaif Domestic Airport
    "OEWD": "WAE",  # medium_airport | Wadi Al Dawasir Domestic Airport
    "OEWJ": "EJH",  # medium_airport | Al Wajh Domestic Airport
    "OEYN": "YNB",  # large_airport | Prince Abdulmohsen Bin Abdulaziz International Airport
    "OIAA": "ABD",  # large_airport | Abadan Ayatollah Jami International Airport
    "OIAD": "DEF",  # medium_airport | Dezful Airport
    "OIAG": "AKW",  # medium_airport | Aghajari Airport
    "OIAH": "GCH",  # medium_airport | Gachsaran Airport
    "OIAI": "QMJ",  # medium_airport | Shahid Asiyaee Airport
    "OIAM": "MRX",  # medium_airport | Mahshahr Airport
    "OIAW": "AWZ",  # large_airport | Qasem Soleimani International Airport
    "OIBA": "AEU",  # medium_airport | Abu Musa Island Airport
    "OIBB": "BUZ",  # medium_airport | Bushehr Airport
    "OIBJ": "KNR",  # medium_airport | Jam Airport
    "OIBK": "KIH",  # large_airport | Kish International Airport
    "OIBL": "BDH",  # medium_airport | Bandar Lengeh International Airport
    "OIBP": "PGU",  # medium_airport | Persian Gulf International Airport
    "OIBQ": "KHK",  # medium_airport | Khark Airport
    "OIBS": "SXI",  # medium_airport | Siri Airport
    "OIBV": "LVP",  # medium_airport | Lavan Airport
    "OICC": "KSH",  # medium_airport | Shahid Ashrafi Esfahani Airport
    "OICI": "IIL",  # medium_airport | Ilam Airport
    "OICK": "KHD",  # medium_airport | Khoram Abad Airport
    "OICS": "SDG",  # medium_airport | Sanandaj Airport
    "OIFK": "KKS",  # medium_airport | Kashan Airport
    "OIFM": "IFN",  # large_airport | Isfahan Shahid Beheshti International Airport
    "OIFS": "CQD",  # medium_airport | Shahrekord Airport
    "OIGG": "RAS",  # medium_airport | Sardar-e-Jangal Airport
    "OIHH": "HDM",  # medium_airport | Hamadan Airport
    "OIHS": "NUJ",  # medium_airport | Nojeh Air Base
    "OIIE": "IKA",  # large_airport | Imam Khomeini International Airport
    "OIII": "THR",  # large_airport | Mehrabad International Airport
    "OIIK": "GZW",  # medium_airport | Qazvin Airport
    "OIIP": "PYK",  # large_airport | Payam International Airport
    "OIKB": "BND",  # large_airport | Bandar Abbas International Airport
    "OIKJ": "JYR",  # medium_airport | Jiroft Airport
    "OIKK": "KER",  # large_airport | Ayatollah Hashemi Rafsanjani International Airport
    "OIKM": "BXR",  # medium_airport | Bam Airport
    "OIKQ": "GSM",  # large_airport | Qeshm International Airport
    "OIKR": "RJN",  # medium_airport | Rafsanjan Airport
    "OIKY": "SYJ",  # medium_airport | Sirjan Airport
    "OIMB": "XBJ",  # large_airport | Birjand International Airport
    "OIMC": "CKT",  # medium_airport | Sarakhs Airport
    "OIMM": "MHD",  # large_airport | Mashhad International Airport
    "OIMN": "BJB",  # medium_airport | Bojnord Airport
    "OIMS": "AFZ",  # medium_airport | Sabzevar National Airport
    "OIMT": "TCX",  # medium_airport | Tabas Airport
    "OING": "GBT",  # medium_airport | Gorgan Airport
    "OINN": "NSH",  # medium_airport | Nowshahr Airport
    "OINR": "RZR",  # medium_airport | Ramsar Airport
    "OINZ": "SRY",  # medium_airport | Sari Dasht-e Naz International Airport
    "OISF": "FAZ",  # medium_airport | Fasa Airport
    "OISL": "LRR",  # medium_airport | Lar Airport
    "OISR": "LFM",  # medium_airport | Lamerd Airport
    "OISS": "SYZ",  # large_airport | Shiraz Shahid Dastghaib International Airport
    "OISY": "YES",  # medium_airport | Yasuj Airport
    "OITL": "ADU",  # medium_airport | Ardabil Airport
    "OITR": "OMH",  # medium_airport | Urmia Airport
    "OITT": "TBZ",  # large_airport | Tabriz International Airport
    "OITU": "IMQ",  # medium_airport | Maku National Airport
    "OITZ": "JWN",  # medium_airport | Zanjan Airport
    "OIYY": "AZD",  # medium_airport | Shahid Sadooghi Airport
    "OIZB": "ACZ",  # medium_airport | Zabol Airport
    "OIZC": "ZBR",  # medium_airport | Chabahar Konarak International Airport
    "OIZH": "ZAH",  # large_airport | Zahedan International Airport
    "OIZI": "IHR",  # medium_airport | Iranshahr Airport
    "OJAI": "AMM",  # large_airport | Queen Alia International Airport
    "OJAM": "ADJ",  # large_airport | Marka International (Amman Civil) Airport
    "OJAQ": "AQJ",  # large_airport | King Hussein International Airport
    "OKAJ": "XIJ",  # medium_airport | Ahmed Al Jaber Air Base
    "OKKK": "KWI",  # large_airport | Kuwait International Airport
    "OLBA": "BEY",  # large_airport | Beirut Rafic Hariri International Airport
    "OLKA": "KYE",  # medium_airport | Rene Mouawad Air Base
    "OMAA": "AUH",  # large_airport | Zayed International Airport
    "OMAD": "AZI",  # large_airport | Al Bateen Executive Airport
    "OMAL": "AAN",  # large_airport | Al Ain International Airport
    "OMAM": "DHF",  # medium_airport | Al Dhafra Air Base
    "OMBY": "XSB",  # medium_airport | Sir Bani Yas Airport
    "OMDB": "DXB",  # large_airport | Dubai International Airport
    "OMDM": "NHD",  # medium_airport | Al Minhad Air Base
    "OMDW": "DWC",  # large_airport | Al Maktoum International Airport
    "OMFJ": "FJR",  # large_airport | Fujairah International Airport
    "OMRK": "RKT",  # large_airport | Ras Al Khaimah International Airport
    "OMSJ": "SHJ",  # large_airport | Sharjah International Airport
    "OOKB": "KHS",  # medium_airport | Khasab Airport
    "OOMA": "MSH",  # medium_airport | RAFO Masirah
    "OOMS": "MCT",  # large_airport | Muscat International Airport
    "OOSA": "SLL",  # large_airport | Salalah International Airport
    "OOSH": "OHS",  # large_airport | Suhar International Airport
    "OOTH": "TTH",  # medium_airport | Thumrait Air Base
    "OPBW": "BHV",  # medium_airport | Bahawalpur Airport
    "OPCH": "CJL",  # medium_airport | Chitral Airport
    "OPDG": "DEA",  # medium_airport | Dera Ghazi Khan Airport
    "OPDI": "DSK",  # medium_airport | Dera Ismael Khan Airport [IN-ACTIVE]
    "OPFA": "LYP",  # large_airport | Faisalabad International Airport
    "OPGD": "GWD",  # large_airport | New Gwadar International Airport
    "OPGT": "GIL",  # medium_airport | Gilgit Airport
    "OPIS": "ISB",  # large_airport | Islamabad International Airport
    "OPJA": "JAG",  # medium_airport | Shahbaz Air Base
    "OPKC": "KHI",  # large_airport | Jinnah International Airport
    "OPLA": "LHE",  # large_airport | Allama Iqbal International Airport
    "OPMA": "XJM",  # medium_airport | Mangla Airport
    "OPMI": "MWD",  # medium_airport | Mianwali Air Base
    "OPMJ": "MJD",  # medium_airport | Moenjodaro Airport
    "OPMS": "ATG",  # medium_airport | Minhas Air Base
    "OPMT": "MUX",  # large_airport | Multan International Airport
    "OPNH": "WNS",  # medium_airport | Shaheed Benazirabad Airport
    "OPPG": "PJG",  # medium_airport | Panjgur Airport
    "OPPI": "PSI",  # medium_airport | Pasni Airport
    "OPPS": "PEW",  # large_airport | Bacha Khan International Airport
    "OPQT": "UET",  # large_airport | Quetta International Airport
    "OPRK": "RYK",  # medium_airport | Shaikh Zaid Airport
    "OPRT": "RAZ",  # medium_airport | Rawalakot Airport
    "OPSD": "KDU",  # large_airport | Skardu International Airport
    "OPSK": "SKZ",  # medium_airport | Begum Nusrat Bhutto International Airport Sukkur
    "OPSN": "SYW",  # medium_airport | Sehwan Sharif Airport
    "OPSR": "SGI",  # medium_airport | Mushaf Air Base
    "OPSS": "SDT",  # medium_airport | Saidu Sharif Airport
    "OPST": "SKT",  # large_airport | Sialkot International Airport
    "OPSU": "SUL",  # medium_airport | Sui Airport
    "OPTU": "TUK",  # large_airport | Turbat International Airport
    "OPZB": "PZH",  # medium_airport | Zhob Airport
    "ORAA": "IQA",  # medium_airport | Al Asad Air Base
    "ORAT": "TQD",  # medium_airport | Al Taqaddum Air Base
    "ORBI": "BGW",  # large_airport | Baghdad International Airport / New Al Muthana Air Base
    "ORBM": "OSM",  # large_airport | Mosul International Airport
    "ORER": "EBL",  # large_airport | Erbil International Airport
    "ORKK": "KIK",  # large_airport | Kirkuk International Airport
    "ORMM": "BSR",  # large_airport | Basra International Airport
    "ORNI": "NJF",  # large_airport | Al Najaf International Airport
    "ORQW": "RQW",  # medium_airport | Qayyarah West Airport
    "ORSU": "ISU",  # medium_airport | Sulaymaniyah International Airport
    "ORTL": "XNH",  # medium_airport | Ali Air Base
    "OSAP": "ALP",  # large_airport | Aleppo International Airport
    "OSDI": "DAM",  # large_airport | Damascus International Airport
    "OSDZ": "DEZ",  # medium_airport | Deir ez-Zor Airport
    "OSKL": "KAC",  # medium_airport | Qamishli International Airport
    "OSLK": "LTK",  # medium_airport | Latakia International Airport
    "OSPR": "PMS",  # medium_airport | Palmyra Airport
    "OTBD": "DIA",  # large_airport | Doha International Airport
    "OTBH": "XJD",  # medium_airport | Al Udeid Air Base
    "OTHH": "DOH",  # large_airport | Hamad International Airport
    "OYAA": "ADE",  # large_airport | Aden International Airport
    "OYAT": "AXK",  # medium_airport | Ataq Airport
    "OYGD": "AAY",  # medium_airport | Al Ghaydah International Airport
    "OYRN": "RIY",  # large_airport | Riyan International Airport
    "OYSN": "SAH",  # large_airport | Sanaa International Airport
    "OYSQ": "SCT",  # medium_airport | Socotra Airport
    "OYSY": "GXF",  # large_airport | Seiyun Hadhramaut International Airport
    "OYTZ": "TAI",  # medium_airport | Taiz International Airport
    "PAAQ": "PAQ",  # medium_airport | Warren \"Bud\" Woods Palmer Municipal Airport
    "PABA": "BTI",  # medium_airport | Barter Island Long Range Radar Station Airport
    "PABE": "BET",  # medium_airport | Bethel Airport
    "PABI": "BIG",  # medium_airport | Allen Army Airfield
    "PABR": "BRW",  # medium_airport | Wiley Post Will Rogers Memorial Airport
    "PACD": "CDB",  # medium_airport | Cold Bay Airport
    "PACV": "CDV",  # medium_airport | Merle K (Mudhole) Smith Airport
    "PACZ": "CZF",  # medium_airport | Cape Romanzof LRRS Airport
    "PADE": "DRG",  # medium_airport | Deering Airport
    "PADK": "ADK",  # medium_airport | Adak Airport
    "PADL": "DLG",  # medium_airport | Dillingham Airport
    "PADQ": "ADQ",  # medium_airport | Kodiak Airport
    "PADU": "DUT",  # medium_airport | Tom Madsen (Dutch Harbor) Airport
    "PAED": "EDF",  # medium_airport | Elmendorf Air Force Base
    "PAEH": "EHM",  # medium_airport | Cape Newenham LRRS Airport
    "PAEI": "EIL",  # medium_airport | Eielson Air Force Base
    "PAEM": "EMK",  # medium_airport | Emmonak Airport
    "PAEN": "ENA",  # medium_airport | Kenai Municipal Airport
    "PAFA": "FAI",  # medium_airport | Fairbanks International Airport
    "PAFB": "FBK",  # medium_airport | Ladd Army Airfield
    "PAFM": "ABL",  # medium_airport | Ambler Airport
    "PAGA": "GAL",  # medium_airport | Edward G. Pitka Sr Airport
    "PAGK": "GKN",  # medium_airport | Gulkana Airport
    "PAGM": "GAM",  # medium_airport | Gambell Airport
    "PAGS": "GST",  # medium_airport | Gustavus Airport
    "PAHC": "HCR",  # medium_airport | Holy Cross Airport
    "PAHL": "HSL",  # medium_airport | Huslia Airport
    "PAHN": "HNS",  # medium_airport | Haines Airport
    "PAHO": "HOM",  # medium_airport | Homer Airport
    "PAII": "EGX",  # medium_airport | Egegik Airport
    "PAIK": "IAN",  # medium_airport | Bob Baker Memorial Airport
    "PAIL": "ILI",  # medium_airport | Iliamna Airport
    "PAIM": "UTO",  # medium_airport | Indian Mountain LRRS Airport
    "PAJN": "JNU",  # medium_airport | Juneau International Airport
    "PAKN": "AKN",  # medium_airport | King Salmon Airport
    "PAKP": "AKP",  # medium_airport | Anaktuvuk Pass Airport
    "PAKT": "KTN",  # medium_airport | Ketchikan International Airport
    "PAKW": "KLW",  # medium_airport | Klawock Airport
    "PALU": "LUR",  # medium_airport | Cape Lisburne LRRS Airport
    "PAMC": "MCG",  # medium_airport | McGrath Airport
    "PAMR": "MRI",  # medium_airport | Merrill Field
    "PAMY": "MYU",  # medium_airport | Mekoryuk Airport
    "PANC": "ANC",  # large_airport | Ted Stevens Anchorage International Airport
    "PANI": "ANI",  # medium_airport | Aniak Airport
    "PANN": "ENN",  # medium_airport | Nenana Municipal Airport
    "PANT": "ANN",  # medium_airport | Annette Island Airport
    "PANV": "ANV",  # medium_airport | Anvik Airport
    "PAOM": "OME",  # medium_airport | Nome Airport
    "PAOR": "ORT",  # medium_airport | Northway Airport
    "PAOT": "OTZ",  # medium_airport | Ralph Wien Memorial Airport
    "PAPB": "STG",  # medium_airport | St George Airport
    "PAPC": "KPC",  # medium_airport | Port Clarence Coast Guard Station
    "PAPG": "PSG",  # medium_airport | Petersburg James A Johnson Airport
    "PAPH": "PTH",  # medium_airport | Port Heiden Airport
    "PAPM": "PTU",  # medium_airport | Platinum Airport
    "PAQT": "NUI",  # medium_airport | Nuiqsut Airport
    "PARC": "ARC",  # medium_airport | Arctic Village Airport
    "PARY": "RBY",  # medium_airport | Ruby Airport
    "PASA": "SVA",  # medium_airport | Savoonga Airport
    "PASC": "SCC",  # medium_airport | Deadhorse Airport
    "PASD": "SDP",  # medium_airport | Sand Point Airport
    "PASI": "SIT",  # medium_airport | Sitka Rocky Gutierrez Airport
    "PASN": "SNP",  # medium_airport | St Paul Island Airport
    "PASV": "SVW",  # medium_airport | Sparrevohn LRRS Airport
    "PASX": "SXQ",  # medium_airport | Soldotna Airport
    "PASY": "SYA",  # medium_airport | Eareckson Air Station
    "PATK": "TKA",  # medium_airport | Talkeetna Airport
    "PATL": "TLJ",  # medium_airport | Tatalina LRRS Airport
    "PATQ": "ATK",  # medium_airport | Atqasuk Edward Burnell Sr Memorial Airport
    "PAUN": "UNK",  # medium_airport | Unalakleet Airport
    "PAVD": "VDZ",  # medium_airport | Valdez Pioneer Field
    "PAWD": "SWD",  # medium_airport | Seward Airport
    "PAWG": "WRG",  # medium_airport | Wrangell Airport
    "PAWI": "AIN",  # medium_airport | Wainwright Airport
    "PAWS": "WWA",  # medium_airport | Wasilla Airport
    "PAYA": "YAK",  # medium_airport | Yakutat Airport
    "PCIS": "CIS",  # medium_airport | Canton Island Airport
    "PFYU": "FYU",  # medium_airport | Fort Yukon Airport
    "PGRO": "ROP",  # large_airport | Rota International Airport
    "PGSN": "SPN",  # large_airport | Saipan International Airport
    "PGUA": "UAM",  # medium_airport | Andersen Air Force Base
    "PGUM": "GUM",  # large_airport | Antonio B. Won Pat International Airport
    "PGWT": "TIQ",  # large_airport | Tinian International Airport
    "PHBK": "BKH",  # medium_airport | Barking Sands Airport
    "PHHN": "HNM",  # medium_airport | Hana Airport
    "PHJH": "JHM",  # medium_airport | Kapalua Airport
    "PHJR": "JRF",  # medium_airport | Kalaeloa Airport
    "PHKO": "KOA",  # large_airport | Ellison Onizuka Kona International Airport at Keāhole
    "PHLI": "LIH",  # large_airport | Lihue Airport
    "PHMK": "MKK",  # medium_airport | Molokai Airport
    "PHMU": "MUE",  # medium_airport | Waimea Kohala Airport
    "PHNG": "NGF",  # medium_airport | Kaneohe Bay MCAS (Marion E. Carl Field) Airport
    "PHNL": "HNL",  # large_airport | Daniel K. Inouye International Airport
    "PHNY": "LNY",  # medium_airport | Lanai Airport
    "PHOG": "OGG",  # large_airport | Kahului International Airport
    "PHTO": "ITO",  # medium_airport | Hilo International Airport
    "PKMJ": "MAJ",  # large_airport | Marshall Islands International Airport
    "PKWA": "KWA",  # medium_airport | Bucholz Army Air Field
    "PLCH": "CXI",  # large_airport | Cassidy International Airport
    "PMDY": "MDY",  # medium_airport | Henderson Field
    "PPIZ": "PIZ",  # medium_airport | Point Lay LRRS Airport
    "PTKK": "TKK",  # large_airport | Chuuk International Airport
    "PTPN": "PNI",  # medium_airport | Pohnpei International Airport
    "PTRO": "ROR",  # large_airport | Roman Tmetuchl International Airport
    "PTSA": "KSA",  # large_airport | Kosrae International Airport
    "PTYA": "YAP",  # large_airport | Yap International Airport
    "PWAK": "AWK",  # medium_airport | Wake Island Airfield
    "RCBS": "KNH",  # medium_airport | Kinmen Airport
    "RCFG": "LZN",  # medium_airport | Matsu Nangan Airport
    "RCFN": "TTT",  # medium_airport | Taitung Airport
    "RCKH": "KHH",  # large_airport | Kaohsiung International Airport
    "RCKU": "CYI",  # medium_airport | Chiayi Airport
    "RCKW": "HCN",  # medium_airport | Hengchun Airport
    "RCLY": "KYD",  # medium_airport | Lanyu Airport
    "RCMQ": "RMQ",  # large_airport | Taichung International Airport / Ching Chuang Kang Air Base
    "RCMT": "MFK",  # medium_airport | Matsu Beigan Airport
    "RCNN": "TNN",  # large_airport | Tainan International Airport / Tainan Air Base
    "RCPO": "HSZ",  # medium_airport | Hsinchu Air Base
    "RCQC": "MZG",  # large_airport | Penghu Magong Airport
    "RCSQ": "PIF",  # medium_airport | Pingtung Air Force Base North
    "RCSS": "TSA",  # large_airport | Taipei Songshan International Airport
    "RCTP": "TPE",  # large_airport | Taiwan Taoyuan International Airport
    "RCYU": "HUN",  # large_airport | Hualien Chiashan Airport
    "RJAA": "NRT",  # large_airport | Narita International Airport
    "RJAF": "MMJ",  # medium_airport | Shinshu-Matsumoto Airport
    "RJAH": "IBR",  # large_airport | Ibaraki Airport
    "RJAW": "IWO",  # medium_airport | Ioto (Iwo Jima) Airbase
    "RJBB": "KIX",  # large_airport | Kansai International Airport
    "RJBD": "SHM",  # medium_airport | Nanki Shirahama Airport
    "RJBE": "UKB",  # large_airport | Kobe Airport
    "RJBT": "TJH",  # medium_airport | Konotori Tajima Airport
    "RJCB": "OBO",  # medium_airport | Tokachi-Obihiro Airport
    "RJCC": "CTS",  # large_airport | New Chitose Airport
    "RJCH": "HKD",  # large_airport | Hakodate Airport
    "RJCK": "KUH",  # medium_airport | Kushiro Airport
    "RJCM": "MMB",  # medium_airport | Memanbetsu Airport
    "RJCN": "SHB",  # medium_airport | Nakashibetsu Airport
    "RJCO": "OKD",  # medium_airport | Sapporo Okadama Airport
    "RJCW": "WKJ",  # medium_airport | Wakkanai Airport
    "RJDA": "AXJ",  # medium_airport | Amakusa Airport
    "RJDB": "IKI",  # medium_airport | Iki Airport
    "RJDC": "UBJ",  # medium_airport | Yamaguchi Ube Airport
    "RJDT": "TSJ",  # medium_airport | Tsushima Airport
    "RJEB": "MBE",  # medium_airport | Monbetsu Airport
    "RJEC": "AKJ",  # medium_airport | Asahikawa Airport
    "RJEO": "OIR",  # medium_airport | Okushiri Airport
    "RJER": "RIS",  # medium_airport | Rishiri Airport
    "RJFC": "KUM",  # medium_airport | Yakushima Airport
    "RJFE": "FUJ",  # medium_airport | Fukue Airport
    "RJFF": "FUK",  # large_airport | Fukuoka Airport
    "RJFG": "TNE",  # medium_airport | New Tanegashima Airport
    "RJFK": "KOJ",  # large_airport | Kagoshima Airport
    "RJFM": "KMI",  # large_airport | Miyazaki Airport
    "RJFO": "OIT",  # medium_airport | Oita Airport
    "RJFR": "KKJ",  # large_airport | Kitakyushu Airport
    "RJFS": "HSG",  # large_airport | Kyushu Saga International Airport
    "RJFT": "KMJ",  # large_airport | Kumamoto Airport
    "RJFU": "NGS",  # large_airport | Nagasaki Airport
    "RJGG": "NGO",  # large_airport | Chubu Centrair International Airport
    "RJKA": "ASJ",  # medium_airport | Amami Airport
    "RJKB": "OKE",  # medium_airport | Okinoerabu Airport
    "RJKI": "KKX",  # medium_airport | Kikai Airport
    "RJKN": "TKN",  # medium_airport | Tokunoshima Airport
    "RJNA": "NKM",  # medium_airport | Nagoya Airport / JASDF Komaki Air Base
    "RJNF": "FKJ",  # medium_airport | Fukui Airport
    "RJNG": "QGU",  # medium_airport | Gifu Airport
    "RJNK": "KMQ",  # large_airport | Komatsu Airport / JASDF Komatsu Air Base
    "RJNO": "OKI",  # medium_airport | Oki Global Geopark Airport
    "RJNS": "FSZ",  # large_airport | Mount Fuji Shizuoka Airport
    "RJNT": "TOY",  # medium_airport | Toyama Kitokito Airport
    "RJNW": "NTQ",  # medium_airport | Noto Satoyama Airport
    "RJOA": "HIJ",  # large_airport | Hiroshima Airport
    "RJOB": "OKJ",  # large_airport | Okayama Momotaro Airport
    "RJOC": "IZO",  # medium_airport | Izumo Enmusubi Airport
    "RJOH": "YGJ",  # medium_airport | Yonago Kitaro Airport / JASDF Miho Air Base
    "RJOI": "IWK",  # medium_airport | Iwakuni Kintaikyo Airport
    "RJOK": "KCZ",  # large_airport | Kochi Ryoma Airport
    "RJOM": "MYJ",  # large_airport | Matsuyama Airport
    "RJOO": "ITM",  # large_airport | Osaka Itami International Airport
    "RJOR": "TTJ",  # medium_airport | Tottori Sand Dunes Conan Airport
    "RJOS": "TKS",  # large_airport | Tokushima Awaodori Airport / JMSDF Tokushima Air Base
    "RJOT": "TAK",  # large_airport | Takamatsu Airport
    "RJOW": "IWJ",  # medium_airport | Iwami Airport
    "RJSA": "AOJ",  # large_airport | Aomori Airport
    "RJSC": "GAJ",  # medium_airport | Yamagata Airport
    "RJSD": "SDS",  # medium_airport | Sado Airport
    "RJSF": "FKS",  # medium_airport | Fukushima Airport
    "RJSH": "HHE",  # medium_airport | JMSDF Hachinohe Air Base / Hachinohe Airport
    "RJSI": "HNA",  # medium_airport | Iwate Hanamaki Airport
    "RJSK": "AXT",  # medium_airport | Akita Airport
    "RJSM": "MSJ",  # medium_airport | Misawa Airport / Misawa Air Base
    "RJSN": "KIJ",  # large_airport | Niigata Airport
    "RJSR": "ONJ",  # medium_airport | Odate Noshiro Airport
    "RJSS": "SDJ",  # large_airport | Sendai Airport
    "RJSY": "SYO",  # medium_airport | Shonai Airport
    "RJTA": "NJA",  # medium_airport | JMSDF Atsugi Air Base / Naval Air Facility Atsugi
    "RJTH": "HAC",  # medium_airport | Hachijojima Airport
    "RJTO": "OIM",  # medium_airport | Oshima Airport
    "RJTQ": "MYE",  # medium_airport | Miyakejima Airport
    "RJTT": "HND",  # large_airport | Tokyo Haneda International Airport
    "RJTY": "OKO",  # medium_airport | Yokota Air Base
    "RKJB": "MWX",  # large_airport | Muan International Airport
    "RKJJ": "KWJ",  # medium_airport | Gwangju Airport
    "RKJK": "KUV",  # medium_airport | Gunsan Airport / Gunsan Air Base
    "RKJY": "RSU",  # medium_airport | Yeosu Airport
    "RKNN": "KAG",  # medium_airport | Gangneung Airport (K-18)
    "RKNW": "WJU",  # medium_airport | Wonju Airport / Hoengseong Air Base (K-38/K-46)
    "RKNY": "YNY",  # large_airport | Yangyang International Airport
    "RKPC": "CJU",  # large_airport | Jeju International Airport
    "RKPD": "JDG",  # medium_airport | Jeongseok Airport
    "RKPK": "PUS",  # large_airport | Gimhae International Airport
    "RKPS": "HIN",  # medium_airport | Sacheon Airport / Sacheon Air Base
    "RKPU": "USN",  # medium_airport | Ulsan Airport
    "RKSI": "ICN",  # large_airport | Incheon International Airport
    "RKSM": "SSN",  # medium_airport | Seoul Air Base (K-16)
    "RKSO": "OSN",  # medium_airport | Osan Air Base
    "RKSS": "GMP",  # large_airport | Gimpo International Airport
    "RKSW": "SWU",  # medium_airport | Suwon Airport
    "RKTH": "KPO",  # medium_airport | Pohang Airport (G-815/K-3)
    "RKTI": "JWO",  # medium_airport | Jungwon Air Base/Chungju Airport
    "RKTN": "TAE",  # large_airport | Daegu International Airport
    "RKTU": "CJJ",  # large_airport | Cheongju International Airport/Cheongju Air Base (K-59/G-513)
    "RKTY": "YEC",  # medium_airport | Yecheon Airbase
    "ROAH": "OKA",  # large_airport | Naha International Airport
    "RODN": "DNA",  # large_airport | Kadena Air Base
    "ROIG": "ISG",  # medium_airport | New Ishigaki Airport
    "ROKJ": "UEO",  # medium_airport | Kumejima Airport
    "ROMD": "MMD",  # medium_airport | Minamidaito Airport
    "ROMY": "MMY",  # medium_airport | Miyako Airport
    "RORE": "IEJ",  # medium_airport | Iejima Airport
    "RORK": "KTD",  # medium_airport | Kitadaito Airport
    "RORS": "SHI",  # medium_airport | Shimojishima Airport
    "RORT": "TRA",  # medium_airport | Tarama Airport
    "RORY": "RNJ",  # medium_airport | Yoron Airport
    "ROYN": "OGN",  # medium_airport | Yonaguni Airport
    "RPLB": "SFS",  # large_airport | Subic Bay International Airport / Naval Air Station Cubi Point
    "RPLC": "CRK",  # large_airport | Clark International Airport / Clark Air Base
    "RPLH": "LLC",  # medium_airport | Cagayan North International Airport
    "RPLI": "LAO",  # large_airport | Laoag International Airport
    "RPLK": "DRP",  # large_airport | Bicol International Airport
    "RPLL": "MNL",  # large_airport | Ninoy Aquino International Airport
    "RPLS": "SGL",  # medium_airport | Danilo Atienza Air Base
    "RPLU": "LBX",  # medium_airport | Lubang Airport
    "RPMA": "AAV",  # medium_airport | Allah Valley Airport
    "RPMC": "CBO",  # medium_airport | Cotabato (Awang) Airport
    "RPMD": "DVO",  # large_airport | Francisco Bangoy International Airport
    "RPME": "BXU",  # medium_airport | Bancasi Airport
    "RPMF": "BPH",  # medium_airport | Bislig Airport
    "RPMG": "DPL",  # medium_airport | Dipolog Airport
    "RPMH": "CGM",  # medium_airport | Camiguin Airport
    "RPMJ": "JOL",  # medium_airport | Jolo Airport
    "RPMN": "TWT",  # medium_airport | Sanga Sanga Airport
    "RPMO": "OZC",  # medium_airport | Labo Airport
    "RPMP": "PAG",  # medium_airport | Pagadian Airport
    "RPMQ": "MXI",  # medium_airport | Mati National Airport
    "RPMR": "GES",  # large_airport | General Santos International Airport
    "RPMS": "SUG",  # medium_airport | Surigao Airport
    "RPMW": "TDG",  # medium_airport | Tandag Airport
    "RPMY": "CGY",  # large_airport | Laguindingan International Airport
    "RPMZ": "ZAM",  # large_airport | Zamboanga International Airport
    "RPSP": "TAG",  # medium_airport | Bohol-Panglao International Airport
    "RPUB": "BAG",  # medium_airport | Loakan Airport
    "RPUD": "DTE",  # medium_airport | Daet Airport
    "RPUH": "SJI",  # medium_airport | San Jose Airport
    "RPUM": "MBO",  # medium_airport | Mamburao Airport
    "RPUN": "WNP",  # medium_airport | Naga Airport
    "RPUO": "BSO",  # medium_airport | Basco Airport
    "RPUR": "BQA",  # medium_airport | Dr. Juan C. Angara Airport
    "RPUS": "SFE",  # medium_airport | San Fernando Airport
    "RPUT": "TUG",  # medium_airport | Tuguegarao Airport
    "RPUV": "VRC",  # medium_airport | Virac Airport
    "RPUW": "MRQ",  # medium_airport | Marinduque Airport
    "RPUY": "CYZ",  # medium_airport | Cauayan Airport
    "RPVA": "TAC",  # medium_airport | Daniel Z. Romualdez Airport
    "RPVB": "BCD",  # large_airport | Bacolod-Silay International Airport
    "RPVC": "CYP",  # medium_airport | Calbayog Airport
    "RPVD": "DGT",  # medium_airport | Sibulan Airport
    "RPVE": "MPH",  # medium_airport | Godofredo P. Ramos Airport
    "RPVF": "CRM",  # medium_airport | Catarman National Airport
    "RPVI": "ILO",  # large_airport | Iloilo International Airport
    "RPVJ": "MBT",  # medium_airport | Moises R. Espinosa Airport
    "RPVK": "KLO",  # large_airport | Kalibo International Airport
    "RPVM": "CEB",  # large_airport | Mactan Cebu International Airport
    "RPVO": "OMC",  # medium_airport | Ormoc Airport
    "RPVP": "PPS",  # large_airport | Puerto Princesa International Airport / PAF Antonio Bautista Air Base
    "RPVR": "RXS",  # medium_airport | Roxas Airport
    "RPVS": "EUQ",  # medium_airport | Evelio Javier Airport
    "RPVU": "TBH",  # medium_airport | Tugdan Airport
    "RPVV": "USU",  # medium_airport | Francisco B. Reyes (Busuanga) Airport
    "SAAC": "COC",  # medium_airport | Comodoro Pierrestegui Airport
    "SAAG": "GHU",  # medium_airport | Gualeguaychu Airport
    "SAAP": "PRA",  # medium_airport | General Urquiza Airport
    "SAAR": "ROS",  # large_airport | Rosario Islas Malvinas International Airport
    "SAAV": "SFN",  # medium_airport | Sauce Viejo Airport
    "SABE": "AEP",  # large_airport | Aeroparque Jorge Newbery
    "SACO": "COR",  # large_airport | Ingeniero Aeronáutico Ambrosio L.V. Taravella International Airport
    "SADL": "LPG",  # medium_airport | La Plata Airport
    "SADP": "EPA",  # medium_airport | El Palomar Airport
    "SAEZ": "EZE",  # large_airport | Ezeiza International Airport - Ministro Pistarini
    "SAHS": "RDS",  # medium_airport | Rincon De Los Sauces Airport
    "SAHZ": "APZ",  # medium_airport | Zapala Airport
    "SAME": "MDZ",  # large_airport | Governor Francisco Gabrielli International Airport
    "SAMM": "LGS",  # medium_airport | Comodoro D.R. Salomón Airport
    "SAMR": "AFA",  # medium_airport | Suboficial Ay Santiago Germano Airport
    "SANC": "CTC",  # medium_airport | Coronel Felipe Varela International Airport
    "SANE": "SDE",  # medium_airport | Vicecomodoro Angel D. La Paz Aragonés Airport
    "SANL": "IRJ",  # medium_airport | Capitan V A Almonacid Airport
    "SANR": "RHD",  # medium_airport | Termas de Río Hondo international Airport
    "SANT": "TUC",  # large_airport | Teniente Benjamín Matienzo International Airport
    "SANU": "UAQ",  # medium_airport | Domingo Faustino Sarmiento Airport
    "SAOC": "RCU",  # medium_airport | Area De Material Airport
    "SAOD": "VDR",  # medium_airport | Villa Dolores Airport
    "SAOR": "VME",  # medium_airport | Villa Reynolds Airport
    "SAOU": "LUQ",  # medium_airport | Brigadier Mayor D Cesar Raul Ojeda Airport
    "SARC": "CNQ",  # medium_airport | Corrientes Airport
    "SARE": "RES",  # large_airport | Resistencia International Airport
    "SARF": "FMA",  # medium_airport | Formosa National Airport
    "SARI": "IGR",  # medium_airport | Cataratas Del Iguazú International Airport
    "SARL": "AOL",  # medium_airport | Paso De Los Libres Airport
    "SARM": "MCS",  # medium_airport | Monte Caseros Airport
    "SARP": "PSS",  # medium_airport | Libertador Gral D Jose De San Martin Airport
    "SASA": "SLA",  # large_airport | Martín Miguel de Güemes International Airport
    "SASJ": "JUJ",  # large_airport | Gobernador Horacio Guzman International Airport
    "SASO": "ORA",  # medium_airport | Orán Airport
    "SAST": "TTG",  # medium_airport | General Enrique Mosconi Airport
    "SATG": "OYA",  # medium_airport | Goya Airport
    "SATR": "RCQ",  # medium_airport | Reconquista Airport
    "SATU": "UZU",  # medium_airport | Curuzu Cuatia Airport
    "SAVB": "EHL",  # medium_airport | El Bolsón Airfield
    "SAVC": "CRD",  # large_airport | General Enrique Mosconi International Airport
    "SAVE": "EQS",  # medium_airport | Esquel Brigadier Antonio Parodi International Airport
    "SAVH": "LHS",  # medium_airport | Las Heras Airport
    "SAVT": "REL",  # medium_airport | Almirante Marco Andres Zar Airport
    "SAVV": "VDM",  # medium_airport | Gobernador Castello Airport
    "SAVY": "PMY",  # medium_airport | El Tehuelche Airport
    "SAWC": "FTE",  # large_airport | El Calafate - Commander Armando Tola International Airport
    "SAWD": "PUD",  # medium_airport | Puerto Deseado Airport
    "SAWE": "RGA",  # medium_airport | Hermes Quijada International Airport
    "SAWG": "RGL",  # large_airport | Piloto Civil Norberto Fernández International Airport
    "SAWH": "USH",  # medium_airport | Ushuaia - Malvinas Argentinas International Airport
    "SAWJ": "ULA",  # medium_airport | Capitan D Daniel Vazquez Airport
    "SAWP": "PMQ",  # medium_airport | Perito Moreno Jalil Hamer Airport
    "SAWU": "RZA",  # medium_airport | Santa Cruz Airport
    "SAZB": "BHI",  # medium_airport | Comandante Espora Airport
    "SAZG": "GPO",  # medium_airport | General Pico Airport
    "SAZH": "OYO",  # medium_airport | Tres Arroyos Airport
    "SAZL": "SST",  # medium_airport | Santa Teresita Airport
    "SAZM": "MDQ",  # medium_airport | Ástor Piazzola International Airport
    "SAZN": "NQN",  # large_airport | Presidente Perón International Airport
    "SAZO": "NEC",  # medium_airport | Necochea Airport
    "SAZP": "PEH",  # medium_airport | Comodoro Pedro Zanni Airport
    "SAZR": "RSA",  # medium_airport | Santa Rosa Airport
    "SAZS": "BRC",  # large_airport | Teniente Luis Candelaria International Airport
    "SAZT": "TDL",  # medium_airport | Héroes de Malvinas Airport
    "SAZV": "VLG",  # medium_airport | Villa Gesell Airport
    "SAZW": "CUT",  # medium_airport | Cutral-Co Airport
    "SAZY": "CPC",  # medium_airport | Aviador C. Campos Airport
    "SBAA": "CDJ",  # medium_airport | Conceição do Araguaia Airport
    "SBAC": "ARX",  # medium_airport | Aracati Dragão do Mar Regional Airport
    "SBAE": "JTC",  # medium_airport | Bauru/Arealva–Moussa Nakhal Tobias State Airport
    "SBAQ": "AQA",  # medium_airport | Araraquara Airport
    "SBAR": "AJU",  # medium_airport | Aracaju - Santa Maria Airport
    "SBAT": "AFL",  # medium_airport | Piloto Osvaldo Marques Dias Airport
    "SBAU": "ARU",  # medium_airport | Araçatuba Airport
    "SBAX": "AAX",  # medium_airport | Romeu Zema Airport
    "SBBE": "BEL",  # large_airport | Val de Cans/Júlio Cezar Ribeiro International Airport
    "SBBG": "BGX",  # medium_airport | Comandante Gustavo Kraemer Airport
    "SBBH": "PLU",  # medium_airport | Pampulha - Carlos Drummond de Andrade Airport
    "SBBI": "BFH",  # medium_airport | Bacacheri Airport
    "SBBR": "BSB",  # large_airport | Presidente Juscelino Kubitschek International Airport
    "SBBT": "BAT",  # medium_airport | Chafei Amsei Airport
    "SBBV": "BVB",  # large_airport | Atlas Brasil Cantanhede International Airport
    "SBBW": "BPG",  # medium_airport | Barra do Garças Airport
    "SBBZ": "BZC",  # medium_airport | Umberto Modiano Airport
    "SBCA": "CAC",  # medium_airport | Coronel Adalberto Mendes da Silva Airport
    "SBCF": "CNF",  # large_airport | Tancredo Neves International Airport
    "SBCG": "CGR",  # medium_airport | Campo Grande Airport
    "SBCH": "XAP",  # medium_airport | Serafin Enoss Bertaso Airport
    "SBCI": "CLN",  # medium_airport | Brig. Lysias Augusto Rodrigues Airport
    "SBCJ": "CKS",  # medium_airport | Carajás Airport
    "SBCM": "CCM",  # medium_airport | Forquilhinha - Criciúma  Airport
    "SBCO": "QNS",  # medium_airport | Canoas Air Force Base
    "SBCP": "CAW",  # medium_airport | Bartolomeu Lisandro Airport
    "SBCR": "CMG",  # medium_airport | Corumbá International Airport
    "SBCT": "CWB",  # large_airport | Curitiba-Afonso Pena International Airport
    "SBCV": "CRQ",  # medium_airport | Caravelas Airport
    "SBCX": "CXJ",  # medium_airport | Hugo Cantergiani Regional Airport
    "SBCY": "CGB",  # large_airport | Várzea Grande–Marechal Rondon International Airport
    "SBCZ": "CZS",  # medium_airport | Cruzeiro do Sul Airport
    "SBDN": "PPB",  # medium_airport | Presidente Prudente Airport
    "SBEG": "MAO",  # large_airport | Eduardo Gomes International Airport
    "SBEK": "JCR",  # medium_airport | Jacareacanga Airport
    "SBFI": "IGU",  # large_airport | Cataratas International Airport
    "SBFL": "FLN",  # large_airport | Hercílio Luz International Airport
    "SBFN": "FEN",  # medium_airport | Fernando de Noronha Airport
    "SBFZ": "FOR",  # large_airport | Pinto Martins International Airport
    "SBGL": "GIG",  # large_airport | Rio Galeão – Tom Jobim International Airport
    "SBGM": "GJM",  # medium_airport | Guajará-Mirim Airport
    "SBGO": "GYN",  # large_airport | Santa Genoveva International Airport
    "SBGR": "GRU",  # large_airport | São Paulo/Guarulhos–Governor André Franco Montoro International Airport
    "SBGV": "GVR",  # medium_airport | Coronel Altino Machado Airport
    "SBGW": "GUJ",  # medium_airport | Edu Chaves Field
    "SBHT": "ATM",  # medium_airport | Altamira Interstate Airport
    "SBIC": "ITA",  # medium_airport | Itacoatiara Airport
    "SBIH": "ITB",  # medium_airport | Itaituba Airport
    "SBIL": "IOS",  # medium_airport | Bahia - Jorge Amado Airport
    "SBIP": "IPN",  # medium_airport | Usiminas Airport
    "SBIZ": "IMP",  # medium_airport | Prefeito Renato Moreira Airport
    "SBJE": "JJD",  # medium_airport | Comandante Ariston Pessoa Airport
    "SBJF": "JDF",  # medium_airport | Francisco de Assis Airport
    "SBJH": "JHF",  # medium_airport | São Paulo Catarina Executive Airport
    "SBJP": "JPA",  # large_airport | Presidente Castro Pinto International Airport
    "SBJR": "RRJ",  # medium_airport | Jacarepaguá - Roberto Marinho Airport
    "SBJV": "JOI",  # medium_airport | Lauro Carneiro de Loyola Airport
    "SBKG": "CPV",  # medium_airport | Presidente João Suassuna Airport
    "SBKP": "VCP",  # large_airport | Viracopos International Airport
    "SBLJ": "LAJ",  # medium_airport | Lages Airport
    "SBLN": "LIP",  # medium_airport | Lins Airport
    "SBLO": "LDB",  # medium_airport | Governor José Richa Airport
    "SBLP": "LAZ",  # medium_airport | Bom Jesus da Lapa Airport
    "SBMA": "MAB",  # medium_airport | João Correa da Rocha Airport
    "SBMC": "MQH",  # medium_airport | Minaçu Airport
    "SBMD": "MEU",  # medium_airport | Monte Dourado - Serra do Areão Airport
    "SBME": "MEA",  # medium_airport | Macaé Benedito Lacerda Airport
    "SBMG": "MGF",  # medium_airport | Regional de Maringá - Sílvio Name Júnior Airport
    "SBMK": "MOC",  # medium_airport | Mário Ribeiro Airport
    "SBML": "MII",  # medium_airport | Frank Miloye Milenkowichi–Marília State Airport
    "SBMN": "PLL",  # medium_airport | Ponta Pelada Airport / Manaus Air Base
    "SBMO": "MCZ",  # large_airport | Zumbi dos Palmares International Airport
    "SBMQ": "MCP",  # medium_airport | Macapá - Alberto Alcolumbre International Airport
    "SBMS": "MVF",  # medium_airport | Dix-Sept Rosado Airport
    "SBMT": "RTE",  # medium_airport | Campo de Marte Airport
    "SBMY": "MNX",  # medium_airport | Manicoré Airport
    "SBNF": "NVT",  # large_airport | Ministro Victor Konder International Airport
    "SBNM": "GEL",  # medium_airport | Santo Ângelo Airport
    "SBOI": "OYK",  # medium_airport | Oiapoque Airport
    "SBPA": "POA",  # large_airport | Porto Alegre-Salgado Filho International Airport
    "SBPB": "PHB",  # medium_airport | Parnaíba - Prefeito Doutor João Silva Filho International Airport
    "SBPC": "POO",  # medium_airport | Poços de Caldas - Embaixador Walther Moreira Salles Airport
    "SBPF": "PFB",  # medium_airport | Lauro Kurtz Airport
    "SBPG": "PGZ",  # medium_airport | Ponta Grossa Airport - Comandante Antonio Amilton Beraldo
    "SBPJ": "PMW",  # medium_airport | Brigadeiro Lysias Rodrigues Airport
    "SBPK": "PET",  # medium_airport | João Simões Lopes Neto International Airport
    "SBPL": "PNZ",  # medium_airport | Senador Nilo Coelho Airport
    "SBPN": "PNB",  # medium_airport | Porto Nacional Airport
    "SBPP": "PMG",  # medium_airport | Ponta Porã Airport
    "SBPS": "BPS",  # large_airport | Porto Seguro International Airport
    "SBPV": "PVH",  # large_airport | Governador Jorge Teixeira de Oliveira International Airport
    "SBRB": "RBR",  # large_airport | Rio Branco-Plácido de Castro International Airport
    "SBRD": "ROO",  # medium_airport | Maestro Marinho Franco Airport
    "SBRF": "REC",  # large_airport | Recife/Guararapes - Gilberto Freyre International Airport
    "SBRJ": "SDU",  # large_airport | Santos Dumont Airport
    "SBRP": "RAO",  # medium_airport | Leite Lopes Airport
    "SBSC": "SNZ",  # medium_airport | Santa Cruz Air Force Base
    "SBSG": "NAT",  # large_airport | Rio Grande do Norte/São Gonçalo do Amarante–Governador Aluízio Alves International Airport
    "SBSJ": "SJK",  # medium_airport | Professor Urbano Ernesto Stumpf Airport
    "SBSL": "SLZ",  # large_airport | Marechal Cunha Machado International Airport
    "SBSM": "RIA",  # medium_airport | Santa Maria Airport
    "SBSN": "STM",  # medium_airport | Santarém - Maestro Wilson Fonseca International Airport
    "SBSP": "CGH",  # large_airport | Congonhas–Deputado Freitas Nobre Airport
    "SBSR": "SJP",  # medium_airport | Prof. Eribelto Manoel Reino State Airport
    "SBST": "SSZ",  # medium_airport | Santos Nero Moura Air Base / Guarujá Airport
    "SBSV": "SSA",  # large_airport | Deputado Luiz Eduardo Magalhães International Airport
    "SBTB": "TMT",  # medium_airport | Trombetas Airport
    "SBTE": "THE",  # medium_airport | Senador Petrônio Portela Airport
    "SBTF": "TFF",  # medium_airport | Tefé Airport
    "SBTK": "TRQ",  # medium_airport | Tarauacá Airport
    "SBTL": "TEC",  # medium_airport | Telêmaco Borba Airport
    "SBTT": "TBT",  # medium_airport | Tabatinga International Airport
    "SBTU": "TUR",  # medium_airport | Tucuruí Airport
    "SBUA": "SJL",  # medium_airport | São Gabriel da Cachoeira Airport
    "SBUF": "PAV",  # medium_airport | Paulo Afonso Airport
    "SBUG": "URG",  # medium_airport | Rubem Berta Airport
    "SBUL": "UDI",  # medium_airport | Ten. Cel. Aviador César Bombonato Airport
    "SBUR": "UBA",  # medium_airport | Mário de Almeida Franco Airport
    "SBVG": "VAG",  # medium_airport | Major Brigadeiro Trompowsky Airport
    "SBVH": "BVH",  # medium_airport | Brigadeiro Camarão Airport
    "SBVT": "VIX",  # large_airport | Eurico de Aguiar Salles International Airport
    "SBYS": "QPS",  # medium_airport | Campo Fontenelle
    "SBZM": "IZA",  # medium_airport | Presidente Itamar Franco Airport
    "SCAR": "ARI",  # medium_airport | Chacalluta International Airport
    "SCAT": "CPO",  # medium_airport | Desierto de Atacama Airport
    "SCBA": "BBA",  # medium_airport | Balmaceda Airport
    "SCBE": "TOQ",  # medium_airport | Barriles Airport
    "SCCC": "CCH",  # medium_airport | Chile Chico Airport
    "SCCF": "CJC",  # medium_airport | El Loa Airport
    "SCCH": "YAI",  # medium_airport | Gral. Bernardo O´Higgins Airport
    "SCCI": "PUQ",  # large_airport | President Carlos Ibáñez International Airport
    "SCCY": "GXQ",  # medium_airport | Teniente Vidal Airport
    "SCDA": "IQQ",  # large_airport | Diego Aracena International Airport
    "SCEL": "SCL",  # large_airport | Comodoro Arturo Merino Benítez International Airport
    "SCES": "ESR",  # medium_airport | Ricardo García Posada Airport
    "SCFA": "ANF",  # large_airport | Andrés Sabella Gálvez International Airport
    "SCFM": "WPR",  # medium_airport | Captain Fuentes Martinez Airport
    "SCGZ": "WPU",  # medium_airport | Guardia Marina Zañartu Airport
    "SCHR": "LGR",  # medium_airport | Cochrane Airport
    "SCIE": "CCP",  # large_airport | Carriel Sur International Airport
    "SCIP": "IPC",  # large_airport | Mataveri International Airport
    "SCJO": "ZOS",  # medium_airport | Cañal Bajo Carlos Hott Siebert Airport
    "SCLL": "VLR",  # medium_airport | Vallenar Airport
    "SCNT": "PNT",  # medium_airport | Lieutenant Julio Gallardo Airport
    "SCQP": "ZCO",  # large_airport | La Araucanía International Airport
    "SCRA": "CNR",  # medium_airport | Chañaral Airport
    "SCSE": "LSC",  # medium_airport | La Florida Airport
    "SCTC": "PZS",  # medium_airport | Maquehue Airport
    "SCTE": "PMC",  # large_airport | El Tepual International Airport
    "SCTL": "TLX",  # medium_airport | Panguilemo Airport
    "SCTN": "WCH",  # medium_airport | Nuevo Chaitén Airport
    "SCTO": "ZIC",  # medium_airport | Victoria Airport
    "SCTT": "TTC",  # medium_airport | Las Breas Airport
    "SCVD": "ZAL",  # medium_airport | Pichoy Airport
    "SCVM": "KNA",  # medium_airport | Viña del Mar Airport
    "SDIY": "FEC",  # medium_airport | João Durval Carneiro Airport
    "SEAM": "ATF",  # medium_airport | Chachoán Regional Airport
    "SECO": "OCC",  # medium_airport | Francisco De Orellana Airport
    "SECU": "CUE",  # medium_airport | Mariscal Lamar Airport
    "SEGS": "GPS",  # medium_airport | Seymour Galapagos Ecological Airport
    "SEGU": "GYE",  # large_airport | José Joaquín de Olmedo International Airport
    "SEJD": "TNW",  # medium_airport | Jumandy Airport
    "SELT": "LTX",  # medium_airport | Cotopaxi International Airport
    "SEMA": "MRR",  # medium_airport | Jose Maria Velasco Ibarra Airport
    "SEMC": "XMS",  # medium_airport | Coronel E Carvajal Airport
    "SEMT": "MEC",  # medium_airport | Eloy Alfaro International Airport
    "SEPV": "PVO",  # medium_airport | Reales Tamarindos Airport
    "SEQM": "UIO",  # large_airport | Mariscal Sucre International Airport
    "SERO": "ETR",  # medium_airport | Santa Rosa - Artillery Colonel Victor Larrea International Airport
    "SESA": "SNC",  # large_airport | General Ulpiano Paez International Airport
    "SETN": "ESM",  # large_airport | Carlos Concha Torres International Airport
    "SETR": "TPC",  # medium_airport | Tarapoa Airport
    "SETU": "TUA",  # medium_airport | Lieutenant Colonel Luis A. Mantilla International Airport
    "SGAS": "ASU",  # large_airport | Silvio Pettirossi International Airport
    "SGAY": "AYO",  # medium_airport | Aeropuerto Nacional Juan de Ayolas
    "SGCO": "CIO",  # medium_airport | Lieutenant Colonel Carmelo Peralta National Airport
    "SGEN": "ENO",  # large_airport | Teniente Ramon A. Ayub Gonzalez International Airport
    "SGES": "AGT",  # large_airport | Guaraní International Airport
    "SGME": "ESG",  # medium_airport | Dr. Luis María Argaña International Airport
    "SGPI": "PIL",  # medium_airport | Aeródromo Don Carlos Miguel Gimenez
    "SGPJ": "PJC",  # medium_airport | Aeropuerto Nacional Dr. Augusto Roberto Fuster
    "SKAP": "API",  # medium_airport | Gomez Nino Apiay Air Base
    "SKAR": "AXM",  # medium_airport | El Eden Airport
    "SKAS": "PUU",  # medium_airport | Tres De Mayo Airport
    "SKBC": "ELB",  # medium_airport | Las Flores Airport
    "SKBG": "BGA",  # medium_airport | Palonegro Airport
    "SKBO": "BOG",  # large_airport | El Dorado International Airport
    "SKBQ": "BAQ",  # large_airport | Ernesto Cortissoz International Airport
    "SKBS": "BSC",  # medium_airport | José Celestino Mutis Airport
    "SKBU": "BUN",  # medium_airport | Gerardo Tobar López Airport
    "SKCC": "CUC",  # medium_airport | Camilo Daza International Airport
    "SKCG": "CTG",  # large_airport | Rafael Nuñez International Airport
    "SKCL": "CLO",  # large_airport | Alfonso Bonilla Aragon International Airport
    "SKCO": "TCO",  # medium_airport | La Florida Airport
    "SKCU": "CAQ",  # medium_airport | Juan H White Airport
    "SKCV": "CVE",  # medium_airport | Coveñas Airport
    "SKCZ": "CZU",  # medium_airport | Las Brujas Airport
    "SKEB": "EBG",  # medium_airport | El Bagre Airport
    "SKEJ": "EJA",  # medium_airport | Yariguíes Airport
    "SKFL": "FLA",  # medium_airport | Gustavo Artunduaga Paredes Airport
    "SKGI": "GIR",  # medium_airport | Santiago Vila Airport
    "SKGO": "CRC",  # medium_airport | Santa Ana Airport
    "SKGP": "GPI",  # medium_airport | Guapi Airport
    "SKIB": "IBE",  # medium_airport | Perales Airport
    "SKIP": "IPI",  # medium_airport | San Luis Airport
    "SKLC": "APO",  # medium_airport | Antonio Roldán Betancur Airport
    "SKLM": "MCJ",  # medium_airport | Jorge Isaac Airport
    "SKLT": "LET",  # medium_airport | Alfredo Vásquez Cobo International Airport
    "SKMD": "EOH",  # medium_airport | Enrique Olaya Herrera Airport
    "SKMG": "MGN",  # medium_airport | Baracoa Airport
    "SKMR": "MTR",  # medium_airport | Los Garzones Airport
    "SKMU": "MVP",  # medium_airport | Fabio Alberto Leon Bentley Airport
    "SKMZ": "MZL",  # medium_airport | La Nubia Airport
    "SKNV": "NVA",  # medium_airport | Benito Salas Airport
    "SKOC": "OCV",  # medium_airport | Aguas Claras Airport
    "SKPC": "PCR",  # medium_airport | German Olano Airport
    "SKPD": "PDA",  # medium_airport | Obando Cesar Gaviria Trujillo Airport
    "SKPE": "PEI",  # medium_airport | Matecaña International Airport
    "SKPI": "PTX",  # medium_airport | Pitalito Airport
    "SKPP": "PPN",  # medium_airport | Guillermo León Valencia Airport
    "SKPQ": "PAL",  # medium_airport | German Olano Air Base
    "SKPS": "PSO",  # medium_airport | Antonio Nariño Airport
    "SKPV": "PVA",  # medium_airport | El Embrujo Airport
    "SKPZ": "PZA",  # medium_airport | Paz de Ariporo Airport
    "SKQU": "MQU",  # medium_airport | Mariquita Airport
    "SKRG": "MDE",  # large_airport | Jose Maria Córdova International Airport
    "SKRH": "RCH",  # medium_airport | Almirante Padilla Airport
    "SKSJ": "SJE",  # medium_airport | Jorge E. Gonzalez Torres Airport
    "SKSM": "SMR",  # medium_airport | Simón Bolívar International Airport
    "SKSP": "ADZ",  # large_airport | Gustavo Rojas Pinilla International Airport
    "SKSV": "SVI",  # medium_airport | Eduardo Falla Solano Airport
    "SKTM": "TME",  # medium_airport | Gustavo Vargas Airport
    "SKTQ": "TQS",  # medium_airport | Captain Ernesto Esguerra Cubides Air Base
    "SKUC": "AUC",  # medium_airport | Santiago Perez Airport
    "SKUI": "UIB",  # medium_airport | El Caraño Airport
    "SKUL": "ULQ",  # medium_airport | Heriberto Gíl Martínez Airport
    "SKVP": "VUP",  # medium_airport | Alfonso López Pumarejo Airport
    "SKVV": "VVC",  # medium_airport | Vanguardia Airport
    "SKYP": "EYP",  # medium_airport | El Alcaravan - Yopal Airport
    "SLAL": "SRE",  # large_airport | Alcantarí International Airport
    "SLBJ": "BJO",  # medium_airport | Bermejo Airport
    "SLCB": "CBB",  # large_airport | Jorge Wilsterman International Airport
    "SLCO": "CIJ",  # medium_airport | Capitán Aníbal Arab Airport
    "SLET": "SRZ",  # medium_airport | El Trompillo Airport
    "SLGM": "GYA",  # medium_airport | Guayaramerín Airport
    "SLLP": "LPB",  # large_airport | El Alto International Airport
    "SLOR": "ORU",  # large_airport | Juan Mendoza International Airport
    "SLPO": "POI",  # medium_airport | Capitan Nicolas Rojas Airport
    "SLPS": "PSZ",  # medium_airport | Capitán Av. Salvador Ogaya G. airport
    "SLRI": "RIB",  # medium_airport | Capitán Av. Selin Zeitun Lopez Airport
    "SLSA": "SBL",  # medium_airport | Santa Ana Del Yacuma Airport
    "SLTJ": "TJA",  # medium_airport | Capitan Oriel Lea Plaza Airport
    "SLTR": "TDD",  # medium_airport | Teniente Av. Jorge Henrich Arauz Airport
    "SLVM": "VLM",  # medium_airport | Teniente Coronel Rafael Pabón Airport
    "SLVR": "VVI",  # large_airport | Viru Viru International Airport
    "SLYA": "BYC",  # medium_airport | Yacuiba Airport
    "SMJP": "PBM",  # large_airport | Johan Adolf Pengel International Airport
    "SNCP": "EEA",  # medium_airport | Planalto Serrano Regional Airport
    "SNLN": "LHN",  # medium_airport | Linhares Municipal Airport
    "SOCA": "CAY",  # large_airport | Cayenne – Félix Eboué Airport
    "SOOA": "MPY",  # medium_airport | Maripasoula Airport
    "SOOG": "OYP",  # medium_airport | Saint-Georges-de-l'Oyapock Airport
    "SOOM": "LDX",  # medium_airport | Saint-Laurent-du-Maroni Airport
    "SPAY": "AYX",  # medium_airport | Teniente General Gerardo Pérez Pinedo Airport
    "SPBR": "IBP",  # medium_airport | Iberia Airport
    "SPCL": "PCL",  # large_airport | Cap FAP David Abenzur Rengifo International Airport
    "SPEO": "CHM",  # medium_airport | FAP Lieutenant Jaime Andres de Montreuil Morales Airport
    "SPHI": "CIX",  # large_airport | Capitán FAP José A. Quiñones González International Airport
    "SPHO": "AYP",  # medium_airport | Air Force Colonel Alfredo Mendivil Duarte Airport
    "SPHZ": "ATA",  # medium_airport | Comandante FAP German Arias Graziani Airport
    "SPIM": "LIM",  # large_airport | Jorge Chávez International Airport
    "SPJA": "RIJ",  # medium_airport | Juan Simons Vela Airport
    "SPJE": "JAE",  # medium_airport | Shumba Airport
    "SPJI": "JJI",  # medium_airport | Juanjui Airport
    "SPJJ": "JAU",  # medium_airport | Francisco Carle Airport
    "SPJL": "JUL",  # large_airport | Inca Manco Capac International Airport
    "SPJR": "CJA",  # medium_airport | Mayor General FAP Armando Revoredo Iglesias Airport
    "SPLO": "ILQ",  # medium_airport | General Jorge Fernandez Maldon Airport
    "SPME": "TBP",  # medium_airport | Captain Pedro Canga Rodríguez International Airport
    "SPMS": "YMS",  # medium_airport | Moises Benzaquen Rengifo Airport
    "SPNC": "HUU",  # medium_airport | Alferez Fap David Figueroa Fernandini Airport
    "SPPY": "CHH",  # medium_airport | Chachapoyas Airport
    "SPQT": "IQT",  # large_airport | Coronel FAP Francisco Secada Vignetta International Airport
    "SPQU": "AQP",  # large_airport | Rodríguez Ballón International Airport
    "SPRU": "TRU",  # large_airport | Capitán FAP Carlos Martínez de Pinillos International Airport
    "SPSO": "PIO",  # large_airport | Captain Renán Elías Olivera International Airport
    "SPST": "TPP",  # medium_airport | Cadete FAP Guillermo Del Castillo Paredes Airport
    "SPTN": "TCQ",  # medium_airport | Coronel FAP Carlos Ciriani Santa Rosa International Airport
    "SPTU": "PEM",  # medium_airport | Padre Aldamiz International Airport
    "SPUR": "PIU",  # medium_airport | PAF Captain Guillermo Concha Iberico International Airport
    "SPYL": "TYL",  # medium_airport | Captain Victor Montes Arias International Airport
    "SPZA": "NZC",  # medium_airport | Maria Reiche Neuman Airport
    "SPZO": "CUZ",  # large_airport | Alejandro Velasco Astete International Airport
    "SUDU": "DZO",  # medium_airport | Santa Bernardina International Airport
    "SULS": "PDP",  # medium_airport | Capitan Corbeta CA Curbelo International Airport
    "SUMU": "MVD",  # large_airport | Carrasco General Cesáreo L. Berisso International Airport
    "SUPU": "PDU",  # medium_airport | Tydeo Larre Borges Airport
    "SURV": "RVY",  # medium_airport | Pres. Gral. Óscar D. Gestido Binational Airport
    "SUSO": "STY",  # medium_airport | Nueva Hesperides International Airport
    "SVAC": "AGV",  # medium_airport | Oswaldo Guevara Mujica Airport
    "SVAN": "AAO",  # medium_airport | Anaco Airport
    "SVBC": "BLA",  # large_airport | General José Antonio Anzoategui International Airport
    "SVBI": "BNS",  # medium_airport | Barinas Airport
    "SVBM": "BRM",  # large_airport | Jacinto Lara International Airport
    "SVBS": "MYC",  # medium_airport | Escuela Mariscal Sucre Airport
    "SVCB": "CBL",  # medium_airport | General Tomas de Heres Airport
    "SVCD": "CXA",  # medium_airport | Caicara del Orinoco Airport
    "SVCL": "CLZ",  # medium_airport | Calabozo Airport
    "SVCN": "CAJ",  # medium_airport | Canaima Airport
    "SVCP": "CUP",  # medium_airport | General Francisco Bermúdez Airport
    "SVCR": "CZE",  # medium_airport | José Leonardo Chirinos Airport
    "SVCU": "CUM",  # medium_airport | Antonio José de Sucre Airport
    "SVED": "EOR",  # medium_airport | El Dorado Airport
    "SVEZ": "EOZ",  # medium_airport | Elorza Airport
    "SVGD": "GDO",  # medium_airport | Guasdualito Airport
    "SVGI": "GUI",  # medium_airport | Guiria Airport
    "SVGU": "GUQ",  # medium_airport | Guanare Airport
    "SVJC": "LSP",  # medium_airport | Josefa Camejo International Airport
    "SVLF": "LFR",  # medium_airport | La Fria Airport
    "SVMC": "MAR",  # large_airport | La Chinita International Airport
    "SVMD": "MRD",  # medium_airport | Alberto Carnevalli Airport
    "SVMG": "PMV",  # large_airport | Del Caribe Santiago Mariño International Airport
    "SVMI": "CCS",  # large_airport | Maiquetía Simón Bolívar International Airport
    "SVMT": "MUN",  # medium_airport | José Tadeo Monagas International Airport
    "SVPA": "PYH",  # medium_airport | Cacique Aramare Airport
    "SVPC": "PBL",  # medium_airport | General Bartolome Salom International Airport
    "SVPM": "SCI",  # medium_airport | Paramillo Airport
    "SVPR": "PZO",  # large_airport | General Manuel Carlos Piar International Airport
    "SVPT": "PTM",  # medium_airport | Palmarito Airport
    "SVSA": "SVZ",  # medium_airport | Juan Vicente Gómez International Airport
    "SVSE": "SNV",  # medium_airport | Santa Elena de Uairén Airport
    "SVSO": "STD",  # medium_airport | Mayor Buenaventura Vivas International Airport
    "SVSP": "SNF",  # medium_airport | Sub Teniente Nestor Arias Airport
    "SVSR": "SFD",  # medium_airport | San Fernando de Apure Las Flecheras National Airport
    "SVST": "SOM",  # medium_airport | San Tomé Airport
    "SVSZ": "STB",  # medium_airport | Miguel Urdaneta Fernández Airport
    "SVTC": "TUV",  # medium_airport | Tucupita Airport
    "SVTM": "TMO",  # medium_airport | Tumeremo Airport
    "SVVA": "VLN",  # large_airport | Arturo Michelena International Airport
    "SVVG": "VIG",  # medium_airport | Juan Pablo Pérez Alfonso Airport
    "SVVL": "VLV",  # medium_airport | Dr. Antonio Nicolás Briceño Airport
    "SVVP": "VDP",  # medium_airport | Valle de La Pascua Airport
    "SWGN": "AUX",  # medium_airport | Araguaína Airport
    "SYCJ": "GEO",  # large_airport | Cheddi Jagan International Airport
    "SYGO": "OGL",  # medium_airport | Eugene F. Correia International Airport
    "SYKA": "KAI",  # medium_airport | Kaieteur Airport
    "SYLT": "LTM",  # medium_airport | Lethem Airport
    "TAPA": "ANU",  # large_airport | V. C. Bird International Airport
    "TBPB": "BGI",  # large_airport | Grantley Adams International Airport
    "TDCF": "DCF",  # medium_airport | Canefield Airport
    "TDPD": "DOM",  # medium_airport | Douglas-Charles Airport
    "TFFF": "FDF",  # large_airport | Martinique Aimé Césaire International Airport
    "TFFG": "SFG",  # medium_airport | Grand Case-l'Espérance Airport
    "TFFJ": "SBH",  # medium_airport | St. Jean Airport
    "TFFM": "GBJ",  # medium_airport | Marie-Galante Airport
    "TFFR": "PTP",  # large_airport | Maryse Condé International Airport
    "TGPY": "GND",  # large_airport | Maurice Bishop International Airport
    "TIST": "STT",  # large_airport | Cyril E. King Airport
    "TISX": "STX",  # medium_airport | Henry E. Rohlsen Airport
    "TJAB": "ARE",  # medium_airport | Antonio Nery Juarbe Pol Airport
    "TJBQ": "BQN",  # medium_airport | Rafael Hernández International Airport
    "TJCP": "CPX",  # medium_airport | Benjamin Rivera Noriega Airport
    "TJIG": "SIG",  # medium_airport | Fernando Luis Ribas Dominicci Airport
    "TJMZ": "MAZ",  # medium_airport | Eugenio Maria De Hostos Airport
    "TJPS": "PSE",  # medium_airport | Mercedita International Airport
    "TJRV": "NRR",  # medium_airport | José Aponte de la Torre Airport
    "TJSJ": "SJU",  # large_airport | Luis Munoz Marin International Airport
    "TJVQ": "VQS",  # medium_airport | Antonio Rivera Rodriguez Airport
    "TKPK": "SKB",  # large_airport | Robert L. Bradshaw International Airport
    "TKPN": "NEV",  # medium_airport | Vance W. Amory International Airport
    "TLPC": "SLU",  # medium_airport | George F. L. Charles Airport
    "TLPL": "UVF",  # large_airport | Hewanorra International Airport
    "TNCA": "AUA",  # large_airport | Queen Beatrix International Airport
    "TNCB": "BON",  # large_airport | Flamingo International Airport
    "TNCC": "CUR",  # large_airport | Hato International Airport
    "TNCE": "EUX",  # medium_airport | F. D. Roosevelt Airport
    "TNCM": "SXM",  # large_airport | Princess Juliana International Airport
    "TNCS": "SAB",  # medium_airport | Juancho E. Yrausquin Airport
    "TQPF": "AXA",  # medium_airport | Clayton J. Lloyd International Airport
    "TRPG": "MNI",  # large_airport | John A. Osborne Airport
    "TTCP": "TAB",  # large_airport | A.N.R. Robinson International Airport
    "TTPP": "POS",  # large_airport | Piarco International Airport
    "TUPJ": "EIS",  # large_airport | Terrance B. Lettsome International Airport
    "TUPW": "VIJ",  # medium_airport | Virgin Gorda Airport
    "TVSA": "SVD",  # large_airport | Argyle International Airport
    "TVSB": "BQU",  # medium_airport | J F Mitchell Airport
    "TVSC": "CIW",  # medium_airport | Canouan Airport
    "TVSM": "MQS",  # medium_airport | Mustique Airport
    "TVSU": "UNI",  # medium_airport | Union Island International Airport
    "TXKF": "BDA",  # large_airport | L.F. Wade International Airport
    "UAAA": "ALA",  # large_airport | Almaty International Airport
    "UAAH": "BXH",  # medium_airport | Balkhash Airport
    "UAAT": "TDK",  # medium_airport | Taldykorgan Airport
    "UACC": "NQZ",  # large_airport | Nursultan Nazarbayev International Airport
    "UACK": "KOV",  # large_airport | Kokshetau International Airport
    "UACP": "PPK",  # large_airport | Petropavl International Airport
    "UADD": "DMB",  # large_airport | Taraz International Airport
    "UAFM": "BSZ",  # large_airport | Manas International Airport
    "UAFO": "OSS",  # large_airport | Osh International Airport
    "UAII": "CIT",  # large_airport | Shymkent International Airport
    "UAIT": "HSA",  # large_airport | Hazrat Sultan International Airport
    "UAKD": "DZN",  # large_airport | Zhezkazgan National Airport
    "UAKK": "KGF",  # large_airport | Sary-Arka Airport
    "UAOL": "BXY",  # large_airport | Baikonur Krayniy International Airport
    "UAOO": "KZO",  # large_airport | Korkyt Ata International Airport
    "UARR": "URA",  # large_airport | Manshuk Mametova International Airport
    "UASB": "EKB",  # medium_airport | Ekibastuz Airport
    "UASK": "UKK",  # large_airport | Oskemen International Airport
    "UASP": "PWQ",  # large_airport | Pavlodar International Airport
    "UASS": "PLX",  # large_airport | Semei International Airport
    "UATE": "SCO",  # large_airport | Aktau International Airport
    "UATG": "GUW",  # large_airport | Atyrau International Airport
    "UATT": "AKX",  # large_airport | Aktobe International Airport
    "UAUU": "KSN",  # large_airport | Kostanay International Airport
    "UBBB": "GYD",  # large_airport | Heydar Aliyev International Airport
    "UBBG": "GNJ",  # large_airport | Ganja International Airport
    "UBBN": "NAJ",  # large_airport | Nakhchivan International Airport
    "UBBQ": "GBB",  # medium_airport | Gabala International Airport
    "UBBY": "ZTU",  # medium_airport | Zaqatala International Airport
    "UCFL": "IKU",  # large_airport | Issyk-Kul International Airport
    "UDSG": "LWN",  # large_airport | Shirak International Airport
    "UDYZ": "EVN",  # large_airport | Zvartnots International Airport
    "UEEE": "YKS",  # large_airport | Platon Oyunsky Yakutsk International Airport
    "UELL": "NER",  # medium_airport | Chulman Airport
    "UEMA": "MQJ",  # medium_airport | Moma Airport
    "UEMM": "GYG",  # medium_airport | Magan Airport
    "UEMO": "OLZ",  # medium_airport | Olyokminsk Airport
    "UEMT": "USR",  # medium_airport | Ust-Nera Airport
    "UENW": "VYI",  # medium_airport | Vilyuisk Airport
    "UERL": "ULK",  # medium_airport | Lensk Airport
    "UERP": "PYJ",  # medium_airport | Polyarny Airport
    "UERR": "MJZ",  # medium_airport | Mirny Airport
    "UERS": "SYS",  # medium_airport | Saskylakh Airport
    "UESG": "BGN",  # medium_airport | Belaya Gora Airport
    "UESK": "SEK",  # medium_airport | Srednekolymsk Airport
    "UESO": "CKH",  # medium_airport | Chokurdakh Airport
    "UESS": "CYX",  # medium_airport | Cherskiy Airport
    "UEST": "IKS",  # medium_airport | Tiksi Airport
    "UESU": "ZKP",  # medium_airport | Zyryanka Airport
    "UEVV": "ZIX",  # medium_airport | Zhigansk Airport
    "UGKO": "KUT",  # large_airport | David the Builder Kutaisi International Airport
    "UGSB": "BUS",  # large_airport | Alexander Kartveli Batumi International Airport
    "UGSS": "SUI",  # medium_airport | Vladislav Ardzinba Sukhum International Airport
    "UGTB": "TBS",  # large_airport | Tbilisi International Airport
    "UHBB": "BQS",  # medium_airport | Ignatyevo Airport
    "UHHH": "KHV",  # medium_airport | Khabarovsk Novy Airport
    "UHKK": "KXK",  # medium_airport | Komsomolsk-on-Amur Airport
    "UHKM": "GVN",  # medium_airport | Sovetskaya Gavan (Maygatka) Airport
    "UHMA": "DYR",  # medium_airport | Ugolny Yuri Ryktheu Airport
    "UHMD": "PVS",  # medium_airport | Provideniya Bay Airport
    "UHMK": "KPW",  # medium_airport | Keperveem Airport
    "UHMM": "GDX",  # medium_airport | Sokol Airport
    "UHMP": "PWE",  # medium_airport | Pevek Airport
    "UHMW": "SWV",  # medium_airport | Severo-Evensk Airport
    "UHNN": "NLI",  # medium_airport | Nikolayevsk-na-Amure Airport
    "UHOO": "OHO",  # medium_airport | Okhotsk Airport
    "UHPP": "PKC",  # large_airport | Yelizovo Airport
    "UHSS": "UUS",  # large_airport | Yuzhno-Sakhalinsk International Airport
    "UHWW": "VVO",  # large_airport | Vladivostok International Airport
    "UIAA": "HTA",  # large_airport | Chita-Kadala International Airport
    "UIBB": "BTK",  # medium_airport | Bratsk Airport
    "UIII": "IKT",  # large_airport | Irkutsk International Airport
    "UITT": "UKX",  # medium_airport | Ust-Kut Airport
    "UIUU": "UUD",  # large_airport | Baikal International Airport
    "UKBB": "KBP",  # medium_airport | Boryspil International Airport
    "UKCM": "MPW",  # medium_airport | Mariupol International Airport
    "UKDB": "ERD",  # medium_airport | Berdyansk Airport
    "UKDD": "DNK",  # medium_airport | Dnipro International Airport
    "UKDE": "OZH",  # large_airport | Zaporizhzhia International Airport
    "UKDR": "KWG",  # medium_airport | Kryvyi Rih International Airport
    "UKFB": "UKS",  # medium_airport | Sevastopol International Airport / Belbek Air Base
    "UKFF": "SIP",  # large_airport | Simferopol International Airport
    "UKHH": "HRK",  # medium_airport | Kharkiv International Airport
    "UKKE": "CKC",  # medium_airport | Cherkasy International Airport
    "UKKK": "IEV",  # medium_airport | Ihor Sikorsky Kyiv International Airport (Zhuliany)
    "UKLH": "HMJ",  # medium_airport | Khmelnytskyi Airport
    "UKLI": "IFO",  # medium_airport | Ivano-Frankivsk International Airport
    "UKLL": "LWO",  # large_airport | Lviv International Airport
    "UKLN": "CWC",  # medium_airport | Chernivtsi International Airport
    "UKLR": "RWN",  # medium_airport | Rivne International Airport
    "UKLU": "UDJ",  # large_airport | Uzhhorod International Airport
    "UKOH": "KHE",  # medium_airport | Kherson International Airport
    "UKOO": "ODS",  # large_airport | Odesa International Airport
    "UKWW": "VIN",  # medium_airport | Vinnytsia/Gavyryshivka International Airport
    "ULAA": "ARH",  # medium_airport | Talagi Airport
    "ULAH": "VKV",  # medium_airport | Vaskovo Airport
    "ULAM": "NNM",  # medium_airport | Naryan Mar Airport
    "ULDD": "AMV",  # medium_airport | Amderma Airport
    "ULKK": "KSZ",  # medium_airport | Kotlas Airport
    "ULLI": "LED",  # large_airport | Pulkovo Airport
    "ULMM": "MMK",  # large_airport | Emperor Nicholas II Murmansk Airport
    "ULOO": "PKV",  # medium_airport | Princess Olga Pskov International Airport
    "ULPB": "PES",  # medium_airport | Petrozavodsk Airport
    "ULWC": "CEE",  # medium_airport | Cherepovets Airport
    "ULWU": "VUS",  # medium_airport | Velikiy Ustyug Airport
    "ULWW": "VGD",  # medium_airport | Vologda Airport
    "UMBB": "BQT",  # large_airport | Brest International Airport
    "UMGG": "GME",  # medium_airport | Gomel Airport
    "UMII": "VTB",  # medium_airport | Vitebsk Vostochny Airport
    "UMKK": "KGD",  # large_airport | Khrabrovo Airport
    "UMMG": "GNA",  # medium_airport | Hrodna Airport
    "UMMS": "MSQ",  # large_airport | Minsk National Airport
    "UMOO": "MVQ",  # medium_airport | Mogilev Airport
    "UNAA": "ABA",  # large_airport | Abakan International Airport
    "UNBB": "BAX",  # large_airport | Barnaul Gherman Titov International Airport
    "UNBG": "RGK",  # medium_airport | Gorno-Altaysk Airport
    "UNEE": "KEJ",  # large_airport | Alexei Leonov Kemerovo International Airport
    "UNIB": "BKA",  # medium_airport | Baykit Airport
    "UNII": "EIE",  # medium_airport | Yeniseysk Airport
    "UNIP": "TGP",  # medium_airport | Podkamennaya Tunguska Airport
    "UNIS": "VEO",  # medium_airport | Severo-Yeniseysk Airport
    "UNIW": "VAQ",  # medium_airport | Vanavara Airport
    "UNKL": "KJA",  # large_airport | Krasnoyarsk International Airport
    "UNKM": "KCY",  # medium_airport | Krasnoyarsk Cheremshanka Airport
    "UNKS": "ACS",  # medium_airport | Achinsk Airport
    "UNKY": "KYZ",  # medium_airport | Kyzyl Airport
    "UNNT": "OVB",  # large_airport | Novosibirsk Tolmachevo Airport
    "UNOO": "OMS",  # large_airport | Omsk Central Airport
    "UNSS": "SWT",  # medium_airport | Strezhevoy Airport
    "UNTT": "TOF",  # large_airport | Tomsk Kamov Airport
    "UNWW": "NOZ",  # medium_airport | Spichenkovo Airport
    "UODD": "DKS",  # medium_airport | Dikson Airport
    "UOHH": "HTG",  # medium_airport | Khatanga Airport
    "UOIG": "SES",  # medium_airport | Svetlogorsk Airport
    "UOII": "IAA",  # medium_airport | Igarka Airport
    "UOOO": "NSK",  # large_airport | Alykel International Airport
    "URKA": "AAQ",  # medium_airport | Anapa Vityazevo Airport
    "URKG": "GDZ",  # medium_airport | Gelendzhik Airport
    "URKK": "KRR",  # large_airport | Krasnodar Pashkovsky International Airport
    "URMG": "GRV",  # large_airport | Akhmat Kadyrov Grozny International Airport
    "URML": "MCX",  # large_airport | Makhachkala Uytash International Airport
    "URMM": "MRV",  # large_airport | Mineralnye Vody Airport
    "URMN": "NAL",  # medium_airport | Nalchik Airport
    "URMO": "OGZ",  # medium_airport | Vladikavkaz Beslan International Airport
    "URMS": "IGT",  # medium_airport | Magas Airport
    "URMT": "STW",  # medium_airport | Stavropol Shpakovskoye Airport
    "URRP": "ROV",  # large_airport | Platov International Airport
    "URRT": "TGK",  # medium_airport | Taganrog Yuzhny Airport
    "URSS": "AER",  # large_airport | Sochi International Airport
    "URWA": "ASF",  # large_airport | Astrakhan Narimanovo Boris M. Kustodiev International Airport
    "URWI": "ESL",  # medium_airport | Elista Airport
    "URWW": "VOG",  # large_airport | Volgograd International Airport
    "USCC": "CEK",  # large_airport | Kurchatov Chelyabinsk International Airport
    "USCM": "MQF",  # large_airport | Magnitogorsk International Airport
    "USDA": "SBT",  # medium_airport | Sabetta International Airport
    "USDB": "BVJ",  # medium_airport | Bovanenkovo Airport
    "USDD": "SLY",  # medium_airport | Salekhard Airport
    "USHB": "EZV",  # medium_airport | Berezovo Airport
    "USHH": "HMA",  # medium_airport | Khanty Mansiysk Airport
    "USHN": "NYA",  # medium_airport | Nyagan Airport
    "USHQ": "EYK",  # medium_airport | Beloyarskiy Airport
    "USHS": "OVS",  # medium_airport | Sovetskiy Airport
    "USHU": "URJ",  # medium_airport | Uray Airport
    "USII": "IJK",  # medium_airport | Izhevsk Airport
    "USKK": "KVX",  # medium_airport | Pobedilovo Airport
    "USMM": "NYM",  # medium_airport | Nadym Airport
    "USMU": "NUX",  # medium_airport | Novy Urengoy Airport
    "USNN": "NJC",  # large_airport | Nizhnevartovsk Airport
    "USPP": "PEE",  # large_airport | Perm International Airport
    "USRK": "KGP",  # medium_airport | Kogalym International Airport
    "USRN": "NFG",  # medium_airport | Nefteyugansk Airport
    "USRO": "NOJ",  # medium_airport | Noyabrsk Airport
    "USRR": "SGC",  # large_airport | Surgut International Airport
    "USSS": "SVX",  # large_airport | Koltsovo Airport
    "USTJ": "RMZ",  # medium_airport | Tobolsk Remezov Airport
    "USTR": "TJM",  # large_airport | Roshchino International Airport
    "USUU": "KRO",  # medium_airport | Kurgan Airport
    "UTAA": "ASB",  # large_airport | Ashgabat International Airport
    "UTAK": "KRW",  # large_airport | Turkmenbaşy International Airport
    "UTAM": "MYP",  # large_airport | Mary International Airport
    "UTAT": "TAZ",  # large_airport | Dashoguz International Airport
    "UTAV": "CRZ",  # large_airport | Türkmenabat International Airport
    "UTDD": "DYU",  # large_airport | Dushanbe International Airport
    "UTDK": "TJU",  # large_airport | Kulob International Airport
    "UTDL": "LBD",  # large_airport | Khujand International Airport
    "UTDT": "KQT",  # large_airport | Bokhtar International Airport
    "UTFN": "NMA",  # large_airport | Namangan International Airport
    "UTKA": "AZN",  # large_airport | Andijan International Airport
    "UTKF": "FEG",  # medium_airport | Fergana International Airport
    "UTNN": "NCU",  # large_airport | Nukus International Airport
    "UTNU": "UGC",  # large_airport | Urgench International Airport
    "UTSA": "NVI",  # medium_airport | Navoi International Airport
    "UTSB": "BHK",  # large_airport | Bukhara International Airport
    "UTSS": "SKD",  # large_airport | Samarkand International Airport
    "UTST": "TMJ",  # medium_airport | Termez Airport
    "UTTT": "TAS",  # large_airport | Tashkent International Airport
    "UTTZ": "OMN",  # medium_airport | Zomin Airport
    "UUBA": "KMW",  # medium_airport | Kostroma Sokerkino Airport
    "UUBC": "KLF",  # medium_airport | Grabtsevo Airport
    "UUBI": "IWA",  # medium_airport | Ivanovo South Airport
    "UUBK": "RYB",  # medium_airport | Staroselye Airport
    "UUBP": "BZK",  # medium_airport | Bryansk International Airport
    "UUBW": "ZIA",  # large_airport | Zhukovsky International Airport
    "UUDD": "DME",  # large_airport | Domodedovo International Airport
    "UUDL": "IAR",  # large_airport | Golden Ring Yaroslavl International Airport
    "UUEE": "SVO",  # large_airport | Sheremetyevo International Airport
    "UUEM": "KLD",  # medium_airport | Migalovo Air Base
    "UUMU": "CKL",  # medium_airport | Chkalovskiy Air Base
    "UUOB": "EGO",  # medium_airport | Belgorod International Airport
    "UUOK": "URS",  # medium_airport | Kursk East Airport
    "UUOL": "LPK",  # medium_airport | Lipetsk Airport
    "UUOO": "VOZ",  # large_airport | Voronezh International Airport
    "UUOT": "TBW",  # medium_airport | Donskoye Airport
    "UUWW": "VKO",  # large_airport | Vnukovo International Airport
    "UUYH": "UCT",  # medium_airport | Ukhta Airport
    "UUYI": "INA",  # medium_airport | Inta Airport
    "UUYP": "PEX",  # medium_airport | Pechora Airport
    "UUYS": "USK",  # medium_airport | Usinsk Airport
    "UUYW": "VKT",  # medium_airport | Vorkuta Airport
    "UUYX": "UTS",  # medium_airport | Ust-Tsylma Airport
    "UUYY": "SCW",  # medium_airport | Syktyvkar Airport
    "UWGG": "GOJ",  # large_airport | Nizhny Novgorod / Strigino International Airport
    "UWKB": "UUA",  # medium_airport | Bugulma Airport
    "UWKD": "KZN",  # large_airport | Kazan International Airport
    "UWKE": "NBC",  # medium_airport | Begishevo Airport
    "UWKJ": "JOK",  # medium_airport | Yoshkar-Ola Airport
    "UWKS": "CSY",  # medium_airport | Cheboksary Airport
    "UWLL": "ULV",  # large_airport | Ulyanovsk Baratayevka Airport
    "UWLW": "ULY",  # medium_airport | Ulyanovsk Vostochny Airport
    "UWOO": "REN",  # medium_airport | Orenburg Central Airport
    "UWOR": "OSW",  # medium_airport | Orsk Airport
    "UWPP": "PEZ",  # medium_airport | Penza Airport
    "UWPS": "SKX",  # large_airport | Saransk International Airport
    "UWSB": "BWO",  # medium_airport | Balakovo Airport
    "UWSG": "GSV",  # large_airport | Gagarin International Airport
    "UWUU": "UFA",  # large_airport | Ufa International Airport
    "UWWW": "KUF",  # large_airport | Kurumoch International Airport
    "VAAH": "AMD",  # large_airport | Sardar Vallabh Patel International Airport
    "VAAK": "AKD",  # medium_airport | Akola Airport
    "VAAU": "IXU",  # medium_airport | Aurangabad Airport
    "VABB": "BOM",  # large_airport | Chhatrapati Shivaji Maharaj International Airport
    "VABJ": "BHJ",  # medium_airport | Bhuj Airport
    "VABM": "IXG",  # medium_airport | Belagavi Airport
    "VABO": "BDQ",  # large_airport | Vadodara International Airport
    "VABP": "BHO",  # large_airport | Raja Bhoj International Airport
    "VABV": "BHU",  # medium_airport | Bhavnagar Airport
    "VADN": "NMB",  # medium_airport | Daman Airport
    "VAHB": "HBX",  # medium_airport | Hubballi Airport
    "VAHS": "HSR",  # large_airport | Rajkot International Airport
    "VAID": "IDR",  # large_airport | Devi Ahilya Bai Holkar International Airport
    "VAJB": "JLR",  # medium_airport | Jabalpur Airport
    "VAJM": "JGA",  # medium_airport | Jamnagar Airport
    "VAKE": "IXY",  # medium_airport | Kandla Airport
    "VAKJ": "HJR",  # medium_airport | Khajuraho Airport
    "VAKP": "KLH",  # medium_airport | Kolhapur Airport
    "VAKS": "IXK",  # medium_airport | Keshod Airport
    "VALT": "LTU",  # medium_airport | Murod Kond Airport
    "VAND": "NDC",  # medium_airport | Nanded Airport
    "VANP": "NAG",  # large_airport | Dr. Babasaheb Ambedkar International Airport
    "VAOZ": "ISK",  # large_airport | Nashik International Airport
    "VAPO": "PNQ",  # large_airport | Pune International Airport
    "VAPR": "PBD",  # medium_airport | Porbandar Airport
    "VARG": "RTC",  # medium_airport | Ratnagiri Airport
    "VARK": "RAJ",  # medium_airport | Rajkot Airport
    "VARP": "RPR",  # medium_airport | Swami Vivekananda Airport
    "VASD": "SAG",  # large_airport | Shirdi International Airport
    "VASL": "SSE",  # medium_airport | Solapur Airport
    "VASU": "STV",  # large_airport | Surat International Airport
    "VAUD": "UDR",  # medium_airport | Maharana Pratap Airport
    "VCBI": "CMB",  # large_airport | Bandaranaike International Colombo Airport
    "VCCA": "ACJ",  # medium_airport | Anuradhapura Airport
    "VCCB": "BTC",  # medium_airport | Batticaloa International Airport
    "VCCC": "RML",  # large_airport | Colombo Ratmalana International Airport
    "VCCG": "ADP",  # medium_airport | Ampara Airport
    "VCCH": "HIM",  # medium_airport | Hingurakgoda Air Force Base
    "VCCJ": "JAF",  # large_airport | Jaffna International Airport
    "VCCK": "KCT",  # medium_airport | Koggala Airport
    "VCCT": "TRR",  # medium_airport | China Bay Airport
    "VCRI": "HRI",  # large_airport | Mattala Rajapaksa International Airport
    "VDBG": "BBM",  # medium_airport | Battambang Airport
    "VDPP": "PNH",  # large_airport | Phnom Penh International Airport
    "VDRK": "RBE",  # medium_airport | Ratanakiri Airport
    "VDSA": "SAI",  # large_airport | Siem Reap-Angkor International Airport
    "VDSV": "KOS",  # large_airport | Sihanouk International Airport
    "VEAN": "IXV",  # medium_airport | Along Airport
    "VEAT": "IXA",  # medium_airport | Agartala - Maharaja Bir Bikram Airport
    "VEBD": "IXB",  # large_airport | Bagdogra Airport
    "VEBI": "SHL",  # medium_airport | Shillong Airport
    "VEBN": "VNS",  # large_airport | Lal Bahadur Shastri International Airport
    "VEBS": "BBI",  # large_airport | Biju Patnaik International Airport
    "VEBU": "PAB",  # medium_airport | Bilaspur Airport
    "VECC": "CCU",  # large_airport | Netaji Subhash Chandra Bose International Airport
    "VEDB": "DBD",  # medium_airport | Dhanbad Airport
    "VEDG": "RDP",  # medium_airport | Kazi Nazrul Islam Airport
    "VEDH": "DBR",  # medium_airport | Darbhanga Airport
    "VEGK": "GOP",  # medium_airport | Gorakhpur Airport
    "VEGT": "GAU",  # large_airport | Lokpriya Gopinath Bordoloi International Airport
    "VEGY": "GAY",  # medium_airport | Gaya Airport
    "VEIM": "IMF",  # large_airport | Bir Tikendrajit International Airport
    "VEJS": "IXW",  # medium_airport | Sonari Airport
    "VEJT": "JRH",  # medium_airport | Jorhat Airport
    "VEKI": "KBK",  # medium_airport | Kushinagar International Airport
    "VEKR": "IXH",  # medium_airport | Kailashahar Airport
    "VEKU": "IXS",  # medium_airport | Silchar Airport
    "VELP": "AJL",  # medium_airport | Lengpui Airport
    "VELR": "IXI",  # medium_airport | Lilabari North Lakhimpur Airport
    "VEMN": "DIB",  # medium_airport | Dibrugarh Airport
    "VEMR": "DMU",  # medium_airport | Dimapur Airport
    "VEMZ": "MZU",  # medium_airport | Muzaffarpur Airport
    "VEPT": "PAT",  # medium_airport | Jay Prakash Narayan Airport
    "VERC": "IXR",  # medium_airport | Birsa Munda Airport
    "VERK": "RRK",  # medium_airport | Rourkela Airport
    "VETZ": "TEZ",  # medium_airport | Tezpur Airport
    "VEVZ": "VTZ",  # large_airport | Visakhapatnam International Airport
    "VEZO": "ZER",  # medium_airport | Ziro Airport
    "VGBR": "BZL",  # medium_airport | Barisal Airport
    "VGCB": "CXB",  # medium_airport | Cox's Bazar Airport
    "VGEG": "CGP",  # large_airport | Shah Amanat International Airport
    "VGHS": "DAC",  # large_airport | Hazrat Shahjalal International Airport
    "VGIS": "IRD",  # medium_airport | Ishurdi Airport
    "VGJR": "JSR",  # medium_airport | Jessore Airport
    "VGRJ": "RJH",  # medium_airport | Shah Makhdum Airport
    "VGSD": "SPD",  # medium_airport | Saidpur Airport
    "VGSY": "ZYL",  # large_airport | Osmany International Airport
    "VHHH": "HKG",  # large_airport | Hong Kong International Airport
    "VIAG": "AGR",  # medium_airport | Agra Airport / Agra Air Force Station
    "VIAL": "IXD",  # medium_airport | Prayagraj Airport
    "VIAR": "ATQ",  # large_airport | Sri Guru Ram Das Ji International Airport
    "VIBK": "BKB",  # medium_airport | Nal Airport
    "VIBR": "KUU",  # medium_airport | Kullu Manali Airport
    "VIBT": "BUP",  # medium_airport | Bhatinda Air Force Station
    "VIBY": "BEK",  # medium_airport | Bareilly Air Force Station
    "VICG": "IXC",  # large_airport | Shaheed Bhagat Singh International Airport
    "VICX": "KNU",  # medium_airport | Kanpur Airport
    "VIDN": "DED",  # medium_airport | Dehradun Jolly Grant Airport
    "VIDP": "DEL",  # large_airport | Indira Gandhi International Airport
    "VIGG": "DHM",  # medium_airport | Kangra Airport
    "VIGR": "GWL",  # medium_airport | Gwalior Airport
    "VIHR": "HSS",  # large_airport | Maharaja Agrasen International Airport
    "VIHX": "HWR",  # large_airport | Halwara International Airport
    "VIJO": "JDH",  # medium_airport | Jodhpur Airport
    "VIJP": "JAI",  # large_airport | Jaipur International Airport
    "VIJR": "JSA",  # medium_airport | Jaisalmer Airport
    "VIJU": "IXJ",  # medium_airport | Jammu Airport
    "VIKG": "KQH",  # medium_airport | Kishangarh Airport Ajmer
    "VIKO": "KTU",  # medium_airport | Kota Airport
    "VILD": "LUH",  # medium_airport | Ludhiana Airport
    "VILH": "IXL",  # medium_airport | Leh Kushok Bakula Rimpochee Airport
    "VILK": "LKO",  # large_airport | Chaudhary Charan Singh International Airport
    "VIMB": "MZS",  # medium_airport | Moradabad Airport
    "VIPK": "IXP",  # medium_airport | Pathankot Airport
    "VIPT": "PGH",  # medium_airport | Pantnagar Airport
    "VISR": "SXR",  # large_airport | Sheikh ul Alam International Airport
    "VLLB": "LPQ",  # large_airport | Luang Phabang International Airport
    "VLPS": "PKZ",  # large_airport | Pakse International Airport
    "VLSK": "ZVK",  # medium_airport | Savannakhet Airport
    "VLSN": "NEU",  # medium_airport | Sam Neua Airport
    "VLVT": "VTE",  # large_airport | Wattay International Airport
    "VMMC": "MFM",  # large_airport | Macau International Airport
    "VNBW": "BWA",  # large_airport | Gautam Buddha International Airport
    "VNJP": "JKR",  # medium_airport | Janakpur Airport
    "VNKT": "KTM",  # large_airport | Tribhuvan International Airport
    "VNLK": "LUA",  # medium_airport | Tenzing-Hillary Airport
    "VNNG": "KEP",  # medium_airport | Nepalgunj Airport
    "VNPK": "PKR",  # medium_airport | Pokhara Domestic Airport
    "VNTJ": "TPJ",  # medium_airport | Taplejung Airport
    "VNVT": "BIR",  # medium_airport | Biratnagar Airport
    "VOAT": "AGX",  # medium_airport | Agatti Airport
    "VOBI": "BEP",  # medium_airport | Bellary Airport
    "VOBL": "BLR",  # large_airport | Kempegowda International Airport Bengaluru
    "VOBR": "IXX",  # medium_airport | Bidar Airport / Bidar Air Force Station
    "VOBZ": "VGA",  # large_airport | Vijayawada International Airport
    "VOCB": "CJB",  # large_airport | Coimbatore International Airport
    "VOCI": "COK",  # large_airport | Cochin International Airport
    "VOCL": "CCJ",  # large_airport | Calicut International Airport
    "VOCP": "CDP",  # medium_airport | Kadapa Airport
    "VOCX": "CBD",  # medium_airport | Car Nicobar Air Force Base
    "VOGA": "GOX",  # large_airport | Manohar International Airport
    "VOGO": "GOI",  # large_airport | Goa Dabolim International Airport
    "VOHS": "HYD",  # large_airport | Rajiv Gandhi International Airport
    "VOHY": "BPM",  # medium_airport | Begumpet Airport
    "VOKN": "CNN",  # large_airport | Kannur International Airport
    "VOKU": "KJB",  # medium_airport | Kurnool Airport
    "VOMD": "IXM",  # medium_airport | Madurai Airport
    "VOML": "IXE",  # large_airport | Mangaluru International Airport
    "VOMM": "MAA",  # large_airport | Chennai International Airport
    "VOMY": "MYQ",  # medium_airport | Mysore Airport
    "VOPB": "IXZ",  # large_airport | Veer Savarkar International Airport / INS Utkrosh
    "VOPC": "PNY",  # medium_airport | Pondicherry Airport
    "VOPN": "PUT",  # medium_airport | Sri Sathya Sai Airport
    "VORY": "RJA",  # medium_airport | Rajahmundry Airport
    "VOSM": "SXV",  # medium_airport | Salem Airport
    "VOTP": "TIR",  # large_airport | Tirupati International Airport
    "VOTR": "TRZ",  # large_airport | Tiruchirappalli International Airport
    "VOTV": "TRV",  # large_airport | Thiruvananthapuram International Airport
    "VQGP": "GLU",  # medium_airport | Gelephu Airport
    "VQPR": "PBH",  # large_airport | Paro International Airport
    "VRDA": "NMF",  # large_airport | Maafaru International Airport
    "VRMG": "GAN",  # large_airport | Gan International Airport
    "VRMH": "HAQ",  # large_airport | Hanimaadhoo International Airport
    "VRMK": "KDO",  # medium_airport | Kadhdhoo Airport
    "VRMM": "MLE",  # large_airport | Velana International Airport
    "VRMT": "KDM",  # medium_airport | Kaadedhdhoo Airport
    "VRMV": "VAM",  # medium_airport | Villa International Airport Maamigili
    "VTBD": "DMK",  # large_airport | Don Mueang International Airport
    "VTBK": "KDT",  # medium_airport | Kamphaeng Saen Airport
    "VTBL": "KKM",  # medium_airport | Khok Kathiam Airport
    "VTBO": "TDX",  # medium_airport | Trat Airport
    "VTBS": "BKK",  # large_airport | Suvarnabhumi Airport
    "VTBU": "UTP",  # large_airport | U-Tapao–Rayong–Pattaya International Airport
    "VTCC": "CNX",  # large_airport | Chiang Mai International Airport
    "VTCH": "HGN",  # medium_airport | Mae Hong Son Airport
    "VTCL": "LPT",  # medium_airport | Lampang Airport
    "VTCN": "NNT",  # medium_airport | Nan Airport
    "VTCP": "PRH",  # medium_airport | Phrae Airport
    "VTCT": "CEI",  # large_airport | Mae Fah Luang - Chiang Rai International Airport
    "VTPB": "PHY",  # medium_airport | Phetchabun Airport
    "VTPH": "HHQ",  # medium_airport | Hua Hin Airport
    "VTPI": "TKH",  # medium_airport | Takhli Royal Thai Air Force Base
    "VTPM": "MAQ",  # medium_airport | Mae Sot Airport
    "VTPO": "THS",  # medium_airport | Sukhothai Airport
    "VTPP": "PHS",  # medium_airport | Phitsanulok Airport
    "VTPT": "TKT",  # medium_airport | Tak Airport
    "VTSB": "URT",  # medium_airport | Surat Thani Airport
    "VTSC": "NAW",  # medium_airport | Narathiwat Airport
    "VTSE": "CJM",  # medium_airport | Chumphon Airport
    "VTSF": "NST",  # medium_airport | Nakhon Si Thammarat Airport
    "VTSG": "KBV",  # large_airport | Krabi International Airport
    "VTSH": "SGZ",  # medium_airport | Songkhla Airport
    "VTSK": "PAN",  # medium_airport | Pattani Airport
    "VTSM": "USM",  # large_airport | Samui International Airport
    "VTSP": "HKT",  # large_airport | Phuket International Airport
    "VTSR": "UNN",  # medium_airport | Ranong Airport
    "VTSS": "HDY",  # large_airport | Hat Yai International Airport
    "VTST": "TST",  # medium_airport | Trang Airport
    "VTUD": "UTH",  # large_airport | Udon Thani International Airport
    "VTUI": "SNO",  # medium_airport | Sakon Nakhon Airport
    "VTUJ": "PXR",  # medium_airport | Surin Airport
    "VTUK": "KKC",  # medium_airport | Khon Kaen Airport
    "VTUL": "LOE",  # medium_airport | Loei Airport
    "VTUO": "BFV",  # medium_airport | Buri Ram Airport
    "VTUQ": "NAK",  # medium_airport | Nakhon Ratchasima Airport
    "VTUU": "UBP",  # medium_airport | Ubon Ratchathani Airport
    "VTUV": "ROI",  # medium_airport | Roi Et Airport
    "VTUW": "KOP",  # medium_airport | Nakhon Phanom Airport
    "VVBM": "BMV",  # medium_airport | Buon Ma Thuot Airport
    "VVCI": "HPH",  # large_airport | Cat Bi International Airport
    "VVCM": "CAH",  # medium_airport | Cà Mau Airport
    "VVCR": "CXR",  # large_airport | Cam Ranh International Airport / Cam Ranh Air Base
    "VVCS": "VCS",  # medium_airport | Con Dao Airport
    "VVCT": "VCA",  # large_airport | Can Tho International Airport
    "VVDB": "DIN",  # medium_airport | Dien Bien Phu Airport
    "VVDH": "VDH",  # medium_airport | Dong Hoi Airport
    "VVDL": "DLI",  # medium_airport | Lien Khuong Airport
    "VVDN": "DAD",  # large_airport | Da Nang International Airport
    "VVNB": "HAN",  # large_airport | Noi Bai International Airport
    "VVPB": "HUI",  # medium_airport | Phu Bai International Airport
    "VVPC": "UIH",  # medium_airport | Phu Cat Airport
    "VVPK": "PXU",  # medium_airport | Pleiku Airport
    "VVPQ": "PQC",  # large_airport | Phú Quốc International Airport
    "VVRG": "VKG",  # medium_airport | Rach Gia Airport
    "VVTH": "TBB",  # medium_airport | Dong Tac Airport
    "VVTS": "SGN",  # large_airport | Tan Son Nhat International Airport
    "VVVD": "VDO",  # medium_airport | Van Don International Airport
    "VVVH": "VII",  # medium_airport | Vinh Airport
    "VYDW": "TVY",  # medium_airport | Dawei Airport
    "VYHH": "HEH",  # medium_airport | Heho Airport
    "VYKG": "KET",  # medium_airport | Kengtung Airport
    "VYKP": "KYP",  # medium_airport | Kyaukpyu Airport
    "VYKT": "KAW",  # medium_airport | Kawthoung Airport
    "VYLK": "LIW",  # medium_airport | Loikaw Airport
    "VYLS": "LSH",  # medium_airport | Lashio Airport
    "VYMD": "MDL",  # large_airport | Mandalay International Airport
    "VYME": "MGZ",  # medium_airport | Myeik Airport
    "VYMK": "MYT",  # medium_airport | Myitkyina Airport
    "VYMO": "MOE",  # medium_airport | Momeik Airport
    "VYMS": "MOG",  # medium_airport | Mong Hsat Airport
    "VYNS": "NMS",  # medium_airport | Namsang Airport
    "VYNT": "NYT",  # large_airport | Nay Pyi Taw International Airport
    "VYPT": "PBU",  # medium_airport | Putao Airport
    "VYSW": "AKY",  # medium_airport | Sittwe Airport
    "VYTD": "SNW",  # medium_airport | Thandwe Airport
    "VYTL": "THL",  # medium_airport | Tachileik Airport
    "VYYY": "RGN",  # large_airport | Yangon International Airport
    "WAAA": "UPG",  # large_airport | Sultan Hasanuddin International Airport
    "WABB": "BIK",  # medium_airport | Frans Kaisiepo Airport
    "WABI": "NBX",  # medium_airport | Douw Aturure Airport
    "WABO": "ZRI",  # medium_airport | Stevanus Rumbewas Airport
    "WABP": "TIM",  # medium_airport | Mozes Kilangin Airport
    "WADB": "BMU",  # medium_airport | Sultan Muhammad Salahuddin Airport
    "WADD": "DPS",  # large_airport | Denpasar I Gusti Ngurah Rai International Airport
    "WADL": "LOP",  # large_airport | Lombok International Airport
    "WAEE": "TTE",  # medium_airport | Sultan Babullah Airport
    "WAEW": "OTI",  # medium_airport | Pitu Airport
    "WAFB": "TRT",  # medium_airport | Toraja Airport
    "WAFF": "PLW",  # medium_airport | Mutiara - SIS Al-Jufrie Airport
    "WAFP": "PSJ",  # medium_airport | Kasiguncu Airport
    "WAFW": "LUW",  # medium_airport | Syukuran Aminuddin Amir Airport
    "WAGG": "PKY",  # medium_airport | Tjilik Riwut Airport
    "WAHI": "YIA",  # medium_airport | Yogyakarta International Airport
    "WAHL": "CXP",  # medium_airport | Tunggul Wulung Airport
    "WAJJ": "DJJ",  # large_airport | Dortheys Hiyo Eluay International Airport
    "WAJO": "OKL",  # medium_airport | Oksibil Airport
    "WAKK": "MKQ",  # medium_airport | Mopah International Airport
    "WAKT": "TMH",  # medium_airport | Tanah Merah Airport
    "WALK": "IVD",  # medium_airport | Nusantara International Airport
    "WALL": "BPN",  # large_airport | Sultan Aji Muhammad Sulaiman Sepinggan International Airport
    "WALR": "TRK",  # medium_airport | Juwata International Airport / Suharnoko Harbani AFB
    "WALS": "AAP",  # medium_airport | Aji Pangeran Tumenggung Pranoto International Airport
    "WAMH": "NAH",  # medium_airport | Naha Airport
    "WAMM": "MDC",  # large_airport | Sam Ratulangi International Airport
    "WAON": "TJG",  # medium_airport | Warukin Airport
    "WAOO": "BDJ",  # large_airport | Syamsudin Noor International Airport
    "WAPF": "LUV",  # medium_airport | Karel Sadsuitubun Airport
    "WAPN": "NAM",  # medium_airport | Namniwel Airport
    "WAPP": "AMQ",  # large_airport | Pattimura International Airport
    "WAQT": "BEJ",  # medium_airport | Kalimarau Airport
    "WARA": "MLG",  # medium_airport | Abdul Rachman Saleh Airport
    "WARJ": "JOG",  # large_airport | Adisutjipto International Airport
    "WARQ": "SOC",  # medium_airport | Adisumarmo Airport
    "WARR": "SUB",  # large_airport | Juanda International Airport
    "WARS": "SRG",  # large_airport | Jenderal Ahmad Yani Airport
    "WASF": "FKQ",  # medium_airport | Fakfak Airport
    "WASK": "KNG",  # medium_airport | Utarom Airport
    "WASO": "BXB",  # medium_airport | Babo Airport
    "WASR": "MKW",  # medium_airport | Rendani Airport
    "WASS": "SOQ",  # medium_airport | Domine Eduard Osok Airport
    "WATT": "KOE",  # medium_airport | El Tari Airport
    "WAVV": "WMX",  # medium_airport | Wamena Airport
    "WAWD": "WNI",  # medium_airport | Matahora Airport
    "WAWP": "KXB",  # medium_airport | Sangia Nibandera Airport
    "WBGB": "BTU",  # medium_airport | Bintulu Airport
    "WBGG": "KCH",  # large_airport | Kuching International Airport
    "WBGJ": "LMN",  # medium_airport | Limbang Airport
    "WBGK": "MKM",  # medium_airport | Mukah Airport
    "WBGM": "MUR",  # medium_airport | Marudi Airport
    "WBGR": "MYY",  # medium_airport | Miri Airport
    "WBGS": "SBW",  # medium_airport | Sibu Airport
    "WBGZ": "BBN",  # medium_airport | Bario Airport
    "WBKD": "LDU",  # medium_airport | Lahad Datu Airport
    "WBKK": "BKI",  # large_airport | Kota Kinabalu International Airport
    "WBKL": "LBU",  # medium_airport | Labuan Airport
    "WBKS": "SDK",  # medium_airport | Sandakan Airport
    "WBKW": "TWU",  # medium_airport | Tawau Airport
    "WBMU": "MZV",  # medium_airport | Mulu Airport
    "WBSB": "BWN",  # large_airport | Brunei International Airport
    "WIBB": "PKU",  # medium_airport | Sultan Syarif Kasim II International Airport / Roesmin Nurjadin AFB
    "WIBD": "DUM",  # medium_airport | Pinang Kampai Airport
    "WIBJ": "RGT",  # medium_airport | Japura Airport
    "WICA": "KJT",  # medium_airport | Kertajati International Airport
    "WICC": "BDO",  # medium_airport | Husein Sastranegara International Airport
    "WIDD": "BTH",  # large_airport | Hang Nadim International Airport
    "WIDN": "TNJ",  # medium_airport | Raja Haji Fisabilillah International Airport
    "WIHH": "HLP",  # large_airport | Halim Perdanakusuma International Airport
    "WIII": "CGK",  # large_airport | Soekarno-Hatta International Airport
    "WILL": "TKG",  # medium_airport | Radin Inten II International Airport
    "WIMB": "GNS",  # medium_airport | Binaka Airport
    "WIME": "AEG",  # medium_airport | Aek Godang Airport
    "WIMK": "MES",  # medium_airport | Soewondo Air Force Base
    "WIMM": "KNO",  # large_airport | Kualanamu International Airport
    "WIMS": "FLZ",  # medium_airport | Dr. Ferdinand Lumban Tobing Airport
    "WIMU": "LSR",  # medium_airport | Alas Leuser Airport
    "WIOG": "NPO",  # medium_airport | Nanga Pinoh Airport
    "WIOK": "KTG",  # medium_airport | Rahadi Osman Airport
    "WION": "NTX",  # medium_airport | Ranai Airport
    "WIOO": "PNK",  # large_airport | Supadio International Airport
    "WIOP": "PSU",  # medium_airport | Pangsuma Airport
    "WIOS": "SQG",  # medium_airport | Tebelian Airport
    "WIPK": "PGK",  # medium_airport | Depati Amir Airport
    "WIPL": "BKS",  # medium_airport | Fatmawati Soekarno Airport
    "WIPP": "PLM",  # medium_airport | Sultan Mahmud Badaruddin II Airport
    "WIPQ": "PDO",  # medium_airport | Pendopo Airport
    "WIPT": "PDG",  # medium_airport | Minangkabau International Airport
    "WITC": "MEQ",  # medium_airport | Cut Nyak Dhien Airport
    "WITK": "TXE",  # medium_airport | Rembele Airport
    "WITL": "LSX",  # medium_airport | Lhok Sukon Airport
    "WITT": "BTJ",  # large_airport | Sultan Iskandar Muda International Airport
    "WMBT": "TOD",  # medium_airport | Tioman Airport
    "WMKA": "AOR",  # medium_airport | Sultan Abdul Halim Airport
    "WMKB": "BWH",  # medium_airport | RMAF Butterworth Air Base
    "WMKC": "KBR",  # medium_airport | Sultan Ismail Petra Airport
    "WMKD": "KUA",  # medium_airport | Kuantan Airport
    "WMKE": "KTE",  # medium_airport | Kerteh Airport
    "WMKI": "IPH",  # large_airport | Sultan Azlan Shah Airport
    "WMKJ": "JHB",  # large_airport | Senai International Airport
    "WMKK": "KUL",  # large_airport | Kuala Lumpur International Airport
    "WMKL": "LGK",  # large_airport | Langkawi International Airport
    "WMKM": "MKZ",  # medium_airport | Malacca International Airport
    "WMKN": "TGG",  # medium_airport | Sultan Mahmud Airport
    "WMKP": "PEN",  # large_airport | Penang International Airport
    "WMSA": "SZB",  # large_airport | Sultan Abdul Aziz Shah International Airport
    "WPDB": "UAI",  # medium_airport | Commander in Chief of FALINTIL, Kay Rala Xanana Gusmão, International Airport
    "WPDL": "DIL",  # large_airport | Presidente Nicolau Lobato International Airport
    "WPEC": "BCH",  # medium_airport | Baucau Airport
    "WPOC": "OEC",  # large_airport | Oecusse Route of the Sandalwood International Airport
    "WSAP": "QPG",  # medium_airport | Paya Lebar Air Base
    "WSAT": "TGA",  # medium_airport | Tengah Air Base
    "WSSL": "XSP",  # medium_airport | Seletar Airport
    "WSSS": "SIN",  # large_airport | Singapore Changi Airport
    "YABA": "ALH",  # medium_airport | Albany Airport
    "YARA": "ARY",  # medium_airport | Ararat Airport
    "YARM": "ARM",  # medium_airport | Armidale Airport
    "YAYE": "AYQ",  # medium_airport | Ayers Rock Connellan Airport
    "YBAR": "BCI",  # medium_airport | Barcaldine Airport
    "YBAS": "ASP",  # medium_airport | Alice Springs Airport
    "YBBN": "BNE",  # large_airport | Brisbane International Airport
    "YBCG": "OOL",  # large_airport | Gold Coast Airport
    "YBCK": "BKQ",  # medium_airport | Blackall Airport
    "YBCS": "CNS",  # large_airport | Cairns International Airport
    "YBCV": "CTL",  # medium_airport | Charleville Airport
    "YBDV": "BVI",  # medium_airport | Birdsville Airport
    "YBHI": "BHQ",  # medium_airport | Broken Hill Airport
    "YBHM": "HTI",  # medium_airport | Hamilton Island Airport
    "YBIE": "BEU",  # medium_airport | Bedourie Airport
    "YBKE": "BRK",  # medium_airport | Bourke Airport
    "YBLA": "BLN",  # medium_airport | Benalla Airport
    "YBMA": "ISA",  # medium_airport | Mount Isa Airport
    "YBMK": "MKY",  # medium_airport | Mackay Airport
    "YBNA": "BNK",  # medium_airport | Ballina Byron Gateway Airport
    "YBNS": "BSJ",  # medium_airport | Bairnsdale Airport
    "YBOK": "OKY",  # medium_airport | Oakey Army Aviation Centre
    "YBOU": "BQL",  # medium_airport | Boulia Airport
    "YBPN": "PPP",  # medium_airport | Proserpine Whitsunday Coast Airport
    "YBRK": "ROK",  # medium_airport | Rockhampton Airport
    "YBRM": "BME",  # large_airport | Broome International Airport
    "YBRN": "BZD",  # medium_airport | Balranald Airport
    "YBRW": "BWQ",  # medium_airport | Brewarrina Airport
    "YBSU": "MCY",  # large_airport | Sunshine Coast Airport
    "YBTH": "BHS",  # medium_airport | Bathurst Airport
    "YBTI": "BRT",  # medium_airport | Bathurst Island Airport
    "YBTL": "TSV",  # medium_airport | Townsville Airport / RAAF Base Townsville
    "YBTR": "BLT",  # medium_airport | Blackwater Airport
    "YBUD": "BDB",  # medium_airport | Bundaberg Airport
    "YBWP": "WEI",  # medium_airport | Weipa Airport
    "YBWW": "WTB",  # large_airport | Toowoomba Wellcamp Airport
    "YCAR": "CVQ",  # medium_airport | Carnarvon Airport
    "YCBA": "CAZ",  # medium_airport | Cobar Airport
    "YCBB": "COJ",  # medium_airport | Coonabarabran Airport
    "YCBP": "CPD",  # medium_airport | Coober Pedy Airport
    "YCCA": "CCL",  # medium_airport | Chinchilla Airport
    "YCCY": "CNJ",  # medium_airport | Cloncurry Airport
    "YCDU": "CED",  # medium_airport | Ceduna Airport
    "YCEE": "CVC",  # medium_airport | Cleve Airport
    "YCFS": "CFS",  # medium_airport | Coffs Harbour Airport
    "YCIN": "DCN",  # medium_airport | RAAF Base Curtin
    "YCKN": "CTN",  # medium_airport | Cooktown Airport
    "YCMT": "CMQ",  # medium_airport | Clermont Airport
    "YCMU": "CMA",  # medium_airport | Cunnamulla Airport
    "YCNM": "CNB",  # medium_airport | Coonamble Airport
    "YCOE": "CUQ",  # medium_airport | Coen Airport
    "YCOM": "OOM",  # medium_airport | Cooma Snowy Mountains Airport
    "YCOR": "CWW",  # medium_airport | Corowa Airport
    "YCRG": "CYG",  # medium_airport | Corryong Airport
    "YCTM": "CMD",  # medium_airport | Cootamundra Airport
    "YCWR": "CWT",  # medium_airport | Cowra Airport
    "YDBI": "DRN",  # medium_airport | Dirranbandi Airport
    "YDBY": "DRB",  # medium_airport | Derby Airport
    "YDLQ": "DNQ",  # medium_airport | Deniliquin Airport
    "YDPO": "DPO",  # medium_airport | Devonport Airport
    "YDYS": "DYA",  # medium_airport | Dysart Airport
    "YECH": "ECH",  # medium_airport | Echuca Airport
    "YELD": "ELC",  # medium_airport | Elcho Island Airport
    "YEML": "EMD",  # medium_airport | Emerald Airport
    "YESP": "EPR",  # medium_airport | Esperance Airport
    "YEWA": "WHB",  # medium_airport | Eliwana
    "YFBS": "FRB",  # medium_airport | Forbes Airport
    "YFRT": "FOS",  # medium_airport | Forrest Airport
    "YFTZ": "FIZ",  # medium_airport | Fitzroy Crossing Airport
    "YGDH": "GUH",  # medium_airport | Gunnedah Airport
    "YGEL": "GET",  # medium_airport | Geraldton Airport
    "YGFN": "GFN",  # medium_airport | Clarence Valley Regional Airport
    "YGLA": "GLT",  # medium_airport | Gladstone Airport
    "YGLB": "GUL",  # medium_airport | Goulburn Airport
    "YGLI": "GLI",  # medium_airport | Glen Innes Airport
    "YGPT": "GPN",  # medium_airport | Garden Point Airport
    "YGTE": "GTE",  # medium_airport | Groote Eylandt Airport
    "YGTH": "GFF",  # medium_airport | Griffith Airport
    "YHAY": "HXX",  # medium_airport | Hay Airport
    "YHBA": "HVB",  # medium_airport | Hervey Bay Airport
    "YHID": "HID",  # medium_airport | Horn Island Airport
    "YHLC": "HCQ",  # medium_airport | Halls Creek Airport
    "YHML": "HLT",  # medium_airport | Hamilton Airport
    "YHOT": "MHU",  # medium_airport | Mount Hotham Airport
    "YHPN": "HTU",  # medium_airport | Hopetoun Airport
    "YHSM": "HSM",  # medium_airport | Horsham Airport
    "YIVL": "IVR",  # medium_airport | Inverell Airport
    "YKER": "KRA",  # medium_airport | Kerang Airport
    "YKII": "KNS",  # medium_airport | King Island Airport
    "YKMP": "KPS",  # medium_airport | Kempsey Airport
    "YKOW": "KWM",  # medium_airport | Kowanyama Airport
    "YKRY": "KGY",  # medium_airport | Kingaroy Airport
    "YKSC": "KGC",  # medium_airport | Kingscote Airport
    "YLEC": "LGH",  # medium_airport | Leigh Creek Airport
    "YLEO": "LNO",  # medium_airport | Leonora Airport
    "YLHR": "IRG",  # medium_airport | Lockhart River Airport
    "YLIS": "LSY",  # medium_airport | Lismore Airport
    "YLRD": "LHG",  # medium_airport | Lightning Ridge Airport
    "YLRE": "LRE",  # medium_airport | Longreach Airport
    "YLST": "LER",  # medium_airport | Leinster Airport
    "YLTV": "TGN",  # medium_airport | Latrobe Valley Airport
    "YMAV": "AVV",  # large_airport | Melbourne Avalon International Airport
    "YMAY": "ABX",  # medium_airport | Albury Airport
    "YMBA": "MRG",  # medium_airport | Mareeba Airport
    "YMDG": "DGE",  # medium_airport | Mudgee Airport
    "YMEK": "MKR",  # medium_airport | Meekatharra Airport
    "YMEN": "MEB",  # medium_airport | Melbourne Essendon Airport
    "YMER": "MIM",  # medium_airport | Merimbula Airport
    "YMGD": "MNG",  # medium_airport | Maningrida Airport
    "YMHB": "HBA",  # large_airport | Hobart International Airport
    "YMIA": "MQL",  # medium_airport | Mildura Airport
    "YMLT": "LST",  # medium_airport | Launceston Airport
    "YMMB": "MBW",  # medium_airport | Melbourne Moorabbin Airport
    "YMML": "MEL",  # large_airport | Melbourne Airport
    "YMNE": "WME",  # medium_airport | Mount Keith Airport
    "YMOG": "MMG",  # medium_airport | Mount Magnet Airport
    "YMOR": "MRZ",  # medium_airport | Moree Airport
    "YMRB": "MOV",  # medium_airport | Moranbah Airport
    "YMRE": "RRE",  # medium_airport | Marree Airport
    "YMRY": "MYA",  # medium_airport | Moruya Airport
    "YMTG": "MGB",  # medium_airport | Mount Gambier Airport
    "YNAR": "NRA",  # medium_airport | Narrandera Airport
    "YNBR": "NAA",  # medium_airport | Narrabri Airport
    "YNGU": "RPM",  # medium_airport | Ngukurr Airport
    "YNRM": "QRM",  # medium_airport | Narromine Airport
    "YNTN": "NTN",  # medium_airport | Normanton Airport
    "YNWN": "ZNE",  # medium_airport | Newman Airport
    "YORG": "OAG",  # medium_airport | Orange Airport
    "YPAD": "ADL",  # large_airport | Adelaide International Airport
    "YPAG": "PUG",  # medium_airport | Port Augusta Airport
    "YPBO": "PBO",  # medium_airport | Paraburdoo Airport
    "YPCC": "CCK",  # large_airport | Cocos (Keeling) Islands Airport
    "YPDN": "DRW",  # large_airport | Darwin International Airport / RAAF Darwin
    "YPGV": "GOV",  # medium_airport | Gove Airport
    "YPIR": "PPI",  # medium_airport | Port Pirie Airport
    "YPJT": "JAD",  # medium_airport | Perth Jandakot Airport
    "YPKA": "KTA",  # medium_airport | Karratha Airport
    "YPKG": "KGI",  # medium_airport | Kalgoorlie Boulder Airport
    "YPKS": "PKE",  # medium_airport | Parkes Airport
    "YPKT": "PKT",  # medium_airport | Port Keats Airport
    "YPKU": "KNX",  # medium_airport | East Kimberley Regional (Kununurra) Airport
    "YPLC": "PLO",  # medium_airport | Port Lincoln Airport
    "YPLM": "LEA",  # medium_airport | Learmonth Airport
    "YPMQ": "PQQ",  # medium_airport | Port Macquarie Airport
    "YPOD": "PTJ",  # medium_airport | Portland Airport
    "YPPD": "PHE",  # large_airport | Port Hedland International Airport
    "YPPH": "PER",  # large_airport | Perth International Airport
    "YPTN": "KTR",  # medium_airport | Tindal Airport
    "YPXM": "XCH",  # medium_airport | Christmas Island International Airport
    "YQLP": "ULP",  # medium_airport | Quilpie Airport
    "YREN": "RMK",  # medium_airport | Renmark Airport
    "YROM": "RMA",  # medium_airport | Roma Airport
    "YSBK": "BWU",  # medium_airport | Sydney Bankstown Airport
    "YSCB": "CBR",  # medium_airport | Canberra Airport
    "YSCN": "CDU",  # medium_airport | Camden Airport
    "YSDU": "DBO",  # medium_airport | Dubbo City Regional Airport
    "YSHK": "MJK",  # medium_airport | Shark Bay Airport
    "YSHL": "WOL",  # medium_airport | Shellharbour Airport
    "YSHT": "SHT",  # medium_airport | Shepparton Airport
    "YSMI": "SIO",  # medium_airport | Smithton Airport
    "YSNB": "SNB",  # medium_airport | Snake Bay Airport
    "YSNF": "NLK",  # medium_airport | Norfolk Island International Airport
    "YSNW": "NOA",  # medium_airport | Naval Air Station Nowra - HMAS Albatross
    "YSRI": "XRH",  # medium_airport | RAAF Base Richmond
    "YSSY": "SYD",  # large_airport | Sydney Kingsford Smith International Airport
    "YSTW": "TMW",  # medium_airport | Tamworth Airport
    "YSWG": "WGA",  # medium_airport | Wagga Wagga Airport
    "YSWH": "SWH",  # medium_airport | Swan Hill Airport
    "YSWL": "SWC",  # medium_airport | Stawell Airport
    "YTEF": "TEF",  # medium_airport | Telfer Airport
    "YTEM": "TEM",  # medium_airport | Temora Airport
    "YTGM": "XTG",  # medium_airport | Thargomindah Airport
    "YTIB": "TYB",  # medium_airport | Tibooburra Airport
    "YTMU": "TUM",  # medium_airport | Tumut Aerodrome
    "YTNG": "THG",  # medium_airport | Thangool Airport
    "YTNK": "TCA",  # medium_airport | Tennant Creek Airport
    "YTRE": "TRO",  # medium_airport | Taree Airport
    "YWDH": "WNR",  # medium_airport | Windorah Airport
    "YWGT": "WGT",  # medium_airport | Wangaratta Airport
    "YWHA": "WYA",  # medium_airport | Whyalla Airport
    "YWKB": "WKB",  # medium_airport | Warracknabeal Airport
    "YWLG": "WGE",  # medium_airport | Walgett Airport
    "YWLM": "NTL",  # large_airport | Newcastle Airport
    "YWLU": "WUN",  # medium_airport | Wiluna Airport
    "YWSL": "SXE",  # medium_airport | West Sale Airport
    "YWTN": "WIN",  # medium_airport | Winton Airport
    "YWWL": "WWY",  # medium_airport | West Wyalong Airport
    "YWYY": "BWT",  # medium_airport | Wynyard Airport
    "YYNG": "NGA",  # medium_airport | Young Airport
    "ZBAA": "PEK",  # large_airport | Beijing Capital International Airport
    "ZBAD": "PKX",  # large_airport | Beijing Daxing International Airport
    "ZBCD": "CDE",  # medium_airport | Chengde Puning Airport
    "ZBCF": "CIF",  # medium_airport | Chifeng Yulong Airport
    "ZBDH": "BPE",  # medium_airport | Qinhuangdao Beidaihe Airport
    "ZBDS": "DSN",  # large_airport | Ordos Ejin Horo International Airport
    "ZBDT": "DAT",  # large_airport | Datong Yungang International Airport
    "ZBER": "ERL",  # medium_airport | Erenhot Saiwusu International Airport
    "ZBES": "YIE",  # medium_airport | Arxan Yi'ershi Airport
    "ZBHD": "HDG",  # medium_airport | Handan Airport
    "ZBHH": "HET",  # large_airport | Hohhot Baita International Airport
    "ZBHZ": "HUO",  # medium_airport | Holingol Huolinhe Airport
    "ZBLA": "HLD",  # large_airport | Hulunbuir Hailar Airport
    "ZBLF": "LFQ",  # medium_airport | Linfen Yaodu Airport
    "ZBLL": "LLV",  # medium_airport | Lüliang Dawu Airport
    "ZBMZ": "NZH",  # medium_airport | Manzhouli Xijiao Airport
    "ZBOW": "BAV",  # large_airport | Baotou Donghe International Airport
    "ZBSG": "SZH",  # medium_airport | Shuozhou Zirun Airport
    "ZBSJ": "SJW",  # large_airport | Shijiazhuang Zhengding International Airport
    "ZBTJ": "TSN",  # large_airport | Tianjin Binhai International Airport
    "ZBTL": "TGO",  # medium_airport | Tongliao Airport
    "ZBUC": "UCB",  # medium_airport | Ulanqab Jining Airport
    "ZBUH": "WUA",  # medium_airport | Wuhai Airport
    "ZBXH": "XIL",  # medium_airport | Xilinhot Airport
    "ZBYC": "YCU",  # large_airport | Yuncheng Yanhu International Airport
    "ZBYN": "TYN",  # large_airport | Taiyuan Wusu International Airport
    "ZBYZ": "RLK",  # medium_airport | Bayannur Tianjitai Airport
    "ZBZJ": "ZQZ",  # medium_airport | Zhangjiakou Ningyuan Airport
    "ZBZL": "NZL",  # medium_airport | Zhalantun Genghis Khan Airport
    "ZGBH": "BHY",  # medium_airport | Beihai Fucheng Airport
    "ZGBS": "AEB",  # medium_airport | Baise (Bose) Bama Airport
    "ZGCD": "CGD",  # medium_airport | Changde Taohuayuan Airport
    "ZGCJ": "HJJ",  # medium_airport | Huaihua Zhijiang Airport
    "ZGCZ": "HCZ",  # medium_airport | Chenzhou Beihu Airport
    "ZGDY": "DYG",  # large_airport | Zhangjiajie Hehua International Airport
    "ZGFS": "FUO",  # medium_airport | Foshan Shadi Airport
    "ZGGG": "CAN",  # large_airport | Guangzhou Baiyun International Airport
    "ZGHA": "CSX",  # large_airport | Changsha Huanghua International Airport
    "ZGHC": "HCJ",  # medium_airport | Hechi Jinchengjiang Airport
    "ZGHZ": "HUZ",  # medium_airport | Huizhou Pingtan Airport
    "ZGKL": "KWL",  # large_airport | Guilin Liangjiang International Airport
    "ZGLG": "LLF",  # medium_airport | Yongzhou Lingling Airport
    "ZGNN": "NNG",  # large_airport | Nanning Wuxu International Airport
    "ZGOW": "SWA",  # large_airport | Jieyang Chaoshan International Airport
    "ZGSD": "ZUH",  # large_airport | Zhuhai Jinwan Airport
    "ZGSY": "WGN",  # medium_airport | Shaoyang Wugang Airport
    "ZGSZ": "SZX",  # large_airport | Shenzhen Bao'an International Airport
    "ZGWZ": "WUZ",  # medium_airport | Wuzhou Xijiang Airport
    "ZGYL": "YLX",  # medium_airport | Yulin Fumian Airport
    "ZGYY": "YYA",  # medium_airport | Yueyang Sanhe Airport
    "ZGZH": "LZH",  # medium_airport | Liuzhou Bailian Airport / Bailian Air Base
    "ZGZJ": "ZHA",  # large_airport | Zhanjiang Wuchuan International Airport
    "ZHCC": "CGO",  # large_airport | Zhengzhou Xinzheng International Airport
    "ZHEC": "EHU",  # large_airport | Ezhou Huahu International Airport
    "ZHES": "ENH",  # medium_airport | Enshi Xujiaping Airport
    "ZHGH": "LHK",  # medium_airport | Guangzhou MR Air Base / Guanghua Airport
    "ZHHH": "WUH",  # large_airport | Wuhan Tianhe International Airport
    "ZHJZ": "SHS",  # medium_airport | Jingzhou Shashi Airport
    "ZHLY": "LYA",  # large_airport | Luoyang Beijiao Airport
    "ZHSN": "HPG",  # medium_airport | Shennongjia Hongping Airport
    "ZHSY": "WDS",  # medium_airport | Shiyan Wudangshan Airport
    "ZHXF": "XFN",  # medium_airport | Xiangyang Liuji Airport
    "ZHXY": "XAI",  # medium_airport | Xinyang Minggang Airport
    "ZHYC": "YIH",  # medium_airport | Yichang Sanxia Airport
    "ZJHK": "HAK",  # large_airport | Haikou Meilan International Airport
    "ZJQH": "BAR",  # medium_airport | Qionghai Bo'ao Airport
    "ZJSY": "SYX",  # large_airport | Sanya Phoenix International Airport
    "ZKHM": "RGO",  # medium_airport | Orang (Chongjin) Airport
    "ZKPY": "FNJ",  # large_airport | Pyongyang Sunan International Airport
    "ZKSD": "DSO",  # medium_airport | Sondok Airport
    "ZKWS": "WOS",  # medium_airport | Wonsan Kalma Airport
    "ZLDH": "DNH",  # large_airport | Dunhuang Mogao International Airport
    "ZLGL": "GMQ",  # medium_airport | Golog Maqên Airport
    "ZLGM": "GOQ",  # medium_airport | Golmud Airport
    "ZLGY": "GYU",  # medium_airport | Guyuan Liupanshan Airport
    "ZLHX": "HTT",  # medium_airport | Huatugou Airport
    "ZLHZ": "HZG",  # medium_airport | Hanzhong Chenggu Airport
    "ZLIC": "INC",  # large_airport | Yinchuan Hedong International Airport
    "ZLJQ": "JGN",  # large_airport | Jiayuguan International Airport
    "ZLLL": "LHW",  # large_airport | Lanzhou Zhongchuan International Airport
    "ZLLN": "LNL",  # medium_airport | Longnan Chengzhou Airport
    "ZLQY": "IQN",  # medium_airport | Qingyang Xifeng Airport
    "ZLSN": "SIA",  # medium_airport | Xi'an Xiguan Airport
    "ZLTS": "THQ",  # medium_airport | Tianshui Maijishan Airport
    "ZLXH": "GXH",  # medium_airport | Gannan Xiahe Airport
    "ZLXN": "XNN",  # large_airport | Xining Caojiabao International Airport
    "ZLXY": "XIY",  # large_airport | Xi'an Xianyang International Airport
    "ZLYA": "ENY",  # medium_airport | Yan'an Nanniwan Airport
    "ZLYL": "UYN",  # medium_airport | Yulin Yuyang Airport
    "ZLYS": "YUS",  # medium_airport | Yushu Batang Airport
    "ZLZW": "ZHY",  # medium_airport | Zhongwei Shapotou Airport
    "ZLZY": "YZY",  # medium_airport | Zhangye Ganzhou Airport
    "ZMAH": "AVK",  # medium_airport | Arvaikheer Airport
    "ZMAT": "LTI",  # medium_airport | Altai Airport
    "ZMBH": "BYN",  # medium_airport | Bayankhongor Airport
    "ZMBN": "UGA",  # medium_airport | Bulgan Airport
    "ZMBU": "UUN",  # medium_airport | Baruun Urt Airport
    "ZMCD": "COQ",  # medium_airport | Choibalsan Airport
    "ZMCK": "UBN",  # large_airport | Ulaanbaatar Chinggis Khaan International Airport
    "ZMDZ": "DLZ",  # medium_airport | Dalanzadgad Airport
    "ZMKD": "HVD",  # medium_airport | Khovd Airport
    "ZMMN": "MXV",  # medium_airport | Mörön Airport
    "ZMUB": "ULN",  # large_airport | Buyant-Ukhaa International Airport
    "ZMUG": "ULO",  # medium_airport | Ulaangom Airport
    "ZMUL": "ULG",  # medium_airport | Ölgii Mongolei International Airport
    "ZPBS": "BSD",  # medium_airport | Baoshan Yunrui Airport
    "ZPCW": "CWJ",  # medium_airport | Cangyuan Washan Airport
    "ZPDL": "DLU",  # medium_airport | Dali Fengyi Airport
    "ZPDQ": "DIG",  # medium_airport | Diqing Shangri-La Airport
    "ZPJH": "JHG",  # large_airport | Xishuangbanna Gasa International Airport
    "ZPJM": "JMJ",  # medium_airport | Lancang Jingmai Airport
    "ZPLC": "LNJ",  # medium_airport | Lincang Boshang Airport
    "ZPLJ": "LJG",  # large_airport | Lijiang Sanyi International Airport
    "ZPMS": "LUM",  # medium_airport | Dehong Mangshi International Airport
    "ZPPP": "KMG",  # large_airport | Kunming Changshui International Airport
    "ZPYM": "YUA",  # medium_airport | Yuanmou Air Base
    "ZSAM": "XMN",  # large_airport | Xiamen Gaoqi International Airport
    "ZSAQ": "AQG",  # medium_airport | Anqing Tianzhushan Airport / Anqing North Air Base
    "ZSBB": "BFU",  # medium_airport | Bengbu Renheji Airport
    "ZSCG": "CZX",  # medium_airport | Changzhou Benniu International Airport
    "ZSCN": "KHN",  # large_airport | Nanchang Changbei International Airport
    "ZSDY": "DOY",  # medium_airport | Dongying Shengli Airport
    "ZSFY": "FUG",  # medium_airport | Fuyang Xiguan Airport
    "ZSFZ": "FOC",  # large_airport | Fuzhou Changle International Airport
    "ZSHC": "HGH",  # large_airport | Hangzhou Xiaoshan International Airport
    "ZSHZ": "HZA",  # medium_airport | Heze Mudan Airport
    "ZSJD": "JDZ",  # medium_airport | Jingdezhen Luojia Airport
    "ZSJG": "JNG",  # medium_airport | Jining Da'an Airport
    "ZSJN": "TNA",  # large_airport | Jinan Yaoqiang International Airport
    "ZSJU": "JUZ",  # medium_airport | Quzhou Airport
    "ZSLG": "LYG",  # large_airport | Lianyungang Huaguoshan International Airport
    "ZSLO": "LCX",  # medium_airport | Liancheng Guanzhishan Airport
    "ZSLQ": "HYN",  # medium_airport | Taizhou Luqiao Airport
    "ZSLY": "LYI",  # medium_airport | Linyi Qiyang Airport
    "ZSNB": "NGB",  # large_airport | Ningbo Lishe International Airport
    "ZSNJ": "NKG",  # large_airport | Nanjing Lukou International Airport
    "ZSNT": "NTG",  # medium_airport | Nantong Xingdong International Airport
    "ZSOF": "HFE",  # large_airport | Hefei Xinqiao International Airport
    "ZSPD": "PVG",  # large_airport | Shanghai Pudong International Airport
    "ZSQD": "TAO",  # large_airport | Qingdao Jiaodong International Airport
    "ZSQZ": "JJN",  # large_airport | Quanzhou Jinjiang International Airport
    "ZSRG": "RUG",  # medium_airport | Rugao Air Base
    "ZSRZ": "RIZ",  # medium_airport | Rizhao Shanzihe Airport
    "ZSSH": "HIA",  # large_airport | Huai'an Lianshui Airport
    "ZSSM": "SQJ",  # medium_airport | Sanming Shaxian Airport
    "ZSSR": "SQD",  # medium_airport | Shangrao Sanqingshan Airport
    "ZSSS": "SHA",  # large_airport | Shanghai Hongqiao International Airport
    "ZSSZ": "SZV",  # medium_airport | Suzhou Guangfu Airport
    "ZSTX": "TXN",  # large_airport | Huangshan Tunxi International Airport
    "ZSWA": "WHA",  # medium_airport | Wuhu Xuanzhou Airport
    "ZSWF": "WEF",  # medium_airport | Weifang Nanyuan Airport
    "ZSWH": "WEH",  # medium_airport | Weihai Dashuibo Airport
    "ZSWX": "WUX",  # large_airport | Sunan Shuofang International Airport
    "ZSWY": "WUS",  # medium_airport | Nanping Wuyishan Airport
    "ZSWZ": "WNZ",  # large_airport | Wenzhou Longwan International Airport
    "ZSXZ": "XUZ",  # medium_airport | Xuzhou Guanyin International Airport
    "ZSYA": "YTY",  # medium_airport | Yangzhou Taizhou Airport
    "ZSYC": "YIC",  # medium_airport | Yichun Mingyueshan Airport
    "ZSYN": "YNZ",  # large_airport | Yancheng Nanyang International Airport
    "ZSYT": "YNT",  # large_airport | Yantai Penglai International Airport
    "ZSYW": "YIW",  # large_airport | Yiwu Airport
    "ZSZS": "HSN",  # large_airport | Zhoushan Putuoshan International Airport
    "ZUAL": "NGQ",  # medium_airport | Ngari Gunsa Airport
    "ZUAS": "AVA",  # medium_airport | Anshun Huangguoshu Airport
    "ZUBD": "BPX",  # medium_airport | Qamdo Bangda Airport
    "ZUBJ": "BFJ",  # medium_airport | Bijie Feixiong Airport
    "ZUCK": "CKG",  # large_airport | Chongqing Jiangbei International Airport
    "ZUDA": "DZH",  # medium_airport | Dazhou Jinya Airport
    "ZUDC": "DCY",  # medium_airport | Daocheng Yading Airport
    "ZUDJ": "DEJ",  # medium_airport | Tongren Dejiang Airport (Under Construction)
    "ZUGH": "GHN",  # medium_airport | Guanghan Airport
    "ZUGU": "GYS",  # medium_airport | Guangyuan Panlong Airport
    "ZUGY": "KWE",  # large_airport | Guiyang Longdongbao International Airport
    "ZUHY": "AHJ",  # medium_airport | Hongyuan Airport
    "ZUJZ": "JZH",  # medium_airport | Jiuzhai Huanglong Airport
    "ZUKD": "KGT",  # medium_airport | Kangding Airport
    "ZUKJ": "KJH",  # medium_airport | Kaili Huangping Airport
    "ZULS": "LXA",  # large_airport | Lhasa Gonggar International Airport
    "ZULZ": "LZO",  # medium_airport | Luzhou Yunlong Airport
    "ZUMT": "WMT",  # medium_airport | Zunyi Maotai Airport
    "ZUMY": "MIG",  # medium_airport | Mianyang Nanjiao Airport
    "ZUNP": "HZH",  # medium_airport | Liping Airport
    "ZUNZ": "LZY",  # medium_airport | Nyingchi Mainling Airport
    "ZUPS": "LPF",  # medium_airport | Liupanshui Yuezhao Airport
    "ZUQJ": "JIQ",  # medium_airport | Qianjiang Wulingshan Airport
    "ZURK": "RKZ",  # large_airport | Xigaze Peace Airport / Shigatse Air Base
    "ZUTC": "TCZ",  # medium_airport | Tengchong Tuofeng Airport
    "ZUTF": "TFU",  # large_airport | Chengdu Tianfu International Airport
    "ZUTR": "TEN",  # medium_airport | Tongren Fenghuang Airport
    "ZUUU": "CTU",  # large_airport | Chengdu Shuangliu International Airport
    "ZUWL": "CQW",  # medium_airport | Chongqing Xiannüshan Airport
    "ZUXC": "XIC",  # medium_airport | Xichang Qingshan Airport
    "ZUYB": "YBP",  # medium_airport | Yibin Wuliangye Airport
    "ZUYI": "ACX",  # medium_airport | Xingyi Wanfenglin Airport
    "ZUZH": "PZI",  # medium_airport | Panzhihua Bao'anying Airport
    "ZUZY": "ZYI",  # medium_airport | Zunyi Xinzhou Airport
    "ZWAK": "AKU",  # medium_airport | Aksu Hongqipo Airport
    "ZWAT": "AAT",  # medium_airport | Altay Xuedu Airport
    "ZWBL": "BPL",  # medium_airport | Bole Alashankou Airport
    "ZWCM": "IQM",  # medium_airport | Qiemo Yudu Airport
    "ZWFY": "FYN",  # medium_airport | Fuyun Koktokay Airport
    "ZWHM": "HMI",  # medium_airport | Hami Airport
    "ZWKL": "KRL",  # medium_airport | Korla Licheng Airport
    "ZWKN": "KJI",  # medium_airport | Burqin Kanas Airport
    "ZWLK": "DHH",  # medium_airport | Barkol Dahe Airport
    "ZWNL": "NLT",  # medium_airport | Xinyuan Nalati Airport
    "ZWRQ": "RQA",  # medium_airport | Ruoqiang Loulan Airport
    "ZWSC": "QSZ",  # medium_airport | Shache Airport
    "ZWSH": "KHG",  # large_airport | Kashgar Laining International Airport
    "ZWSS": "SXJ",  # medium_airport | Shanshan Airport
    "ZWTL": "TLQ",  # medium_airport | Turpan Jiaohe Airport
    "ZWTN": "HTN",  # medium_airport | Hotan Airport
    "ZWWW": "URC",  # large_airport | Ürümqi Tianshan International Airport
    "ZYAS": "AOG",  # medium_airport | Anshan Teng'ao Airport / Anshan Air Base
    "ZYBA": "DBC",  # medium_airport | Baicheng Chang'an Airport
    "ZYBS": "NBS",  # medium_airport | Changbaishan Airport
    "ZYCC": "CGQ",  # large_airport | Changchun Longjia International Airport
    "ZYCY": "CHG",  # medium_airport | Chaoyang Airport
    "ZYDD": "DDG",  # medium_airport | Dandong Langtou International Airport
    "ZYDU": "DTU",  # medium_airport | Wudalianchi Dedu Airport
    "ZYFY": "FYJ",  # medium_airport | Fuyuan Dongji Airport
    "ZYHB": "HRB",  # large_airport | Harbin Taiping International Airport
    "ZYHE": "HEK",  # medium_airport | Heihe Aihui Airport
    "ZYJD": "JGD",  # medium_airport | Daxing'anling Elunchun Airport
    "ZYJM": "JMU",  # medium_airport | Jiamusi Songjiang International Airport
    "ZYJS": "JSJ",  # medium_airport | Jiansanjiang Shidi Airport
    "ZYJX": "JXA",  # medium_airport | Jixi Xingkaihu Airport
    "ZYJZ": "JNZ",  # medium_airport | Jinzhou Bay Airport
    "ZYLD": "LDS",  # medium_airport | Yichun Lindu Airport
    "ZYMD": "MDG",  # medium_airport | Mudanjiang Hailang International Airport
    "ZYMH": "OHE",  # medium_airport | Mohe Gulian Airport
    "ZYQQ": "NDG",  # large_airport | Qiqihar Sanjiazi Airport
    "ZYSQ": "YSQ",  # medium_airport | Songyuan Chaganhu Airport
    "ZYTL": "DLC",  # large_airport | Dalian Zhoushuizi International Airport
    "ZYTN": "TNH",  # medium_airport | Tonghua Sanyuanpu Airport
    "ZYTX": "SHE",  # large_airport | Shenyang Taoxian International Airport
    "ZYXC": "XEN",  # medium_airport | Xingcheng Air Base
    "ZYYJ": "YNJ",  # medium_airport | Yanji Chaoyangchuan Airport
    "ZYYK": "YKH",  # medium_airport | Yingkou Lanqi Airport
}


def icao_to_iata(code: Optional[str]) -> str:
    normalized = str(code or "").strip().upper()
    if not normalized:
        return ""
    return ICAO_TO_IATA.get(normalized, normalized)
