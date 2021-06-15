import telebot
import time
import random
import os
import glob
import requests
import sys
import json
import os.path
from telebot import types
bot = telebot.TeleBot("<TOKEN>")
#Netflix
Netflixmovielanguage = ['Yoruba', 'Yiddish', 'Wolof', 'Vietnamese', 'Urdu', 'Turkish', 'Thai', 'Telugu', 'Tamil', 'Tagalog', 'Swedish', 'Spanish', 'Russian', 'Romanian', 'Punjabi', 'Portuguese', 'Polish', 'Norwegian', 'Marathi', 'Mandarin', 'Malayalam', 'Malay', 'Korean', 'Khmer', 'Kannada', 'Japanese', 'Italian', 'Indonesian', 'Hindi', 'Hebrew', 'Gujarati', 'German', 'French', 'Flemish', 'Filipino', 'English', 'Dutch', 'Danish', 'Chinese', 'Catalan', 'Cantonese', 'BrazilianPortuguese', 'Bengali', 'Bangla', 'Arabic', 'Afrikaans']
Netflixmovieyear = ['2021', '2020', '2019', '2018', '2017', '2016', '2015', '2014', '2013', '2012', '2011', '2010', '2009', '2008', '2007', '2006', '2005', '2004', '2003', '2002', '2001', '2000', '1999', '1998', '1997', '1996', '1995', '1994', '1993', '1992', '1991', '1990', '1989', '1988', '1987', '1986', '1985', '1984', '1983', '1982', '1981', '1980', '1979', '1978', '1977', '1976', '1975', '1974', '1973', '1971', '1969', '1967', '1964', '1960', '1958', '1956', '1954']
Netflixmovierating = ['8', '7', '6', '5', '4', '3', '2', '1', '0']
Netflixtvshowlanguage =['Urdu', 'Turkish', 'Thai', 'Telugu', 'Tamil', 'Taiwanese', 'Swedish', 'Spanish', 'Simplified Chinese', 'Russian', 'Portuguese', 'Polish', 'Norwegian', 'Mandarin', 'Malayalam', 'Malay', 'Luxembourgish', 'Korean', 'Japanese', 'Italian', 'Indonesian', 'Icelandic', 'Hindi', 'Hebrew', 'German', 'Galician', 'French', 'Flemish', 'Finnish', 'Filipino', 'English', 'Dutch', 'Danish', 'Croatian', 'Chinese', 'Catalan', 'Cantonese', 'Brazilian Portuguese', 'Arabic']
Netflixtvshowrating = ['9', '8', '7', '6', '5', '4', '3', '2', '1', '0']
#Amazonprime
Amazonprimemovielanguage = ['Yoruba', 'Urdu', 'Unknown', 'Turkish', 'Tibetan', 'Thai', 'Telugu', 'Tamil', 'Tagalog', 'Spanish', 'Sindhi', 'Serbo-Croatian', 'Sanskrit', 'Russian', 'Romanian', 'Rajasthani', 'Quechua', 'Punjabi', 'Portuguese', 'Persian', 'Oriya', 'Norwegian', 'Navajo', 'Mongolian', 'Marathi', 'Mandarin', 'Malayalam', 'Latin', 'Ladino', 'Korean', 'Kannada', 'Japanese', 'Italian', 'Inuktitut', 'Hungarian', 'Hindi', 'Hebrew', 'Gujarati', 'Greek', 'German', 'Gaelic', 'French', 'Filipino', 'English', 'Dutch', 'Dari', 'Czech', 'Croatian', 'Chinese', 'Cantonese', 'Bulgarian', 'Bhojpuri', 'Bengali', 'Assamese', 'Armenian', 'Arabic', 'Albanian', 'Aboriginal']
Amazonprimemovieyear = ['2021', '2020', '2019', '2018', '2017', '2016', '2015', '2014', '2013', '2012', '2011', '2010', '2009', '2008', '2007', '2006', '2005', '2004', '2003', '2002', '2001', '2000', '1999', '1998', '1997', '1996', '1995', '1994', '1993', '1992', '1991', '1990', '1989', '1988', '1987', '1986', '1985', '1984', '1983', '1982', '1981', '1980', '1979', '1978', '1977', '1976', '1975', '1974', '1973', '1972', '1971', '1970', '1969', '1968', '1967', '1966', '1965', '1964', '1963', '1962', '1961', '1960', '1959', '1958', '1957', '1956', '1955', '1954', '1953', '1952', '1951']
Amazonprimemovierating = ['8', '7', '6', '5', '4', '3', '2', '1']
Amazonprimetvshowlanguage = ['Yiddish', 'Wolof', 'Welsh', 'Vietnamese', 'Unknown', 'Ukrainian', 'Turkish', 'Telugu', 'Tamil', 'Tagalog', 'Swedish', 'Swahili', 'Spanish', 'Slovak', 'Samoan', 'Russian', 'Romanian', 'Pushto', 'Portuguese', 'Polish', 'Persian', 'Mandarin', 'Lingala', 'Latvian', 'Latin', 'Korean', 'Klingon', 'Japanese', 'Italian', 'Hungarian', 'Hindi', 'Hebrew', 'Greek', 'German', 'Gallegan', 'French', 'Filipino', 'English', 'Dutch', 'Danish', 'Czech', 'Chinese', 'Chechen', 'Catalan', 'Bulgarian', 'Aramaic', 'Arabic', 'AmericanSign', 'Albanian']
Amazonprimetvshowyear = ['2021', '2020', '2019', '2018', '2017', '2016', '2015', '2014', '2013', '2012', '2011', '2010', '2009', '2008', '2007', '2006', '2005', '2004', '2003', '2002', '2000', '1999', '1998', '1997', '1996', '1995', '1994', '1992', '1991', '1990', '1989', '1988', '1987', '1986', '1985', '1984', '1983', '1982', '1981', '1980', '1978', '1960', '1959', '1958', '1957']
Amazonprimetvshowrating =['9', '8', '7', '6', '5', '4', '3', '2']
#Hotstar
Hotstarmovielanguage = ['Zulu', 'Yiddish', 'Xhosa', 'Vietnamese', 'Urdu', 'Unknown', 'Ukrainian', 'Turkish', 'Tulu', 'Thai', 'Telugu', 'Tamil', 'Tagalog', 'Swedish', 'Swahili', 'Spanish', 'Sioux', 'Sindhi', 'Sindarin', 'Sign', 'Serbo-Croatian', 'Serbian', 'Sanskrit', 'Russian', 'Romanian', 'Rajasthani', 'Quenya', 'Punjabi', 'Portuguese', 'Polish', 'Persian', 'Pashtu', 'Oriya', 'Norwegian', 'NorthAmericanIndian', 'None', 'Nepali', 'Nama', 'Mongolian', 'MinNan', 'Marathi', 'Mandarin', 'Malayalam', 'Malay', 'Latin', 'Kurdish', 'Korean', 'Konkani', 'Kashmiri', 'Kannada', 'Japanese', 'Italian', 'Inuktitut', 'Indonesian', 'IndianSignLanguage', 'Icelandic', 'Hungarian', 'Hindi', 'Hebrew', 'Hawaiian', 'Haryanvi', 'Gujarati', 'Greek', 'German', 'French', 'Flemish', 'Finnish', 'English', 'Egyptian(Ancient)', 'Dzongkha', 'Dutch', 'Dari', 'Danish', 'Czech', 'Chinese', 'CentralKhmer', 'Cantonese', 'Bulgarian', 'BrazilianSignLanguage', 'Bengali', 'Assamese', 'Armenian', 'Arabic', 'AmericanSign', 'Algonquin']
Hotstarmovieyear = ['2021', '2020', '2019', '2018', '2017', '2016', '2015', '2014', '2013', '2012', '2011', '2010', '2009', '2008', '2007', '2006', '2005', '2004', '2003', '2002', '2001', '2000', '1999', '1998', '1997', '1996', '1995', '1994', '1993', '1992', '1991', '1990', '1989', '1988', '1987', '1986', '1985', '1984', '1983', '1982', '1981', '1980', '1979', '1978', '1977', '1976', '1975', '1974', '1973', '1972', '1971', '1970', '1969', '1968', '1967', '1966', '1965', '1964', '1963', '1961', '1959', '1957', '1955', '1953', '1947', '1942', '1941', '1940', '1938', '1928']
Hotstarmovierating = ['9', '8', '7', '6', '5', '4', '3', '2', '1']
Hotstartvshowlanguage = ['Yiddish', 'Vietnamese', 'Unknown', 'Ukrainian', 'Turkish', 'Tibetan', 'Thai', 'Telugu', 'Tamil', 'Swedish', 'Swahili', 'Spanish', 'Serbian', 'Russian', 'Portuguese', 'Polish', 'Persian', 'Norwegian', 'Nepali', 'Mongolian', 'Marathi', 'Mandarin', 'Malayalam', 'Lithuanian', 'Latvian', 'Latin', 'Korean', 'Klingon', 'Kazakh', 'Kannada', 'Japanese', 'Italian', 'Irish', 'Indonesian', 'IndianSign', 'Icelandic', 'Hindi', 'Hebrew', 'Greek', 'German', 'French', 'Finnish', 'English', 'Dutch', 'Danish', 'Czech', 'Chinese', 'Cantonese', 'Bengali', 'Aramaic', 'Arabic', 'Albanian', 'Afrikaans']
Hotstartvshowyear = ['2021', '2020', '2019', '2018', '2017', '2016', '2015', '2014', '2013', '2012', '2011', '2010', '2009', '2008', '2007', '2006', '2005', '2004', '2003', '2002', '2001', '2000', '1999', '1998', '1997', '1996', '1995', '1994', '1993', '1992', '1991', '1990', '1989', '1988', '1986', '1985', '1980', '1979', '1973', '1970', '1964', '1961', '1953', '1948']
Hotstartvshowrating =['9', '8', '7', '6', '5', '4', '3', '2', '1']
def save(S):
    file = open('usernames.txt', 'a')
    file.write(str(S)+'\n')
    file.close()
