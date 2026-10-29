"""Local ICAO-to-IATA airline codes for chart labels only.

Verified: 2026-10-29. This is a partial reference, not a live airline registry.
The IATA member directory supplies the base records; official airport,
airline and aviation-authority pages supplement carriers absent from that
snapshot. Unknown codes stay unchanged. Do not use this table to rewrite
API queries, original flight identifiers, assignment keys or stored data.
"""
from __future__ import annotations

import re

VERIFIED_ON = "2026-10-29"
BASE_SOURCE = "https://www.iata.org/en/about/members/airline-list/"

# Official pages for records supplementing the IATA member snapshot.
SUPPLEMENTAL_SOURCES = {
    "ABL": "https://www.narita-airport.jp/en/flight/airline-search/abl/",
    "AIQ": "https://www.narita-airport.jp/en/flight/airline-search/aiq/",
    "AJX": "https://airport.kr/ap_en/1408/subview.do",
    "APG": "https://www.narita-airport.jp/en/flight/airline-search/apg/",
    "APJ": "https://www.narita-airport.jp/en/flight/airline-search/apj/",
    "ASV": "https://www.narita-airport.jp/en/flight/airline-search/asv/",
    "AWQ": "https://www.caam.gov.my/legislation-regulations/general/schedule-operators/",
    "AXM": "https://www.caam.gov.my/legislation-regulations/general/schedule-operators/",
    "CDC": "https://www.iata.org/en/about/members/airline-list/loong-air/533/",
    "CHH": "https://www.narita-airport.jp/en/flight/airline-search/chh/",
    "CKS": "https://airport.kr/ap_en/1408/subview.do",
    "CQH": "https://www.narita-airport.jp/en/flight/airline-search/cqh/",
    "DAL": "https://www.narita-airport.jp/en/flight/airline-search/dal/",
    "DHK": "https://airport.kr/ap_en/1408/subview.do",
    "DLH": "https://araib.molit.go.kr/sroa/USR/WPGE0201/m_35700/DTL.jsp",
    "EOK": "https://www.narita-airport.jp/en/flight/airline-search/eok/",
    "ESR": "https://www.narita-airport.jp/en/flight/airline-search/esr/",
    "ETD": "https://www.narita-airport.jp/en/flight/airline-search/etd/",
    "ETH": "https://www.narita-airport.jp/en/flight/airline-search/eth/",
    "EVA": "https://www.narita-airport.jp/en/flight/airline-search/eva/",
    "FDX": "https://airport.kr/ap_en/1408/subview.do",
    "FIN": "https://www.narita-airport.jp/en/flight/airline-search/fin/",
    "GGC": "https://airport.kr/ap_en/1408/subview.do",
    "GIA": "https://www.narita-airport.jp/en/flight/airline-search/gia/",
    "HLF": "https://airport.kr/ap_en/1408/subview.do",
    "ICV": "https://airport.kr/ap_en/1408/subview.do",
    "JJP": "https://www.narita-airport.jp/en/flight/airline-search/jjp/",
    "JST": "https://airport.kr/ap_en/1408/subview.do",
    "KAL": "https://www.narita-airport.jp/en/flight/airline-search/kal/",
    "KLM": "https://www.narita-airport.jp/en/flight/airline-search/klm/",
    "LAO": "https://airport.kr/ap_en/1408/subview.do",
    "LHA": "https://airport.kr/ap_en/1408/subview.do",
    "LOT": "https://www.narita-airport.jp/en/flight/airline-search/lot/",
    "MAA": "https://airport.kr/ap_en/1408/subview.do",
    "MAS": "https://www.narita-airport.jp/en/flight/airline-search/mas/",
    "MFX": "https://airport.kr/ap_en/1408/subview.do",
    "MGL": "https://airport.kr/ap_en/1408/subview.do",
    "MMA": "https://www.iata.org/en/about/members/airline-list/myanmar-airways-international/475/",
    "MPH": "https://airport.kr/ap_en/1408/subview.do",
    "PTA": "https://www.narita-airport.jp/en/flight/airline-search/pta/",
    "QNT": "https://airport.kr/ap_en/1408/subview.do",
    "SPQ": "https://airport.kr/ap_en/1408/subview.do",
    "SWM": "https://airport.kr/ap_en/1408/subview.do",
    "TAX": "https://www.narita-airport.jp/en/flight/airline-search/tax/",
    "TTW": "https://www.narita-airport.jp/en/flight/airline-search/ttw/",
    "TUA": "https://airport.kr/ap_en/1408/subview.do",
    "TZP": "https://airport.kr/ap_en/1408/subview.do",
    "UAE": "https://www.narita-airport.jp/en/flight/airline-search/uae/",
    "XAX": "https://www.caam.gov.my/legislation-regulations/general/schedule-operators/",
}

