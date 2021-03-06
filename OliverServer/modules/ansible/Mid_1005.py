# -*- coding: utf-8 -*-
from Public_lib import *

#同步业务文件模块#

class Modulehandle():
    def __init__(self,moduleid,hosts,sys_param_row):
        self.hosts = ""
        self.Runresult = ""
        self.moduleid = moduleid
        self.sys_param_array= sys_param_row
        self.hosts=target_host(hosts,"IP")

    def run(self):
        try:
            commonname=str(self.sys_param_array[0])
            if commonname=="nginx":
                #源文件
                source="/etc/init.d/nginx"
                
                #目标文件
                goal="/etc/init.d/nginx"
                
                #处理后续工作
                hx="chmod u+x "+str(goal)
            elif commonname=="haproxy":
                source="/home/Appconfig/RsyncFile/haproxy.cfg"
                goal="/usr/local/haproxy/haproxy.cfg"
                hx="ls "+str(goal)
                
            elif commonname=="syslog":
                source="/home/Appconfig/RsyncFile/syslog.conf"
                goal="/etc/syslog.conf"
                hx="/etc/init.d/syslog restart"

            elif commonname=="nginx_config":
                source="/home/Appconfig/RsyncFile/nginx.conf"
                goal="/usr/local/nginx/conf/nginx.conf"
                hx="ls "+str(goal)

            elif commonname=="sysctl":
                source="/home/Appconfig/RsyncFile/sysctl.conf"
                goal="/etc/sysctl.conf"
                hx="sysctl -p"
                
            elif commonname=="resin":
                source="/home/Appconfig/RsyncFile/resin.conf"
                goal="/usr/java/resin-3.0.22/conf/resin.conf"
                hx="ls /usr/java/resin-3.0.22/conf/resin.conf"

            elif commonname=="resinhttpd":
                source="/home/Appconfig/RsyncFile/httpd.sh"
                goal="/usr/java/resin-3.0.22/bin/httpd.sh"
                hx="chmod u+x /usr/java/resin-3.0.22/bin/httpd.sh"

            elif commonname=="resinjar":
                source="/home/Appconfig/RsyncFile/resin.jar"
                goal="/usr/java/resin-3.0.22/lib/resin.jar"
                hx="ls /usr/java/resin-3.0.22/lib/resin.jar"
                
            ansible.runner.Runner(
            pattern=self.hosts, forks=forks,
            module_name="copy", module_args="src="+source+" dest="+goal,).run()

            self.Runresult = ansible.runner.Runner(
            pattern=self.hosts, forks=forks,
            module_name="command", module_args=hx,).run()
            if len(self.Runresult['dark']) == 0 and len(self.Runresult['contacted']) == 0:
                return "<font color=#ffffff><b>No hosts found,请确认主机已经添加ansible环境！</b>"

        except Exception,e:
            return str(e)
        return self.Runresult