def chatsave(chat_id,msg):
    file = open(str(chat_id)+'.txt', 'w')
    file.write(str(msg))
    file.close()
def see(chat_id):
    with open(str(chat_id)+'.txt') as f:
        firstline = f.readlines()[0].rstrip()
    f.close()
    return(str(firstline))
def randgeneration(A):
    CAPTCHA_IMAGE_FOLDER = A
# Get a list of all the captcha images we need to process
    captcha_image_files = glob.glob(os.path.join(CAPTCHA_IMAGE_FOLDER, "*"))
    r = random.randint(0,len(os.listdir(A))-1)
    image = ''
    #r =random.randint(0,len(captcha_image_files)-1)
    for (i, captcha_image_file) in enumerate(captcha_image_files):
        if i == r :
            image = captcha_image_file
    return(image)
def newrand(A,B,L,R):
    S=[]
    folder = '/home/srijithreddy/Desktop/Srijith reddy/Movies/'+str(A)+'/'+str(B)+'/language/'+str(L)+'/'
    captcha_image_files = glob.glob(os.path.join(folder, "*"))
    for (i, captcha_image_file) in enumerate(captcha_image_files):
        filename = os.path.basename(captcha_image_file)
        if filename[filename.index('⭐')+1:len(filename)] in ['Non','one']:
            rat = '6.5'
            if float(rat)>=float(R):
                S+= [captcha_image_file]
        else :
            rat = filename[filename.index('⭐')+1:len(filename)]
            if float(rat)>=float(R):
                S+= [captcha_image_file]
    if len(S) == 0:
        re = 'No such file'
    else :
        re = S[random.randint(0,len(S)-1)]
    return(re)
def newrand2(A,B,L,R):
    S=[]
    folder = '/home/srijithreddy/Desktop/Srijith reddy/Movies/'+str(A)+'/'+str(B)+'/language/'+str(L)+'/'
    captcha_image_files = glob.glob(os.path.join(folder, "*"))
    for (i, captcha_image_file) in enumerate(captcha_image_files):
        filename = os.path.basename(captcha_image_file)
        if filename[filename.index('⭐')+1:len(filename)] in ['Non','one']:
            rat = '6.5'
            if float(rat)>=float(R):
                S+= [captcha_image_file]
        else :
            rat = filename[filename.index('⭐')+1:len(filename)]
            if float(rat)>=float(R):
                S+= [captcha_image_file]
    if len(S) == 0:
        re = ['No such file']
    else :
        re = S
    return(re)
def generatestring1(A):
    stm = ""
    for i in A:
        stm+=  "Send "+str(i)+"  for "+i+ " language"+"\n"
    return(stm)
def generatestring2(A):
    stm = ""
    for i in A:
        stm+=  "Send "+str(i)+"  for "+i+ " year"+"\n"
    return(stm)
def generatestring3(A):
    stm = ""
    for i in A:
        stm+=  "Send "+str(i)+"  for  rating greater than "+i+"\n"
    return(stm)
def language(A,B):
    response = requests.get('http://www.omdbapi.com/?apikey=a2d1da4c&t='+str(A)+'&y='+str(B)).text
    response_info = json.loads(response)
    if response_info["Response"] == "True" and response_info["imdbRating"] != "N/A":
        tex = response_info["imdbRating"]
    elif response_info["Response"] == "False":
        tex = 'None'
    elif response_info["Response"] == "True" and response_info["imdbRating"] == "N/A":
        tex = 'None'
    return(tex)
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    name = message.from_user.first_name
    save(name)
    bot.send_chat_action(message.chat.id, 'typing')
    bot.send_message(message.chat.id, " 🙋‍♂️ Hi  " + str(name)+"\nChoose streaming platform and type:\n/Netflixmovie 🔴  \n/Netflixtvshow 🔴  \n /Amazonprimemovie 🔵 \n/Amazonprimetvshow 🔵 \n/Hotstarmovie 🟢  \n/Hotstartvshow 🟢  \n/Ahamovie 🟠 \n/Ahatvshow 🟠 \n/Multiplefilters  - For filters like rating and language and streaming platform at a time. \n\n/howtouse\n",reply_markup=None)

@bot.message_handler(commands=['Netflixmovie', 'Netflixtvshow','Amazonprimemovie','Amazonprimetvshow','Hotstarmovie','Hotstartvshow'])
def info_options(message):
    name = message.from_user.first_name
    save(name)
    bot.send_chat_action(message.chat.id, 'typing')
    markup2 = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('')
    itembtn2 = types.KeyboardButton('hello')
    markup2.add(itembtn1, itembtn2)
    bot.send_message(message.chat.id, "Choose by :\n/"+str(message.text[1:len(message.text)])+"language  - To suggest movie by Language \n/"+str(message.text[1:len(message.text)])+"year  - To suggest movie by Year \n/"+str(message.text[1:len(message.text)])+"rating  - To suggest movie by IMDB Rating   \n",reply_markup=None)
#tb.send_message(chat_id, "Choose one letter:", reply_markup=markup)
#Netflix


