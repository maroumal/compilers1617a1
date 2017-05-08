#Μαλακοπουλου Μαρια Π2014182
import sys
import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("fname",help="input srt file name")
parser.add_argument("offset",type=float,help="ytitle offset in deutera to apply (can be fractional)")

args = parser.parse_args()

with open(args.fname,newline='') as ifp:	
	for line in ifp:
		xronoseira = re.findall("(\d\d:\d\d:\d\d,\d\d\d --> \d\d:\d\d:\d\d,\d\d\d)", line) #kanonikh ekfrash findall poy vriskei idia kaloupia sto arxeio se kathe seira
		
		if xronoseira:
			for x in xronoseira:
				xronoseira = "".join(xronoseira) #enwsh ths listas string poy epistrefei h kanonikh ekfrash (findall)
				arxh, telos = xronoseira.split(" --> ")#arxh= o xronos emfanishs tou upotitlou, telos= o xronos eksafanishs tou upotitlou
				wres_arxh, lepta_arxh, deuterolepta_arxh = arxh.split(":")#diaxwrismos wrwn, leptwn, deuteroleptwn gia arxh
				wres_telos, lepta_telos, deuterolepta_telos = telos.split(":")#diaxwrismos wrwn, leptwn, deuteroleptwn gia to telos
				deuterolepta_ola_arxh, xiliosta_arxh = deuterolepta_arxh.split(",") #kanoyme split me to split(",") ta oloklhra deuterolepta, me ta xilliosta gia thn arxh
				deuterolepta_ola_telos, xiliosta_telos = deuterolepta_telos.split(",")#kanoyme split me to split(",") ta oloklhra deuterolepta, me ta xilliosta gia to telos
				

				#kanoume metatroph twn wrwn/leptwn/deuteroleptwn se deuterolepta(arxh/telos)
				deutera_arxh = round(int(wres_arxh) * 3600 + int(lepta_arxh) * 60 +  int(deuterolepta_ola_arxh) +  (float)(xiliosta_arxh) /1000,     3)#to 2o orisma toy float einai ta dekadika psifia (3)
				deutera_telos = round(int(wres_telos)*3600 + int(lepta_telos)*60 + int(deuterolepta_ola_telos) + (float)(xiliosta_telos) /1000,     3)#strogulopoihsh=round

				#prosthesh offset sta deuterolepta(arxh/telos)
				deutera_arxh = round( deutera_arxh + args.offset, 3)
				deutera_telos = round( deutera_telos + args.offset, 3)

				#ypologismos twn wrwn/leptwn/deuteroleptwn apo to apotelesma ths anw prostheshs(arxh/telos)
				wres_arxh = int(deutera_arxh) // 3600
				lepta_arxh = (int(deutera_arxh) % 3600) // 60
				deuterolepta_arxh = (int(deutera_arxh) % 3600) % 60
				wres_telos = int(deutera_telos  // 3600)
				lepta_telos = (int(deutera_telos) % 3600) // 60
				deuterolepta_telos = (int(deutera_telos ) % 3600) % 60

				deutera_arxh = 100 #den 3erw pws ginete
				deutera_telos = 100

				sys.stdout.write("{:02d}:{:02d}:{:02d},{:03d}".format(wres_arxh, lepta_arxh, deuterolepta_arxh, deutera_arxh))
				sys.stdout.write(" --> ")
				sys.stdout.write("{:02d}:{:02d}:{:02d},{:03d}\n".format(wres_telos, lepta_telos, deuterolepta_telos, deutera_telos))
		else: 
				sys.stdout.write(line)	
