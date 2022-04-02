#!/usr/bin/python3



class ClassName(object):

    def __init__(self,auth,SSID,passw,hidden,EAP,Anonymous,Identity,Phase_2):
        pass


    def formating(auth,SSID,passw,hidden,EAP,Anonymous,Identity,Phase_2):
        param = "WIFI:{Authentication}:{SSID};{Password}:{hidden};{EAP}:{Anonymous};{Identity};{Phase_2}".format(
            Authentication=auth,
            SSID=SSID,
            Password=passw,
            hidden=hidden,
            EAP=EAP,
            Anonymous=Anonymous,
            Identity=Identity,
            Phase_2=Phase_2
            )