@bot.message_handler(commands=['Netflixmovielanguage'])
def Netflix_movie_lang(message):
    chatsave(message.chat.id,message.text[1:])
    name = message.from_user.first_name
    save(name)
    markup3= types.ReplyKeyboardMarkup(row_width=4)
    item = [None] * len(Netflixmovielanguage)
    for i in range(len(Netflixmovielanguage)):
        item[i]= types.KeyboardButton(Netflixmovielanguage[i])
    markup3.add(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8], item[9], item[10], item[11], item[12], item[13], item[14], item[15], item[16], item[17], item[18], item[19], item[20], item[21], item[22], item[23], item[24], item[25], item[26], item[27], item[28], item[29], item[30], item[31], item[32], item[33], item[34], item[35], item[36], item[37], item[38], item[39], item[40], item[41], item[42], item[43], item[44], item[45])
    bot.send_chat_action(message.chat.id, 'typing')
    S = generatestring1(Netflixmovielanguage)
    bot.send_message(message.chat.id, "Choose Language: \n"+S,reply_markup=markup3)

@bot.message_handler(func=lambda message: message.text in Netflixmovielanguage and (see(message.chat.id) == 'Netflixmovielanguage'))
def Netflix_movie_lang(message):
    name = message.from_user.first_name
    save(name)
    bot.send_chat_action(message.chat.id, 'typing')
    msg = message.text
    ph =randgeneration('/home/srijithreddy/Desktop/Srijith reddy/Movies/Netflix/movies/language/'+msg[0:len(msg)]+'/')
    #ph = '/home/srijithreddy/Desktop/Srijith reddy/Movies/Netflix/movies/language/English/As Above, So Below✔️English🧁2014⭐6.2'
    photo = open(ph, 'rb')
    bot.send_photo(message.chat.id, photo)
    filename = os.path.basename(ph)
    if filename[filename.index('⭐')+1:] in ['Non','one']:
        rate = language(filename[0:filename.index('✔️')],filename[filename.index('🧁')+1:filename.index('⭐')])
        bot.send_message(message.chat.id, filename[0:filename.index('⭐')+1]+rate)
    else:
        bot.send_message(message.chat.id, filename)

#Netflixmovieyear
@bot.message_handler(commands=['Netflixmovieyear'])
def Netflix_movie_year(message):
    chatsave(message.chat.id,message.text[1:])
    name = message.from_user.first_name
    save(name)
    markup3= types.ReplyKeyboardMarkup(row_width=4)
    item = [None] * len(Netflixmovieyear)
    for i in range(len(Netflixmovieyear)):
        item[i]= types.KeyboardButton(Netflixmovieyear[i])
    markup3.add(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8], item[9], item[10], item[11], item[12], item[13], item[14], item[15], item[16], item[17], item[18], item[19], item[20], item[21], item[22], item[23], item[24], item[25], item[26], item[27], item[28], item[29], item[30], item[31], item[32], item[33], item[34], item[35], item[36], item[37], item[38], item[39], item[40], item[41], item[42], item[43], item[44], item[45], item[46], item[47], item[48], item[49], item[50], item[51], item[52], item[53], item[54], item[55], item[56])
    bot.send_chat_action(message.chat.id, 'typing')
    S = generatestring2(Netflixmovieyear)
    bot.send_message(message.chat.id, "Choose Language: \n"+S,reply_markup=markup3)

@bot.message_handler(func=lambda message: message.text in Netflixmovieyear and (see(message.chat.id) == 'Netflixmovieyear'))
def Netflix_movie_year(message):
    name = message.from_user.first_name
    save(name)
    bot.send_chat_action(message.chat.id, 'typing')
    msg = message.text
    ph =randgeneration('/home/srijithreddy/Desktop/Srijith reddy/Movies/Netflix/movies/year/'+msg[0:len(msg)]+'/')
    #ph = '/home/srijithreddy/Desktop/Srijith reddy/Movies/Netflix/movies/language/English/As Above, So Below✔️English🧁2014⭐6.2'
    photo = open(ph, 'rb')
    bot.send_photo(message.chat.id, photo)
    filename = os.path.basename(ph)
    if filename[filename.index('⭐')+1:] in ['Non','one']:
        rate = language(filename[0:filename.index('✔️')],filename[filename.index('🧁')+1:filename.index('⭐')])
        bot.send_message(message.chat.id, filename[0:filename.index('⭐')+1]+rate)
    else:
        bot.send_message(message.chat.id, filename)
 #Netflixmovierating
@bot.message_handler(commands=['Netflixmovierating'])
def Netflix_movie_rat(message):
    chatsave(message.chat.id,message.text[1:])
    name = message.from_user.first_name
    save(name)
    markup3= types.ReplyKeyboardMarkup(row_width=4)
    item = [None] * len(Netflixmovierating)
    for i in range(len(Netflixmovierating)):
        item[i]= types.KeyboardButton(Netflixmovierating[i])
    markup3.add(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8])
    bot.send_chat_action(message.chat.id, 'typing')
    S = generatestring3(Netflixmovierating)
    bot.send_message(message.chat.id, "Choose Language: \n"+S,reply_markup=markup3)

@bot.message_handler(func=lambda message: message.text in Netflixmovierating and (see(message.chat.id) == 'Netflixmovierating'))
def Netflix_movie_rat(message):
    name = message.from_user.first_name
    save(name)
    bot.send_chat_action(message.chat.id, 'typing')
    msg = message.text
    ph =randgeneration('/home/srijithreddy/Desktop/Srijith reddy/Movies/Netflix/movies/rating/'+msg[0:len(msg)]+'/')
    #ph = '/home/srijithreddy/Desktop/Srijith reddy/Movies/Netflix/movies/language/English/As Above, So Below✔️English🧁2014⭐6.2'
    photo = open(ph, 'rb')
    bot.send_photo(message.chat.id, photo)
    filename = os.path.basename(ph)
    if filename[filename.index('⭐')+1:] in ['Non','one']:
        rate = language(filename[0:filename.index('✔️')],filename[filename.index('🧁')+1:filename.index('⭐')])
        bot.send_message(message.chat.id, filename[0:filename.index('⭐')+1]+rate)
    else:
        bot.send_message(message.chat.id, filename)

#Netflix
@bot.message_handler(commands=['Netflixtvshowlanguage'])
def Netflix_tvshow_lang(message):
    chatsave(message.chat.id,message.text[1:])
    name = message.from_user.first_name
    save(name)
    markup3= types.ReplyKeyboardMarkup(row_width=4)
    item = [None] * len(Netflixtvshowlanguage)
    for i in range(len(Netflixtvshowlanguage)):
        item[i]= types.KeyboardButton(Netflixtvshowlanguage[i])
    markup3.add(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8], item[9], item[10], item[11], item[12], item[13], item[14], item[15], item[16], item[17], item[18], item[19], item[20], item[21], item[22], item[23], item[24], item[25], item[26], item[27], item[28], item[29], item[30], item[31], item[32], item[33], item[34], item[35], item[36], item[37], item[38])
    bot.send_chat_action(message.chat.id, 'typing')
    S = generatestring1(Netflixtvshowlanguage)
    bot.send_message(message.chat.id, "Choose Language: \n"+S,reply_markup=markup3)

