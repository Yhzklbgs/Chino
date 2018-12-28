# Created by Yehezkiel Bagas 2k18
# Chino My Waifu
# Special Thanks to Dolphin Kimak
# Thanks to 7DfB, Hello World, Eater, TE[A]MAN BOT, Etc
# Thanks to All People Beside Me

from LineAPI.linepy import *
from LineAPI.akad.ttypes import Message, ContentType as Type, LoginRequest, ChatRoomAnnouncementContents, ChatRoomAnnouncement
from gtts import gTTS
from time import sleep
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from googletrans import Translator
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, pafy, threading, glob, re, string, os, humanize, requests, six, ast, pytz, urllib, urllib3, urllib.parse, traceback, atexit, youtube_dl, LineService
from threading import Thread
from zalgo_text import zalgo
from urllib.parse import urlencode, quote
from pathlib import Path
_session = requests.session()

chino = LINE() #Login QR
chino = LINE("Your Token") #Login Token
chinoMid = chino.profile.mid
chinoProfile = chino.getProfile()
chinoProfile = chino.profile
chinoSettings = chino.getSettings()
chinoPoll = OEPoll(chino)
botStart = time.time()

Owner = ["u6347d96f19332503ee90b48d630ec27e","u207798f56d8ab11343e1507cceef374e"]
owner = ("u6347d96f19332503ee90b48d630ec27e","u207798f56d8ab11343e1507cceef374e")
admin = ["u6347d96f19332503ee90b48d630ec27e","u207798f56d8ab11343e1507cceef374e"]
#==============================================================================#


temp_flood = {}
msg_dict = {}
unsendchat = {}
msg_image={}
msg_video={}
msg_sticker={}
msg_waktu={}
offbot = []

settings = {
    "userAgent": ['Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36'],
    "selfbot" : True,
    "addPict" : True,
    "expire" : True,
    "time": time.time(),
    "flood": 0,
    "temp_flood" : False,
    "leave": True,
    "autoAdd": True,
    "autoJoin": True,
    "autoLeave": False,
    "autoRead": False,
    "autoRespon": False,
    "autoJoinTicket": True,
    "checkContact": False,
    "checkPost": False,
    "checkSticker": False,
    "changePictureProfile": False,
    "userMentioned": {},
    "Welcome": False,
    "WelcomeMessage": False,
    "siderMessage1": "Hey @! sider mulu jomblo ya (｡-_-｡)",
    "siderMessage2": "Halo @! sini dong gabung chat ఠ_ఠ",
    "siderMessage3": "Hi @! join chat please (╥﹏╥)",
    "autoAddMessage": "This is Bot Public By X̡̱̻n͓͡o̹̦ͬo̼̍̕b̞̐͝ Ft.Dͨͭ͘ö̸́̈ḻ̥̇p̖͖̈́h̢͂ͥi̙ͪ̾ń̸̬\n\nThanks @!,  for add me as a friends\n\nX̡̱̻n͓͡o̹̦ͬo̼̍̕b̞̐͝ Gans In Here http://line.me/ti/p/2fX-rPF8EL",
    "commentPost": "Autolike by X̡̱̻n͓͡o̹̦ͬo̼̍̕b̞̐͝\nhttp://line.me/ti/p/2fX-rPF8EL\n\nSupport by Team DFB Bot",
    "postMessage": "Auto Like By Me >.<\nhttp://line.me/ti/p/2fX-rPF8EL\n\n{\__/} \n( • - •) \n/ >🍪 mau biskuit? \n{\__/} \n( • - •) \n🍪< \ beli sendiri lah\n\n{\__/}\n( • - •)\n/ >👩🏻 Mau cewe ?\n{\__/}\n( • - •)\n👩🏻< \ W aja nikung temen\n\n{\_/}\n( •_•)\n/>📱Mau iPhoneX ?\n{\_/}\n( •_•)\n📱<\Kerja gblk\n\n{\__/} \n( • - •) \n/ >💰 mau line credit? \n{\__/} \n( • - •) \n💰< \ kumpulin sendiri lah\n\n{\_/}\n(• - •)\n/>💔 . mau?\n{\_/}\n(• - •)\n/>💔 . Ambil aja gapapa",
    "autoLike": False,
    "wcMsg":False,
    "botMute": [],
    "botOff": [],
    "sniff": [],
    "changeGroupPicture": [],
    "keyCommand": "",
    "myProfile": {
        "displayName": "",
        "coverId": "",
        "pictureStatus": "",
        "statusMessage": "",
        "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ]
    },
    "mimic": {
        "copy": False,
        "status": False,
        "target": {}
    },
    "setKey": False,
    "unsendMessage": False
}

read = {
    "ROM": {},
    "readPoint": {},
    "readMember": {},
    "readTime": {}
}
 
wait = {
    "selfbot" : True,
    "leavemessage" : True,
    "MentionKick" : True,
    "Sider" : False,
    "unsendMessage" : False,
    "Mentionkick":False,
}

