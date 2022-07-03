import requests
from bs4 import BeautifulSoup
from lxml import html
import requests

cookie_do_zerozero = ""


def getByIDWithFilenameSet(idd, filename, page, cookie):
    URL = "https://www.zerozero.pt/edition_matches.php?id_edicao=" + idd + "&fase_in&equipa=0&estado=&filtro=&op=calendario&page=" + page

    headers_necess = {
    "Cookie": cookie,
    "Host": "www.zerozero.pt",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "identity",
    "Connection": "keep-alive",
    "Referer": URL,
    "Sec-Fetch-Dest": "style",
    "Sec-Fetch-Mode": "no-cors",
    "Sec-Fetch-Site": "same-origin",
    "DNT": "1",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "TE": "trailers"
    }

    page = requests.get(URL, headers=headers_necess)
    print(page.status_code)

    f = open("demofile2.html", "w")
    f.write(page.text)
    f.close()

    soup = BeautifulSoup(page.content, 'html.parser')

    all_tr = soup.find(class_="zztable stats")
    strsx = ""
    for tr in all_tr:
        for x in tr:
            for y in x:
                if y.text.contains("1234"):
                    break
                strsx = strsx + y.text + "\t"
            strsx = strsx + "\n"


    f = open(idd + ".csv", "a")
    f.write(strsx)
    f.close()


def getPageByID(idd, page, cookie):
    return getByIDWithFilenameSet(idd, idd, page, cookie)


def getByID(idd, cookie):
    getPageByID(idd, "1", cookie)
    getPageByID(idd, "2", cookie)
    getPageByID(idd, "3", cookie)
    getPageByID(idd, "4", cookie)
    getPageByID(idd, "5", cookie)
    getPageByID(idd, "6", cookie)


zerozero_ids = {"165864",#2022/23
"156405",#2021/22
"147383",#2020/21
"135717",#2019/20
"125220",#2018/19
"109369",#2017/18
"98399",#2016/17
"87508",#2015/16
"70079",#2014/15
"58581",#2013/14
"47487",#2012/13
"22951",#2011/12
"15339",#2010/11
"8838",#2009/10
"2306",#2008/09
"1582",#2007/08
"1295",#2006/07
"1138",#2005/06
"495",#2004/05
"5",#2003/04
"1",#2002/03
"119",#2001/02
"116",#2000/01
"114",#1999/00
"112",#1998/99
"110",#1997/98
"108",#1996/97
"106",#1995/96
"121",#1994/95
"123",#1993/94
"124",#1992/93
"122",#1991/92
"120",#1990/91
"102",#1989/90
"100",#1988/89
"98",#1987/88
"96",#1986/87
"94",#1985/86
"92",#1984/85
"89",#1983/84
"87",#1982/83
"85",#1981/82
"84",#1980/81
"118",#1979/80
"117",#1978/79
"115",#1977/78
"113",#1976/77
"111",#1975/76
"109",#1974/75
"107",#1973/74
"105",#1972/73
"104",#1971/72
"103",#1970/71
"101",#1969/70
"99",#1968/69
"97",#1967/68
"95",#1966/67
"93",#1965/66
"91",#1964/65
"90",#1963/64
"88",#1962/63
"86",#1961/62
"83",#1960/61
"82",#1959/60
"81",#1958/59
"79",#1957/58
"77",#1956/57
"75",#1955/56
"74",#1954/55
"72",#1953/54
"71",#1952/53
"70",#1951/52
"68",#1950/51
"80",#1949/50
"78",#1948/49
"76",#1947/48
"73",#1946/47
"69",#1945/46
"67",#1944/45
"65",#1943/44
"63",#1942/43
"61",#1941/42
"60",#1940/41
"66",#1939/40
"64",#1938/39
"62",#1937/38
"59",#1936/37
"58",#1935/36
"57"#1934/35
}

for x in zerozero_ids:
    getByID(x, cookie_do_zerozero)