@bot.message_handler(func=lambda message: message.text in Netflixtvshowlanguage and (see(message.chat.id) == 'Netflixtvshowlanguage'))
def Netflix_tvshow_lang(message):
    name = message.from_user.first_name
    save(name)
    bot.send_chat_action(message.chat.id, 'typing')
    msg = message.text
    ph =randgeneration('/home/srijithreddy/Desktop/Srijith reddy/Movies/Netflix/tvshows/language/'+msg[0:len(msg)]+'/')
    #ph = '/home/srijithreddy/Desktop/Srijith reddy/Movies/Netflix/tvshows/language/English/As Above, So Below✔️English🧁2014⭐6.2'
    photo = open(ph, 'rb')
    bot.send_photo(message.chat.id, photo)
    filename = os.path.basename(ph)
    if filename[filename.index('⭐')+1:] in ['Non','one']:
        rate = language(filename[0:filename.index('✔️')],filename[filename.index('🧁')+1:filename.index('⭐')])
        bot.send_message(message.chat.id, filename[0:filename.index('⭐')+1]+rate)
    else:
        bot.send_message(message.chat.id, filename)

#Netflixtvshowyear
@bot.message_handler(commands=['Netflixtvshowyear'])
def Netflix_tvshow_year(message):
    name = message.from_user.first_name
    save(name)
    bot.send_message(message.chat.id, "Not available by year",reply_markup=None)

@bot.message_handler(commands=['Netflixtvshowrating'])
def Netflix_tvshow_rat(message):
    chatsave(message.chat.id,message.text[1:])
    name = message.from_user.first_name
    save(name)
    markup3= types.ReplyKeyboardMarkup(row_width=4)
    item = [None] * len(Netflixtvshowrating)
    for i in range(len(Netflixtvshowrating)):
        item[i]= types.KeyboardButton(Netflixtvshowrating[i])
    markup3.add(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8], item[9])
    bot.send_chat_action(message.chat.id, 'typing')
    S = generatestring3(Netflixtvshowrating)
    bot.send_message(message.chat.id, "Choose Language: \n"+S,reply_markup=markup3)

@bot.message_handler(func=lambda message: message.text in Netflixtvshowrating and (see(message.chat.id) == 'Netflixtvshowrating'))
def Netflix_tvshow_rat(message):
    name = message.from_user.first_name
    save(name)
    bot.send_chat_action(message.chat.id, 'typing')
    msg = message.text
    ph =randgeneration('/home/srijithreddy/Desktop/Srijith reddy/Movies/Netflix/tvshows/rating/'+msg[0:len(msg)]+'/')
    #ph = '/home/srijithreddy/Desktop/Srijith reddy/Movies/Netflix/tvshows/language/English/As Above, So Below✔️English🧁2014⭐6.2'
    photo = open(ph, 'rb')
    bot.send_photo(message.chat.id, photo)
    filename  = os.path.basename(ph)
    if filename[filename.index('⭐')+1:] in ['Non','one']:
        rate = language(filename[0:filename.index('✔️')],filename[filename.index('🧁')+1:filename.index('⭐')])
        bot.send_message(message.chat.id, filename[0:filename.index('⭐')+1]+rate)
    else:
        bot.send_message(message.chat.id, filename)
#Amazonprime
@bot.message_handler(commands=['Amazonprimemovielanguage'])
def Amazonprime_movie_lang(message):
    chatsave(message.chat.id,message.text[1:])
    name = message.from_user.first_name
    save(name)
    markup3= types.ReplyKeyboardMarkup(row_width=4)
    item = [None] * len(Amazonprimemovielanguage)
    for i in range(len(Amazonprimemovielanguage)):
        item[i]= types.KeyboardButton(Amazonprimemovielanguage[i])
    markup3.add(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8], item[9], item[10], item[11], item[12], item[13], item[14], item[15], item[16], item[17], item[18], item[19], item[20], item[21], item[22], item[23], item[24], item[25], item[26], item[27], item[28], item[29], item[30], item[31], item[32], item[33], item[34], item[35], item[36], item[37], item[38], item[39], item[40], item[41], item[42], item[43], item[44], item[45], item[46], item[47], item[48], item[49], item[50], item[51], item[52], item[53], item[54], item[55], item[56], item[57])
    bot.send_chat_action(message.chat.id, 'typing')
    S = generatestring1(Amazonprimemovielanguage)
    bot.send_message(message.chat.id, "Choose Language: \n"+S,reply_markup=markup3)

@bot.message_handler(func=lambda message: message.text in Amazonprimemovielanguage and (see(message.chat.id) == 'Amazonprimemovielanguage'))
def Amazonprime_movie_lang(message):
    name = message.from_user.first_name
    save(name)
    bot.send_chat_action(message.chat.id, 'typing')
    msg = message.text
    ph =randgeneration('/home/srijithreddy/Desktop/Srijith reddy/Movies/Amazonprime/movies/language/'+msg[0:len(msg)]+'/')
    #ph = '/home/srijithreddy/Desktop/Srijith reddy/Movies/Amazonprime/movies/language/English/As Above, So Below✔️English🧁2014⭐6.2'
    photo = open(ph, 'rb')
    bot.send_photo(message.chat.id, photo)
    filename = os.path.basename(ph)
    if filename[filename.index('⭐')+1:] in ['Non','one']:
        rate = language(filename[0:filename.index('✔️')],filename[filename.index('🧁')+1:filename.index('⭐')])
        bot.send_message(message.chat.id, filename[0:filename.index('⭐')+1]+rate)
    else:
        bot.send_message(message.chat.id, filename)
#Amazonprimemovieyear
@bot.message_handler(commands=['Amazonprimemovieyear'])
def Amazonprime_movie_year(message):
    chatsave(message.chat.id,message.text[1:])
    name = message.from_user.first_name
    save(name)
    markup3= types.ReplyKeyboardMarkup(row_width=4)
    item = [None] * len(Amazonprimemovieyear)
    for i in range(len(Amazonprimemovieyear)):
        item[i]= types.KeyboardButton(Amazonprimemovieyear[i])
    markup3.add(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8], item[9], item[10], item[11], item[12], item[13], item[14], item[15], item[16], item[17], item[18], item[19], item[20], item[21], item[22], item[23], item[24], item[25], item[26], item[27], item[28], item[29], item[30], item[31], item[32], item[33], item[34], item[35], item[36], item[37], item[38], item[39], item[40], item[41], item[42], item[43], item[44], item[45], item[46], item[47], item[48], item[49], item[50], item[51], item[52], item[53], item[54], item[55], item[56], item[57], item[58], item[59], item[60], item[61], item[62], item[63], item[64], item[65], item[66], item[67], item[68], item[69], item[70])
    bot.send_chat_action(message.chat.id, 'typing')
    S = generatestring2(Amazonprimemovieyear)
    bot.send_message(message.chat.id, "Choose Language: \n"+S,reply_markup=markup3)

@bot.message_handler(func=lambda message: message.text in Amazonprimemovieyear and (see(message.chat.id) == 'Amazonprimemovieyear'))
def Amazonprime_movie_year(message):
    name = message.from_user.first_name
    save(name)
    bot.send_chat_action(message.chat.id, 'typing')
    msg = message.text
    ph =randgeneration('/home/srijithreddy/Desktop/Srijith reddy/Movies/Amazonprime/movies/year/'+msg[0:len(msg)]+'/')
    #ph = '/home/srijithreddy/Desktop/Srijith reddy/Movies/Amazonprime/movies/language/English/As Above, So Below✔️English🧁2014⭐6.2'
    photo = open(ph, 'rb')
    bot.send_photo(message.chat.id, photo)
    filename = os.path.basename(ph)
    if filename[filename.index('⭐')+1:] in ['Non','one']:
        rate = language(filename[0:filename.index('✔️')],filename[filename.index('🧁')+1:filename.index('⭐')])
        bot.send_message(message.chat.id, filename[0:filename.index('⭐')+1]+rate)
    else:
        bot.send_message(message.chat.id, filename)
 #Amazonprimemovierating
