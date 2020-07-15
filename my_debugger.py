from ctypes import *
from my_debugger_define import *


kernel32 = windll.kernel32


class debugger():

    #构造函数
    def __init__(self):
        pass

    def load(self,path_to_exe):

        #调用线程将启动并调试新进程以及新进程创建的所有子进程
        creation_flags = DEBUG_PROCESS

        #实例化结构体，用于CreateProcessA函数传参
        startupinfo = STARTUPINFO()
        process_information = PROCESS_INFORMATION()


        #

        startupinfo.dwFlags = 0x1
        startupinfo.wShowWindow = 0x0


        #

        startupinfo.cb = sizeof(startupinfo)


        #调用CreateProcessA函数创建子进程

        if kernel32.CreateProcessA(
            path_to_exe,
            None,
            None,
            None,
            None,
            creation_flags,
            None,
            None,
            byref(startupinfo),
            byref(process_information),

        ):
            print(" [*] We have successfully launched the process")
            print(" [*] PID: %d" % process_information.dwProcessId)

        else:
            print(" [*] Error: 0x%08x." % kernel32.GetLastError())










