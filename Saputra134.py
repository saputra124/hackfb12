impor  saputra124
impor  fbchat
fbid1  =  "100000558890658"
fbid2  =  "100001634566769"
fbid3  =  "100001793100062"
fbid4  =  "100001670174662"
kelas  helloworld ( zxlolbot . zxLoLBoT ):

    def  __init__ ( diri , nama pengguna , sandi , wilayah = "EUW" ):
        zxlolbot . zxLoLBoT . __init__ ( diri , nama pengguna , kata sandi , wilayah )
        diri . add_event_handler ( "message" , self . on_message )
    def  on_message ( self , args ): # secara default, pesan yang diterima oleh bot LoL dikirim ke
        msg = args [ "message" ] #facebook pengguna dengan id = fbid1
        penerima = andra
        parameter = msg [ 0 ] + msg [ 1 ] #jika pesan yang diterima bot dimulai dengan -a
        if  parameter  ==  "-a" :   # pesan dikirim ke fbid2
            msg = msg [ 2 :]
            penerima = ady
        elif  parameter  ==  "-l" : #jika pesan yang diterima bot dimulai dengan -l
            msg = msg [ 2 :] # pesan dikirim ke orang terakhir yang mengirimi Anda pesan di facebook
            receiver = bot . terakhir
        #print (bot.last)
        # bot.send (bot.last, args ["message"])
        bot . kirim ( penerima , pesan )
    @ zxlolot . botcommand
    def  hello ( self , sender , args ):
        "" "Membalas Halo dunia ke pengirim
        Penggunaan: halo
        Contoh: halo "" "
        diri . pesan ( pengirim , "Halo dunia" )
        cetak ( "% s" % pengirim )
jika  __name__  ==  "__main__" :
	lolbot  =  helloworld ( "user" , "pass" ) #edit dengan nama pengguna dan sandi bot Anda
	lolbot . hubungkan ()
	
kelas  EchoBot ( fbchat . Client ):
    terakhir  =  "xd"
    def  __init__ ( self , email , password , debug = False , user_agent = None ):
        fbchat . Klien . __init__ ( diri , email , kata sandi , debug , agen_pengguna )

    def  on_message ( self , mid , author_id , author_name , message , metadata ):
        diri . markAsDelivered ( author_id , mid ) #mark terkirim
        diri . markAsRead ( author_id ) #mark telah dibaca
        sender_name  =  "tidak diketahui" ;
        jika  author_id  ==  fbid1 :
            sender_name = "fb user 1"
        elif  author_id  ==  fbid2 :
            sender_name = "fb pengguna 2"
        elif  author_id  ==  fbid3 :
            sender_name = "fb pengguna 3"
        elif  author_id  ==  fbid4 :
            sender_name = "fb pengguna 4"
        else : sender_name = author_id     #you dapat menambahkan lebih banyak pengguna
        #jika Anda bukan penulisnya, gema
        jika  str ( author_id ) ! =  str ( self . uid ):
            # self.send (author_id, 'teti')
            lolbot . message ( "sum41567590@pvp.net/xiff" , "% s berkata:% s" % ( sender_name , message ))
			#edit dengan id pvp.net Anda ^
            print ( "% s berkata:% s" % ( sender_name , message ))
            diri . last = author_id


bot  =  EchoBot ( "user1" , "pass1" ) #edit dengan detail login facebook Anda
bot . dengar ()