ICAO_TO_IATA = {
    "AAL": "AA",  # American Airlines
    "AAR": "OZ",  # Asiana Airlines
    "ABD": "CC",  # Air Atlanta Icelandic
    "ABL": "BX",  # Air Busan
    "ABR": "5H",  # ASL Airlines Ireland
    "ABX": "GB",  # ABX Air
    "ABY": "G9",  # Air Arabia
    "ACA": "AC",  # Air Canada
    "ACI": "SB",  # Aircalin
    "AEA": "UX",  # Air Europa
    "AEE": "A3",  # Aegean Airlines
    "AEZ": "XZ",  # Aeroitalia
    "AFL": "SU",  # Aeroflot
    "AFR": "AF",  # Air France
    "AFW": "AW",  # Africa World Airlines
    "AHK": "LD",  # Air Hong Kong
    "AHY": "J2",  # Azerbaijan Airlines
    "AIA": "8R",  # Amelia
    "AIC": "AI",  # Air India
    "AIH": "KJ",  # AIRZETA
    "AIQ": "FD",  # Thai AirAsia
    "AIZ": "IZ",  # Arkia Israeli Airlines
    "AJX": "NQ",  # Air Japan
    "AKJ": "QP",  # Akasa Air
    "ALK": "UL",  # SriLankan Airlines
    "AMU": "NX",  # Air Macau
    "AMX": "AM",  # Aeromexico
    "ANA": "NH",  # ANA
    "ANE": "YW",  # Air Nostrum
    "ANG": "PX",  # Air Niugini
    "ANZ": "NZ",  # Air New Zealand
    "APF": "HP",  # PopulAir
    "APG": "Z2",  # Philippines AirAsia
    "APJ": "MM",  # Peach Aviation
    "APK": "P4",  # Air Peace
    "APZ": "YP",  # Air Premia
    "ARG": "AR",  # Aerolineas Argentinas
    "ASA": "AS",  # Alaska Airlines
    "ASL": "JU",  # Air Serbia
    "ASV": "RS",  # Air Seoul
    "ATC": "TC",  # Air Tanzania
    "AUA": "OS",  # Austrian
    "AUL": "5N",  # Smartavia
    "AVA": "AV",  # Avianca
    "AVN": "NF",  # Air Vanuatu
    "AWA": "2A",  # Air Astra
    "AWQ": "QZ",  # Indonesia AirAsia
    "AXB": "IX",  # Air India Express
    "AXM": "AK",  # AirAsia Malaysia
    "AZG": "7L",  # Silk Way West Airlines
    "AZP": "ZP",  # Paranair
    "AZU": "AD",  # Azul Brazilian Airlines
    "BAV": "QH",  # Bamboo Airways
    "BAW": "BA",  # British Airways
    "BBC": "BG",  # Biman Bangladesh Airlines
    "BBG": "BZ",  # Blue Bird Airways
    "BBL": "0B",  # BBN Airlines Indonesia
    "BBT": "B5",  # BBN Airlines
    "BDR": "J4",  # Badr Airlines
    "BEL": "SN",  # Brussels Airlines
    "BHS": "UP",  # Bahamasair
    "BKP": "PG",  # Bangkok Airways
    "BOT": "BP",  # Air Botswana
    "BOV": "OB",  # BoA Boliviana de Aviacion
    "BRU": "B2",  # Belavia Belarusian Airlines
    "BRX": "TF",  # Braathens Regional Airways
    "BTI": "BT",  # Air Baltic
    "BTK": "ID",  # Batik Air
    "BWA": "BW",  # Caribbean Airlines
    "CAL": "CI",  # China Airlines
    "CBJ": "JD",  # Capital Airlines
    "CCA": "CA",  # Air China
    "CCM": "XK",  # Air Corsica
    "CDC": "GJ",  # Loong Air
    "CDG": "SC",  # Shandong Airlines
    "CEB": "5J",  # Cebu Pacific
    "CES": "MU",  # China Eastern
    "CGH": "GT",  # Air Guilin
    "CGN": "9H",  # Air Changan
    "CHB": "PN",  # West Air
    "CHG": "X7",  # Challenge Airlines (BE)
    "CHH": "HU",  # Hainan Airlines
    "CJT": "W8",  # Cargojet Airways
    "CKK": "CK",  # China Cargo Airlines
    "CKS": "K4",  # Kalitta Air
    "CLG": "CE",  # Chalair
    "CLX": "CV",  # Cargolux
    "CPA": "CX",  # Cathay Pacific
    "CQH": "9C",  # Spring Airlines
    "CRC": "QC",  # Camair-Co
    "CRK": "HX",  # Hong Kong Airlines
    "CSC": "3U",  # Sichuan Airlines
    "CSH": "FM",  # Shanghai Airlines
    "CSN": "CZ",  # China Southern Airlines
    "CSS": "O3",  # SF Airlines
    "CSW": "CS",  # Chair Airlines
    "CSZ": "ZH",  # Shenzhen Airlines
    "CUH": "UQ",  # Urumqi Air
    "CXA": "MF",  # Xiamen Airlines
    "CYF": "U8",  # TUS Airways
    "CYZ": "CF",  # China Postal Airlines
    "DAH": "AH",  # Air Algérie
    "DAL": "DL",  # Delta Air Lines
    "DHK": "D0",  # DHL Air
    "DKH": "HO",  # Juneyao Airlines
    "DLA": "EN",  # Air Dolomiti
    "DLH": "LH",  # Lufthansa
    "DTA": "DT",  # TAAG Angola Airlines
    "DWI": "DM",  # Arajet
    "EIN": "EI",  # Aer Lingus
    "EOK": "RF",  # Aero K
    "ESR": "ZE",  # Eastar Jet
    "ETD": "EY",  # Etihad Airways
    "ETH": "ET",  # Ethiopian Airlines
    "EVA": "BR",  # EVA Air
    "EVE": "E9",  # Iberojet Airlines
    "FCM": "N7",  # Norra
    "FDX": "FX",  # FedEx Express
    "FIN": "AY",  # Finnair
    "FLI": "RC",  # Atlantic Airways
    "FPO": "5O",  # ASL Airlines France
    "FWI": "TX",  # Air Caraibes
    "GAP": "2P",  # PAL Express
    "GCR": "GS",  # Tianjin Airlines
    "GEL": "D4",  # Airline GEO SKY
    "GGC": "GG",  # Sky Lease Cargo
    "GIA": "GA",  # Garuda Indonesia
    "GJM": "RE",  # Airhub Airlines
    "GLG": "2K",  # Avianca Ecuador
    "GRL": "GL",  # Air Greenland
    "GTI": "5Y",  # Atlas Air
    "HKC": "RH",  # Hong Kong Air Cargo
    "HKE": "UO",  # Hong Kong Express Airways
    "HLF": "I9",  # Central Airlines
    "HVN": "VN",  # Vietnam Airlines
    "HXA": "G5",  # China Express Airlines
    "HYT": "YG",  # YTO Cargo Airlines
    "IAN": "QI",  # Ibom Air
    "IBB": "NT",  # Binter Canarias
    "IBE": "IB",  # IBERIA
    "ICE": "FI",  # Icelandair
    "ICL": "5C",  # Challenge Airlines (IL)
    "ICV": "C8",  # Cargolux Italia
    "IGO": "6E",  # IndiGo
    "IRA": "IR",  # Iran Air
    "IRB": "B9",  # Iran Airtour Airline
    "IRC": "EP",  # Iran Aseman Airlines
    "ISR": "6H",  # Israir
    "ITY": "AZ",  # ITA Airways
    "JAL": "JL",  # Japan Airlines
    "JAP": "JZ",  # JetSMART Peru
    "JAT": "JA",  # JetSMART Chile
    "JAV": "R5",  # Jordan Aviation
    "JBU": "B6",  # JetBlue
    "JDL": "JG",  # JD Airlines
    "JEC": "J6",  # JetSMART Colombia
    "JES": "WJ",  # JetSMART Argentina
    "JJA": "7C",  # Jeju Air
    "JJP": "GK",  # Jetstar Japan
    "JNA": "LJ",  # Jin Air
    "JST": "JQ",  # Jetstar Airways
    "JTA": "NU",  # Japan Transocean Air
    "JTD": "JP",  # Jettime
    "JZR": "J9",  # Jazeera Airways
    "KAL": "KE",  # Korean Air
    "KAR": "EO",  # Ikar
    "KEM": "5Z",  # CemAir
    "KHV": "K6",  # Air Cambodia
    "KLM": "KL",  # KLM
    "KMF": "RQ",  # Kam Air
    "KOR": "JS",  # Air Koryo
    "KRP": "V3",  # Carpatair
    "KZR": "KC",  # Air Astana
    "KZU": "GO",  # ULS Airlines Cargo
    "LAO": "QV",  # Lao Airlines
    "LAV": "AP",  # Albastar
    "LBT": "BJ",  # Nouvelair
    "LHA": "GI",  # Longhao Airlines
    "LMU": "UJ",  # AlMasria Universal Airlines
    "LNK": "4Z",  # Airlink
    "LOT": "LO",  # LOT Polish Airlines
    "LRC": "LR",  # Avianca Costa Rica
    "LZB": "FB",  # Bulgaria Air
    "MAA": "M7",  # MasAir
    "MAS": "MH",  # Malaysia Airlines
    "MAU": "MK",  # Air Mauritius
    "MFX": "C6",  # Centrum Air
    "MGL": "OM",  # MIAT Mongolian Airlines
    "MLH": "4X",  # Avion Express Malta
    "MMA": "8M",  # Myanmar Airways International
    "MNE": "4O",  # Air Montenegro
    "MNG": "M0",  # Aero Mongolia
    "MPH": "MP",  # Martinair
    "MSA": "M4",  # Poste Air Cargo
    "MSC": "SM",  # Air Cairo
    "MXD": "OD",  # Batik Air Malaysia
    "NUA": "UN",  # United Nigeria Airlines
    "NVD": "X9",  # Avion Express
    "NWS": "N4",  # Nordwind Airlines
    "OAL": "OA",  # Olympic Air
    "OBS": "6O",  # Iberojet
    "OKA": "BK",  # Okay Airways
    "OLA": "OF",  # Overland Airways
    "OMA": "WY",  # Oman Air
    "OMS": "OV",  # Salam Air
    "PAC": "PO",  # Polar Air Cargo
    "PAL": "PR",  # Philippine Airlines
    "PER": "UF",  # PAS
    "PFZ": "P0",  # Proflight Zambia
    "PGA": "NI",  # PGA-Portugalia Airlines
    "PGT": "PC",  # Pegasus Airlines
    "PIA": "PK",  # Pakistan International Airlines
    "PLM": "EB",  # Wamos Air
    "POE": "PD",  # Porter Airlines
    "PRF": "PW",  # Precision Air
    "PTA": "WE",  # Parata Air
    "PUE": "PU",  # Plus Ultra
    "PVG": "P6",  # Privilege Style
    "QAZ": "IQ",  # Qazaq Air
    "QDA": "QW",  # Qingdao Airlines
    "QFA": "QF",  # Qantas
    "QNT": "HH",  # Qanot Sharq
    "QTR": "QR",  # Qatar Airways
    "RAM": "AT",  # Royal Air Maroc
    "RBA": "BI",  # Royal Brunei
    "REU": "UU",  # Air Austral
    "RIV": "GP",  # APG Airlines
    "RJA": "RJ",  # Royal Jordanian
    "RLH": "DR",  # Ruili Airlines
    "RLU": "7R",  # RusLine
    "ROT": "RO",  # TAROM
    "RPB": "P5",  # Aero Republica
    "RSX": "4S",  # Red Sea Airlines
    "RWD": "WB",  # RwandAir
    "RXI": "RX",  # Riyadh Air
    "RZO": "S4",  # Azores Airlines
    "SAA": "SA",  # South African Airways
    "SAS": "SK",  # SAS
    "SAT": "SP",  # SATA Air Acores
    "SBI": "S7",  # S7 Airlines
    "SCX": "SY",  # Sun Country Airlines
    "SDM": "FV",  # Rossiya Airlines
    "SEH": "GQ",  # Sky express
    "SEJ": "SG",  # SpiceJet
    "SEY": "HM",  # Air Seychelles
    "SFR": "FA",  # Safair
    "SIA": "SQ",  # Singapore Airlines
    "SJX": "JX",  # STARLUX Airlines
    "SKK": "KP",  # ASKY
    "SKU": "H2",  # SKY Airline
    "SMR": "SZ",  # Somon Air
    "SOL": "IE",  # Solomon Airlines
    "SPQ": "9G",  # Sun PhuQuoc Airways
    "SQP": "PQ",  # SkyUp Airlines
    "STW": "2S",  # Southwind Airlines
    "SVA": "SV",  # Saudi Arabian Airlines
    "SVR": "U6",  # Ural Airlines
    "SWA": "WN",  # Southwest Airlines
    "SWM": "ZA",  # Sky Angkor Airlines
    "SWR": "LX",  # SWISS
    "SWT": "WT",  # Swiftair
    "SXS": "XQ",  # SunExpress
    "SYR": "RB",  # Syrianair
    "SZN": "HC",  # Air Senegal
    "TAI": "TA",  # TACA
    "TAP": "TP",  # TAP Air Portugal
    "TAR": "TU",  # Tunisair
    "TAX": "XJ",  # Thai AirAsia X
    "TAY": "3V",  # ASL Airlines Belgium
    "TBA": "TV",  # Xizang Airlines
    "TGU": "5U",  # TAG Airlines
    "TGW": "TR",  # Scoot
    "THA": "TG",  # Thai Airways International
    "THT": "TN",  # Air Tahiti Nui
    "THY": "TK",  # Turkish Airlines
    "TKJ": "VF",  # AJet
    "TLM": "SL",  # Thai Lion Air
    "TPC": "TY",  # Air Caledonie
    "TSC": "TS",  # Air Transat
    "TTW": "IT",  # Tigerair Taiwan
    "TUA": "T5",  # Turkmenistan Airlines
    "TUI": "X3",  # TUIfly
    "TVS": "QS",  # Smartwings
    "TWB": "TW",  # Trinity Airways
    "TWI": "TI",  # Tailwind Airlines
    "TZP": "ZG",  # ZIPAIR Tokyo
    "UAE": "EK",  # Emirates
    "UAL": "UA",  # United Airlines
    "UBG": "BS",  # US-Bangla Airlines
    "UEA": "EU",  # Chengdu Airlines
    "UIA": "B7",  # UNI AIR
    "UPS": "5X",  # UPS Airlines
    "UTA": "UT",  # UTair
    "UVL": "VO",  # Universal Air
    "UZB": "HY",  # Uzbekistan Airways
    "VAU": "VA",  # Virgin Australia
    "VIR": "VS",  # Virgin Atlantic
    "VJC": "VJ",  # Vietjet
    "VLG": "VY",  # Vueling
    "VOE": "V7",  # Volotea
    "VOI": "Y4",  # Volaris
    "VSV": "DV",  # SCAT Airlines
    "VTA": "VT",  # Air Tahiti
    "WFL": "2W",  # World2Fly
    "WHT": "WI",  # White coloured by you
    "WIF": "WF",  # Wideroe
    "WJA": "WS",  # WestJet
    "XAX": "D7",  # AirAsia X
    "YZR": "Y8",  # Suparna Airlines
}

_FLIGHT_NUMBER = re.compile(r"([A-Za-z]{3})([0-9]+[A-Za-z]?)")


def flight_label(flight: object) -> str:
    """Convert a recognized leading ICAO code, preserving number and suffix.

    Already-IATA, unknown, missing and nonstandard identifiers retain their
    existing string representation; no substring replacements are performed.
    """
    original = str(flight)
    match = _FLIGHT_NUMBER.fullmatch(original)
    if match is None:
        return original
    iata = ICAO_TO_IATA.get(match.group(1).upper())
    if iata is None:
        return original
    return iata + match.group(2)