@bot.message_handler(commands=['Amazonprimemovierating'])
def Amazonprime_movie_rat(message):
    chatsave(message.chat.id,message.text[1:])
    name = message.from_user.first_name
    save(name)
    markup3= types.ReplyKeyboardMarkup(row_width=4)
    item = [None] * len(Amazonprimemovierating)
    for i in range(len(Amazonprimemovierating)):
        item[i]= types.KeyboardButton(Amazonprimemovierating[i])
    markup3.add(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7])
    bot.send_chat_action(message.chat.id, 'typing')
    S = generatestring3(Amazonprimemovierating)
    bot.send_message(message.chat.id, "Choose Language: \n"+S,reply_markup=markup3)

@bot.message_handler(func=lambda message: message.text in Amazonprimemovierating and (see(message.chat.id) == 'Amazonprimemovierating'))
def Amazonprime_movie_rat(message):
    name = message.from_user.first_name
    save(name)
    bot.send_chat_action(message.chat.id, 'typing')
    msg = message.text
    ph =randgeneration('/home/srijithreddy/Desktop/Srijith reddy/Movies/Amazonprime/movies/rating/'+msg[0:len(msg)]+'/')
    #ph = '/home/srijithreddy/Desktop/Srijith reddy/Movies/Amazonprime/movies/language/English/As Above, So Below✔️English🧁2014⭐6.2'
    photo = open(ph, 'rb')
    bot.send_photo(message.chat.id, photo)
    filename = os.path.basename(ph)
    if filename[filename.index('⭐')+1:] in ['Non','one']:
        rate = language(filename[0:filename.index('✔️')],filename[filename.index('🧁')+1:filename.index('⭐')])
        bot.send_message(message.chat.id, filename[0:filename.index('⭐')+1]+rate)
    else:
        bot.send_message(message.chat.id, filename)
#Amazonprime
@bot.message_handler(commands=['Amazonprimetvshowlanguage'])
def Amazonprime_tvshow_lang(message):
    chatsave(message.chat.id,message.text[1:])
    name = message.from_user.first_name
    save(name)
    markup3= types.ReplyKeyboardMarkup(row_width=4)
    item = [None] * len(Amazonprimetvshowlanguage)
    for i in range(len(Amazonprimetvshowlanguage)):
        item[i]= types.KeyboardButton(Amazonprimetvshowlanguage[i])
    markup3.add(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8], item[9], item[10], item[11], item[12], item[13], item[14], item[15], item[16], item[17], item[18], item[19], item[20], item[21], item[22], item[23], item[24], item[25], item[26], item[27], item[28], item[29], item[30], item[31], item[32], item[33], item[34], item[35], item[36], item[37], item[38], item[39], item[40], item[41], item[42], item[43], item[44], item[45], item[46], item[47], item[48])
    bot.send_chat_action(message.chat.id, 'typing')
    S = generatestring1(Amazonprimetvshowlanguage)
    bot.send_message(message.chat.id, "Choose Language: \n"+S,reply_markup=markup3)

@bot.message_handler(func=lambda message: message.text in Amazonprimetvshowlanguage and (see(message.chat.id) == 'Amazonprimetvshowlanguage'))
def Amazonprime_tvshow_lang(message):
    name = message.from_user.first_name
    save(name)
    bot.send_chat_action(message.chat.id, 'typing')
    msg = message.text
    ph =randgeneration('/home/srijithreddy/Desktop/Srijith reddy/Movies/Amazonprime/tvshows/language/'+msg[0:len(msg)]+'/')
    #ph = '/home/srijithreddy/Desktop/Srijith reddy/Movies/Amazonprime/tvshows/language/English/As Above, So Below✔️English🧁2014⭐6.2'
    photo = open(ph, 'rb')
    bot.send_photo(message.chat.id, photo)
    filename = os.path.basename(ph)
    if filename[filename.index('⭐')+1:] in ['Non','one']:
        rate = language(filename[0:filename.index('✔️')],filename[filename.index('🧁')+1:filename.index('⭐')])
        bot.send_message(message.chat.id, filename[0:filename.index('⭐')+1]+rate)
    else:
        bot.send_message(message.chat.id, filename)


#Amazonprimetvshowyear
@bot.message_handler(commands=['Amazonprimetvshowyear'])
def Amazonprime_tvshow_year(message):
    chatsave(message.chat.id,message.text[1:])
    name = message.from_user.first_name
    save(name)
    markup3= types.ReplyKeyboardMarkup(row_width=4)
    item = [None] * len(Amazonprimetvshowyear)
    for i in range(len(Amazonprimetvshowyear)):
        item[i]= types.KeyboardButton(Amazonprimetvshowyear[i])
    markup3.add(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8], item[9], item[10], item[11], item[12], item[13], item[14], item[15], item[16], item[17], item[18], item[19], item[20], item[21], item[22], item[23], item[24], item[25], item[26], item[27], item[28], item[29], item[30], item[31], item[32], item[33], item[34], item[35], item[36], item[37], item[38], item[39], item[40], item[41], item[42], item[43], item[44])
    bot.send_chat_action(message.chat.id, 'typing')
    S = generatestring2(Amazonprimetvshowyear)
    bot.send_message(message.chat.id, "Choose Language: \n"+S,reply_markup=markup3)

@bot.message_handler(func=lambda message: message.text in Amazonprimetvshowyear and (see(message.chat.id) == 'Amazonprimetvshowyear'))
def Amazonprime_tvshow_year(message):
    name = message.from_user.first_name
    save(name)
    bot.send_chat_action(message.chat.id, 'typing')
    msg = message.text
    ph =randgeneration('/home/srijithreddy/Desktop/Srijith reddy/Movies/Amazonprime/tvshows/year/'+msg[0:len(msg)]+'/')
    #ph = '/home/srijithreddy/Desktop/Srijith reddy/Movies/Amazonprime/tvshows/language/English/As Above, So Below✔️English🧁2014⭐6.2'
    photo = open(ph, 'rb')
    bot.send_photo(message.chat.id, photo)
    filename = os.path.basename(ph)
    if filename[filename.index('⭐')+1:] in ['Non','one']:
        rate = language(filename[0:filename.index('✔️')],filename[filename.index('🧁')+1:filename.index('⭐')])
        bot.send_message(message.chat.id, filename[0:filename.index('⭐')+1]+rate)
    else:
        bot.send_message(message.chat.id, filename)

 #Amazonprimetvshowrating
@bot.message_handler(commands=['Amazonprimetvshowrating'])
def Amazonprime_tvshow_rat(message):
    chatsave(message.chat.id,message.text[1:])
    name = message.from_user.first_name
    save(name)
    markup3= types.ReplyKeyboardMarkup(row_width=4)
    item = [None] * len(Amazonprimetvshowrating)
    for i in range(len(Amazonprimetvshowrating)):
        item[i]= types.KeyboardButton(Amazonprimetvshowrating[i])
    markup3.add(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7])
    bot.send_chat_action(message.chat.id, 'typing')
    S = generatestring3(Amazonprimetvshowrating)
    bot.send_message(message.chat.id, "Choose Language: \n"+S,reply_markup=markup3)