simi2 = {
    "simi-simi":{},
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

list_language = {
    "list_textToSpeech": {
        "id": "Indonesia",
        "af" : "Afrikaans",
        "sq" : "Albanian",
        "ar" : "Arabic",
        "hy" : "Armenian",
        "bn" : "Bengali",
        "ca" : "Catalan",
        "zh" : "Chinese",
        "zh-cn" : "Chinese (Mandarin/China)",
        "zh-tw" : "Chinese (Mandarin/Taiwan)",
        "zh-yue" : "Chinese (Cantonese)",
        "hr" : "Croatian",
        "cs" : "Czech",
        "da" : "Danish",
        "nl" : "Dutch",
        "en" : "English",
        "en-au" : "English (Australia)",
        "en-uk" : "English (United Kingdom)",
        "en-us" : "English (United States)",
        "eo" : "Esperanto",
        "fi" : "Finnish",
        "fr" : "French",
        "de" : "German",
        "el" : "Greek",
        "hi" : "Hindi",
        "hu" : "Hungarian",
        "is" : "Icelandic",
        "id" : "Indonesian",
        "it" : "Italian",
        "ja" : "Japanese",
        "km" : "Khmer (Cambodian)",
        "ko" : "Korean",
        "la" : "Latin",
        "lv" : "Latvian",
        "mk" : "Macedonian",
        "no" : "Norwegian",
        "pl" : "Polish",
        "pt" : "Portuguese",
        "ro" : "Romanian",
        "ru" : "Russian",
        "sr" : "Serbian",
        "si" : "Sinhala",
        "sk" : "Slovak",
        "es" : "Spanish",
        "es-es" : "Spanish (Spain)",
        "es-us" : "Spanish (United States)",
        "sw" : "Swahili",
        "sv" : "Swedish",
        "ta" : "Tamil",
        "th" : "Thai",
        "tr" : "Turkish",
        "uk" : "Ukrainian",
        "vi" : "Vietnamese",
        "cy" : "Welsh"
    },
    "list_translate": {    
        "af": "afrikaans",
        "sq": "albanian",
        "am": "amharic",
        "ar": "arabic",
        "hy": "armenian",
        "az": "azerbaijani",
        "eu": "basque",
        "be": "belarusian",
        "bn": "bengali",
        "bs": "bosnian",
        "bg": "bulgarian",
        "ca": "catalan",
        "ceb": "cebuano",
        "ny": "chichewa",
        "zh-cn": "chinese (simplified)",
        "zh-tw": "chinese (traditional)",
        "co": "corsican",
        "hr": "croatian",
        "cs": "czech",
        "da": "danish",
        "nl": "dutch",
        "en": "english",
        "eo": "esperanto",
        "et": "estonian",
        "tl": "filipino",
        "fi": "finnish",
        "fr": "french",
        "fy": "frisian",
        "gl": "galician",
        "ka": "georgian",
        "de": "german",
        "el": "greek",
        "gu": "gujarati",
        "ht": "haitian creole",
        "ha": "hausa",
        "haw": "hawaiian",
        "iw": "hebrew",
        "hi": "hindi",
        "hmn": "hmong",
        "hu": "hungarian",
        "is": "icelandic",
        "ig": "igbo",
        "id": "indonesian",
        "ga": "irish",
        "it": "italian",
        "ja": "japanese",
        "jw": "javanese",
        "kn": "kannada",
        "kk": "kazakh",
        "km": "khmer",
        "ko": "korean",
        "ku": "kurdish (kurmanji)",
        "ky": "kyrgyz",
        "lo": "lao",
        "la": "latin",
        "lv": "latvian",
        "lt": "lithuanian",
        "lb": "luxembourgish",
        "mk": "macedonian",
        "mg": "malagasy",
        "ms": "malay",
        "ml": "malayalam",
        "mt": "maltese",
        "mi": "maori",
        "mr": "marathi",
        "mn": "mongolian",
        "my": "myanmar (burmese)",
        "ne": "nepali",
        "no": "norwegian",
        "ps": "pashto",
        "fa": "persian",
        "pl": "polish",
        "pt": "portuguese",
        "pa": "punjabi",
        "ro": "romanian",
        "ru": "russian",
        "sm": "samoan",
        "gd": "scots gaelic",
        "sr": "serbian",
        "st": "sesotho",
        "sn": "shona",
        "sd": "sindhi",
        "si": "sinhala",
        "sk": "slovak",
        "sl": "slovenian",
        "so": "somali",
        "es": "spanish",
        "su": "sundanese",
        "sw": "swahili",
        "sv": "swedish",
        "tg": "tajik",
        "ta": "tamil",
        "te": "telugu",
        "th": "thai",
        "tr": "turkish",
        "uk": "ukrainian",
        "ur": "urdu",
        "uz": "uzbek",
        "vi": "vietnamese",
        "cy": "welsh",
        "xh": "xhosa",
        "yi": "yiddish",
        "yo": "yoruba",
        "zu": "zulu",
        "fil": "Filipino",
        "he": "Hebrew"
    }
}

try:
    with open("Log_data.json","r",encoding="utf_8_sig") as f:
        msg_dict = json.loads(f.read())
except:
    print("Couldn't read Log data")
    
settings["myProfile"]["displayName"] = chinoProfile.displayName
settings["myProfile"]["statusMessage"] = chinoProfile.statusMessage
settings["myProfile"]["pictureStatus"] = chinoProfile.pictureStatus
coverId = chino.getProfileDetail()["result"]["objectId"]
settings["myProfile"]["coverId"] = coverId

mulai = time.time()
#=======================Def Pembatas=====================
def restartBot():
    print ("[ INFO ] BOT RESTART")
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def logError(text):
    chino.log("[ ERROR ] {}".format(str(text)))
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = "{}, {} - {} - {} | {}".format(str(hasil), str(inihari.strftime('%d')), str(bln), str(inihari.strftime('%Y')), str(inihari.strftime('%H:%M:%S')))
    with open("logError.txt","a") as error:
        error.write("\n[ {} ] {}".format(str(time), text))

def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > timedelta(1):
            if "path" in msg_dict[data]:
                chino.deleteFile(msg_dict[data]["path"])
            del msg_dict[data]

def sendAnu(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@BacBac"
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    chino.sendReplyMessage(msg.id, to, textx, {'AGENT_NAME':'「Self Message」', 'AGENT_LINK': 'http://line.me/ti/p/~bacbac.id', 'AGENT_ICON': "http://dl.profile.line-cdn.net/" + chino.getProfile().picturePath, 'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def sendMentionx(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@BagasCOGAN "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    chino.sendReplyMessage(msg.id, to, textx, {'AGENT_NAME':'「  Sayang-Bot  」', 'AGENT_LINK': 'http://line.me/ti/p/%40gjp6777h', 'AGENT_ICON': "http://dl.profile.line-cdn.net/" + chino.getProfile().picturePath, 'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def sendMentionFooter(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@BacBac"
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    chino.sendReplyMessage(msg.id, to, textx, {'AGENT_NAME':'Dont Click!', 'AGENT_LINK': 'http://line.me/ti/p/~bacbac.id', 'AGENT_ICON': "http://dl.profile.line-cdn.net/" + chino.getProfile().picturePath, 'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)    
    #'AGENT_LINK': 'line://ti/p/~{}'.format(chino.getProfile().userid),
    
def sendMessageWithFooter(to, text, name, url, iconlink):
        contentMetadata = {
            'AGENT_NAME': name,
            'AGENT_LINK': url,
            'AGENT_ICON': iconlink
        }
        return chino.sendReplyMessage(msg.id, to, text, contentMetadata, 0)
    
def sendMessageWithFooter(to, text):
 chino.reissueUserTicket()
 dap = chino.getProfile()
 ticket = "http://line.me/ti/p/"+chino.getUserTicket().id
 pict = "http://dl.profile.line-cdn.net/"+chino.pictureStatus
 name = dap.displayName
 dapi = {"AGENT_ICON": pict,
     "AGENT_NAME": name,
     "AGENT_LINK": ticket
 }
 chino.sendReplyMessage(msg.id, to, text, contentMetadata=chino)
            
def sendMention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@zeroxyuuki "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    chino.sendReplyMessage(msg.id, to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def bagasMention(to, text="",ps='', mids=[]):
    arrData = ""
    arr = []
    mention = "@BagasGans "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ''
        h = ''
        for mid in range(len(mids)):
            h+= str(texts[mid].encode('unicode-escape'))
            textx += str(texts[mid])
            if h != textx:slen = len(textx)+h.count('U0');elen = len(textx)+h.count('U0') + 13
            else:slen = len(textx);elen = len(textx) + 13
            arrData = {'S':str(slen), 'E':str(elen), 'M':mids[mid]}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ''
        slen = len(textx)
        elen = len(textx) + 18
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    try:
        chino.sendReplyMessage(msg.id, to, textx, {'MSG_SENDER_NAME': chino.getContact(ps).displayName,'MSG_SENDER_ICON': "https://os.line.naver.jp/os/p/"+ps,'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as e:
        chino.sendReplyMessage(msg.id, to, textx, {'MSG_SENDER_NAME': chino.getContact(to).displayName,'MSG_SENDER_ICON': 'https://os.line.naver.jp/os/p/'+to,'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def command(text):
    pesan = text.lower()
    if settings["setKey"] == True:
        if pesan.startswith(settings["keyCommand"]):
            cmd = pesan.replace(settings["keyCommand"],"")
        else:
            cmd = "Undefined command"
    else:
        cmd = text.lower()
    return cmd
 
def sendCarousel(data):
    data = json.dumps(data)
    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/SendMessage"
    headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Redmi 3S Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/68.0.3440.85 Mobile Safari/537.36 Line/8.11.0'}
    headers['Content-Type'] = 'application/json'
    headers['Accept-Encoding'] = 'gzip,deflate'
    headers['Accept-Language'] = 'id-ID,en-US;q=0.9'
    headers['Connection'] = 'keep-alive'
    return requests.post(url, data=data, headers=headers)

def sendCarousel(data):
    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/SendMessage"
    data = data
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (Linux) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Mobile Safari/537.36 Line/8.10.1'
    headers['Content-Type'] = 'application/json'
    return requests.Session().post(url,data=json.dumps(data),headers=headers)
 
def youtubeMp4(to, link):
   r = requests.get("http://api.zicor.ooo/yt.php?url={}".format(str(link)))
   data = r.text
   data = json.loads(data)
   chino.sendVideoWithURL(to, data["mp4"]["720"]) 
 
def sendSticker(to, version, packageId, stickerId):
    contentMetadata = {
        'STKVER': version,
        'STKPKGID': packageId,
        'STKID': stickerId
    }
    chino.sendReplyMessage(msg.id, to, '', contentMetadata, 7)
   
def sendLineMusic(to):
    contentMetadata = {
        'countryCode': 'ID',
        'i-installUrl': "line://ti/p/~{}".format(chino.getProfile().userid),
        'a-packageName': 'com.spotify.music',
        'linkUri': "line://ti/p/~{}".format(chino.getProfile().userid),
        'type': 'mt',
        'previewUrl':"http://dl.profile.line-cdn.net/{}".format(chino.profile.pictureStatus),
        'a-linkUri': "line://ti/p/~{}".format(chino.getProfile().userid),
        'text': chino.profile.displayName,
        'id': 'mt000000000a6b79f9',
        'subText': chino.profile.statusMessage
    }
    return chino.sendReplyMessage(msg.id, to, chino.profile.displayName, contentMetadata, 19)

def sendMusic(send_to,music_id,title,artist,thumbnail,link):
 chino.sendMessage(send_to, '',
  {'text': title,
  'subText': artist,
  'id': music_id,
  'previewUrl': thumbnail,
  'linkUri': link,
  'i-linkUri': link,
  'a-linkUri': link,
  'i-installUrl': link,
  'a-installUrl': link,
  'a-packageName': 'jp.linecorp.linemusic.android',
  'type': 'mt',
  'countryCode': 'JP',
  'ORGCONTP': 'MUSIC'},
  19)    

def delExpire():
    if temp_flood != {}:
        for tmp in temp_flood:
            if temp_flood[tmp]["expire"] == True:
                if time.time() - temp_flood[tmp]["time"] >= 3*10:
                    temp_flood[tmp]["expire"] = False
                    temp_flood[tmp]["time"] = time.time()
                    try:
                        userid = "https://line.me/ti/p/~" + chino.profile.userid
                        chino.sendReplyMessage(msg.id, to, "Spam is Over,Now Bot Active Again!")
                    except Exception as error:
                        logError(error)

def speedtest(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    weaks, days = divmod(days,7)
    if days == 0:
        return '%02d' % (secs)
    elif days > 0 and weaks == 0:
        return '%02d' %(secs)
    elif days > 0 and weaks > 0:
        return '%02d' %(secs)

def timeChange(secs):
	mins, secs = divmod(secs,60)
	hours, mins = divmod(mins,60)
	days, hours = divmod(hours,24)
	weeks, days = divmod(days,7)
	months, weeks = divmod(weeks,4)
	text = ""
	if months != 0: text += "%02d Bulan" % (months)
	if weeks != 0: text += " %02d Minggu" % (weeks)
	if days != 0: text += " %02d Hari" % (days)
	if hours !=  0: text +=  " %02d Jam" % (hours)
	if mins != 0: text += " %02d Menit" % (mins)
	if secs != 0: text += " %02d Detik" % (secs)
	if text[0] == " ":
		text = text[1:]
	return text
        
def removeCmd(cmd, text):
	key = settings["keyCommand"]
	if settings["setKey"] == False: key = ''
	rmv = len(key + cmd) + 1
	return text[rmv:]        

def cloneProfile(mid):
    contact = chino.getContact(mid)
    if contact.videoProfile == None:
        chino.cloneContactProfile(mid)
    else:
        profile = chino.getProfile()
        profile.displayName, profile.statusMessage = contact.displayName, contact.statusMessage
        chino.updateProfile(profile)
        pict = chino.downloadFileURL('http://dl.profile.line-cdn.net/' + contact.pictureStatus, saveAs="tmp/pict.bin")
        vids = chino.downloadFileURL( 'http://dl.profile.line-cdn.net/' + contact.pictureStatus + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = chino.getProfileDetail(mid)['result']['objectId']
    chino.updateProfileCoverById(coverId)

def backupProfile():
    profile = chino.getContact(chinoMID)
    settings['myProfile']['displayName'] = profile.displayName
    settings['myProfile']['pictureStatus'] = profile.pictureStatus
    settings['myProfile']['statusMessage'] = profile.statusMessage
    settings['myProfile']['videoProfile'] = profile.videoProfile
    coverId = chino.getProfileDetail()['result']['objectId']
    settings['myProfile']['coverId'] = str(coverId)

def restoreProfile():
    profile = chino.getProfile()
    profile.displayName = settings['myProfile']['displayName']
    profile.statusMessage = settings['myProfile']['statusMessage']
    if settings['myProfile']['videoProfile'] == None:
        profile.pictureStatus = settings['myProfile']['pictureStatus']
        chino.updateProfileAttribute(8, profile.pictureStatus)
        chino.updateProfile(profile)
    else:
        chino.updateProfile(profile)
        pict = chino.downloadFileURL('http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'], saveAs="tmp/pict.bin")
        vids = chino.downloadFileURL( 'http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'] + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = settings['myProfile']['coverId']
    chino.updateProfileCoverById(coverId)

def sendMentionV2(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@zeroxyuuki "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    chino.sendReplyMessage(msg.id, to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def yt(query):
    with requests.session() as s:
        isi = []
        if query == "":
            query = "S1B nrik"
        s.headers['user-agent'] = 'Mozilla/5.0'
                     
        url    = 'http://www.youtube.com/results'
        params = {'search_query': query}
                     
        r    = s.get(url, params=params)
        soup = BeautifulSoup(r.content, 'html5lib')
                     
        for a in soup.select('.yt-lockup-title > a[title]'):
            if '&List' not in a['href']:
                if 'watch?v' in a['href']:
                    b = a['href'].replace('watch?v=','')
                    isi += ['youtu.be' + b]
        return isi

def RECEIVE_MESSAGE(op):
    msg = op.message
    try:
        if msg.contentType == 0:
            try:
                if msg.to in settings['readPoint']:
                    if msg._from in settings["ROM"][msg.to]:
                        del settings["ROM"][msg.to][msg._from]
                else:
                    pass
            except:
                pass
        else:
            pass
          
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as error:
        print(error)
        print("\n\nRECEIVE_MESSAGE\n\n")
        return
 
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d day %02d hours %02d Minute %02d Second' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d day %02d hours %02d Minute %02d second' % (days, hours, mins, secs)
   
def joox2(to,q,pl=""):
    try:
        url = "http://api.ntcorp.us/joox/search?q="+q
        r   = requests.get(url)
        data = r.json()
        for music in data['result']:
           finds = music['sid']
        urls = "http://api.ntcorp.us/joox/song_info?sid="+finds
        w = requests.get(urls)
        datax = w.json()
        a = "「Info Song」\n"
        sz = int(datax['result']['size'])
        a+="Title: %s" % datax['result']['song']
        a+='\nAlbum: %s' % datax['result']['album']
        a+='\nSize: '+format_size(sz)
        a+='\nLink: '+shorten(musik)
        chino.sendImageWithURL(to,datax['result']['img'])
        chino.sendReplyMessage(msg.id, to,a)
        chino.sendAudioWithURL(to,musik)
    except:
        chino.sendReplyMessage(msg.id, to,"Please cek your Sid >,<")
        print(traceback.format_exc())    
    
def helpmessage():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
    helpMessage =   "╭──「Help Message」───" + "\n" + \
                    "│ " + key + "⌬ Myself" + "\n" + \
                    "│ " + key + "⌬ Group" + "\n" + \
                    "│ " + key + "⌬ Steal" + "\n" + \
                    "│ " + key + "⌬ Media" + "\n" + \
                    "│ " + key + "⌬ Settings" + "\n" + \
                    "│ " + key + "⌬ Special" + "\n" + \
                    "│ " + key + "⌬ Token" + "\n" + \
                    "├──" + key + "「Help Command」───" + "\n" + \
                    "│ " + key + "⌬ About" + "\n" + \
                    "│ " + key + "⌬ Creator" + "\n" + \
                    "│ " + key + "⌬ Runtime" + "\n" + \
                    "│ " + key + "⌬ Speed" + "\n" + \
                    "│ " + key + "⌬ Chatowner:「Pesanmu」" + "\n" + \
                    "│ " + key + "⌬ Restart" + "\n" + \
                    "│ " + key + "⌬ Logout" + "\n" + \
                    "├──" + key + "───────" + "\n" + \
                    "│ ⌬ Command from : @! " + "\n" + \
                    "│ ⌬ Maker : @! " + "\n" + \
                    "│ ⌬ Day : " + datetime.strftime(timeNow,'%Y-%m-%d') + "\n" + \
                    "│ ⌬ Time : " + datetime.strftime(timeNow,'%H:%M:%S') + " WIB" + "\n" + \
                    "╰────────" 
    return helpMessage

def helpmyself():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    helpMyself =   "╭──「My Self」─────" + "\n" + \
                    "│ " + key + "Me" + "\n" + \
                    "│ " + key + "MyMid" + "\n" + \
                    "│ " + key + "MyName" + "\n" + \
                    "│ " + key + "MyBio" + "\n" + \
                    "│ " + key + "MyPicture" + "\n" + \
                    "│ " + key + "MyVideoProfile" + "\n" + \
                    "│ " + key + "MyCover" + "\n" + \
                    "╰──────────"
    return helpMyself

def helpgroup():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    helpGroup =   "╭──「Help Group」─────" + "\n" + \
                    "│ " + key + "GroupCreator" + "\n" + \
                    "│ " + key + "GroupId" + "\n" + \
                    "│ " + key + "GroupName" + "\n" + \
                    "│ " + key + "GroupPicture" + "\n" + \
                    "│ " + key + "GroupTicket" + "\n" + \
                    "│ " + key + "GroupTicket「On/Off」" + "\n" + \
                    "│ " + key + "GroupList" + "\n" + \
                    "│ " + key + "GroupMemberList" + "\n" + \
                    "│ " + key + "GroupInfo" + "\n" + \
                    "╰──────────"
    return helpGroup

def helpsteal():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    helpSteal =   "╭──「Help Steal」─────" + "\n" + \
                    "│ " + key + "StealMid「Mention」" + "\n" + \
                    "│ " + key + "StealName「Mention」" + "\n" + \
                    "│ " + key + "StealBio「Mention」" + "\n" + \
                    "│ " + key + "StealPicture「Mention」" + "\n" + \
                    "│ " + key + "StealVideoProfile「Mention」" + "\n" + \
                    "│ " + key + "StealCover「Mention」" + "\n" + \
                    "╰──────────"
    return helpSteal

def helpmedia():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    helpMedia =   "╭──「Help Media」────" + "\n" + \
                    "│ " + key + "⌬ Animequotes" + "\n" + \
                    "│ " + key + "⌬ Astronotnow" + "\n" + \
                    "│ " + key + "⌬ Artinama「Search」" + "\n" + \
                    "│ " + key + "⌬ Artisifatnama「Search」" + "\n" + \
                    "│ " + key + "⌬ Asking「Search」" + "\n" + \
                    "│ " + key + "⌬ Bitcoin" + "\n" + \
                    "│ " + key + "⌬ Binary「Query」" + "\n" + \
                    "│ " + key + "⌬ Creepypasta" + "\n" + \
                    "│ " + key + "⌬ CheckPraytime「City」" + "\n" + \
                    "│ " + key + "⌬ CheckWeather「Search」" + "\n" + \
                    "│ " + key + "⌬ Cinema" + "\n" + \
                    "│ " + key + "⌬ Cookies「Text」" + "\n" + \
                    "│ " + key + "⌬ Deviantart「Search」" + "\n" + \
                    "│ " + key + "⌬ Downloadyt「Url」" + "\n" + \
                    "│ " + key + "⌬ Fmylife" + "\n" + \
                    "│ " + key + "⌬ Gift" + "\n" + \
                    "│ " + key + "⌬ Graffiti「Text」" + "\n" + \
                    "│ " + key + "⌬ Image「Search」" + "\n" + \
                    "│ " + key + "⌬ Imageart「Search」" + "\n" + \
                    "│ " + key + "⌬ Imagetext「Text」" + "\n" + \
                    "│ " + key + "⌬ Instagram「Search」" + "\n" + \
                    "│ " + key + "⌬ Liburan「Query」" + "\n" + \
                    "│ " + key + "⌬ Keahlian「Query」" + "\n" + \
                    "│ " + key + "⌬ Kemiripan「Query」" + "\n" + \
                    "│ " + key + "⌬ Motivate" + "\n" + \
                    "│ " + key + "⌬ Music「Search」" + "\n" + \
                    "│ " + key + "⌬ Neon:「Query」" + "\n" + \
                    "│ " + key + "⌬ RandomImage" + "\n" + \
                    "│ " + key + "⌬ Reviewhp「Search」" + "\n" + \
                    "│ " + key + "⌬ Samehadaku" + "\n" + \
                    "│ " + key + "⌬ Samehadaku「Search」" + "\n" + \
                    "│ " + key + "⌬ Sletters「Text」" + "\n" + \
                    "│ " + key + "⌬ Stickerline「Search」" + "\n" + \
                    "│ " + key + "⌬ Ssweb「Url」" + "\n" + \
                    "│ " + key + "⌬ Themeline「Search」" + "\n" + \
                    "│ " + key + "⌬ Timezone「Search」" + "\n" + \
                    "│ " + key + "⌬ Topnews" + "\n" + \
                    "│ " + key + "⌬ Top kaskus" + "\n" + \
                    "│ " + key + "⌬ Waifu「Name」" + "\n" + \
                    "│ " + key + "⌬ Wallpaper-hd「Search」" + "\n" + \
                    "│ " + key + "⌬ Window「Text」" + "\n" + \
                    "│ " + key + "⌬ Whois「Search」" + "\n" + \
                    "│ " + key + "⌬ Ytdl「Url」" + "\n" + \
                    "│ " + key + "⌬ Zodiaceng「Query」" + "\n" + \
                    "│ " + key + "⌬ Zodiacind「Query」" + "\n" + \
                    "│ " + key + "⌬ Ztext「Query」" + "\n" + \
                    "╰────────────"
    return helpMedia
    
def helpspecial():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    helpSpecial =   "╭──「Help Special」────" + "\n" + \
                    "│ " + key + "⌬ Chat|Num|Msg" + "\n" + \
                    "│ " + key + "⌬ Exec「Query」" + "\n" + \
                    "│ " + key + "⌬ Leavegc「Num」" + "\n" + \
                    "│ " + key + "⌬ Like「Mention」" + "\n" + \
                    "│ " + key + "⌬ Infomem「Num」" + "\n" + \
                    "│ " + key + "⌬ Invitetogc「Num」" + "\n" + \
                    "│ " + key + "⌬ Openqr:Num" + "\n" + \
                    "│ " + key + "⌬ Setcomment:「Query」" + "\n" + \
                    "│ " + key + "⌬ Unsend「Num」" + "\n" + \
                    "╰────────────"
    return helpSpecial    

def helptoken():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    helpToken =   "╭──「Help Token」────" + "\n" + \
                    "│ " + key + "⌬ Token Chromeos" + "\n" + \
                    "│ " + key + "⌬ Token Iosipad" + "\n" + \
                    "│ " + key + "⌬ Token Desktopwin" + "\n" + \
                    "│ " + key + "⌬ Token Desktopmac" + "\n" + \
                    "│ " + key + "⌬ Token Win10" + "\n" + \
                    "╰─────────────"
    return helpToken
    
def helpsettings():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    helpSettings =   "╭──「Help Settings」────" + "\n" + \
                    "│ " + key + "⌬ AutoAdd「On/Off」" + "\n" + \
                    "│ " + key + "⌬ AutoJoin「On/Off」" + "\n" + \
                    "│ " + key + "⌬ AutoJoinTicket「On/Off」" + "\n" + \
                    "│ " + key + "⌬ AutoLeave「On/Off」" + "\n" + \
                    "│ " + key + "⌬ AutoRead「On/Off」" + "\n" + \
                    "│ " + key + "⌬ AutoRespon「On/Off」" + "\n" + \
                    "│ " + key + "⌬ CheckContact「On/Off」" + "\n" + \
                    "│ " + key + "⌬ CheckPost「On/Off」" + "\n" + \
                    "│ " + key + "⌬ CheckSticker「On/Off」" + "\n" + \
                    "│ " + key + "⌬ UnsendChat「On/Off」" + "\n" + \
                    "│ " + key + "⌬ Sider「On/Off」" + "\n" + \
                    "│ " + key + "⌬ Simi「On/Off」" + "\n" + \
                    "╰────────────"
    return helpSettings

def chinoBot(op):
    try:
        if op.type == 0:
            print ("[ 0 ] END OF OPERATION")
            return

        if op.type == 5:
            print ("[ 5 ] NOTIFIED ADD CONTACT")
            if settings["autoAdd"] == True:
                chino.findAndAddContactsByMid(op.param1)
            bagasMention(op.param1, "{}".format(settings["autoAddMessage"]), "", [op.param1])
            
        if op.type == 13:
            print ("[ 13 ] NOTIFIED INVITE INTO GROUP")
            if chinoMid in op.param3:
            	G = chino.getGroup(op.param1)
            	if settings["autoJoin"] == True:
            		if settings["autoCancel"]["on"] == True:
            			if len(G.members) <= settings["autoCancel"]["members"]:
            				chino.acceptGroupInvitation(op.param1)
            				sendMention(op.param1, "Maaf Kak @! Anggota Kurang Lebih Dari 20 Member 😕",[op.param2])
            				chino.leaveGroup(op.param1)
            			else:
            				chino.acceptGroupInvitation(op.param1)
            				sendMention(op.param1, "Halo @!\nThanks For Invite Me Type Help For See Command 😆\nType ByeBot for Kick The Bot 😐",[op.param2])
                

#######        if op.type == 15:
##########           print ("[ 15 ] NOTIFIED LEAVE GROUP")
########           if settings["leave"] == True:
#######               contact = chino.getContact(msg._from)
####### ##          ##    chino.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net" + chino.getContact(op.param2).picturePath)
 #######              chino.sendContact(op.param1, op.param2)
   ###########           sendMention(op.param1, "Yah @!, kenapa out kak :'(", [op.param2])

        if op.type == 17:
            print ("[ 17 ] NOTIFIED ACCEPT GROUP INVITATION")
            group = chino.getGroup(op.param1)
            contact = chino.getContact(op.param2)
            if settings["WelcomeMessage"] == True:
                sendMention(op.param1, op.param2, "「 Auto Tag 」\n•", "\n{}".format(str(settings["WelcomeMessage"])))
            
        if op.type in [22, 24]:
            print ("[ 22 And 24 ] NOTIFIED INVITE INTO ROOM & NOTIFIED LEAVE ROOM")
            if settings["autoLeave"] == True:
                sendMention(op.param1, "Oi asw @!,ngapain invite saya")
                chino.leaveRoom(op.param1)
                
        if op.type == 26:
            msg = op.message                    
            if msg.to in simi2["simi-simi"]:
                if simi2["simi-simi"][msg.to] == True:
                 try:
                      if msg.text is not None:
                         simi = msg.text
                         r = requests.get("https://api.eater.site/api/chatbot/?apikey=beta&question="+simi)
                         data = r.text
                         data = json.loads(data)
                         if data["code"] == 200:
                            chino. sendReplyMessage(msg.id, msg.to, str(data["result"]["answer"]))
                 except Exception as error:
                      pass 
                     
        if op.type == 55:
            try:
                if cctv['cyduk'][op.param1]==True:
                    if op.param1 in cctv['point']:
                        Name = chino.getContact(op.param2).displayName
                        if Name in cctv['sidermem'][op.param1]:
                            pass
                        else:
                                cctv['sidermem'][op.param1] += "\n> " + Name
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        sendMention(op.param1, "Hey @! betah banget jadi sider 😑",[op.param2])
                                        #chino.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net" + chino.getContact(op.param2).picturePath)
                                        summon(op.param1,[op.param2])
                                    else:
                                        sendMention(op.param1, "Hey @! sider mulu jomblo ya (｡-_-｡)",[op.param2])
                                        #chino.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net" + chino.getContact(op.param2).picturePath)
                                        summon(op.param1,[op.param2])
                                else:
                                    sendMention(op.param1, "Hey @! cie ketahuan sider ( ͡° ͜ʖ ͡°)",[op.param2])
                                    #chino.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net" + chino.getContact(op.param2).picturePath)
                                    summon(op.param1,[op.param2])
                    else:
                        pass
                else:
                    pass
            except:
                pass                          
        
                                            
        if op.type == 26 or op.type == 25:
            try:
                print ("[ 26 ] SEND MESSAGE")
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                setKey = settings["keyCommand"].title()
                if settings["setKey"] == False:
                    setKey = ''                      
                if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                    if msg.toType == 0:
                        if sender != chino.profile.mid:
                            to = sender
                        else:
                            to = receiver                           
                    elif msg.toType == 1:
                        to = receiver
                    elif msg.toType == 2:
                        to = receiver
                    if msg.contentType == 0:
                        if text is None:
                            return
                        else:
                            cmd = command(text)
                            if receiver in temp_flood:
                               if temp_flood[receiver]["expire"] == True:
                                  if cmd == "open":
                                       temp_flood[receiver]["expire"] = False
                                       temp_flood[receiver]["time"] = time.time()
                                       chino.sendReplyMessage(msg.id, to,"Bot Actived")
                                  return
                               elif time.time() - temp_flood[receiver]["time"] <= 5:
                                   temp_flood[receiver]["flood"] += 1
                                   if temp_flood[receiver]["flood"] >= 20:
                                       temp_flood[receiver]["flood"] = 0
                                       temp_flood[receiver]["expire"] = True
                                       ret_ = "I will be off for 30 seconds, type open to re-enable"
                                       userid = "https://line.me/ti/p/~" + chino.profile.userid
                                       chino.sendReplyMessage(msg.id, to, "Flood Detect ! Bot will silent 30 seconds! Type Open to unmute bot in this room!")
                               else:
                                   temp_flood[receiver]["flood"] = 0
                               temp_flood[receiver]["time"] = time.time()
                            else:
                               temp_flood[receiver] = {
    	                           "time": time.time(),
    	                           "flood": 0,
    	                           "expire": False
                               }
                            if cmd == "help":
                                mid = "u085311ecd9e3e3d74ae4c9f5437cbcb5"
                                helpMessage = helpmessage()
                                chino.sendReplyMention(msg.id, to, helpMessage, [sender, mid])                                                         
                             
                            elif cmd == "settings":
                                helpSettings = helpsettings()                                
                                chino.sendReplyMessage(msg.id, to, str(helpSettings))
                                
                            elif cmd == "media":
                                helpMedia = helpmedia()                                
                                chino.sendReplyMessage(msg.id, to, str(helpMedia))
                                
                            elif cmd == "myself":
                                helpMyself = helpmyself()                                
                                chino.sendReplyMessage(msg.id, to, str(helpMyself))

                            elif cmd == "group":
                                helpGroup = helpgroup()                                
                                chino.sendReplyMessage(msg.id, to, str(helpGroup))

                            elif cmd == "steal":
                                helpSteal = helpsteal()                                
                                chino.sendReplyMessage(msg.id, to, str(helpSteal))      
                                
                            elif cmd == "token":
                                helpToken = helptoken()
                                contact = chino.getContact(msg._from)
                                chino.sendReplyMessage(msg.id, to, str(helpToken), {'AGENT_LINK': 'http://line.me/ti/p/dkjb7i9krs','AGENT_ICON': "http://dl.profile.line-cdn.net/" + contact.pictureStatus,'AGENT_NAME': "Special for u"})
                                
                            elif cmd == "special":
                                if msg._from in Owner:                                    
                                    helpSpecial = helpspecial()                                
                                    chino.sendReplyMessage(msg.id, to, str(helpSpecial))
                                else:
                                    chino.sendReplyMessage(msg.id, to, "Owner Permission")
        
                            elif cmd == "speed":
                                start = time.time()                              
                                elapsed_time = time.time() - start
                                took = time.time() - start
                                chino.sendReplyMessage(msg.id, to,"「 Speed 」\n - Took : %.3fms\n - Taken: %.10f" % (took,elapsed_time))
                                                            
                            elif cmd == "runtime":
                                timeNow = time.time()
                                runtime = timeNow - botStart
                                runtime = format_timespan(runtime)
                                contact = chino.getContact(msg._from)
                                chino.sendReplyMessage(msg.id, to, "Bot sudah berjalan selama {}".format(str(runtime)))
                                
                            elif cmd == "restart":
                                if msg._from in Owner:
                                 chino.sendReplyMessage(msg.id, to, "Berhasil merestart Bot")
                                 restartBot()
                                 
                            elif text.lower() == '@byebot':
                                if msg.toType == 2:
                                   ge = ("u0669082c18c5e369586fcb3cc4723407")
                                   ginfo = chino.getGroup(to)
                                   try:
                                       chino.sendReplyMessage(msg.id, to,"Terimakasih sudah menginvite saya")
                                       time.sleep(1)
                                       chino.leaveGroup(to)
                                   except:
                                       pass                                                                                                                  

                            elif cmd == "byebot":
                                chino.sendReplyMessage(msg.id, to, "Asw lo mau kick w")
                                chino.sendReplyMessage(msg.id, to, "Nich w balikin")
                                chino.sendReplyMessage(msg.id, to, "Wkwkwkwkkw")
                                chino.kickoutFromGroup(msg.to,[sender])
                                chino.inviteIntoGroup(msg.to,[sender])
                           
                            elif cmd == "logout":
                                if msg._from in Owner:
                                    chino.sendReplyMessage(msg.id, to, "Berhasil Mematikan Bot")
                                    sys.exit("[INFO] BOT SHUTDOWN")           
                                  
                            elif cmd.startswith("clearchat"):
                            	if msg._from in Owner:
                                    chino.removeAllMessages(op.param2)
                                    chino.sendReplyMessage(msg.id, to, "Remove chat history")                                                                     

                            elif cmd == "about":
                                try:
                                    arr = []
                                    bagas = "u6347d96f19332503ee90b48d630ec27e"
                                    dolphin = "u4f41ba11fdda78a8181dfeb3a40e64b0"                                    
                                    friend = chino.getAllContactIds()
                                    group = chino.getGroupIdsJoined()
                                    blockedlist = chino.getBlockedContactIds()
                                    favorite = chino.getFavoriteMids()
                                    userid = chino.getProfile().userid
                                    region = chino.getProfile().regionCode
                                    timeNow = time.time()
                                    runtime = timeNow - botStart
                                    runtime = format_timespan(runtime)
                                    tz = pytz.timezone("Asia/Jakarta")
                                    timeNow = datetime.now(tz=tz)
                                    ret_ = "╭──[ About Public Bot ]"
                                    ret_ += "\n├ ⌬ User : @!"
                                    ret_ += "\n├ ⌬ Friend : {}".format(str(len(friend)))
                                    ret_ += "\n├ ⌬ Group : {}".format(str(len(group)))
                                    ret_ += "\n├ ⌬ Runtime : {}".format(str(runtime))
                                    ret_ += "\n├ ⌬ Blocked : {}".format(str(len(blockedlist))) 
                                    ret_ += "\n├ ⌬ Favorite: {}".format(str(len(favorite)))
                                    ret_ += "\n├ ⌬ UserId: {}".format(str(userid))                                    
                                    ret_ += "\n├ ⌬ Region: {}".format(str(region))
                                    ret_ += "\n├ ⌬ Type : Public Bot"
                                    ret_ += "\n├ ⌬ Version : Beta Version "
                                    ret_ += "\n├ ⌬ Creator : @!"
                                    ret_ += "\n├ ⌬ Special Tag : @!"
                                    ret_ += "\n├──[ About Time ]"
                                    ret_ += "\n├ ⌬ Day : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                    ret_ += "\n├ ⌬ Time : " + datetime.strftime(timeNow,'%H:%M:%S') + " WIB"
                                    ret_ += "\n├──[ Special Thanks ]"
                                    ret_ += "\n├ ⌬ The Only One Great God"
                                    ret_ += "\n├ ⌬ My Lovely"
                                    ret_ += "\n├ ⌬ HelloWorld"
                                    ret_ += "\n├ ⌬ Eater Square"
                                    ret_ += "\n├ ⌬ TE[A]MAN BOT"
                                    ret_ += "\n├ ⌬ ChoiceBOT Line "
                                    ret_ += "\n├ ⌬ My Best Friends (Dewii, Valdi, Bima, Raka, San, Dolphin, Rahmat, Fahmi, Ale, Ryn)"
                                    ret_ += "\n├ ⌬ All My Teacher (Nadya, Dzin, Corry, Nazri, Zero, Alin, Tan)"
                                    ret_ += "\n├ ⌬ All People Beside Me "
                                    ret_ += "\n╰───[ Finish ]"
                                    chino.sendReplyMention(msg.id, to, ret_, [chinoMid, bagas, dolphin])
                                except Exception as error:
                                    	chino.sendReplyMessage(msg.id, to, str(error))

                            elif cmd.startswith("gbc "):
                            	if msg._from in Owner:
                                    sep = text.split(" ")
                                    txt = text.replace(sep[0] + " ","")                                                                                                            
                                    groups = chino.groups
                                    contact = chino.getContact(msg._from)
                                    for group in groups:
                                        chino.sendMessage(group, "[ Broadcast ]\n{}".format(str(txt)))
                                    chino.sendReplyMessage(msg.id, to, "Berhasil broadcast ke {} group".format(str(len(groups))))

                            elif cmd.startswith("gbc: "):
                                if msg._from in Owner:
                                    sep = text.split(" ")
                                    txt = text.replace(sep[0] + " ","")
                                    groups = chino.getGroupIdsJoined()
                                    for group in groups:
                                       chino.sendMessage(group, "[ Broadcast ]\n{}".format(str(txt)))
                                    chino.sendReplyMessage(msg.id, to, "Berhasil broadcast ke {} group".format(str(len(groups))))     
                                    
                            elif cmd.startswith("$ "):
                            	if msg._from in Owner:
                                    query = cmd.replace("$ ","")
                                    s = os.popen(query)
                                    p = s.read()
                                    chino.sendReplyMessage(msg.id, to,p)                       
  
                            elif cmd == "mymid":
                                chino.sendReplyMessage(msg.id, to, "[ MID ]\n{}".format(sender))
                              
                            elif cmd == "hmm":
                                contact = chino.getContact(sender)
                                jawab = ["hmm aja lo ajg","ham hem ham","Babyk","Hmmk"]
                                chino.sendReplyMessage(msg.id, to, random.choice(jawab))
                            elif cmd == "hi":
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                mek = "Hi too"
                                mek += "\n\n" + datetime.strftime(timeNow,'%d-%m-%Y')
                                mek += " " + datetime.strftime(timeNow,'%H:%M:%S')
                                g = chino.getGroup(to)
                                a = g.members
                                contact = random.choice(a)
                                chino.sendReplyMessage(msg.id, to, mek)
                            elif cmd == "chino":
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                mek = "Moshimoshi (もしもし)"
                                mek += "\n\n" + datetime.strftime(timeNow,'%d-%m-%Y')
                                mek += " " + datetime.strftime(timeNow,'%H:%M:%S')
                                g = chino.getGroup(to)
                                a = g.members
                                contact = random.choice(a)
                                chino.sendReplyMessage(msg.id, to, mek)
                            elif cmd == "sayang":
                                contact = chino.getContact(sender)
                                jawab = ["Panggil2 sayang ajg","Sayang? Mati aja lo","Sayang lu omdo doang","Iya sayang ada apa?"]
                                chino.sendReplyMessage(msg.id, to, random.choice(jawab))
                            elif cmd == "welcome":
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                mek = "Welcome to groups"
                                mek += "\n\n" + datetime.strftime(timeNow,'%d-%m-%Y')
                                mek += " " + datetime.strftime(timeNow,'%H:%M:%S')
                                contact = chino.getContact(sender)
                                chino.sendReplyMessage(msg.id, to, mek)
# Pembatas Script #
                            elif cmd == "autoadd on":
                            	if msg._from in Owner:
                                 settings["autoAdd"] = True
                                 chino.sendReplyMessage(msg.id, to, "Berhasil mengaktifkan auto add")
                                
                            elif cmd == "autoadd off":
                            	if msg._from in Owner:
                                 settings["autoAdd"] = False
                                 chino.sendReplyMessage(msg.id, to, "Berhasil menonaktifkan auto add")
                                
                            elif cmd == "autojoin on":
                            	if msg._from in Owner:
                                 settings["autoJoin"] = True
                                 chino.sendReplyMessage(msg.id, to, "Berhasil mengaktifkan auto join")
                                
                            elif cmd == "autojoin off":
                            	if msg._from in Owner:
                                 settings["autoJoin"] = False
                                 chino.sendReplyMessage(msg.id, to, "Berhasil menonaktifkan auto join")
                                 
                            elif cmd == "autoleave on":
                            	if msg._from in Owner:
                                 settings["autoLeave"] = True,
                                 chino.sendReplyMessage(msg.id, to, "Berhasil mengaktifkan auto leave")
                                
                            elif cmd == "autoleave off":
                            	if msg._from in Owner:
                                 settings["autoLeave"] = False
                                 chino.sendReplyMessage(msg.id, to, "Berhasil menonaktifkan auto leave")
                                
                            elif cmd == "autorespon on":
                            	if msg._from in Owner:
                                 settings["autoRespon"] = True
                                 chino.sendReplyMessage(msg.id, to, "Berhasil mengaktifkan auto respon")
                                
                            elif cmd == "autorespon off":
                            	if msg._from in Owner:
                                 settings["autoRespon"] = False
                                 chino.sendReplyMessage(msg.id, to, "Berhasil menonaktifkan auto respon")
                                
                            elif cmd == "autoread on":
                            	if msg._from in Owner:
                                 settings["autoRead"] = True
                                 chino.sendReplyMessage(msg.id, to, "Berhasil mengaktifkan auto read")
                                
                            elif cmd == "autoread off":
                            	if msg._from in Owner:
                                 settings["autoRead"] = False
                                 chino.sendReplyMessage(msg.id, to, "Berhasil menonaktifkan auto read")
                                 
                            elif cmd == "autojointicket on":
                            	if msg._from in Owner:
                                 settings["autoJoinTicket"] = True
                                 chino.sendReplyMessage(msg.id, to, "Berhasil mengaktifkan auto join by ticket")
                                
                            elif cmd == "autojointicket off":
                                if msg._from in Owner:                            	
                                 settings["autoJoin"] = False
                                 chino.sendReplyMessage(msg.id, to, "Berhasil menonaktifkan auto join by ticket")
                                 
                            elif cmd == "checkcontact on":
                            	if msg._from in Owner:
                                 settings["checkContact"] = True
                                 chino.sendReplyMessage(msg.id, to, "Berhasil mengaktifkan check details contact")
                                
                            elif cmd == "checkcontact off":
                            	if msg._from in Owner:
                                 settings["checkContact"] = False
                                 chino.sendReplyMessage(msg.id, to, "Berhasil menonaktifkan check details contact")
                                
                            elif cmd == "checkpost on":
                            	if msg._from in Owner:
                                 settings["checkPost"] = True
                                 chino.sendReplyMessage(msg.id, to, "Berhasil mengaktifkan check details post")
                                
                            elif cmd == "checkpost off":
                            	if msg._from in Owner:
                                 settings["checkPost"] = False
                                 chino.sendReplyMessage(msg.id, to, "Berhasil menonaktifkan check details post")
                                
                            elif cmd == "checksticker on":
                            	if msg._from in Owner:
                                 settings["checkSticker"] = True
                                 chino.sendReplyMessage(msg.id, to, "Berhasil mengaktifkan check details sticker")
                                
                            elif cmd == "checksticker off":
                            	if msg._from in Owner:
                                 settings["checkSticker"] = False
                                 chino.sendReplyMessage(msg.id, to, "Berhasil menonaktifkan check details sticker")
                                
                            elif cmd == "unsendchat on":
                            	if msg._from in Owner:
                                 settings["unsendMessage"] = True
                                 chino.sendReplyMessage(msg.id, to, "Berhasil mengaktifkan unsend message")
                                
                            elif cmd == "unsendchat off":
                            	if msg._from in Owner:
                                 settings["unsendMessage"] = False
                                 chino.sendReplyMessage(msg.id, to, "Berhasil menonaktifkan unsend message")
                               
                            elif cmd == "welcome on":
                            	if msg._from in Owner:
                                 settings["welcomeMessage"] = True
                                 chino.sendReplyMessage(msg.id, to, "Berhasil Mengaktifkan Sambutan")
  
                            elif cmd == "welcome off":
                            	if msg._from in Owner:
                                 settings["welcomeMessage"] = False
                                 chino.sendReplyMessage(msg.id, to, "Berhasil Menonatifkan Sambutan")
 
                            elif cmd == "simi on":
                                simi2["simi-simi"][msg.to] = True
                                chino.sendReplyMessage(msg.id, to, "Simi-Simi Sudah Aktif")

                            elif cmd == "simi off":
                                simi2["simi-simi"][msg.to] = False
                                chino.sendReplyMessage(msg.id, to, "Simi-Simi Dinonaktifkan")                            
                             
                            elif cmd == "sider off":
                                if msg.to in cctv['point']:
                                    cctv['cyduk'][msg.to]=False
                                    wait["Sider"] = False
                                    chino.sendMessage(msg.to, "Cek Sider Off")
                                else:
                                    chino.sendMessage(msg.to, "Heh Belom Di Set")
                                    
                            elif cmd =="sider on":
                                try:
                                    del cctv['point'][msg.to]
                                    del cctv['sidermem'][msg.to]
                                    del cctv['cyduk'][msg.to]
                                except:
                                           pass
                                           cctv['point'][msg.to] = msg.id
                                           cctv['sidermem'][msg.to] = ""
                                           cctv['cyduk'][msg.to]=True
                                           wait["Sider"] = True
                                           chino.sendMessage(msg.to,"Siap On Cek Sider")    
                               
   
                            elif cmd == "status":
                                try:
                                    ret_ = "╭──[ Status ]"
                                    if settings["autoAdd"] == True: ret_ += "\n│[ ON ] Auto Add"
                                    else: ret_ += "\n│[ OFF ] Auto Add"
                                    if settings["autoJoin"] == True: ret_ += "\n│[ ON ] Auto Join"
                                    else: ret_ += "\n│[ OFF ] Auto Join"
                                    if settings["autoLeave"] == True: ret_ += "\n│[ ON ] Auto Leave Room"
                                    else: ret_ += "\n│[ OFF ] Auto Leave Room"
                                    if settings["autoJoinTicket"] == True: ret_ += "\n│[ ON ] Auto Join Ticket"
                                    else: ret_ += "\n│[ OFF ] Auto Join Ticket"
                                    if settings["autoRead"] == True: ret_ += "\n│[ ON ] Auto Read"
                                    else: ret_ += "\n│[ OFF ] Auto Read"
                                    if settings["autoRespon"] == True: ret_ += "\n│[ ON ] Detect Mention"
                                    else: ret_ += "\n│[ OFF ] Detect Mention"
                                    if settings["checkContact"] == True: ret_ += "\n│[ ON ] Check Contact"
                                    else: ret_ += "\n│[ OFF ] Check Contact"
                                    if settings["checkPost"] == True: ret_ += "\n│[ ON ] Check Post"
                                    else: ret_ += "\n│[ OFF ] Check Post"
                                    if settings["checkSticker"] == True: ret_ += "\n│[ ON ] Check Sticker"
                                    else: ret_ += "\n│[ OFF ] Check Sticker"
                                    if settings["setKey"] == True: ret_ += "\n│[ ON ] Set Key"
                                    else: ret_ += "\n│[ OFF ] Set Key"
                                    if settings["unsendMessage"] == True: ret_ += "\n│[ ON ] Unsend Message"
                                    else: ret_ += "\n│[ OFF ] Unsend Message"
                                    ret_ += "\n╰──[ Status ]"
                                    contact = chino.getContact(msg._from)
                                    chino.sendReplyMessage(msg.id, to, str(ret_), {'AGENT_LINK': 'line://ti/p/~bacbac.id','AGENT_ICON': "http://dl.profile.line-cdn.net/" + contact.pictureStatus,'AGENT_NAME': "Status"})
                                except Exception as e:
                                    chino.sendMessage(msg.to, str(e))                          
# Pembatas Script #                                
                            elif cmd == "crash":
                            	if msg._from in Owner:
                                 chino.sendContact(to, "u6347d96f19332503ee90b48d630ec27e',")                                 
                                                                                                                                                           
                            elif cmd == 'me':
                                chino.generateReplyMessage(msg.id)
                                contact = chino.getContact(sender)        
                                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                chino.sendReplyMention(msg.id, to, '[ Profile ]\n@!   ',[sender])
                                chino.sendReplyMessage(msg.id,to, "Bagas",contentMetadata={'vCard': 'BEGIN:VCARD\r\nVERSION:3.0\r\nPRODID:ANDROID 8.13.3 Android OS 4.4.4\r\nFN:\\Bagas Gans Here'+'\nTEL;TYPE=mobile:'+chino.getContact(sender).statusMessage+'\r\nN:?;\\,\r\nEND:VCARD\r\n', 'displayName': chino.getContact(sender).displayName},contentType=13)                                
#Self
                            elif cmd == "mymid":
                                chino.sendReplyMessage(msg.id, to, "[ MID ]\n{}".format(sender))
                                
                            elif cmd == "myname":
                                contact = chino.getContact(sender)
                                chino.sendReplyMessage(msg.id, to, "[ Display Name ]\n{}".format(contact.displayName))
                                
                            elif cmd == "mybio":
                                contact = chino.getContact(sender)
                                chino.sendReplyMessage(msg.id, to, "[ Status Message ]\n{}".format(contact.statusMessage))
                                
                            elif cmd == "mypicture":
                                contact = chino.getContact(sender)
                                chino.sendReplyImageWithURL(msg.id, to,"http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))
                                
                            elif cmd == "myvideoprofile":
                                contact = chino.getContact(sender)
                                chino.sendReplyVideoWithURL(msg.id, to,"http://dl.profile.line-cdn.net/{}/vp".format(contact.pictureStatus))
                                
                            elif cmd == "mycover":
                                channel = chino.getProfileCoverURL(sender)          
                                path = str(channel)
                                chino.sendReplyImageWithURL(msg.id, to, path)
#Steal#
                            elif cmd.startswith("stealmid "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    ret_ = "[ Mid User ]"
                                    for ls in lists:
                                        ret_ += "\n{}".format(str(ls))
                                    chino.sendReplyMessage(msg.id, to, str(ret_))
                                    
                            elif cmd.startswith("stealname "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = chino.getContact(ls)
                                        chino.sendReplyMessage(msg.id, to, "[ Display Name ]\n{}".format(str(contact.displayName)))
                                        
                            elif cmd.startswith("stealbio "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = chino.getContact(ls)
                                        chino.sendReplyMessage(msg.id, to, "[ Status Message ]\n{}".format(str(contact.statusMessage)))
                                        
                            elif cmd.startswith("stealpicture"):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = chino.getContact(ls)
                                        path = "http://dl.profile.line.naver.jp/{}".format(contact.pictureStatus)
                                        chino.sendReplyImageWithURL(msg.id, to, str(path))
                                        
                            elif cmd.startswith("stealvideoprofile "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = chino.getContact(ls)
                                        path = "http://dl.profile.line.naver.jp/{}/vp".format(contact.pictureStatus)
                                        chino.sendReplyVideoWithURL(msg.id, to, str(path))
                                        
                            elif cmd.startswith("stealcover "):
                                if chino != None:
                                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                                        names = re.findall(r'@(\w+)', text)
                                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                        mentionees = mention['MENTIONEES']
                                        lists = []
                                        for mention in mentionees:
                                            if mention["M"] not in lists:
                                                lists.append(mention["M"])
                                        for ls in lists:
                                            channel = chino.getProfileCoverURL(ls)
                                            path = str(channel)
                                            chino.sendReplyImageWithURL(msg.id, to, str(path))
#Group#
                            elif cmd == 'groupcreator':
                                group = chino.getGroup(to)
                                GS = group.creator.mid
                                chino.sendContact(to, GS)
                                
                            elif cmd == 'groupid':
                                gid = chino.getGroup(to)
                                chino.sendReplyMessage(msg.id, to, "[ID Group : ]\n" + gid.id)
                                
                            elif cmd == 'grouppicture':
                                group = chino.getGroup(to)
                                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                                chino.sendReplyImageWithURL(msg.id, to, path)
                                
                            elif cmd == 'groupname':
                                gid = chino.getGroup(to)
                                chino.sendReplyMessage(msg.id, to, "[Nama Group : ]\n" + gid.name)
                                
                            elif cmd == 'groupticket':
                                if msg.toType == 2:
                                    group = chino.getGroup(to)
                                    if group.preventedJoinByTicket == False:
                                        ticket = chino.reissueGroupTicket(to)
                                        chino.sendReplyMessage(msg.id, to, "[ Group Ticket ]\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                                    else:
                                        chino.sendReplyMessage(msg.id, to, "Grup qr tidak terbuka silahkan buka terlebih dahulu dengan perintah {}openqr".format(str(settings["keyCommand"])))
                                        
                            elif cmd == 'groupticket on':
                                if msg.toType == 2:
                                    group = chino.getGroup(to)
                                    if group.preventedJoinByTicket == False:
                                        chino.sendReplyMessage(msg.id, to, "Grup qr sudah terbuka")
                                    else:
                                        group.preventedJoinByTicket = False
                                        chino.updateGroup(group)
                                        chino.sendReplyMessage(msg.id, to, "Berhasil membuka grup qr")
                                        
                            elif cmd == 'groupticket off':
                                if msg.toType == 2:
                                    group = chino.getGroup(to)
                                    if group.preventedJoinByTicket == True:
                                        chino.sendReplyMessage(msg.id, to, "Grup qr sudah tertutup")
                                    else:
                                        group.preventedJoinByTicket = True
                                        chino.updateGroup(group)
                                        chino.sendReplyMessage(msg.id, to, "Berhasil menutup grup qr")
                                        
                            elif cmd == 'groupinfo':
                                group = chino.getGroup(to)
                                try:
                                    gCreator = group.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if group.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(group.invitee))
                                if group.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(chino.reissueGroupTicket(group.id)))
                                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                                ret_ = "╭──[ Group Info ]"
                                ret_ += "\n│ Nama Group : {}".format(str(group.name))
                                ret_ += "\n│ ID Group : {}".format(group.id)
                                ret_ += "\n│ Pembuat : {}".format(str(gCreator))
                                ret_ += "\n│ Jumlah Member : {}".format(str(len(group.members)))
                                ret_ += "\n│ Jumlah Pending : {}".format(gPending)
                                ret_ += "\n│ Group Qr : {}".format(gQr)
                                ret_ += "\n│ Group Ticket : {}".format(gTicket)
                                ret_ += "\n╰──[ Finish ]"
                                chino.sendReplyMessage(msg.id, to, str(ret_))
                                chino.sendReplyImageWithURL(msg.id, to, path)
                                
                            elif cmd == 'groupmemberlist':
                                if msg.toType == 2:
                                    group = chino.getGroup(to)
                                    ret_ = "╭──[ Member List ]"
                                    no = 0 + 1
                                    for mem in group.members:
                                        ret_ += "\n│ {}. {}".format(str(no), str(mem.displayName))
                                        no += 1
                                    ret_ += "\n╰──[ Total {} ]".format(str(len(group.members)))
                                    chino.sendReplyMessage(msg.id, to, str(ret_))
#Token#
                            elif text.lower() == 'token chromeos':
                                req = requests.get(url = 'https://api.eater.pw/CHROMEOS')
                                a = req.text
                                b = json.loads(a)
                                tknop = codecs.open("tkn.json","r","utf-8")
                                tkn = json.load(tknop)
                                tkn['{}'.format(msg._from)] = []
                                tkn['{}'.format(msg._from)].append({
                                    'qr': b['result'][0]['linkqr'],
                                    'tkn': b['result'][0]['linktkn']
                                    })
                                qrz = b['result'][0]['linkqr']
                                chino.sendReplyMessage(msg.id, to, "Klik Link ini dan Login \n\n{}\n\nKetik Token done kalau sudah".format(qrz))
                                with open('tkn.json', 'w') as outfile:
                                    json.dump(tkn, outfile)
                                    
                            elif text.lower() == 'token done':
                                tknop= codecs.open("tkn.json","r","utf-8")
                                tkn = json.load(tknop)
                                a = tkn['{}'.format(msg._from)][0]['tkn']
                                req = requests.get(url = '{}'.format(a))
                                b = req.text
                                chino.sendMessage(msg.to, '{}'.format(b))

                            elif text.lower() == 'token iosipad':
                                req = requests.get(url = 'https://api.eater.pw/IOSIPAD')
                                a = req.text
                                b = json.loads(a)
                                tknop = codecs.open("tkn.json","r","utf-8")
                                tkn = json.load(tknop)
                                tkn['{}'.format(msg._from)] = []
                                tkn['{}'.format(msg._from)].append({
                                    'qr': b['result'][0]['linkqr'],
                                    'tkn': b['result'][0]['linktkn']
                                    })
                                qrz = b['result'][0]['linkqr']
                                chino.sendReplyMessage(msg.id, to, "Klik Link ini dan Login \n\n{}\n\nKetik Token done kalau sudah".format(qrz))
                                with open('tkn.json', 'w') as outfile:
                                    json.dump(tkn, outfile)

                            elif text.lower() == 'token desktopwin':
                                req = requests.get(url = 'https://api.eater.pw/DESKTOPWIN')
                                a = req.text
                                b = json.loads(a)
                                tknop = codecs.open("tkn.json","r","utf-8")
                                tkn = json.load(tknop)
                                tkn['{}'.format(msg._from)] = []
                                tkn['{}'.format(msg._from)].append({
                                    'qr': b['result'][0]['linkqr'],
                                    'tkn': b['result'][0]['linktkn']
                                    })
                                qrz = b['result'][0]['linkqr']
                                chino.sendReplyMessage(msg.id, to, "Klik Link ini dan Login \n\n{}\n\nKetik Token done kalau sudah".format(qrz))
                                with open('tkn.json', 'w') as outfile:
                                    json.dump(tkn, outfile)
 
                            elif text.lower() == 'token desktopmac':
                                req = requests.get(url = 'https://api.eater.pw/DESKTOPMAC')
                                a = req.text
                                b = json.loads(a)
                                tknop = codecs.open("tkn.json","r","utf-8")
                                tkn = json.load(tknop)
                                tkn['{}'.format(msg._from)] = []
                                tkn['{}'.format(msg._from)].append({
                                    'qr': b['result'][0]['linkqr'],
                                    'tkn': b['result'][0]['linktkn']
                                    })
                                qrz = b['result'][0]['linkqr']
                                chino.sendReplyMessage(msg.id, to, "Klik Link ini dan Login \n\n{}\n\nKetik Token done kalau sudah".format(qrz))
                                with open('tkn.json', 'w') as outfile:
                                    json.dump(tkn, outfile)

                            elif text.lower() == 'token win10':
                                req = requests.get(url = 'https://api.eater.pw/WIN10')
                                a = req.text
                                b = json.loads(a)
                                tknop = codecs.open("tkn.json","r","utf-8")
                                tkn = json.load(tknop)
                                tkn['{}'.format(msg._from)] = []
                                tkn['{}'.format(msg._from)].append({
                                    'qr': b['result'][0]['linkqr'],
                                    'tkn': b['result'][0]['linktkn']
                                    })
                                qrz = b['result'][0]['linkqr']
                                chino.sendReplyMessage(msg.id, to, "Klik Link ini dan Login \n\n{}\n\nKetik Token done kalau sudah".format(qrz))
                                with open('tkn.json', 'w') as outfile:
                                    json.dump(tkn, outfile)
# Pembatas Script #                            
                            elif cmd == 'grouplist':
                            	if msg._from in Owner:
                                    groups = chino.getGroupIdsJoined()
                                    ret_ = "╭──[ Group List ]"
                                    no = 0 + 1
                                    for gid in groups:
                                        group = chino.getGroup(gid)
                                        ret_ += "\n│{}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                                        no += 1
                                    ret_ += "\n╰──[ Total {} Groups ]".format(str(len(groups)))
                                    chino.sendReplyMessage(msg.id, to, str(ret_))
                                    thread1 = Thread(target=chino.sendMessage, args=(to, str(ret_)))                                                    
# Pembatas Script #
                            elif cmd.startswith("changename:"):
                            	if msg._from in Owner:
                                    sep = text.split(" ")
                                    string = text.replace(sep[0] + " ","")
                                    if len(string) <= 20:
                                        profile = chino.getProfile()
                                        profile.displayName = string
                                        chino.updateProfile(profile)
                                        chino.sendReplyMessage(msg.id, to,"Berhasil mengganti display name menjadi{}".format(str(string)))
                                    
                            elif cmd.startswith("changebio:"):
                            	if msg._from in Owner:
                                    sep = text.split(" ")
                                    string = text.replace(sep[0] + " ","")
                                    if len(string) <= 500:
                                        profile = chino.getProfile()
                                        profile.statusMessage = string
                                        chino.updateProfile(profile)
                                        chino.sendReplyMessage(msg.id, to,"Berhasil mengganti status message menjadi{}".format(str(string)))        
                                                                
                            elif cmd.startswith("byeall"):
                            	if msg._from in Owner:                            		
                            		gr = chino.getGroupIdsJoined()
                            		for group in gr:
                            			chino.sendMessage(group, "Please Invite Me in 5 minutes again i'm sorry (ಥ_ಥ)\n\nmore info? http://line.me/ti/p/2fX-rPF8EL")
                            			chino.leaveGroup(group)
#MEDIA#                           
                            elif cmd.startswith("music"):
                                try:
                                    proses = text.split(" ")
                                    urutan = text.replace(proses[0] + " ","")
                                    r = requests.get("http://api.zicor.ooo/joox.php?song={}".format(str(urllib.parse.quote(urutan))))
                                    data = r.text
                                    data = json.loads(data)
                                    b = data
                                    c = str(b["title"])
                                    d = str(b["singer"])
                                    e = str(b["url"])
                                    f = str(b["lyric"])
                                    g = str(b["image"])
                                    hasil = "Penyanyi: "+str(d)
                                    hasil += "\nJudul : "+str(c)
                                    hasil += "\nLyric : "+str(f)
                                    chino.sendReplyImageWithURL(msg.id, to,g)
                                    chino.sendReplyAudioWithURL(msg.id, to,e)
                                    chino.sendReplyMessage(msg.id, to,hasil)
                                except Exception as error:
                                    chino.sendReplyMessage(msg.id, to, "error\n" + str(error))
                                    logError(error)

                            elif cmd.startswith("image "):
                                try:
                                    search = cmd.replace("image ","")
                                    r = requests.get("https://xeonwz.herokuapp.com/images/google.api?q={}".format(search))
                                    data = r.text
                                    data = json.loads(data)
                                    if data["content"] != []:
                                        items = data["content"]
                                        path = random.choice(items)
                                        a = items.index(path)
                                        b = len(items)
                                        chino.sendReplyImageWithURL(msg.id, to, str(path))
                                        thread1 = Thread(target=chino.sendImageWithURL, args=(to, str(path)))
                                except Exception as error:
                                     logError(error)
                                     var= traceback.print_tb(error.__traceback__)
                                     chino.sendReplyMessage(msg.id, to,str(var))

                            elif cmd.startswith("stickerline "):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                url = requests.get("http://api.zicor.ooo/lstickers.php?search={}".format(txt))
                                data = url.json()
                                no = 0
                                result = "╭──[ Sticker Line ]"
                                for anu in data["items"]:
                                    no += 1
                                    result += "\n│{}. {}".format(str(no),str(anu["title"]))
                                    result += "\nhttps://store.line.me{}".format(str(anu["productUrl"]))
                                result += "\n╰──[ {} Sticker ]".format(str(len(data["items"])))
                                chino.sendReplyMessage(msg.id, to, result)                                                      
                                        
                            elif cmd.startswith("imagetext "):
                                text_ = removeCmd("imagetext", text)
                                web = _session
                                web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                font = random.choice(["arial","comic"])
                                r = web.get("http://api.img4me.com/?text=%s&font=%s&fcolor=FFFFFF&size=35&bcolor=000000&type=jpg" %(urllib.parse.quote(text_),font))
                                data = str(r.text)
                                if "Error" not in data:
                                    path = data
                                    chino.sendImageWithURL(to,path)
                                else:
                                    chino.sendReplyMessage(msg.id, to,"[RESULT] %s" %(data.replace("Error: ")))
                                                      
                            elif cmd.startswith("ytdl "):
                                try:
                                     sep = msg.text.split(" ")
                                     text = msg.text.replace(sep[0] + " ","")
                                     qx = text
                                     vid = pafy.new(qx)
                                     stream = vid.streams
                                     best = vid.getbest()
                                     best.resolution, best.extension
                                     me = best.url
                                     chino.sendReplyMessage(msg.id, to, "Send Video On Process ✈️")
                                     chino.sendVideoWithURL(msg.to, me)
                                     chino.sendMessage(msg.to, me)
                                except Exception as e:
                                     chino.sendMessage(msg.to,str(e))

                            elif cmd.startswith("chatowner: "):
                                contact = chino.getContact(sender)
                                sep = text.split(" ")
                                bagas = text.replace(sep[0] + " ","")
                                for own in Owner:
                                	result = "@!"
                                	result += "\nSender : {}".format(contact.displayName)
                                	result += "\nPesan : {}".format(bagas)
                                	result += "\nMid : {}".format(contact.mid)
                                	chino.sendReplyMessage(msg.id, to, "Succesfully send chat to Owner")
                                	sendMention(own, result, [sender])
                                	chino.sendContact(own, sender)

                            elif cmd.startswith("themeline "):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                url = requests.get("http://api.zicor.ooo/ltheme.php?search={}".format(txt))
                                data = url.json()
                                no = 0
                                result = "╭──[ Theme Line ]"
                                for anu in data["items"]:
                                   no += 1
                                   result += "\n│{}. {}".format(str(no),str(anu["title"]))
                                   result += "\nhttps://store.line.me{}".format(str(anu["productUrl"]))
                                result += "\n╰──[ {} Tema ]".format(str(len(data["items"])))
                                chino.sendReplyMessage(msg.id, to, result)
                            
                            elif text.lower().startswith('artisifatnama'):
                                try:
                                    sep = text.split(" ")
                                    search = text.replace(sep[0] + " ","")
                                    r = requests.get("http://syadnysyz2.herokuapp.com/api/ramalan-nama?nama=/{}".format(search))
                                    data = r.json()
                                    a=" Type: Ramalan Nama\n"
                                    a+="\nRomantis : "+str(data["result"]["romantis"])
                                    a+="\nMesum : "+str(data["result"]["mesum"])
                                    a+="\nMiris : "+str(data["result"]["miris"])
                                    a+="\nTulus : "+str(data["result"]["tulus"])
                                    a+="\nLoyal : "+str(data["result"]["loyal"])
                                    chino.sendReplyMessage(msg.id, to,a)
                                except Exception as e:
                                    chino.sendReplyMessage(msg.id, to, str(e))

                            elif text.lower().startswith('artinama'):
                                try:
                                    sep = text.split(" ")
                                    search = text.replace(sep[0] + " ","")
                                    r = requests.get("http://syadnysyz2.herokuapp.com/api/ramalan-primbon/artinama?nama=/{}".format(search))
                                    data = r.json()
                                    a=" 「 Fun 」\nType: Arti Nama\n"
                                    a+="\nRomantis : "+str(data["arti"])
                                    chino.sendReplyMessage(msg.id, to,a)
                                except Exception as e:
                                    chino.sendReplyMessage(msg.id, to, str(e))
                            
                            elif cmd == "mention":
                            	group = chino.getGroup(to)
                            	midMembers = [contact.mid for contact in group.members]
                            	midSelect = len(midMembers)//20
                            	for mentionMembers in range(midSelect+1):
                            		no = 0
                            		ret_ = "╭──[ Mention Message ]"
                            		dataMid = []
                            		for dataMention in group.members[mentionMembers*20 : (mentionMembers+1)*20]:
                            			dataMid.append(dataMention.mid)
                            			no += 1
                            			ret_ += "\n│{}. @!".format(str(no))
                            		ret_ += "\n╰──[ Total {} Members ]".format(str(len(dataMid)))
                            		sendMention(to, ret_, dataMid)                                    

                            elif cmd.startswith("downloadyt"):
                                #if msg._from in admin:
                                try:
                                    sep = msg.text.split(" ")
                                    kudanil = text.replace(sep[0] + " ","")
                                    r = requests.get("http://api.farzain.com/yt_download.php?id={}&apikey=CariApikeySndirihHu5Tv54tFWtrJy7Sh4zU4ANz".format(kudanil))
                                    data = r.text
                                    data = json.loads(data)
                                    chino.sendVideoWithURL(msg.to, str(data["urls"][0]["id"]))
                                except Exception as e:
                                    chino.sendMessage(msg.to, str(e))

                            elif cmd.startswith("whois "):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                url = requests.get("https://arsybaiapi.herokuapp.com/knowledge={}".format(txt))
                                data = url.json()
                                contact = chino.getContact(sender)
                                no = 0
                                result = "╭──[{}]".format(contact.displayName)
                                anu = data["result"]
                                no += 1
                                result += "\n│{}. {}".format(str(no),(anu["name"]))
                                result += "\n│Url = {}".format(anu["url"])
                                result += "\n│Artikel = {}".format(anu["article"])
                                result += "\n│Deskripsi = {}".format(anu["description"])
                                result += "\n╰──[ {} ]".format(anu["name"])
                                chino.sendReplyMessage(msg.id, to, result)
                                chino.sendReplyImageWithURL(msg.id, to, anu["img"])                             

                            elif cmd.startswith('ssweb'):
                                sep = text.split(" ")
                                query = text.replace(sep[0] + " ","")
                                r = "https://image.thum.io/get/width/1200/http://{}".format(query)
                                chino.sendImageWithURL(receiver, r)

                            elif cmd.startswith("animequotes"):
                                try:
                                    sep = text.split(" ")
                                    r = requests.get("https://rest.farzain.com/api/animequotes.php?apikey=CariApikeySndirihHu5Tv54tFWtrJy7Sh4zU4ANz")
                                    data = r.text
                                    data = json.loads(data)
                                    ret_ = "●Quote : "+ str(data["result"]["quote"])
                                    ret_ += "\n\n●Author : "+ str(data["result"]["author"])
                                    ret_ += "\n\n●Anime : "+ str(data["result"]["anime"])
                                    chino.sendReplyMessage(msg.id, to, str(ret_))
                                except Exception as error:
                                    chino.sendReplyMessage(msg.id, to, "error\n" + str(error))
                                    logError(error)

                            elif cmd.startswith("ztext "):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                zal = zalgo.zalgo().zalgofy('{}'.format(txt))
                                chino.sendReplyMessage(msg.id, to, zal)
                            
                            elif cmd.startswith("fmylife"):
                                result = requests.get("http://www.fmylife.com/random")
                                data = BeautifulSoup(result.content, 'html5lib')                                                                             
                                for sam in data.findAll('figure', attrs={'class':'text-center visible-xs'}):                                        
                                    path = str(sam.find('img')['data-src'])                                    
                                chino.sendReplyImageWithURL(msg.id, to, str(path))
                                thread1 = Thread(target=chino.sendImageWithURL, args=(to, str(path)))

                            elif cmd.startswith("motivate"):
                                r = requests.get("https://talaikis.com/api/quotes/random")
                                data=r.text
                                data=json.loads(data)                                                                   
                                chino.sendReplyMessage(msg.id, to,str(data["quote"]))
     
                            elif cmd == "bitcoin" or cmd == " bitcoin":
                                r=requests.get("https://xeonwz.herokuapp.com/bitcoin.api")
                                data=r.text
                                data=json.loads(data)
                                hasil = "「 Bitcoin 」\n" 
                                hasil += "\nPrice : " +str(data["btc"])
                                hasil += "\nExpensive : " +str(data["high"])
                                hasil += "\nCheap : " +str(data["low"])
                                chino.sendReplyMessage(msg.id, to, str(hasil))  

                            elif cmd.startswith("topnews"):
                                try:
                                    api_key = "a53cb61cee4d4c518b69473893dba73b"
                                    r = _session.get("https://newsapi.org/v2/top-headlines?country=id&apikey=CariApikeySndiri{}".format(str(api_key)))
                                    data = r.text
                                    data = json.loads(data)
                                    ret_ = "Top News"
                                    no = 1
                                    anu = data["articles"]
                                    if len(anu) >= 5:
                                        for s in range(5):
                                            syit = anu[s]
                                            sumber = syit['source']['name']
                                            author = syit['author']
                                            judul = syit['title']
                                            url = syit['url']
                                            ret_ += "\n\n{}. Judul : {}\n    Sumber : {}\n    Penulis : {}\n    Link : {}".format(str(no), str(judul), str(sumber), str(author), str(url))
                                            no += 1
                                    else:
                                         for s in anu:
                                            syit = s
                                            sumber = syit['source']['name']
                                            author = syit['author']
                                            judul = syit['title']
                                            url = syit['url']
                                            ret_ += "\n\n{}. Judul : {}\n    Sumber : {}\n    Penulis : {}\n    Link : {}".format(str(no), str(judul), str(sumber), str(author), str(url))
                                            no += 1
                                    chino.sendReplyMessage(msg.id, to, str(ret_))
                                except:
                                    chino.sendReplyMessage(msg.id, to, "Porn Not Found !")

                            elif cmd.startswith("top kaskus"):                                
                                r = requests.get("https://api.bayyu.net/kaskus-hotthread/?apikey=CariApikeySndiric28c944199384f191335f1f8924414fa839350d&page=2")
                                data=r.text
                                data=json.loads(data)                                                                                                      
                                if data["hot_threads"] != []:
                                    no = 0
                                    hasil = " Kaskus Search \n"
                                    for news in data["hot_threads"]:
                                          no += 1                  
                                          hasil += "\n" + str(no) + ". Judul : " + str(news["title"]) + "\n  Deskripsi : " + str(news["detail"]) + "\n Link: " + str(news["link"]) + "\n"
                                          hasil += "\n"
                                    chino.sendReplyMessage(msg.id, to, str(hasil))      
         
                            elif cmd.startswith("wallpaper-hd "):
                                sep = msg.text.split(" ")
                                nama = msg.text.replace(sep[0] + " ","")
                                cond = nama.split("|")
                                key = str(cond[0])
                                caps = key.upper()
                                chino.sendMessage(msg.to, "Sedang Mencari Data...")
                                webnya = requests.get("https://api.eater.pw/wallp/"+key)
                                data = webnya.text
                                data = json.loads(data)
                                no=0
                                hasil="[ RESULT WALLPAPER HD "+caps+" ]\n\n"
                                if len(cond) == 1:
                                    for nadia in data["result"]:
                                        no+=1
                                        hasil+="{}. {}\n".format(str(no), str(nadia["judul"]))
                                        ret_="\nSelanjutnya ketik :\nWallpaper-hd "+key+"|nomor list\nUntuk melihat detail gambar"
                                    chino.sendReplyMessage(msg.id, to, str(hasil)+ret_)
                                elif len(cond) == 2:
                                    no = int(cond[1])
                                    if no <= len(data["result"]):                                       
                                        gambar = data["result"][no - 1]
                                        chino.sendReplyMessage(msg.id, to, "Judul : "+str(gambar["judul"]))
                                        chino.sendReplyImageWithURL(msg.id, to, str(gambar["link"]))                                          
 
                            elif cmd.startswith("asking "):
                                kata = removeCmd("asking", text)
                                sch = kata.replace(" ","+")
                                with _session as web:
                                    urlz = "http://lmgtfy.com/?q={}".format(str(sch))
                                    r = _session.get("http://tiny-url.info/api/v1/create?apikey=CariApikeySndiriA942F93B8B88C698786A&provider=cut_by&format=json&url={}".format(str(urlz)))
                                    data = r.text
                                    data = json.loads(data)
                                    url = data["shorturl"]
                                    ret_ = "Ask"
                                    ret_ += "\n\nLink : {}".format(str(url))
                                    chino.sendReplyMessage(msg.id, to, str(ret_))

                            elif cmd.startswith("deviantart "):
                                try:
                                    search = cmd.replace("devianart ","")
                                    r = requests.get("https://xeonwz.herokuapp.com/images/deviantart.api?q={}".format(search))
                                    data = r.text
                                    data = json.loads(data)
                                    if data["content"] != []:
                                        items = data["content"]
                                        path = random.choice(items)
                                        a = items.index(path)
                                        b = len(items)
                                        chino.sendReplyImageWithURL(msg.id, to, str(path))
                                        thread1 = Thread(target=chino.sendImageWithURL, args=(to, str(path)))
                                except Exception as error:
                                    logError(error)
                                    var= traceback.print_tb(error.__traceback__)
                                    chino.sendReplyMessage(msg.id, to,str(var))                                                      
                            
                            elif cmd.startswith("randomimage"):
                                 bagasGans = requests.get("https://api.tanyz.xyz/imageGen")
                                 data = bagasGans.json()                               
                                 chino.sendReplyImageWithURL(msg.id, to, data["Hasil"])                        		                             	
                           
                            elif cmd.startswith("creepypasta"):
                                r=requests.get("http://hipsterjesus.com/api")
                                data=r.text
                                data=json.loads(data)
                                hasil = "「 Creepypasta 」\n" 
                                hasil += str(data["text"])
                                chino.sendReplyMessage(msg.id, to, str(hasil))
                            
                            elif cmd.startswith("imageart "):
                                try:                                   
                                    search = cmd.replace("imageart ","")
                                    r = requests.get("https://xeonwz.herokuapp.com/images/deviantart.api?q={}".format(search))
                                    data = r.text
                                    data = json.loads(data)
                                    if data["content"] != []:
                                        items = data["content"]
                                        path = random.choice(items)
                                        a = items.index(path)
                                        b = len(items)
                                        chino.sendReplyImageWithURL(msg.id, to, str(path))
                                        chino.sendReplyMessage(msg.id, to,"Art #%s from #%s." %(str(a),str(b)))
                                        log.info("Art #%s from #%s." %(str(a),str(b)))
                                except Exception as error:
                                    log.info(error)

                            elif cmd.startswith("neon: "):
                                try:
                                     txt = msg.text.split(" ")
                                     teks = msg.text.lower().replace("neon: ","")
                                     color = ["red","yellow","green","purple","violet","blue"]
                                     k = random.choice(color)
                                     foto = "https://ari-api.herokuapp.com/neon?text="+teks+"&color="+k+""
                                     sendMentionV2(msg.to, "@! ini foto neon pesanan kamu..", [msg._from])
                                     chino.sendImageWithURL(msg.to, foto)
                                except Exception as e:
                                     chino.sendMessage(msg.to, str(e))

                            elif cmd.startswith("zodiaceng ") and sender == chinoMid:
                                string = cmd.replace("zodiaceng ","")   
                                r=requests.get("http://horoscope-api.herokuapp.com/horoscope/week/{}".format(str(string)))
                                data=r.text
                                data=json.loads(data)
                                hasil="Zodiac Result:\n"
                                hasil += "\nZodiac: " +str(data["sunsign"])
                                hasil += "\n\n"+str(data["horoscope"])
                                hasil += "\n\nDate: " +str(data["week"])                                                                                                                                                          
                                chino.sendReplyMessage(msg.id, to,str(hasil))

                            elif cmd.startswith("timezone "):
                                try:
                                    search = cmd.replace("timezone ","")
                                    r = requests.get("https://time.siswadi.com/geozone/{}".format(urllib.parse.quote(search)))
                                    data=r.text
                                    data=json.loads(data)
                                    ret_ = "「 Timezone 」\n"
                                    ret_ += "\nLatitude : " +str(data["data"]["latitude"])
                                    ret_ += "\nLongitude : " +str(data["data"]["longitude"])
                                    ret_ += "\nAddress : " +str(data["data"]["address"])
                                    ret_ += "\nCountry : " +str(data["data"]["country"])
                                    chino.sendReplyMessage(msg.id, to, str(ret_))
                                except Exception as error:
                                   chino.sendReplyMessage(msg.id, to, str(error))
                                              
                            elif cmd.startswith("zodiacind "):
                                sep = msg.text.split(" ")
                                url = msg.text.replace(sep[0] + " ","")    
                                with requests.session() as s:
                                    s.headers['user-agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                                    r = s.get("https://www.vemale.com/zodiak/{}".format(urllib.parse.quote(url)))
                                    soup = BeautifulSoup(r.content, 'html5lib')
                                    ret_ = ""
                                    for a in soup.select('div.vml-zodiak-detail'):
                                        ret_ += a.h1.string
                                        ret_ += "\n"+ a.h4.string
                                        ret_ += " : "+ a.span.string +""
                                    for b in soup.select('div.col-center'):
                                        ret_ += "\nTanggal : "+ b.string
                                    for d in soup.select('div.number-zodiak'):
                                        ret_ += "\nAngka keberuntungan : "+ d.string
                                    for c in soup.select('div.paragraph-left'):
                                        ta = c.text
                                        tab = ta.replace("    ", "")
                                        tabs = tab.replace(".", ".\n")
                                        ret_ += "\n"+ tabs
                                        #print (ret_)
                                        chino.sendReplyMessage(msg.id, to, str(ret_))
                                        
                            elif cmd.startswith("binary"):
                                try:
                                     sep = msg.text.split(" ")
                                     teks = text.replace(sep[0] + " ","")
                                     s_b = bytes(teks, "ascii")
                                     anu = (" ".join(["{0:b}".format(x) for x in s_b]))
                                     chino.sendReplyMessage(msg.id, to, str(anu))
                                except Exception as error:
                                     chino.sendReplyMessage(msg.id, to, "error\n" + str(error))
                                     logError(error)
                                     
                            elif cmd.startswith("checkweather "):
                                try:
                                     sep = text.split(" ")
                                     location = text.replace(sep[0] + " ","")
                                     r = requests.get("https://rest.farzain.com/api/cuaca.php?apikey=CariApikeySndiriCariApikeySndirivZRHv2Fptb7CX4OgfHRaLMi6D&id={}".format(location), timeout=3)
                                     data = r.text
                                     data = json.loads(data)
                                     tz = pytz.timezone("Asia/Makassar")
                                     timeNow = datetime.now(tz=tz)
                                     ret_ = "╭──[ Weather Status ]"
                                     ret_ += "\n│Location : " + str(data["respon"]["tempat"])
                                     ret_ += "\n├──[ Weather Info ]"
                                     ret_ += "\n│Weather : " + str(data["respon"]["cuaca"])
                                     ret_ += "\n│Temprature : " + str(data["respon"]["suhu"])
                                     ret_ += "\n│Humidity : " + str(data["respon"]["kelembapan"])
                                     ret_ += "\n│Wind Pressure : " + str(data["respon"]["udara"])
                                     ret_ += "\n│Wind Speed : " + str(data["respon"]["angin"])
                                     ret_ += "\n╰──[ Finish ]"
                                     chino.sendReplyMessage(msg.id, to, str(ret_))
                                except Exception as error:
                                     chino.sendReplyMessage(msg.id, to, "error\n"+str(error))
                                     logError(error)
                                     
                            elif cmd.startswith("checkpraytime "):
                                sep = text.split(" ")
                                txt = text.replace(sep[0]+ " ","")
                                url = requests.get("https://time.siswadi.com/pray/{}".format(txt))
                                data = url.json()
                                ret_ = "╭──「 Praytime at {} 」".format(txt)
                                ret_ += "\n├ Date : {}".format(data["time"]["date"])
                                ret_ += "\n├ Subuh : {}".format(data["data"]["Fajr"])
                                ret_ += "\n├ Dzuhur : {}".format(data["data"]["Dhuhr"])
                                ret_ += "\n├ Ashar : {}".format(data["data"]["Asr"])
                                ret_ += "\n├ Magrib : {}".format(data["data"]["Maghrib"])
                                ret_ += "\n├ Isha : {}".format(data["data"]["Isha"])
                                ret_ += "\n├ 1/3 Malam : {}".format(data["data"]["SepertigaMalam"])
                                ret_ += "\n├ Tengah Malam : {}".format(data["data"]["TengahMalam"])
                                ret_ += "\n├ 2/3 Malam : {}".format(data["data"]["DuapertigaMalam"])
                                ret_ += "\n╰──「 {} 」".format(txt)
                                chino.sendReplyMessage(msg.id, to, str(ret_))
                                address = ''.format(data["location"]["address"])
                                latitude = float(data["location"]["latitude"])
                                longitude = float(data["location"]["longitude"])
                                chino.sendLocation(to, address,latitude,longitude)
                                
                            elif cmd.startswith("astronotnow"):  
                                with requests.session() as web:
                                    web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                    r = web.get("http://api.open-notify.org/astros.json")
                                    data = r.text
                                    data = json.loads(data)
                                    if data["message"] == "success":
                                        if data["people"] != []:
                                            number = data["number"]
                                            people = data["people"]
                                            ret_ = "╭──[ Astronot Di Luar Angkasa ]"
                                            for i in people:
                                               ret_ += "\n│Nama : {}".format(str(i["name"]))
                                               ret_ += "\n│Stasiun : {}".format(str(i["craft"]))
                                               ret_ += "\n│"
                                            ret_ += "\n╰──[ Saat Ini Ada {} ]".format(str(number))
                                            chino.sendReplyMessage(msg.id, to, str(ret_))
                                        else:
                                            chino.sendReplyMessage(msg.id, to, "Tak ada astronot di luar angkasa saat ini.")
                                    else:
                                        chino.sendReplyMessage(msg.id, to, "Ada kesalahan.")                
               
                            elif cmd.startswith("samehadaku"):
                                with requests.session() as web:
                                    web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                    r = web.get("https://api.rss2json.com/v1/api.json?rss_url=https://www.samehadaku.tv/feed")
                                    data = r.text
                                    data = json.loads(data)
                                    if data["status"] == "ok":
                                        if data["items"] != []:
                                            number = len(data["items"])
                                            items = data["items"]
                                            ret_ = "╭──[ Samehadaku ]"
                                            for i in items[:5]:
                                                ret_ += "\n│Judul : {}".format(str(i["title"]))
                                                ret_ += "\n│Rilis : {}".format(str(i["pubDate"]))
                                                ret_ += "\n│URL : {}".format(str(i["guid"]))
                                            ret_ += "\n╰──[ 5 Terbaru ]".format(str(number))
                                            chino.sendReplyMessage(msg.id, to, str(ret_))
                                        else:
                                            chino.sendReplyMessage(msg.id, to, "Tak ada data.")
                                    else:
                                        chino.sendReplyMessage(msg.id, to, "Ada kesalahan.")
                                        
                            elif cmd.startswith("reviewhp "):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split("|")
                                search = str(cond[0])
                                result = requests.get("http://api.farzain.com/gsmarena/gsmarena_search.php?id={}&apikey=CariApikeySndiriCariApikeySndirihHu5Tv54tFWtrJy7Sh4zU4ANz".format(str(search)))
                                data = result.text
                                data = json.loads(data)
                                if len(cond) == 1:
                                    num = 0
                                    ret_ = "╭──「 Result HandPhone 」"
                                    for music in data:
                                        num += 1
                                        ret_ += "\n│ {}. {}".format(str(num), str(music["title"]))
                                    ret_ += "\n╰──「 Total {} HandPhone 」".format(str(len(data)))
                                    ret_ += "\n\nUntuk Melihat Details HandPhone, silahkan gunakan command {} Reviewhp {}|「number」".format(str(setKey), str(search))
                                    chino.sendReplyMessage(msg.id, to, str(ret_))
                                elif len(cond) == 2:
                                    num = int(cond[1])
                                    if num <= len(data):
                                        music = data[num - 1]
                                        result = requests.get("http://api.farzain.com/gsmarena/gsmarena_info.php?apikey=CariApikeySndirihHu5Tv54tFWtrJy7Sh4zU4ANz&id={}".format(str(music["url"])))
                                        data = result.text
                                        data = json.loads(data)
                                        if data != []:
                                            ret_ = "╭──「 Handphone 」"
                                            ret_ += "\n│▪ Released : {}".format(str(data["released"]))
                                            ret_ += "\n│▪ Hardware : {}".format(str(data["hardware"]))
                                            ret_ += "\n│▪ OS : {}".format(str(data["OS"]))
                                            ret_ += "\n│▪ Storage : {}".format(str(data["storage"]))
                                            ret_ += "\n│▪ Popularity : {}".format(str(data["popularity"]))
                                            ret_ += "\n│▪ Fans : {}".format(str(data["fans"]))
                                            ret_ += "\n│▪ Resolution : {}".format(str(data["resolution"]))
                                            ret_ += "\n│▪ Camera : {}".format(str(data["camera"]))
                                            ret_ += "\n│▪ Expansion : {}".format(str(data["expansion"]))
                                            ret_ += "\n│▪ Battery : {}".format(str(data["battery"]))
                                            ret_ += "\n╰──「 FINISH 」"
                                            #gambar_hp = str(music["img"])
                                            #chino.sendImage(to, gambar_hp)
                                            chino.sendReplyMessage(msg.id, to, str(ret_))
                            elif cmd.startswith("window "):
                                dinn = requests.get("http://api.zicor.ooo/fwindow.php?text="+str(msg.text.replace(msg.text.split(' ')[0]+' ','')))
                                data = dinn.json()
                                chino.sendReplyImage(msg.id, to, data["image"])
                            elif cmd.startswith("graffiti "):
                                ano = requests.get("http://api.zicor.ooo/graffiti.php?text="+str(msg.text.replace(msg.text.split(' ')[0]+' ','')))
                                data = ano.json()
                                chino.sendReplyImage(msg.id, to, data["image"])
                            elif cmd.startswith("cookies "):
                                nee = requests.get("http://api.zicor.ooo/wcookies.php?text="+str(msg.text.replace(msg.text.split(' ')[0]+' ','')))
                                data = nee.json()
                                chino.sendReplyImage(msg.id, to, data["image"])
                            elif cmd.startswith("sletters "):
                                shh = requests.get("http://api.zicor.ooo/sletters.php?text="+str(msg.text.replace(msg.text.split(' ')[0]+' ','')))
                                data = shh.json()
                                chino.sendReplyImage(msg.id, to, data["image"])                            
                            elif cmd == "cinema":
                               result = requests.get("http://jadwalnonton.com/")
                               data = BeautifulSoup(result.content, 'html5lib')
                               hasil = "[ Cinema XX1 ]\nType : Movie List Today\n"
                               no = 1
                               for dzin in data.findAll('div', attrs={'class':'col-xs-6 moside'}):
                                   hasil += "\n\n{}. {}".format(str(no), str(dzin.find('h2').text))
                                   hasil += "\n     Link : {}".format(str(dzin.find('a')['href']))
                                   no = (no+1)
                               chino.sendReplyMessage(msg.id, to, str(hasil))
                            elif cmd.startswith("liburan "):
	                            sep = text.split(" ")
	                            search = text.replace(sep[0] + " ","")
	                            url = requests.get("https://rest.farzain.com/api/libur.php?name={}&apikey=CariApikeySndirihHu5Tv54tFWtrJy7Sh4zU4ANz".format(str(search)))
	                            data = url.text
	                            data = json.loads(data) #Ribetnya
	                            anu = data["result"]["result"]
	                            foto = data["result"]["image"]
	                            ret_ = "Hasil Liburan Kamu "
	                            ret_ += "Cocoknya Di : {}".format(anu)                            
	                            chino.sendReplyMessage(msg.id, to, str(ret_))
                            elif cmd.startswith("keahlian "):
	                            sep = text.split(" ")
	                            search = text.replace(sep[0] + " ","")
	                            url = requests.get("https://rest.farzain.com/api/ahli.php?name={}&apikey=CariApikeySndirihHu5Tv54tFWtrJy7Sh4zU4ANz".format(str(search)))
	                            data = url.text
	                            data = json.loads(data) #Ribetnya
	                            anu = data["result"]["result"]
	                            foto = data["result"]["image"]
	                            ret_ = "Kamu Cukup Ahli"
	                            ret_ += " Dalam : {}".format(anu)                            
	                            chino.sendReplyMessage(msg.id, to, str(ret_))
                            elif cmd.startswith("kemiripan "):
	                            sep = text.split(" ")
	                            search = text.replace(sep[0] + " ","")
	                            url = requests.get("https://rest.farzain.com/api/mirip.php?name={}&apikey=CariApikeySndirihHu5Tv54tFWtrJy7Sh4zU4ANz".format(str(search)))
	                            data = url.text
	                            data = json.loads(data)
	                            anu = data["result"]["result"]
	                            foto = data["result"]["image"]
	                            ret_ = "Kamu Mempunyai"
	                            ret_ += " Kemiripan Dengan : {}".format(anu)                            
	                            chino.sendReplyMessage(msg.id, to, str(ret_))
#PEMBATAS#                                    
                            elif cmd == "gift":
                                gf = "b07c07bc-fcc1-42e1-bd56-9b821a826f4f","7f2a5559-46ef-4f27-9940-66b1365950c4","53b25d10-51a6-4c4b-8539-38c242604143","a9ed993f-a4d8-429d-abc0-2692a319afde"
                                contact = chino.getContact(sender)
                                chino.sendGift(contact.mid, random.choice(gf), "theme")                                
                                sendMention(to, "Sudah dikirim ya kak @!,giftnya", [sender])                                                         
          
                            elif cmd.startswith("infomem "):
                            	if msg._from in Owner:
                                    separate = msg.text.split(" ")
                                    number = msg.text.replace(separate[0] + " ","")
                                    groups = chino.getGroupIdsJoined()
                                    ret_ = ""
                                    try:
                                        group = groups[int(number)-1]
                                        G = chino.getGroup(group)
                                        no = 0
                                        ret_ = ""
                                        for mem in G.members:
                                           no += 1
                                           ret_ += "\n " " "+ str(no) + ". " + mem.displayName
                                        chino.sendReplyMessage(msg.id, to," Group Name : [ " + str(G.name) + " ]\n\n   [ List Member ]\n" + ret_ + "\n\nTotal %i Members" % len(G.members))
                                    except: 
                                           pass                                                       
# Pembatas Script #
# Pembatas Script #
                        if text.lower() == "mykey":
                            chino.sendReplyMessage(msg.id, to, "KeyCommand Saat ini adalah [ {} ]".format(str(settings["keyCommand"])))
                            
                        elif text.lower() == "setkey on":
                            settings["setKey"] = True
                            chino.sendReplyMessage(msg.id, to, "Berhasil mengaktifkan setkey")
                            
                        elif text.lower() == "setkey off":
                            settings["setKey"] = False
                            chino.sendReplyMessage(msg.id, to, "Berhasil menonaktifkan setkey")                                               
# Pembatas Script #
                    elif msg.contentType == 1:
                        if settings["addPict"]["status"] == True:
                            with open('image.json','r') as fp:
                                images = json.load(fp)
                            images[settings["addPict"]["name"]] = chino.downloadObjectMsg(msg_id)
                            f = codecs.open('image.json','w','utf-8')
                            json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                            chino.sendReplyMessage(msg.id, to, "Images {} added to list".format(str(settings["addPict"]["name"])))
                            settings["addPict"]["status"] = False
                            settings["addPict"]["name"] = ""
                        
                    elif msg.contentType == 1:
                        if settings["changePictureProfile"] == True:
                            path = chino.downloadObjectMsg(msg_id)
                            settings["changePictureProfile"] = False
                            chino.updateProfilePicture(path)
                            chino.sendReplyMessage(msg.id, to, "Berhasil mengubah foto profile")
                        if msg.toType == 2:
                            if to in settings["changeGroupPicture"]:
                                path = chino.downloadObjectMsg(msg_id)
                                settings["changeGroupPicture"].remove(to)
                                chino.updateGroupPicture(to, path)
                                chino.sendReplyMessage(msg.id, to, "Berhasil mengubah foto group")

                    elif msg.contentType == 7:
                        if settings["checkSticker"] == True:
                            stk_id = msg.contentMetadata['STKID']
                            stk_ver = msg.contentMetadata['STKVER']
                            pkg_id = msg.contentMetadata['STKPKGID']
                            ret_ = "╭──[ Sticker Info ]"
                            ret_ += "\n│STICKER ID : {}".format(stk_id)
                            ret_ += "\n│STICKER PACKAGES ID : {}".format(pkg_id)
                            ret_ += "\n│STICKER VERSION : {}".format(stk_ver)
                            ret_ += "\n│STICKER URL : line://shop/detail/{}".format(pkg_id)
                            ret_ += "\n╰──[ Finish ]"
                            chino.sendReplyMessage(msg.id, to, str(ret_))
                            
                    elif msg.contentType == 13:
                        if settings["checkContact"] == True:
                            try:
                                contact = chino.getContact(msg.contentMetadata["mid"])
                                if chino != None:
                                    cover = chino.getProfileCoverURL(msg.contentMetadata["mid"])
                                else:
                                    cover = "Tidak dapat masuk di line channel"
                                path = "http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                                try:
                                    chino.sendImageWithURL(to, str(path))
                                except:
                                    pass
                                ret_ = "╭──[ Details Contact ]"
                                ret_ += "\n│Nama : {}".format(str(contact.displayName))
                                ret_ += "\n│MID : {}".format(str(msg.contentMetadata["mid"]))
                                ret_ += "\n│Bio : {}".format(str(contact.statusMessage))
                                ret_ += "\n│Gambar Profile : http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                                ret_ += "\n│Gambar Cover : {}".format(str(cover))
                                ret_ += "\n╰──[ Finish ]"
                                chino.sendReplyMessage(msg.id, to, str(ret_))
                            except:
                                chino.sendReplyMessage(msg.id, to, "Kontak tidak valid")
                                
                    elif msg.contentType == 16:
                        if settings["checkPost"] == True:
                            try:
                                ret_ = "╭──[ Details Post ]"
                                if msg.contentMetadata["serviceType"] == "GB":
                                    contact = chino.getContact(sender)
                                    auth = "\n│Penulis : {}".format(str(contact.displayName))
                                else:
                                    auth = "\n│Penulis : {}".format(str(msg.contentMetadata["serviceName"]))
                                purl = "\n│URL : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                                ret_ += auth
                                ret_ += purl
                                if "mediaOid" in msg.contentMetadata:
                                    object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                                    if msg.contentMetadata["mediaType"] == "V":
                                        if msg.contentMetadata["serviceType"] == "GB":
                                            ourl = "\n│Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                            murl = "\n│Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                        else:
                                            ourl = "\n│Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                            murl = "\n│Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                        ret_ += murl
                                    else:
                                        if msg.contentMetadata["serviceType"] == "GB":
                                            ourl = "\n│Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                        else:
                                            ourl = "\n│Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                    ret_ += ourl
                                if "stickerId" in msg.contentMetadata:
                                    stck = "\n│Stiker : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                                    ret_ += stck
                                if "text" in msg.contentMetadata:
                                    text = "\n│Tulisan : {}".format(str(msg.contentMetadata["text"]))
                                    ret_ += text
                                ret_ += "\n╰──[ Finish ]"
                                chino.sendReplyMessage(msg.id, to, str(ret_))
                            except:
                                chino.sendReplyMessage(msg.id, to, "Post tidak valid")
            except Exception as error:
                logError(error)
                traceback.print_tb(error.__traceback__)
                
        if op.type == 26 or op.type == 25:
            try:
                print ("[ 26 ] RECIEVE MESSAGE")
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from                
                if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                    if msg.toType == 0:
                        if sender != chino.profile.mid:
                            to = sender
                        else:
                            to = receiver
                    elif msg.toType == 1:
                        to = receiver
                    elif msg.toType == 2:
                        to = receiver
                    if settings["autoRead"] == True:
                        chino.sendChatChecked(to, msg_id)
                    if to in read["readPoint"]:
                        if sender not in read["ROM"][to]:
                            read["ROM"][to][sender] = True
                    if sender in settings["mimic"]["target"] and settings["mimic"]["status"] == True and settings["mimic"]["target"][sender] == True:
                        text = msg.text
                        if text is not None:
                            chino.sendMessage(msg.to,text)
                    if settings["unsendMessage"] == True:
                        try:
                            msg = op.message
                            if msg.toType == 0:
                                chino.log("[{} : {}]".format(str(msg._from), str(msg.text)))
                            else:
                                chino.log("[{} : {}]".format(str(msg.to), str(msg.text)))
                                msg_dict[msg.id] = {"text": msg.text, "from": msg._from, "createdTime": msg.createdTime, "contentType": msg.contentType, "contentMetadata": msg.contentMetadata}
                        except Exception as error:
                            logError(error)
                    if msg.contentType == 1:
                       if settings["unsendMessage"] == True:
                           try:
                              path = chino.downloadObjectMsg(msg_id, saveAs="chino.png")
                              msg_dict[msg.id] = {"from":msg._from,"image":path,"createdTime": msg.createdTime}
                              with open("Log_data.json", "w") as fp:
                                json.dump(msg_dict, fp, sort_keys=True, indent=4)
                           except Exception as e:
                             print (e)
                    if msg.contentType == 2:
                       if settings["unsendMessage"] == True:
                           try:
                              path = chino.downloadObjectMsg(msg_id, saveAs="rian.mp4")
                              msg_dict[msg.id] = {"from": msg._from,"video":path,"createdTime": msg.createdTime}
                              with open("Log_data.json", "w") as fp:
                                json.dump(msg_dict, fp, sort_keys=True, indent=4)
                           except Exception as e:
                               print (e)
                    if msg.contentType == 7:
                       if settings["unsendMessage"] == True:
                           try:
                              sticker = msg.contentMetadata["STKID"]
                              link = "http://dl.stickershop.line.naver.jp/stickershop/v1/sticker/{}/android/sticker.png".format(sticker)
                              msg_dict[msg.id] = {"from":msg._from,"sticker":link,"createdTime": msg.createdTime}
                              with open("Log_data.json", "w") as fp:
                                json.dump(msg_dict, fp, sort_keys=True, indent=4)
                           except Exception as e:
                             print (e)                          
                    if msg.contentType == 0:
                        if text is None:
                            return
                        if "/ti/g/" in msg.text.lower():
                            if settings["autoJoinTicket"] == True:
                                link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                links = link_re.findall(text)
                                n_links = []
                                for l in links:
                                    if l not in n_links:
                                        n_links.append(l)
                                for ticket_id in n_links:
                                    group = chino.findGroupByTicket(ticket_id)
                                    chino.acceptGroupInvitationByTicket(group.id,ticket_id)
                                    chino.sendReplyMessage(msg.id, to, "Berhasil masuk ke group %s" % str(group.name))
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if chinoMid in mention["M"]:
                                    if settings["autoRespon"] == True:
                                        sendMention(sender, "Oi Asw @!,jangan main tag tag", [sender])
                                    break
            except Exception as error:
                logError(error)
                traceback.print_tb(error.__traceback__)
                
        if op.type == 65:
            print ("[ 65 ] NOTIFIED DESTROY MESSAGE")
            if settings["unsendMessage"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                            contact = chino.getContact(msg_dict[msg_id]["from"])
                            if contact.displayNameOverridden != None:
                                name_ = contact.displayNameOverridden
                            else:
                              if "text" in msg_dict[msg_id]:
                                name_ = contact.displayName
                                ret_ = " Unsend Message "
                                ret_ += "\n\n Sender  : {} @!".format(str(contact.displayName),str(contact.mid))
                                ret_ += "\n\n Waktu  : {}".format(str(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"]))))
                                ret_ += "\n\n Type  : Text "
                                ret_ += "\n\n Text  : {}".format(str(msg_dict[msg_id]["text"]))
                                chino.sendMessage(at, str(ret_), {'AGENT_NAME': 'Unsend Message','AGENT_LINK': 'http://line.me/ti/p/~bacbac.id','AGENT_ICON': "http://dl.profile.line-cdn.net{}".format(str(contact.picturePath))})
                                chino.sendSticker(at, '1482011','17822843')
                                del msg_dict[msg_id]
                              else:
                                if "sticker" in msg_dict[msg_id]:
                                  name_ = contact.displayName
                                  ret_ = " Unsend Message "
                                  ret_ += "\n\n Sender  : {} ".format(str(contact.displayName))
                                  ret_ += "\n\n Waktu  : {}".format(str(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"]))))
                                  ret_ += "\n\n Link Sticker  : {} ".format(str(msg_dict[msg_id]["sticker"]))
                                  ret_ += "\n\n Type  : Sticker"
                                  chino.sendMessage(at, str(ret_), {'AGENT_NAME': 'Unsend Message','AGENT_LINK': 'http://line.me/ti/p/~bacbac.id','AGENT_ICON': "http://dl.profile.line-cdn.net{}".format(str(contact.picturePath))})
                                  chino.sendImageWithURL(at, msg_dict[msg_id]["sticker"])
                                  del msg_dict[msg_id]
                                else:
                                  if "image" in msg_dict[msg_id]:
                                    name_ = contact.displayName
                                    ret_ = " Unsend Message "
                                    ret_ += "\n\n Sender  : {} ".format(str(contact.displayName))
                                    ret_ += "\n\n Waktu : {}".format(str(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"]))))
                                    ret_ += "\n\n Link Image  : Not Found ."
                                    ret_ += "\n\n Type  : Image"
                                    chino.sendMessage(at, str(ret_), {'AGENT_NAME': 'Unsend Message','AGENT_LINK': 'http://line.me/ti/p/~bacbac.id','AGENT_ICON': "http://dl.profile.line-cdn.net{}".format(str(contact.picturePath))})
                                    chino.sendImage(at, "chino.png")
                                    del msg_dict[msg_id]
                                  else:
                                    if "video" in msg_dict[msg_id]:
                                      name_ = contact.displayName
                                      ret_ = " Unsend Message "
                                      ret_ += "\n\n Sender  : @!"
                                      ret_ += "\n\n Waktu : {}".format(str(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"]))))
                                      ret_ += "\n\n Link Video  : Not Found ."
                                      ret_ += "\n\n Type  : Video"
                                      sendMessage(at, str(ret_), [contact.mid])
                                      chino.sendVideo(at, "bagas.mp4")
                                      del msg_dict[msg_id]
                        else:
                            chino.sendMessage(at,"SentMessage .cancelled,But I didn't have log data.\nSorry > <")
                except Exception as error:
                    logError(error)
                    traceback.print_tb(error.__traceback__)
                
        if op.type == 55:
            print ("[ 55 ] NOTIFIED READ MESSAGE")
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                else:
                   pass
            except Exception as error:
                logError(error)
                traceback.print_tb(error.__traceback__)
    except Exception as error:
        logError(error)
        traceback.print_tb(error.__traceback__)

while True:
    try:
        delete_log()
        delExpire()
        ops = chinoPoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                chinoBot(op)
                chinoPoll.setRevision(op.revision)
    except Exception as error:
        logError(error)
        
def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")
atexit.register(atend)
