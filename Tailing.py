import time,os
import threading

class TailError(Exception):
    def __init__(self, msg):
        self.message = msg

    def __str__(self):
        return self.message

class Tail(threading.Thread):
    def __init__(self, callback=None,  tail_file="",wait=1):
        super(Tail, self).__init__(target=self.tail_file)
        self.check_file_validity(tail_file)
        self._file= tail_file
        self.callback = callback
        self.waitTime=wait


    def tail_file(self):
        with open(self._file) as file_:
            # Go to the end of file
            for line in file_:
                self.callback(self._file+":>"+line.rstrip())
            while True:
                curr_position = file_.tell()
                line = file_.readline()
                if not line:
                    file_.seek(curr_position)
                    time.sleep(self.waitTime)
                else:
                    self.callback(self._file+":>"+line.rstrip())


    def check_file_validity(self, file_):
        ''' Check whether the a given file exists, readable and is a file '''
        if not os.access(file_, os.F_OK):
            raise TailError("File '%s' does not exist" % (file_))
        if not os.access(file_, os.R_OK):
            raise TailError("File '%s' not readable" % (file_))
        if os.path.isdir(file_):
            raise TailError("File '%s' is a directory" % (file_))




def p1(s):
    print(s)



# example using BaseThread with callback
thread = Tail(tail_file='/var/log/auth.log',callback=p1,wait=5).start()
thread = Tail(tail_file='/var/log/syslog',callback=p1,wait=5).start()
thread = Tail(tail_file='/var/log/kern.log',callback=p1,wait=5).start()


s='STAR=20080305 18:39:01|PNAM=todbk|PNUM=300|SSTA=20080305 18:39:01|STRT=20080305 18:39:01|STOP=20080305 18:39:01|STPT=20080305 18:39:01|SELA=00:00:00|SUBM=sysx@paul|SBID=sysx|SBND=paul|SNOD=john|CCOD=0|RECI=CTRC|RECC=CAPR|TZDI=-21600|MSGI=SCPA000I|MSST=Copy step successful.|STDL=Wed Mar  5 18:39:01 2008|CSDS=Wed Mar  518:39:01 2008|LCCD=0|LMSG=SCPA000I|OCCD=0|OMSG=SCPA000I|PNAM=todbk|PNUM=300|SNAM=step1|PNOD=paul|SNOD=john|LNOD=S|FROM=P|XLAT=N|SCMP=N|ECMP=N|OERR=N|CKPT=Y|LKFL=N|RSTR=N|RUSZ=65536|PACC=|SACC=|PPMN=|SFIL=/app/fmtprt/data/sysx/send/todtrigger.200803051837.results|SDS1= |SDS2= |SDS3= |SBYR=223|SFSZ=223|SRCR=1|SBYX=225|SRUX=1|SVSQ=0|SVCN=0|SVOL=|DFIL=todtrigger.200803051837.results|PPMN=|DDS1=R|DDS2= |DDS3= |DBYW=223|DRCW=1|DBYX=225|DRUX=1|DVSQ=0|DVCN=0|DVOL=|ICRC=N|PCRC=N|DLDR=/appl/biller/udot/input|ETMC=9|ETMK=0|ETMU=10'

import json
s='{"'+s.replace('|','","').replace('=','":"')+'"}'
s=json.loads(s)
print(s)