@bot.message_handler(func=lambda message: message.text in Amazonprimetvshowrating and (see(message.chat.id) == 'Amazonprimetvshowrating'))
def Amazonprime_tvshow_rat(message):
    name = message.from_user.first_name
    save(name)
    bot.send_chat_action(message.chat.id, 'typing')
    msg = message.text
    ph =randgeneration('/home/srijithreddy/Desktop/Srijith reddy/Movies/Amazonprime/tvshows/rating/'+msg[0:len(msg)]+'/')
    #ph = '/home/srijithreddy/Desktop/Srijith reddy/Movies/Amazonprime/tvshows/language/English/As Above, So Below✔️English🧁2014⭐6.2'
    photo = open(ph, 'rb')
    bot.send_photo(message.chat.id, photo)
    filename = os.path.basename(ph)
    if filename[filename.index('⭐')+1:] in ['Non','one']:
        rate = language(filename[0:filename.index('✔️')],filename[filename.index('🧁')+1:filename.index('⭐')])
        bot.send_message(message.chat.id, filename[0:filename.index('⭐')+1]+rate)
    else:
        bot.send_message(message.chat.id, filename)
#Hotstar
@bot.message_handler(commands=['Hotstarmovielanguage'])
def Hotstar_movie_lang(message):
    chatsave(message.chat.id,message.text[1:])
    name = message.from_user.first_name
    save(name)
    markup3= types.ReplyKeyboardMarkup(row_width=4)
    item = [None] * len(Hotstarmovielanguage)
    for i in range(len(Hotstarmovielanguage)):
        item[i]= types.KeyboardButton(Hotstarmovielanguage[i])
    markup3.add(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8], item[9], item[10], item[11], item[12], item[13], item[14], item[15], item[16], item[17], item[18], item[19], item[20], item[21], item[22], item[23], item[24], item[25], item[26], item[27], item[28], item[29], item[30], item[31], item[32], item[33], item[34], item[35], item[36], item[37], item[38], item[39], item[40], item[41], item[42], item[43], item[44], item[45], item[46], item[47], item[48], item[49], item[50], item[51], item[52], item[53], item[54], item[55], item[56], item[57], item[58], item[59], item[60], item[61], item[62], item[63], item[64], item[65], item[66], item[67], item[68], item[69], item[70], item[71], item[72], item[73], item[74], item[75], item[76], item[77], item[78], item[79], item[80], item[81], item[82], item[83], item[84])
    bot.send_chat_action(message.chat.id, 'typing')
    S = generatestring1(Hotstarmovielanguage)
    bot.send_message(message.chat.id, "Choose Language: \n"+S,reply_markup=markup3)

@bot.message_handler(func=lambda message: message.text in Hotstarmovielanguage and (see(message.chat.id) == 'Hotstarmovielanguage'))
def Hotstar_movie_lang(message):
    name = message.from_user.first_name
    save(name)
    bot.send_chat_action(message.chat.id, 'typing')
    msg = message.text
    ph =randgeneration('/home/srijithreddy/Desktop/Srijith reddy/Movies/Hotstar/movies/language/'+msg[0:len(msg)]+'/')
    #ph = '/home/srijithreddy/Desktop/Srijith reddy/Movies/Hotstar/movies/language/English/As Above, So Below✔️English🧁2014⭐6.2'
    photo = open(ph, 'rb')
    bot.send_photo(message.chat.id, photo)
    filename = os.path.basename(ph)
    if filename[filename.index('⭐')+1:] in ['Non','one']:
        rate = language(filename[0:filename.index('✔️')],filename[filename.index('🧁')+1:filename.index('⭐')])
        bot.send_message(message.chat.id, filename[0:filename.index('⭐')+1]+rate)
    else:
        bot.send_message(message.chat.id, filename)


#Hotstarmovieyear
@bot.message_handler(commands=['Hotstarmovieyear'])
def Hotstar_movie_year(message):
    chatsave(message.chat.id,message.text[1:])
    name = message.from_user.first_name
    save(name)
    markup3= types.ReplyKeyboardMarkup(row_width=4)
    item = [None] * len(Hotstarmovieyear)
    for i in range(len(Hotstarmovieyear)):
        item[i]= types.KeyboardButton(Hotstarmovieyear[i])
    markup3.add(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8], item[9], item[10], item[11], item[12], item[13], item[14], item[15], item[16], item[17], item[18], item[19], item[20], item[21], item[22], item[23], item[24], item[25], item[26], item[27], item[28], item[29], item[30], item[31], item[32], item[33], item[34], item[35], item[36], item[37], item[38], item[39], item[40], item[41], item[42], item[43], item[44], item[45], item[46], item[47], item[48], item[49], item[50], item[51], item[52], item[53], item[54], item[55], item[56], item[57], item[58], item[59], item[60], item[61], item[62], item[63], item[64], item[65], item[66], item[67], item[68], item[69])
    bot.send_chat_action(message.chat.id, 'typing')
    S = generatestring2(Hotstarmovieyear)
    bot.send_message(message.chat.id, "Choose Language: \n"+S,reply_markup=markup3)

@bot.message_handler(func=lambda message: message.text in Hotstarmovieyear and (see(message.chat.id) == 'Hotstarmovieyear'))
def Hotstar_movie_year(message):
    name = message.from_user.first_name
    save(name)
    bot.send_chat_action(message.chat.id, 'typing')
    msg = message.text
    ph =randgeneration('/home/srijithreddy/Desktop/Srijith reddy/Movies/Hotstar/movies/year/'+msg[0:len(msg)]+'/')
    #ph = '/home/srijithreddy/Desktop/Srijith reddy/Movies/Hotstar/movies/language/English/As Above, So Below✔️English🧁2014⭐6.2'
    photo = open(ph, 'rb')
    bot.send_photo(message.chat.id, photo)
    filename = os.path.basename(ph)
    if filename[filename.index('⭐')+1:] in ['Non','one']:
        rate = language(filename[0:filename.index('✔️')],filename[filename.index('🧁')+1:filename.index('⭐')])
        bot.send_message(message.chat.id, filename[0:filename.index('⭐')+1]+rate)
    else:
        bot.send_message(message.chat.id, filename)
 #Hotstarmovierating
@bot.message_handler(commands=['Hotstarmovierating'])
def Hotstar_movie_rat(message):
    chatsave(message.chat.id,message.text[1:])
    name = message.from_user.first_name
    save(name)
    markup3= types.ReplyKeyboardMarkup(row_width=4)
    item = [None] * len(Hotstarmovierating)
    for i in range(len(Hotstarmovierating)):
        item[i]= types.KeyboardButton(Hotstarmovierating[i])
    markup3.add(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8])
    bot.send_chat_action(message.chat.id, 'typing')
    S = generatestring3(Hotstarmovierating)
    bot.send_message(message.chat.id, "Choose Language: \n"+S,reply_markup=markup3)

@bot.message_handler(func=lambda message: message.text in Hotstarmovierating and (see(message.chat.id) == 'Hotstarmovierating'))
def Hotstar_movie_rat(message):
    name = message.from_user.first_name
    save(name)
    bot.send_chat_action(message.chat.id, 'typing')
    msg = message.text
    ph =randgeneration('/home/srijithreddy/Desktop/Srijith reddy/Movies/Hotstar/movies/rating/'+msg[0:len(msg)]+'/')
    #ph = '/home/srijithreddy/Desktop/Srijith reddy/Movies/Hotstar/movies/language/English/As Above, So Below✔️English🧁2014⭐6.2'
    photo = open(ph, 'rb')
    bot.send_photo(message.chat.id, photo)
    filename = os.path.basename(ph)
    if filename[filename.index('⭐')+1:] in ['Non','one']:
        rate = language(filename[0:filename.index('✔️')],filename[filename.index('🧁')+1:filename.index('⭐')])
        bot.send_message(message.chat.id, filename[0:filename.index('⭐')+1]+rate)
    else:
        bot.send_message(message.chat.id, filename)
#Hotstar
@bot.message_handler(commands=['Hotstartvshowlanguage'])
def Hotstar_tvshow_lang(message):
    chatsave(message.chat.id,message.text[1:])
    name = message.from_user.first_name
    save(name)
    markup3= types.ReplyKeyboardMarkup(row_width=4)
    item = [None] * len(Hotstartvshowlanguage)
    for i in range(len(Hotstartvshowlanguage)):
        item[i]= types.KeyboardButton(Hotstartvshowlanguage[i])
    markup3.add(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8], item[9], item[10], item[11], item[12], item[13], item[14], item[15], item[16], item[17], item[18], item[19], item[20], item[21], item[22], item[23], item[24], item[25], item[26], item[27], item[28], item[29], item[30], item[31], item[32], item[33], item[34], item[35], item[36], item[37], item[38], item[39], item[40], item[41], item[42], item[43], item[44], item[45], item[46], item[47], item[48], item[49], item[50], item[51], item[52])
    bot.send_chat_action(message.chat.id, 'typing')
    S = generatestring1(Hotstartvshowlanguage)
    bot.send_message(message.chat.id, "Choose Language: \n"+S,reply_markup=markup3)

@bot.message_handler(func=lambda message: message.text in Hotstartvshowlanguage and (see(message.chat.id) == 'Hotstartvshowlanguage'))
def Hotstar_tvshow_lang(message):
    name = message.from_user.first_name
    save(name)
    bot.send_chat_action(message.chat.id, 'typing')
    msg = message.text
    ph =randgeneration('/home/srijithreddy/Desktop/Srijith reddy/Movies/Hotstar/tvshows/language/'+msg[0:len(msg)]+'/')
    #ph = '/home/srijithreddy/Desktop/Srijith reddy/Movies/Hotstar/tvshows/language/English/As Above, So Below✔️English🧁2014⭐6.2'
    photo = open(ph, 'rb')
    bot.send_photo(message.chat.id, photo)
    filename = os.path.basename(ph)
    if filename[filename.index('⭐')+1:] in ['Non','one']:
        rate = language(filename[0:filename.index('✔️')],filename[filename.index('🧁')+1:filename.index('⭐')])
        bot.send_message(message.chat.id, filename[0:filename.index('⭐')+1]+rate)
    else:
        bot.send_message(message.chat.id, filename)

#Hotstartvshowyear
@bot.message_handler(commands=['Hotstartvshowyear'])
def Hotstar_tvshow_year(message):
    chatsave(message.chat.id,message.text[1:])
    name = message.from_user.first_name
    save(name)
    markup3= types.ReplyKeyboardMarkup(row_width=4)
    item = [None] * len(Hotstartvshowyear)
    for i in range(len(Hotstartvshowyear)):
        item[i]= types.KeyboardButton(Hotstartvshowyear[i])
    markup3.add(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8], item[9], item[10], item[11], item[12], item[13], item[14], item[15], item[16], item[17], item[18], item[19], item[20], item[21], item[22], item[23], item[24], item[25], item[26], item[27], item[28], item[29], item[30], item[31], item[32], item[33], item[34], item[35], item[36], item[37], item[38], item[39], item[40], item[41], item[42], item[43])
    bot.send_chat_action(message.chat.id, 'typing')
    S = generatestring2(Hotstartvshowyear)
    bot.send_message(message.chat.id, "Choose Language: \n"+S,reply_markup=markup3)

@bot.message_handler(func=lambda message: message.text in Hotstartvshowyear and (see(message.chat.id) == 'Hotstartvshowyear'))
def Hotstar_tvshow_year(message):
    name = message.from_user.first_name
    save(name)
    bot.send_chat_action(message.chat.id, 'typing')
    msg = message.text
    ph =randgeneration('/home/srijithreddy/Desktop/Srijith reddy/Movies/Hotstar/tvshows/year/'+msg[0:len(msg)]+'/')
    #ph = '/home/srijithreddy/Desktop/Srijith reddy/Movies/Hotstar/tvshows/language/English/As Above, So Below✔️English🧁2014⭐6.2'
    photo = open(ph, 'rb')
    bot.send_photo(message.chat.id, photo)
    filename = os.path.basename(ph)
    if filename[filename.index('⭐')+1:] in ['Non','one']:
        rate = language(filename[0:filename.index('✔️')],filename[filename.index('🧁')+1:filename.index('⭐')])
        bot.send_message(message.chat.id, filename[0:filename.index('⭐')+1]+rate)
    else:
        bot.send_message(message.chat.id, filename)
 #Hotstartvshowrating
@bot.message_handler(commands=['Hotstartvshowrating'])
def Hotstar_tvshow_rat(message):
    chatsave(message.chat.id,message.text[1:])
    name = message.from_user.first_name
    save(name)
    markup3= types.ReplyKeyboardMarkup(row_width=4)
    item = [None] * len(Hotstartvshowrating)
    for i in range(len(Hotstartvshowrating)):
        item[i]= types.KeyboardButton(Hotstartvshowrating[i])
    markup3.add(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8])
    bot.send_chat_action(message.chat.id, 'typing')
    S = generatestring3(Hotstartvshowrating)
    bot.send_message(message.chat.id, "Choose Language: \n"+S,reply_markup=markup3)

@bot.message_handler(func=lambda message: message.text in Hotstartvshowrating and (see(message.chat.id) == 'Hotstartvshowrating'))
def Hotstar_tvshow_rat(message):
    name = message.from_user.first_name
    save(name)
    bot.send_chat_action(message.chat.id, 'typing')
    msg = message.text
    ph =randgeneration('/home/srijithreddy/Desktop/Srijith reddy/Movies/Hotstar/tvshows/rating/'+msg[0:len(msg)]+'/')
    #ph = '/home/srijithreddy/Desktop/Srijith reddy/Movies/Hotstar/tvshows/language/English/As Above, So Below✔️English🧁2014⭐6.2'
    photo = open(ph, 'rb')
    bot.send_photo(message.chat.id, photo)
    filename = os.path.basename(ph)
    if filename[filename.index('⭐')+1:] in ['Non','one']:
        rate = language(filename[0:filename.index('✔️')],filename[filename.index('🧁')+1:filename.index('⭐')])
        bot.send_message(message.chat.id, filename[0:filename.index('⭐')+1]+rate)
    else:
        bot.send_message(message.chat.id, filename)
@bot.message_handler(func=lambda message: message.text[0] == '$' and message.text[len(message.text)-3:len(message.text)] != 'All')
def search(message):
     name = message.from_user.first_name
     save(name)
     bot.send_chat_action(message.chat.id, 'typing')
     msg = message.text
     L = 'XOXO'
     stream = 'XOXO'
     rating = 'XOXO'
     t ='None'
     try:
         stream = msg[msg.index('$')+1:msg.index('*')]
         stream = str(stream)
     except  ValueError:
         t = 'error'
     try:
         language = msg[msg.index('*')+1:msg.index('=')]
         L = str(language)
     except ValueError:
         t = 'error'
     try:
         rating = msg[msg.index('=')+1:len(msg)]
     except ValueError:
         t = 'error'

    # if L in ['English','Hindi']:
        # bot.send_message(message.chat.id, "This may take some time please wait ,"+str(L)+" database is a lot to search.")
     R = rating
     if stream[0] == 'N':
         A='Netflix'
     elif stream[0] == 'A':
         A = 'Amazonprime'
     elif stream[0] == 'H':
         A = 'Hotstar'
     else:
        t = 'error'
     if stream[1] == 'm':
         B='movies'
     elif stream[1] == 't':
         B = 'tvshows'
     else:
        t = 'error'
     if t == 'error':
            bot.send_message(message.chat.id, "Invalid format use this format: \n $Nt*English=7.2")
            bot.send_chat_action(message.chat.id, 'typing')
     else:
         re = newrand(A,B,L,R)
         if re != 'No such file' :
            # re = '/home/srijithreddy/Desktop/Srijith reddy/Movies/Netflix/tvshows/language/Telugu/Pitta Kathalu✔️Telugu🧁2020⭐Non'
             photo = open(re, 'rb')
             bot.send_photo(message.chat.id, photo)
             filename = os.path.basename(re)
             A = filename[0:filename.index('✔️')]
             B = filename[filename.index('🧁')+1:filename.index('⭐')]
             if filename[filename.index('⭐')+1:] in ['Non','one']:
                 response = requests.get('http://www.omdbapi.com/?apikey=a2d1da4c&t='+str(A)+'&y='+str(B)).text
                 response_info = json.loads(response)
                 if response_info["Response"] == "True" and response_info["imdbRating"] != "N/A":
                     tex = response_info["imdbRating"]
                 elif response_info["Response"] == "False":
                     tex = 'None'
                 elif response_info["Response"] == "True" and response_info["imdbRating"] == "N/A":
                     tex = 'None'
                 bot.send_message(message.chat.id,filename[0:filename.index('⭐')+1]+str(tex))
             else:
                  bot.send_message(message.chat.id,filename)
         else:
            bot.send_message(message.chat.id, "No posters matching given criteria")
@bot.message_handler(func=lambda message: message.text[0] == '$' and message.text[len(message.text)-3:len(message.text)] == 'All')
def search(message):
     name = message.from_user.first_name
     save(name)
     bot.send_chat_action(message.chat.id, 'typing')
     msg = message.text
     L = 'XOXO'
     stream = 'XOXO'
     rating = 'XOXO'
     t ='None'
     try:
         stream = msg[msg.index('$')+1:msg.index('*')]
         stream = str(stream)
     except  ValueError:
         t = 'error'
     try:
         language = msg[msg.index('*')+1:msg.index('=')]
         L = str(language)
     except ValueError:
         t = 'error'
     try:
         rating = msg[msg.index('=')+1:len(msg)-3]
     except ValueError:
         t = 'error'

    # if L in ['English','Hindi']:
        # bot.send_message(message.chat.id, "This may take some time please wait ,"+str(L)+" database is a lot to search.")
     R = rating
     if stream[0] == 'N':
         A='Netflix'
     elif stream[0] == 'A':
         A = 'Amazonprime'
     elif stream[0] == 'H':
         A = 'Hotstar'
     else:
        t = 'error'
     if stream[1] == 'm':
         B='movies'
     elif stream[1] == 't':
         B = 'tvshows'
     else:
        t = 'error'
     if t == 'error':
            bot.send_message(message.chat.id, "Invalid format use this format: \n $Nt*English=7.2All")
            bot.send_chat_action(message.chat.id, 'typing')
     else:
         re = newrand2(A,B,L,R)
         if re != ['No such file'] :
             for i in range(len(re)):

            # re = '/home/srijithreddy/Desktop/Srijith reddy/Movies/Netflix/tvshows/language/Telugu/Pitta Kathalu✔️Telugu🧁2020⭐Non'
                 photo = open(re[i], 'rb')
                 bot.send_photo(message.chat.id, photo)
                 filename = os.path.basename(re[i])
                 A = filename[0:filename.index('✔️')]
                 B = filename[filename.index('🧁')+1:filename.index('⭐')]
                 if filename[filename.index('⭐')+1:] in ['Non','one']:
                     response = requests.get('http://www.omdbapi.com/?apikey=a2d1da4c&t='+str(A)+'&y='+str(B)).text
                     response_info = json.loads(response)
                     if response_info["Response"] == "True" and response_info["imdbRating"] != "N/A":
                         tex = response_info["imdbRating"]
                     elif response_info["Response"] == "False":
                         tex = 'None'
                     elif response_info["Response"] == "True" and response_info["imdbRating"] == "N/A":
                         tex = 'None'
                     bot.send_message(message.chat.id,filename[0:filename.index('⭐')+1]+str(tex))
                 else:
                     bot.send_message(message.chat.id,filename)
         else:
            bot.send_message(message.chat.id, "No posters matching given criteria")
@bot.message_handler(commands=['Multiplefilters'])
def info_options(message):
    name = message.from_user.first_name
    save(name)
    bot.send_chat_action(message.chat.id, 'typing')
    markup2 = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('$Nt*English=7.2')
    itembtn2 = types.KeyboardButton('$Nm*Tamil=6.5All')
    itembtn3 = types.KeyboardButton('$At*Telugu=7.2All')
    itembtn4 = types.KeyboardButton('$Am*Hindi=8.0')
    itembtn5 = types.KeyboardButton('$Ht*French=7.2')
    itembtn6 = types.KeyboardButton('$Hm*Spanish=8.0')
    markup2.add(itembtn1, itembtn2,itembtn3, itembtn4,itembtn5, itembtn6)
    bot.send_message(message.chat.id, "Just use 'All' at end if you want all movies with given criteria \n Ex: $Nm*Tamil=6.5All  for given format \nUse multiple filters in the below format:  \n$Nt*English=7.2\n Here Nt represents Netflix tvshows \nUse Nm in place of Nt for Netflix movie\nsimilarly Use Am in place of Nt for Amazonprime movie\nUse At in place of Nt for Amazonprime tvshows\nsimilarly Use Hm in place of Nt for Hotstar movie\nUse Ht in place of Nt for Hotstar tvshows\nReplace English with any language you want with first letter capital \nReplace 7.2 with any minimum rating you want to use\n ",reply_markup=markup2)
@bot.message_handler(commands=['Ahamovie', 'Ahatvshow'])
def info_options(message):
    name = message.from_user.first_name
    save(name)
    bot.send_chat_action(message.chat.id, 'typing')
    msg = message.text
    ph =randgeneration('/home/srijithreddy/Desktop/Srijith reddy/Movies/Aha/'+str(msg[4:])+'s/Ahaimages/')
     #ph = '/home/srijithreddy/Desktop/Srijith reddy/Movies/Hotstar/tvshows/language/English/As Above, So Below✔️English🧁2014⭐6.2'
    photo = open(ph, 'rb')
    bot.send_photo(message.chat.id, photo)
    filename = os.path.basename(ph)
    if filename[filename.index('⭐')+1:] in ['Non','one']:
        rate = language(filename[0:filename.index('✔️')],filename[filename.index('🧁')+1:filename.index('⭐')])
        bot.send_message(message.chat.id, filename[0:filename.index('⭐')+1]+rate)
    else:
        bot.send_message(message.chat.id, filename)
#tb.send_message(chat_id, "Choose one letter:", reply_markup=markup)
#Netflix
@bot.message_handler(commands=['stop'])
def info_options(message):
    print('stop')
    exit()
    exit()
@bot.message_handler(commands=['stop'])
def info_options(message):
    print('stop')
    exit()
    exit()

@bot.message_handler(commands=['howtouse'])
def info_options(message):
    name = message.from_user.first_name
    save(name)
    bot.send_chat_action(message.chat.id, 'typing')
    ph ='/home/srijithreddy/Desktop/Srijith reddy/Movies/1623398535260.mp4'
    video = open(ph, 'rb')
    bot.send_video(message.chat.id, video)
while True:
    try:
        status = "Connected"
        bot.polling(none_stop=False, interval=0.8)
        pass

    except Exception as e:
        print(e)
        status = "failure"
        print(status)

    else:
        print(status)
    #do something..
    time.sleep(1)
#bot.polling(none_stop=False, interval=1)
