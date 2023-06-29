import os
from abc import ABC, abstractmethod, abstractproperty
from pick import pick

import sys
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QPushButton, QWidget, QHBoxLayout, QVBoxLayout, QLabel
from PyQt5.QtGui import QPixmap








class SingletonManager :
    _Username = []
    _Password = []
    def __init__(self) :
        self._Username = self._Username
        self._Password = self._Password

    def isValid(self, Username, Password) :
        if ( Username in self._Username ) :
            index = self._Username.index( Username )
            if ( self._Password[index] == Password ) :
                return True
        return False

class Manager(SingletonManager) :
    def __init__(self, Username, Password ) :
        SingletonManager.__init__(self)
        self._Username.append( Username )
        self._Password.append( Password )











class SingletonStaff :
    _Username = []
    _Password = []
    def __init__(self) :
        self._Username = self._Username
        self._Password = self._Password

    def isValid(self, Username, Password) :
        if ( Username in self._Username ) :
            index = self._Username.index( Username )
            if ( self._Password[index] == Password ) :
                return True
        return False

class Staff(SingletonStaff) :
    def __init__(self, Username, Password ) :
        SingletonStaff.__init__(self)
        self._Username.append( Username )
        self._Password.append( Password )
        self.StateA = None
        self.StateB = None

    def InterfaceMakanan(self) :
        self.StateA = Makanan
        self.StateB = MakananBersize

        print("Menu Makanan :\n")
        self.StateA.TampilinSemuaMenu()
        print()
        self.StateB.TampilinSemuaMenu()
        print("\n! Input /BACK untuk kembali ke menu sebelumnya.")
        Kode = str(input("Beli Makanan dengan Kode : "))

        if ( Kode == "/BACK" ) :
            pass
        elif ( self.StateA.CheckKode(Kode) ) :
            os.system("cls")
            Objek = self.StateA.Pembelian(Kode)
            if ( Objek == "Tidak Jadi Beli" ) :
                input("\nTekan Enter untuk melanjutkan ...")

            else :
                DataPembelian.AddData( Objek )
                print("\nPembelian berhasil dilakukan.")
                input("\nTekan Enter untuk melanjutkan ...")
        elif ( self.StateB.CheckKode(Kode) ) :
            os.system("cls")
            Objek = self.StateB.Pembelian(Kode)
            if ( Objek == "Tidak Jadi Beli" ) :
                input("\nTekan Enter untuk melanjutkan ...")
                pass
            else :
                DataPembelian.AddData( Objek )
                print("\nPembelian berhasil dilakukan.")
                input("\nTekan Enter untuk melanjutkan ...")
        else :
            print(f"\n! Kode {Kode} tidak ditemukan")
            input("\nTekan Enter untuk melanjutkan ...")

        

    def InterfaceMinuman(self) :
        self.StateA = Minuman
        self.StateB = MinumanBersize

        print("Menu Minuman :\n")
        self.StateA.TampilinSemuaMenu()
        print()
        self.StateB.TampilinSemuaMenu()
        print("\n! Input /BACK untuk kembali ke menu sebelumnya.")
        Kode = str(input("Beli Minuman dengan Kode : "))

        if ( Kode == "/BACK" ) :
            pass
        elif ( self.StateA.CheckKode(Kode) ) :
            os.system("cls")
            Objek = self.StateA.Pembelian(Kode)
            if ( Objek == "Tidak Jadi Beli" ) :
                input("\nTekan Enter untuk melanjutkan ...")

            else :
                DataPembelian.AddData( Objek )
                print("\nPembelian berhasil dilakukan.")
                input("\nTekan Enter untuk melanjutkan ...")
        elif ( self.StateB.CheckKode(Kode) ) :
            os.system("cls")
            Objek = self.StateB.Pembelian(Kode)
            if ( Objek == "Tidak Jadi Beli" ) :
                input("\nTekan Enter untuk melanjutkan ...")

            else :
                DataPembelian.AddData( Objek )
                print("\nPembelian berhasil dilakukan.")
                input("\nTekan Enter untuk melanjutkan ...")
        else :
            print(f"\n! Kode {Kode} tidak ditemukan")
            input("\nTekan Enter untuk melanjutkan ...")

    def InterfaceTiket (self) :

        AllAgesMovie.CetakInfoMovie()
        print("\n\n")
        RestrictedMovie.CetakInfoMovie()
        print("\n\n")

        print("! Input /BACK untuk kembali ke menu sebelumnya.")
        Kode = str(input("Beli Tiket Film dengan Kode : "))

        if ( Kode == "/BACK" ) :
            pass

        elif ( AllAgesMovie.CheckKode(Kode) ) :
            ObjekArr = AllAgesMovie.PembelianTiket(Kode)
            if ( len(ObjekArr) > 0 ) :
                for Tiket in ObjekArr :
                    DataPembelian.AddData( Tiket )
            input("\nTekan Enter untuk melanjutkan ...")
        elif ( RestrictedMovie.CheckKode(Kode) ) :
            ObjekArr = RestrictedMovie.PembelianTiket(Kode)
            if ( len(ObjekArr) > 0 ) :
                for Tiket in ObjekArr :
                    DataPembelian.AddData( Tiket )
            input("\nTekan Enter untuk melanjutkan ...")
        else :
            print(f"\n! Kode {Kode} tidak ditemukan")
            input("\nTekan Enter untuk melanjutkan ...")
        


        












class SyaratMenu (ABC) :
    @abstractproperty
    def Type (self) :
        pass
    @abstractproperty
    def Menu (self) :
        pass  
    @abstractmethod
    def RunInterface(self) :
        pass
    @abstractmethod
    def TampilinSemuaMenu (self) :
        pass
    @abstractmethod
    def NaikanHargaSemuaMenu (self) :
        pass





class Menuinterface ( SyaratMenu ) :
    Type = ""
    Menu = []
    def __init__(self, Type) :
        self.Type = Type
        self.Menu = []

    def RunInterface(self) :
        while( True ) :
            os.system("cls")

            title = f'Data {self.Type} : '
            options = [ "1. Cetak Semua Menu", "2. Input Menu Baru", "3. Edit Menu", "4. Delete Menu", "5. Naikan Harga Semua Menu", "0. Back" ]
            option, index = pick(options, title, "->")
            os.system("cls")

            if ( option == "1. Cetak Semua Menu" ) :
                print(f"Data Semua {self.Type} :\n")
                self.TampilinSemuaMenu()
            elif ( option == "2. Input Menu Baru" ) :
                self.InputMenuBaru()
            elif( option == "3. Edit Menu" ) :
                self.EditMenu()
            elif ( option == "4. Delete Menu" ) :
                self.DeleteMenu()
            elif ( option == "5. Naikan Harga Semua Menu" ) :
                self.NaikanHargaSemuaMenu()
            elif ( option == "0. Back" ) :
                break

            input("\nTekan Enter untuk melanjutkan ...")

    def TampilinSemuaMenu (self) :
        for i in range( len(self.Menu) ) :
            Count = str(i+1)
            self.Menu[i].CetakMenu( Count )

    def InputMenuBaru(self) :
        try :
            print( f"Input Menu {self.Type}\n")
            NamaMenu = str(input( f"Nama {self.Type} \t: " ))

            # Mengecek apakah sudah ada nama menu yang sama di array Menu
            if ( NamaMenu in [ Object.NamaMenu for Object in self.Menu ] ) :
                raise Exception( f"Menu {NamaMenu} sudah pernah diregister.")
            if ( len (NamaMenu) > 30 ) :
                raise Exception( f"Jumlah karakter untuk Nama {self.Type} tidak boleh lebih besar dari 30.")

            Harga = int(input( f"Harga {self.Type} \t: Rp. " ))
            if ( Harga <= 0 ) :
                raise Exception( f"Harga harus bernilai lebih besar dari 0.")
            
            # Update dan sorting Array Menu
            self.Menu.append( Menu( NamaMenu, Harga ) )
            self.Menu.sort(key=lambda x: x.NamaMenu)

            print("\nInput berhasil dilakukan.")

        except ValueError :
            print( "\n! Input harga harus berupa angka." )
        except Exception as e :
            print( "\n! ", end="" )
            print( str(e) )
    
    def EditMenu(self) :
        print(f"Data Semua {self.Type} :\n")
        self.TampilinSemuaMenu()
        print()
        Input = str(input(f"Edit Menu {self.Type} dengan kode : "))
        try :
            if ( Input[0] == "A" and 0 < int(Input[1::]) <= len(self.Menu) ) :
                index = int(Input[1::]) - 1
                self.Menu[ index ].EditMenu(self.Type)
                self.Menu.sort(key=lambda x: x.NamaMenu)            
            else :
                raise Exception
        except Exception:
            print( f"\n! Kode Menu {self.Type} : {Input} tidak tersedia" )

    def DeleteMenu(self) :
        print(f"Data Semua {self.Type} :\n")
        self.TampilinSemuaMenu()
        print()
        Input = str(input("Edit Menu makanan dengan kode : "))
        try :
            if ( Input[0] == "A" and 0 < int(Input[1::]) <= len(self.Menu) ) :
                index = int(Input[1::]) - 1
                del self.Menu[ index ]   
                print( "\nDelete menu berhasil dilakukan." ) 
            else :
                raise Exception
        except Exception:
            print( f"\n! Kode Menu {self.Type} : {Input} tidak tersedia" )

    def NaikanHargaSemuaMenu (self) :
        print(f"Naikan Harga Semua Menu {self.Type}\n")
        try :
            KenaikanHarga = int(input( f"Kenaikan Harga {self.Type} \t: Rp. " ))
            if ( KenaikanHarga <= 0 ) :
                raise Exception( f"Kenaikan Harga harus bernilai lebih besar dari 0.")
            for item in self.Menu :
                item.Harga += KenaikanHarga
            print(f"\nKenaikan Harga Semua Menu {self.Type} berhasil dilakukan.")
            
        except ValueError :
            print( "\n! Input harga harus berupa angka." )
        except Exception as e:
            print( "\n! ", end="" )
            print( str(e) )

    def CheckKode (self, Kode) :
        try :
            if ( Kode[0] == "A" and 0 < int(Kode[1::]) <= len(self.Menu) ) :
                return True
            else :
                return False
        except :
            return False

    def Pembelian (self, Kode) :
        index = int(Kode[1::]) - 1
        print( f"Pembelian Menu {self.Type}\n" )
        print( f"Nama Menu \t: { self.Menu[index].NamaMenu }" )
        FormatHarga = "{:,.2f}".format(self.Menu[index].Harga)
        print( f"Harga Menu \t: Rp. {FormatHarga}" )
        print()
        Quantity = int(input("Quantity \t: "))

        if ( Quantity == 0 ) :
            return "Tidak Jadi Beli"
        else :
            return PembelianKonsumsi( self.Type, self.Menu[ index ].NamaMenu, self.Menu[index].Harga, Quantity  )
        




class Menu :
    def __init__(self, NamaMenu, Harga) :
        self.NamaMenu = NamaMenu
        self.Harga = Harga

    def CetakMenu(self, Count) :
        CharCount = "." * ( 35 - len( self.NamaMenu ) - len(Count) )
        FormatHarga = "{:,.2f}".format(self.Harga)
        print( f"A{Count}. {self.NamaMenu} {CharCount}..... Rp. {FormatHarga}" )

    def EditMenu(self, Type) :
        os.system("cls")
        print( f"Edit Menu {Type}\n" )
        print( f"Data {Type}" )
        print( f"Nama {Type} \t: {self.NamaMenu}" )

        FormatHarga = "{:,.2f}".format(self.Harga)

        print( f"Harga {Type} \t: Rp. {FormatHarga}" )
        print()
        print( "Pengeditan Data" )
        try :
            NamaMenu = str(input( f"Nama {Type} \t: " ))
            if ( len (NamaMenu) > 30 ) :
                raise Exception( f"Jumlah karakter untuk Nama {Type} tidak boleh lebih besar dari 30.")
            Harga = int(input( f"Harga {Type} \t: Rp. " ))
            if ( Harga <= 0 ) :
                raise Exception( f"Harga harus bernilai lebih besar dari 0.")

            self.NamaMenu = NamaMenu
            self.Harga = Harga

            print("\nEdit Menu berhasil dilakukan.")

        except ValueError :
            print( "\n! Input harga harus berupa angka." )
        except Exception as e :
            print( "\n! ", end="" )
            print( str(e) )










class MenuBersizeInterface ( SyaratMenu ) :
    Type = ""
    Menu = []
    def __init__(self, Type) :
        self.Type = Type
        self.Menu = []

    def RunInterface (self) :
        while( True ) :
            os.system("cls")
            title = f'Data {self.Type} Bersize : '
            options = [ "1. Cetak Semua Menu", "2. Input Menu Baru", "3. Input Size baru untuk Menu tertentu", "4. Edit Nama Menu", "5. Edit Data Size Tertentu", "6. Delete Menu", "7. Delete Size Menu Tertentu", "8. Naikan Harga Semua Menu", "0. Back" ]
            option, index = pick(options, title, "->")

            os.system("cls")

            if ( option == "1. Cetak Semua Menu" ) :
                print(f"Data Semua {self.Type} Bersize :\n")
                self.TampilinSemuaMenu()
            elif ( option == "2. Input Menu Baru" ) :
                self.InputMenuBaru()
            elif( option == "3. Input Size baru untuk Menu tertentu" ) :
                self.InputSizeBaru()
            elif ( option == "4. Edit Nama Menu" ) :
                self.EditNamaMenu()
            elif ( option == "5. Edit Data Size Tertentu" ) :
                self.EditSize()
            elif ( option == "6. Delete Menu" ) :
                self.DeleteMenu()
            elif ( option == "7. Delete Size Menu Tertentu" ) :
                self.DeleteSizeTertentu()
            elif ( option == "8. Naikan Harga Semua Menu" ) :
                self.NaikanHargaSemuaMenu()
            elif ( option == "0. Back" ) :
                break

            input("\nTekan Enter untuk melanjutkan ...")

    def TampilinSemuaMenu(self) :
        Count = 1
        for Menu in self.Menu :
            Count = Menu.CetakMenu( Count )

    def InputMenuBaru (self) :
        try :
            print(f"Input Menu {self.Type} Bersize")
            print()
            NamaMenu = str( input(f"Nama {self.Type} \t: ") )
            # Mengecek apakah sudah ada nama menu yang sama di array Menu
            if ( NamaMenu in [ Object.NamaMenu for Object in self.Menu ] ) :
                raise Exception( f"Menu {NamaMenu} sudah pernah diregister.")
            if ( len (NamaMenu) > 30 ) :
                raise Exception( f"Jumlah karakter untuk Nama {self.Type} tidak boleh lebih besar dari 30.")
            MenuBaru = HeaderMenuBersize(NamaMenu)
            MenuBaru.InputSize()
            self.Menu.append( MenuBaru )
            self.Menu.sort(key=lambda x: x.NamaMenu)

        except Exception as e :
            print( "\n! ", end="" )
            print( str(e) )

    def InputSizeBaru (self) :
        print(f"Data Semua {self.Type} Bersize :\n")
        Count = 1
        for Menu in self.Menu :
            Menu.CetakMenuPerKategori( Count )
            Count += 1
        print()
        Input = str(input(f"Input Size baru untuk Menu {self.Type} dengan kode : "))
        try :
            if ( Input[0] == "B" and 0 < int(Input[1::]) <= len(self.Menu) ) :
                index = int(Input[1::]) - 1
                self.Menu[ index ].InputSize()
            else :
                raise Exception
        except Exception:
            print( f"\n! Kode Menu {self.Type} : {Input} tidak tersedia" )

    def EditNamaMenu (self) :
        print(f"Data Semua {self.Type} Bersize :\n")
        Count = 1
        for Menu in self.Menu :
            Menu.CetakMenuPerKategori( Count )
            Count += 1
        print()
        Input = str(input(f"Edit Nama Menu {self.Type} dengan kode : "))
        try :
            if ( Input[0] == "B" and 0 < int(Input[1::]) <= len(self.Menu) ) :
                index = int(Input[1::]) - 1
                try :
                    os.system("cls")
                    print("Edit Nama Menu\n")
                    print(f"Nama Menu Lama \t: {self.Menu[ index ].NamaMenu}\n")
                    NamaMenuBaru = str(input("Nama Menu Baru \t: "))
                    if ( NamaMenuBaru in [ Object.NamaMenu for Object in self.Menu ] ) :
                        raise Exception( f"Menu {NamaMenuBaru} sudah pernah diregister.")
                    if ( len (NamaMenuBaru) > 30 ) :
                        raise Exception( f"Jumlah karakter untuk Nama {self.Type} tidak boleh lebih besar dari 30.")
                    self.Menu[ index ].NamaMenu = NamaMenuBaru
                    self.Menu.sort(key=lambda x: x.NamaMenu)
                    print("\nNama Menu berhasil diganti.")

                except Exception as e :
                    print( "\n! ", end="" )
                    print( str(e) )

            else :
                raise Exception
        except Exception:
            print( f"\n! Kode Menu {self.Type} : {Input} tidak tersedia" )

    def EditSize (self) :
        print(f"Data Semua {self.Type} Bersize :\n")
        Count = 1
        for Menu in self.Menu :
            Count = Menu.CetakMenu( Count )
        print()
        Input = str(input(f"Edit Menu {self.Type} dengan kode : "))
        try :
            if ( Input[0] == "B" and 0 < int(Input[1::]) <= Count-1 ) :
                Kode = int(Input[1::])
                BeforeIndex = 0
                AfterIndex = 0
                for item in self.Menu :
                    AfterIndex += len( item.MenuSize )
                    if ( BeforeIndex <= Kode <= AfterIndex ) :
                        SizeIndex = Kode - 1 - BeforeIndex
                        os.system("cls")
                        item.EditSize( SizeIndex )
                        break
                    else :
                        BeforeIndex = AfterIndex
            else :
                raise Exception
        except Exception:
            print( f"\n! Kode Menu {self.Type} : {Input} tidak tersedia" )

    def DeleteMenu(self) :
        print(f"Data Semua {self.Type} Bersize :\n")
        Count = 1
        for Menu in self.Menu :
            Menu.CetakMenuPerKategori( Count )
            Count += 1
        print()
        Input = str(input(f"Delete Menu {self.Type} dengan kode : "))
        try :
            if ( Input[0] == "B" and 0 < int(Input[1::]) <= len(self.Menu) ) :
                index = int(Input[1::]) - 1
                del self.Menu[ index ]
                print("\nDelete Menu berhasil dilakukan.")
            else :
                raise Exception
        except Exception:
            print( f"\n! Kode Menu {self.Type} : {Input} tidak tersedia" )

    def DeleteSizeTertentu(self) :
        print(f"Data Semua {self.Type} Bersize :\n")
        Count = 1
        for Menu in self.Menu :
            Count = Menu.CetakMenu( Count )
        print()
        Input = str(input(f"Edit Menu {self.Type} dengan kode : "))
        try :
            if ( Input[0] == "B" and 0 < int(Input[1::]) <= Count-1 ) :
                Kode = int(Input[1::])
                BeforeIndex = 0
                AfterIndex = 0
                for item in self.Menu :
                    AfterIndex += len( item.MenuSize )
                    if ( BeforeIndex <= Kode <= AfterIndex ) :
                        SizeIndex = Kode - 1 - BeforeIndex
                        del item.MenuSize[ SizeIndex ]
                        print("\nDelete Size Menu berhasil.")
                        break
                    else :
                        BeforeIndex = AfterIndex
            else :
                raise Exception
        except Exception:
            print( f"\n! Kode Menu {self.Type} : {Input} tidak tersedia" )

    def NaikanHargaSemuaMenu(self):
        print(f"Naikan Harga Semua Menu {self.Type}\n")
        try :
            KenaikanHarga = int(input( f"Kenaikan Harga {self.Type} \t: Rp. " ))
            if ( KenaikanHarga <= 0 ) :
                raise Exception( f"Kenaikan Harga harus bernilai lebih besar dari 0.")
            for item in self.Menu :
                item.NaikanHargaSemuaSize( KenaikanHarga )
            print(f"\nKenaikan Harga Semua Menu {self.Type} Bersize berhasil dilakukan.")
            
        except ValueError :
            print( "\n! Input harga harus berupa angka." )
        except Exception as e:
            print( "\n! ",end="" )
            print( str(e) )

    def CheckKode ( self, Kode ) :
        Count = 0
        for Menu in self.Menu :
            Count += len ( Menu.MenuSize )
        try :
            if ( Kode[0] == "B" and 0 < int(Kode[1::]) <= Count ) :
                return True
            else :
                return False
        except :
            return False

    def Pembelian(self, Kode) :
        Index = int(Kode[1::]) 
        BeforeIndex = 0
        AfterIndex = 0
        for Menu in self.Menu :
            AfterIndex += len( Menu.MenuSize )
            if ( BeforeIndex <= Index <= AfterIndex ) :
                SizeIndex = Index - 1 - BeforeIndex
                
                print( f"Pembelian Menu {self.Type}\n" )
                print( f"Nama Menu \t: { Menu.NamaMenu }" )
                print( f"Size \t\t: {Menu.MenuSize[ SizeIndex ].Size}" )
                FormatHarga = "{:,.2f}".format(Menu.MenuSize[ SizeIndex ].Harga)
                print( f"Harga Menu \t: Rp. {FormatHarga}" )
                print()
                Quantity = int(input("Quantity \t: "))

                if ( Quantity == 0 ) :
                    return "Tidak Jadi Beli"
                else :
                    FormatType = self.Type + " Bersize"
                    return PembelianKonsumsiBersize( FormatType, Menu.NamaMenu, Menu.MenuSize[ SizeIndex ].Size, Menu.MenuSize[ SizeIndex ].Harga, Quantity )
                
            else :
                BeforeIndex = AfterIndex





class HeaderMenuBersize :
    def __init__(self, NamaMenu):
        self.NamaMenu = NamaMenu
        self.MenuSize = []

    def CetakMenu(self, Count) :
        if ( len (self.MenuSize) > 0 ) :
            print(self.NamaMenu)
            for i in range ( len(self.MenuSize) ) :
                FormatNamaMenu = f"({self.MenuSize[i].Size})"
                FormatHargaArr = "{:,.2f}".format( self.MenuSize[i].Harga )
                CharCount = "." * ( 27 - len( FormatNamaMenu ) - len( str(Count) ) )
                print( f"        B{Count}. {FormatNamaMenu} {CharCount}..... Rp. {FormatHargaArr}" )
                Count += 1
        return Count

    def CetakMenuPerKategori(self, Count) :
        print(f"B{Count}. {self.NamaMenu}")
        for i in range ( len(self.MenuSize) ) :
            FormatNamaMenu = f"({self.MenuSize[i].Size})"
            FormatHargaArr = "{:,.2f}".format( self.MenuSize[i].Harga )
            CharCount = "." * ( 30 - len( FormatNamaMenu ) - len( str(Count) ) )
            print( f"         {FormatNamaMenu} {CharCount}..... Rp. {FormatHargaArr}" )

    def InputSize(self) :
        while( True ) :
            os.system("cls")
            if ( len(self.MenuSize) == 0 ) :
                pass
            elif ( len(self.MenuSize) > 0 ) :
                print(f"Size lain untuk Menu ", end="")
                self.CetakMenu(1)
                print()

            print( f"Input Size Menu {self.NamaMenu}\n")
            print("! Masukkan perintah /STOP pada inputan Size Menu untuk menghentikan input size baru.\n")

            try :
                Size = str(input("Size Menu \t: "))

                if ( Size in [ Object.Size for Object in self.MenuSize ] ) :
                    raise Exception( f"Size {Size} untuk menu {self.NamaMenu} sudah pernah diregister.")
                if ( len(Size) >= 15 ) :
                    raise Exception( "Size tidak boleh lebih besar dari 15 Karakter.")
                if ( Size == "/STOP" ) :
                    print("\nInput berhasil diberhentikan.")
                    break

                Harga = int(input("Harga Menu \t: Rp. "))
                if ( Harga <= 0 ) :
                    raise Exception( f"Harga harus bernilai lebih besar dari 0.")

                self.MenuSize.append( SubMenuBersize(Size, Harga) )
                self.MenuSize.sort(key=lambda x: x.Harga)

                print("\nInput Size baru berhasil dilakukan.")
                input("\nTekan Enter untuk melanjutkan ...")

            except ValueError :
                print( "\n! Input harga harus berupa angka." )
                input("\nTekan Enter untuk melanjutkan ...")
            except Exception as e :
                print( "\n! ", end="" )
                print( str(e) )
                input("\nTekan Enter untuk melanjutkan ...")
        
    def EditSize(self, SizeIndex) :

        print( f"Edit Size Menu {self.NamaMenu}\n" )
        print( f"Size Lama \t: {self.MenuSize[ SizeIndex ].Size}" )
        FormatHarga = "{:,.2f}".format( self.MenuSize[ SizeIndex ].Harga )
        print( f"Harga Lama \t: {FormatHarga}\n" )
        try :
            Size = str(input("Size Baru \t: "))

            if ( Size in [ Object.Size for Object in self.MenuSize ] and Size != self.MenuSize[ SizeIndex ].Size ) :
                raise Exception( f"Size {Size} untuk menu {self.NamaMenu} sudah pernah diregister.")
            if ( len(Size) >= 15 ) :
                raise Exception( "Size tidak boleh lebih besar dari 15 Karakter.")

            Harga = int(input("Harga Menu \t: Rp. "))
            if ( Harga <= 0 ) :
                raise Exception( f"Harga harus bernilai lebih besar dari 0.")

            self.MenuSize[ SizeIndex ].Size = Size 
            self.MenuSize[ SizeIndex ].Harga = Harga
            self.MenuSize.sort(key=lambda x: x.Harga)

            print(f"\nPengeditan Size Menu {self.NamaMenu} berhasil dilakukan.")

        except ValueError :
            print( "\n! Input harga harus berupa angka." )
        except Exception as e :
            print( "\n! ", end="" )
            print( str(e) )

    def NaikanHargaSemuaSize(self, KenaikanHarga):
        for Size in self.MenuSize :
            Size.Harga += KenaikanHarga
        
        



class SubMenuBersize :
    def __init__(self, Size, Harga):
        self.Size = Size
        self.Harga = Harga










class InterfaceMovie :
    def __init__(self, Type, Kode) :
        self.JenisMovie = Type
        self.Kode = Kode
        self.MovieList = []
        self.SoldOutMovieList = []

    def RunInterface(self) :
        while ( True ) :
            os.system("cls")

            title = f'Data {self.JenisMovie} Movie : '
            options = [ "1. Cetak Semua Film", "2. Cetak Sold Out Movie", "3. Input Film Baru", "0. Back" ]
            option, index = pick(options, title, "->")
            os.system("cls")

            if ( option == "1. Cetak Semua Film" ) :
                self.CetakInfoMovie()
            elif ( option == "2. Cetak Sold Out Movie" ) :
                self.CetakSoldOutMovie()
            elif ( option == "3. Input Film Baru" ) :
                self.InputMovie()
            elif ( option == "0. Back" ) :
                break

            input("\nTekan Enter untuk melanjutkan ...")

    def CetakInfoMovie (self) :
        print(f"Movie {self.JenisMovie} : \n")
        Count = 1
        for Movie in self.MovieList :
            Movie.CetakInfoMovie( Count, self.Kode )
            print()
            Count += 1

    def CetakSoldOutMovie(self) :
        if ( len(self.SoldOutMovieList) == 0 ) :
            print(f"Tidak ada Movie {self.JenisMovie} yang Sold Out.")
        else :
            Count = 1
            print("Sold Out Movie\n")
            for Movie in self.SoldOutMovieList :
                Movie.CetakInfoMovie( Count, self.Kode )
                print()
                Count += 1

    def InputMovie (self) :
        print(f"Input Movie {self.JenisMovie} Baru\n")
        Judul = str( input("Judul \t\t: ") )
        index = 1
        Genre = []
        print("\n! Input /STOP untuk menghentikan input genre.")
        while( True ) :

            InputGenre = str( input(f"Genre {index} \t: ") )
            if ( InputGenre == "/STOP" ) :
                break
            else :
                Genre.append(InputGenre)
            index += 1

        Genre.sort()

        FormatGenre = ", ".join(Genre)
        os.system("cls")

        title = f'Input Movie {self.JenisMovie} Baru\n\nJudul \t\t: {Judul}\nGenre \t\t: {FormatGenre}\nStudio \t: '
        options = ['1 - VIP', '2 - VIP', '3 - JUNIOR', '4 - JUNIOR', '5 - REGULER', '6 - REGULER', '7 - REGULER']
        option, index = pick(options, title, "=>")

        StudioArr = option.split(" - ")
        Studio = int(StudioArr[0])
        Tipe_Studio = StudioArr[1]

        while (True) :
            os.system("cls")
            print(f"Input Movie {self.JenisMovie} Baru\n\nJudul \t\t: {Judul}\nGenre \t\t: {FormatGenre}\nStudio \t\t: {option}\n")
            try :
                print("Contoh Format input jadwal \t : 01-10-2003 12:30")
                InputJadwal = str( input("Jadwal (DD-MM-YYYY Hour:Minutes) : ") )
                Day = int( InputJadwal[0:2] )
                Month = int( InputJadwal[3:5] )
                Year = int( InputJadwal[6:10] )
                Hour = int( InputJadwal[11:13] )
                Minutes = int( InputJadwal[14:16] )
                Jadwal = datetime( Year, Month, Day, Hour, Minutes, 0 )
                break
            except ValueError:
                print("\n! Format Input Jadwal Movie salah.")
                input("\nTekan Enter untuk melanjutkan ...")

        objekMovieBaru = Movie( Judul, Genre, Jadwal, Studio, Tipe_Studio )

        if( [ objekMovieBaru.Judul, objekMovieBaru.Jadwal, objekMovieBaru.Studio ] in [ [ MovieList.Judul, MovieList.Jadwal, MovieList.Studio ] for MovieList in self.MovieList ] ) :
            print( "\n! Ditemukan Movie dengan Judul, Studio dan Jadwal Penayangan yang sama." )
        else :
            self.MovieList.append( objekMovieBaru )
            self.MovieList.sort( key=lambda x: x.Jadwal )
            print("\nMovie Baru berhasil ditambahkan.")

    def PembelianTiket (self, Kode) :
        
        index = int(Kode[1::]) - 1
        MovieTemp = self.MovieList[ index ]
        MovieTemp.PembelianTmptDuduk()


        # Setiap kursi dibeli, maka akan dicek apakah studio sudah full/ tiketnya sudah sold out.
        TempCekSoldOut = [ True ] * len(MovieTemp.ListTmptDuduk)
        if( MovieTemp.ListTmptDuduk == TempCekSoldOut ) :
            SoldOutMovie = self.MovieList.pop( index )
            self.SoldOutMovieList.append( SoldOutMovie )
            self.SoldOutMovieList.sort( key=lambda x: x.Jadwal )


        Arr = []
        for SeatNumber in MovieTemp.DapatkanTiketYgDibeli() :
            FormatType = "Tiket " + str(MovieTemp.Tipe_Studio)
            Arr.append( PembelianTiket(MovieTemp.Judul, FormatType, SeatNumber, MovieTemp.Jadwal, MovieTemp.Studio, MovieTemp.Tipe_Studio, MovieTemp.Harga) )

        return Arr

    def CheckKode (self, Kode) :
        if ( Kode[0] == self.Kode and 0 < int(Kode[1::]) <= len(self.MovieList) ) :
            return True
        else :
            return False
        




class Movie :
    def __init__(self, Judul, Genre, Jadwal, Studio, Tipe_Studio) :
        self.Judul = Judul
        self.Genre = Genre
        self.Jadwal = Jadwal
        self.Studio = Studio
        self.Tipe_Studio = Tipe_Studio
        self.TiketPembelian = []

    @property
    def Tipe_Studio(self) :
        return self._Tipe_Studio
    
    @Tipe_Studio.setter
    def Tipe_Studio(self, param) :
        self._Tipe_Studio = param
        if ( param == "REGULER" ) :
            self.Harga = 40000
            self.ListTmptDuduk = [ False ] * 40
        elif ( param == "JUNIOR" ) :
            self.Harga = 50000
            self.ListTmptDuduk = [ False ] * 30
        elif ( param == "VIP" ) :
            self.Harga = 100000
            self.ListTmptDuduk = [ False ] * 20

    def CetakInfoMovie(self, Count, Kode) :
        print( f"{Kode}{Count}. {self.Judul}" )
        Spasing = " " * len( str(Count) )
        FormatGenre = ", ".join( self.Genre )
        print( f"{Spasing}   Genre \t: {FormatGenre}" )
        FormatJadwal = self.Jadwal.strftime("%A, %d-%m-%Y %H:%M")
        print( f"{Spasing}   Jadwal \t: {FormatJadwal} \t\t\t Studio : {self.Studio}" )
        FormatHarga = "{:,.2f}".format(self.Harga)
        print( f"{Spasing}   Harga \t: Rp. {FormatHarga} \t\t\t\t {self.Tipe_Studio}" ) 

    def PembelianTmptDuduk(self) :

        ListSeatNumber = [ "A1", "A2", "A3", "A4", "A5", "B1", "B2", "B3", "B4", "B5", "C1", "C2", "C3", "C4", "C5", "D1", "D2", "D3", "D4", "D5", "E1", "E2", "E3", "E4", "E5", "F1", "F2", "F3", "F4", "F5", "G1", "G2", "G3", "G4", "G5", "H1", "H2", "H3", "H4", "H5" ]
        Temp = []
        self.TiketPembelian = []

        # Buat jendela utama
        app = QApplication(sys.argv)
        window = QMainWindow()
        window.setWindowTitle(f"{self.Judul} - Studio {self.Studio} - {self.Tipe_Studio}")

        # Buat layout untuk menampilkan kursi
        layout = QGridLayout()
        layout.setSpacing(0)
        
        # Buat gambar layar bioskop
        screen = QLabel()
        screen.setPixmap(QPixmap("screen.jpg"))  # Sesuaikan dengan nama file gambar layar bioskop yang Anda miliki

        # Buat tombol untuk masing-masing kursi dengan loop
        index1 = 0
        for row in range( len( self.ListTmptDuduk ) // 5 ):
            for col in range(5):
                seat_number = ListSeatNumber[index1]
                seat = QPushButton(seat_number)
                seat.setFixedSize(100, 50)
                if ( self.ListTmptDuduk[index1] == True ) :
                    seat.setEnabled(False)
                    seat.setStyleSheet("background-color: #EFF5F5")
                else :
                    seat.setStyleSheet("background-color: #B9E0FF")
                # seat.setStyleSheet("background-color: green")  # Set warna hijau untuk tombol yang belum terisi
                layout.addWidget(seat, row, col)
                index1 += 1

        # Buat fungsi yang akan dipanggil saat tombol diklik
        def button_clicked(param):
            indexTmptDuduk = ListSeatNumber.index( param.text() )
            if ( self.ListTmptDuduk[ indexTmptDuduk ] == True ) :
                Temp.remove( param.text() )
                param.setStyleSheet("background-color: #B9E0FF")
                self.ListTmptDuduk[ indexTmptDuduk ] = False
            elif ( self.ListTmptDuduk[ indexTmptDuduk ] == False ) :
                Temp.append( param.text() )
                param.setStyleSheet("background-color: #BCEAD5")
                self.ListTmptDuduk[ indexTmptDuduk ] = True

        # Tugas tombol ke fungsi button_clicked dengan loop
        index2 = 10
        for row in range( len(self.ListTmptDuduk)//5 ):
            for col in range(5):
                seat = layout.itemAtPosition(row, col).widget()
                seat.clicked.connect(lambda checked, seat=seat: button_clicked(seat) )
                index2 += 1

        # OK / SUBMIT button dan onclick function
        seat = QPushButton(f"OK")
        seat.setFixedHeight(50)
        seat.setStyleSheet("color: red")
        layout.addWidget(seat, len(self.ListTmptDuduk)//5 ,1,1,3)

        seat = layout.itemAtPosition(len(self.ListTmptDuduk)//5, 1).widget()
        seat.clicked.connect(lambda checked, seat=seat: Close())
                

        def Close():
            self.TiketPembelian = Temp
            QApplication.quit()
            
        main_layout = QVBoxLayout()

        # Buat gambar layar bioskop
        screen = QLabel()
        screen.setPixmap(QPixmap("screen.jpg"))  # Sesuaikan dengan nama file gambar layar bioskop yang Anda miliki
        # Buat layout vertikal untuk menampilkan layar dan layout kursi
        main_layout = QVBoxLayout()
        main_layout.addWidget(screen)
        main_layout.addLayout(layout)

        # Buat widget untuk menampilkan layout di jendela utama
        widget = QWidget()
        widget.setLayout(main_layout)

        # Tampilkan widget di jendela utama
        window.setCentralWidget(widget)
        window.show()

        # sys.exit(app.exec_())
        app.exec_()

    def DapatkanTiketYgDibeli(self) :
        return self.TiketPembelian











class Pembelian :
    def __init__( self ) :
        self.DataMakanan = []
        self.DataMinuman = []
        self.DataMakananBersize = []
        self.DataMinumanBersize = []
        self.DataTiketReguler = []
        self.DataTiketJunior = []
        self.DataTiketVIP = []

    def AddData(self, Objek) :
        if ( Objek.Type == "Makanan" ) :
            self.DataMakanan.append( Objek )
            self.DataMakanan.sort(key=lambda x: x.Nama)

        elif ( Objek.Type == "Minuman" ) :
            self.DataMinuman.append( Objek )
            self.DataMinuman.sort(key=lambda x: x.Nama)

        elif ( Objek.Type == "Makanan Bersize" ) :
            self.DataMakananBersize.append( Objek )
            self.DataMakananBersize.sort(key=lambda x: x.Nama)
        elif ( Objek.Type == "Minuman Bersize" ) :
            self.DataMinumanBersize.append( Objek )
            self.DataMinumanBersize.sort(key=lambda x: x.Nama)

        elif ( Objek.Type == "Tiket REGULER" ) :
            self.DataTiketReguler.append( Objek )
            self.DataTiketReguler.sort(key=lambda x: x.Jadwal)
        
        elif ( Objek.Type == "Tiket JUNIOR" ) :
            self.DataTiketJunior.append( Objek )
            self.DataTiketJunior.sort(key=lambda x: x.Jadwal)

        elif ( Objek.Type == "Tiket VIP" ) :
            self.DataTiketVIP.append( Objek )
            self.DataTiketVIP.sort(key=lambda x: x.Jadwal)

    def CheckBeli(self) :
        if ( len(self.DataMakanan) > 0 or len(self.DataMakananBersize) > 0 or len(self.DataMinuman) > 0 or len(self.DataMinumanBersize) > 0 or len(self.DataTiketReguler) > 0 or len(self.DataTiketJunior) > 0 or len(self.DataTiketVIP) > 0 ) :
            return True
        else :
            return False
            
    def RunInterface(self) :
        
        if ( len(self.DataMakanan) > 0 or len(self.DataMakananBersize) > 0 or len(self.DataMinuman) > 0 or len(self.DataMinumanBersize) > 0 ) :
            self.CetakStrukKonsumsi()

        if ( len(self.DataTiketReguler) > 0 or len(self.DataTiketJunior) > 0 or len(self.DataTiketVIP) > 0 ) :
            self.CetakStrukMovie()
            self.CetakTiket()   

    def CetakStrukKonsumsi(self) :

        SubTotal = 0

        os.system("cls")
        print()
        print("Cinema Mikroskil Medan".center(40) )
        print("Jln Mikroskil No. 777 Medan".center(40))
        print()
        print("="*40)
        print()

        for item1 in self.DataMakanan :
            item1.CetakStruk()
            SubTotal += item1.ReturnSubtotal()

        for item2 in self.DataMakananBersize :
            item2.CetakStruk()
            SubTotal += item2.ReturnSubtotal()

        for item3 in self.DataMinuman :
            item3.CetakStruk()
            SubTotal += item3.ReturnSubtotal()

        for item4 in self.DataMinumanBersize :
            item4.CetakStruk()
            SubTotal += item4.ReturnSubtotal()

        print("=" * 40)

        FormatSubtotal = "{:,}".format(SubTotal).replace(",", ".")
        Spasing1 = " " * ( 40 - 8 - len(FormatSubtotal) )
        print(f"Subtotal{Spasing1}{FormatSubtotal}")

        Pajak = int(0.1 * SubTotal)
        FormatPajak = "{:,}".format(Pajak).replace(",", ".")
        Spasing2 = " " * ( 40 - 14 - len(FormatPajak) )
        print(f"Service Charge{Spasing2}{FormatPajak}")

        Total = SubTotal + Pajak
        FormatTotal = "{:,}".format(Total).replace(",", ".")
        Spasing3 = " " * ( 40 - 5 - len(FormatTotal) )
        print(f"TOTAL{Spasing3}{FormatTotal}")
        print("\n\n")
        input("\nTekan Enter untuk melanjutkan ...")

    def CetakStrukMovie (self) :
        Total = 0
        
        os.system("cls")
        print()
        print("Cinema Mikroskil Medan".center(40) )
        print("Jln Mikroskil No. 777 Medan".center(40))
        print()
        print("="*40)
        print()

        if ( len(self.DataTiketReguler) > 0 ) :
            Harga1 = self.DataTiketReguler[0].Harga
            Quantity1 = len( self.DataTiketReguler )
            Total1 = Quantity1 * Harga1
            FormatTotal1 = "{:,}".format(Total1).replace(",", ".")
            FormatHarga1 = "{:,}".format(Harga1).replace(",", ".")
            Spasing1 = " " * ( 40 - 13 - len(FormatTotal1) )
            print(f"Tiket REGULER{Spasing1}{FormatTotal1}")
            print(f" {Quantity1} x {FormatHarga1}")
            print()
            Total += Total1

        if ( len(self.DataTiketJunior) > 0 ) :
            Harga2 = self.DataTiketJunior[0].Harga
            Quantity2 = len( self.DataTiketJunior )
            Total2 = Quantity2 * Harga2
            FormatTotal2 = "{:,}".format(Total2).replace(",", ".")
            FormatHarga2 = "{:,}".format(Harga2).replace(",", ".")
            Spasing2 = " " * ( 40 - 12 - len(FormatTotal2) )
            print(f"Tiket JUNIOR{Spasing2}{FormatTotal2}")
            print(f" {Quantity2} x {FormatHarga2}")
            print()
            Total += Total2

        if ( len(self.DataTiketVIP) > 0 ) :
            Harga3 = self.DataTiketVIP[0].Harga
            Quantity3 = len( self.DataTiketVIP )
            Total3 = Quantity3 * Harga3
            FormatTotal3 = "{:,}".format(Total3).replace(",", ".")
            FormatHarga3 = "{:,}".format(Harga3).replace(",", ".")
            Spasing3 = " " * ( 40 - 9 - len(FormatTotal3) )
            print(f"Tiket VIP{Spasing3}{FormatTotal3}")
            print(f" {Quantity3} x {FormatHarga3}")
            print()
            Total += Total3 

        print("=" * 40)
        print()
        FormatTotal = "{:,}".format(Total).replace(",", ".")
        SpasingTotal = " " * ( 40 - 5 - len(FormatTotal) )
        print(f"TOTAL{SpasingTotal}{FormatTotal}")
        print("\n\n")
        input("\nTekan Enter untuk melanjutkan ...")

    def CetakTiket (self) :
        os.system("cls")
        for Movie1 in self.DataTiketReguler :
            Movie1.CetakTiket()
        for Movie2 in self.DataTiketJunior :
            Movie2.CetakTiket()
        for Movie3 in self.DataTiketVIP :
            Movie3.CetakTiket()
        print("\n\n")
        input("\nTekan Enter untuk melanjutkan ...")



        

class PembelianKonsumsi :
    def __init__(self, Type, Nama, Harga, Quantity) :
        self.Type = Type
        self.Nama = Nama
        self.Harga = Harga
        self.Quantity = Quantity
    def CetakStruk (self) :
        TotalHarga = self.Harga * self.Quantity
        FormatHarga = "{:,}".format(TotalHarga).replace(",", ".")
        Spasing = " " * ( 40 - len(FormatHarga) - len(self.Nama) )
        print( f"{self.Nama}{Spasing}{FormatHarga}" )
        print( f" {self.Quantity} x {self.Harga}")
        print()
    def ReturnSubtotal (self) :
        return self.Harga * self.Quantity




class PembelianKonsumsiBersize ( PembelianKonsumsi ) :
    def __init__(self, Type, Nama, Size, Harga, Quantity):
        super().__init__(Type, Nama, Harga, Quantity)
        self.Size = Size
    def CetakStruk(self):
        FormatNama = f"{self.Nama} ({self.Size})"
        TotalHarga = self.Harga * self.Quantity
        FormatHarga = "{:,}".format(TotalHarga).replace(",", ".")
        Spasing = " " * ( 40 - len(FormatHarga) - len(FormatNama) )
        print( f"{FormatNama}{Spasing}{FormatHarga}" )
        print( f" {self.Quantity} x {self.Harga}")
        print()





class PembelianTiket :
    def __init__(self, Judul, Type, Seat, Jadwal, Studio, Tipe_Studio, Harga) :
        self.Judul = Judul
        self.Type = Type
        self.Harga = Harga
        self.Seat = Seat
        self.Jadwal = Jadwal
        self.Studio = Studio
        self.Tipe_Studio = Tipe_Studio
    def CetakTiket (self) :
        print("="*70)
        print()
        print((self.Type).center(70))
        print()
        print("Movie \t:", self.Judul)
        FormatStudio = str(self.Studio) + " - " + str(self.Tipe_Studio)
        print("Studio \t:", FormatStudio)
        print("Seat \t:", self.Seat)
        FormatJadwal = self.Jadwal.strftime("%A, %d-%m-%Y %H:%M")
        print("Jadwal \t:", FormatJadwal )
        print()
        print("=" * 70)







if __name__ == "__main__" :

    # Data Manager
    DataManager = Manager( "Arwin", "Arwin123" )
    Manager( "Charles", "Charles123" )
    Manager( "Darwin", "Darwin123" )
    Manager( "Kelvin", "Kelvin123" )





    # Data Staff
    DataStaff = Staff( "Cheris", "Cheris123" )
    Staff( "Nicholas", "Nicholas123" )
    Staff( "William", "William123" )
    Staff( "Wilsen", "Wilsen123" )





    # Data Makanan
    Makanan = Menuinterface("Makanan")
    Makanan.Menu = [
        Menu("Cheeseburger", 55000),
        Menu("Fish and Chips", 75000),
        Menu("French Fries", 40000),
        Menu("Hot Dog", 45000),
        Menu("Nachos", 65000),
        Menu("Sosis Bakar", 45000),
        Menu("Sosis Goreng", 45000),
        Menu("Pangsit Goreng", 40000),
        Menu("Pizza", 95000),
        Menu("Waffle", 30000)
        ]





    # Data Minuman
    Minuman = Menuinterface("Minuman")
    Minuman.Menu = [

        Menu("Ice Tea", 30000),
        Menu("Lemonade", 35000),
        Menu("Mango Juice", 40000),
        Menu("Milkshake Strawberry", 45000),
        Menu("Milkshake Chocolate", 50000),
        Menu("Smoothies", 40000),
        Menu("Soft Drink", 30000),
        Menu("Water", 20000)
    ]





    ## Data Makanan Bersize
    Cookies = HeaderMenuBersize("Cookies & Cream Popcorn")
    Popcorn1 = HeaderMenuBersize("Popcorn Butter")
    Popcorn2 = HeaderMenuBersize("Popcorn Cornell")
    Popcorn3 = HeaderMenuBersize("Popcorn Caramel")
    Popcorn4 = HeaderMenuBersize("Popcorn Mix")
    Popcorn5 = HeaderMenuBersize("Popcorn Salt")
    Popcorn6 = HeaderMenuBersize("Popcorn Sweet")

    Cookies.MenuSize = [ SubMenuBersize("S", 50000), SubMenuBersize("M",60000)]
    Popcorn1.MenuSize = [ SubMenuBersize("S", 40000), SubMenuBersize("M",50000), SubMenuBersize("L",60000) ]
    Popcorn2.MenuSize = [ SubMenuBersize("S", 45000), SubMenuBersize("M",55000), SubMenuBersize("L",65000) ]
    Popcorn3.MenuSize = [ SubMenuBersize("S", 29000), SubMenuBersize("M",34000), SubMenuBersize("L",39000) ]
    Popcorn4.MenuSize = [ SubMenuBersize("S", 40000), SubMenuBersize("M",50000), SubMenuBersize("L",60000) ]
    Popcorn5.MenuSize = [ SubMenuBersize("S", 45000), SubMenuBersize("M",55000), SubMenuBersize("L",65000) ]
    Popcorn6.MenuSize = [ SubMenuBersize("S", 42000), SubMenuBersize("M",54000), SubMenuBersize("L",59000) ]

    MakananBersize = MenuBersizeInterface("Makanan")
    MakananBersize.Menu = [ Cookies , Popcorn1, Popcorn2, Popcorn3, Popcorn4 ,Popcorn5, Popcorn6 ]





    # Data Minuman Bersize
    minuman1 = HeaderMenuBersize("Brown Sugar Milk Boba")
    minuman2 = HeaderMenuBersize("Es Kopi Susu Pandan")
    minuman3 = HeaderMenuBersize("Hot Java Tea")
    minuman4 = HeaderMenuBersize("Iced Mango Latte")
    minuman5 = HeaderMenuBersize("Iced Thai Tea")
    minuman6 = HeaderMenuBersize("Lychee Tea")
    minuman7 = HeaderMenuBersize("Taro Milk Tea")

    minuman1.MenuSize = [ SubMenuBersize("S", 49000), SubMenuBersize("M",57000), SubMenuBersize("L",63000) ]
    minuman2.MenuSize = [ SubMenuBersize("S", 21000), SubMenuBersize("M",28000), SubMenuBersize("L",32000) ]
    minuman3.MenuSize = [ SubMenuBersize("S", 18000), SubMenuBersize("M",25000), SubMenuBersize("L",28000) ]
    minuman4.MenuSize = [ SubMenuBersize("S", 24000), SubMenuBersize("M",28000), SubMenuBersize("L",32000) ]
    minuman5.MenuSize = [ SubMenuBersize("S", 21000), SubMenuBersize("M",28000), SubMenuBersize("L",32000) ]
    minuman6.MenuSize = [ SubMenuBersize("S", 23000), SubMenuBersize("M",30000), SubMenuBersize("L",34000) ]
    minuman7.MenuSize = [ SubMenuBersize("S", 38000), SubMenuBersize("M",36000), SubMenuBersize("L",42000) ]

    MinumanBersize = MenuBersizeInterface("Minuman")
    MinumanBersize.Menu = [ minuman1 , minuman2 , minuman3 , minuman4 , minuman5 , minuman6 , minuman7 ]





    # Data All Ages Movie
    # Format Datetime : datetime( Year, Month, Day, Hour, Minutes, Seconds ) 
    MovieA1 = Movie( "Kungfu Panda", ["Action", "Adventure", "Animation", "Comedy", "Martial Arts"], datetime( 2023, 1, 1, 12, 0, 0 ), 3, "JUNIOR" )
    MovieA2 = Movie( "Angry Birds", ["Action", "Adventure", "Animation", "Comedy"], datetime( 2023, 1, 1, 14, 0, 0 ), 5, "REGULER" )
    MovieA3 = Movie("One Piece Red", ["Action", "Advanture" ,"Animation" , "Comedy" , "Mystery"], datetime( 2023, 1, 1, 14, 0, 0 ), 6, "REGULER" )
    MovieA4 = Movie("Harry Potter and the Goblet of Fire", ["Adventure", "Fantasy", "Mystery"], datetime( 2023, 1, 1, 14, 0, 0 ), 7, "REGULER")
    MovieA5 = Movie("Tom & Jerry: The Movie", ["Animation", "Comedy"], datetime(2023, 1, 4, 14, 15, 0), 3, "JUNIOR")
    MovieA6 = Movie("The Lego Movie", ["Animation", "Comedy"], datetime(2023, 1, 5, 15, 30, 0), 4, "JUNIOR")
    MovieA7 = Movie("Moana", ["Animation", "Musical"], datetime(2023, 1, 6, 16, 45, 0), 4, "JUNIOR")
    MovieA8 = Movie("Zootopia", ["Animation", "Adventure"], datetime(2023, 1, 7, 18, 0, 0),5, "JUNIOR")

    AllAgesMovie = InterfaceMovie("All Ages Movie", "A")
    AllAgesMovie.MovieList = [ MovieA1, MovieA2, MovieA3, MovieA4, MovieA5, MovieA6, MovieA7, MovieA8 ]





    # Data Restricted Movie
    # Format Datetime : datetime( Year, Month, Day, Hour, Minutes, Seconds )
    MovieB0 = Movie("The Matrix", ["Action", "Sci-fi"] , datetime( 2023, 1, 1, 14, 0, 0 ), 7, "REGULER")
    MovieB1 = Movie("Interstellar", ["Adventure", "Drama", "Sci-fi"] , datetime( 2023, 1, 1, 12, 0, 0 ), 7, "REGULER")
    MovieB2 = Movie("Jurassic Park",  ["Adventure", "Sci-fi", "Thriller"] , datetime( 2023, 1, 1, 7, 0, 0 ), 7, "REGULER")
    MovieB3 = Movie("The Fifth Element", ["Action", "Adventure", "Sci-fi"] , datetime( 2023, 1, 1, 7, 0, 0 ), 6, "REGULER")
    MovieB4 = Movie("Indiana Jones 2", ["Action", "Adventure"] , datetime( 2023, 1, 1, 6, 0, 0 ), 8, "REGULER")
    MovieB5 = Movie("The Princess Bride", ["Adventure", "Comedy", "Fantasy"] , datetime( 2023, 1, 1, 14, 0, 0 ), 2, "VIP")
    MovieB6 = Movie("The Prestige", ["Drama", "Mystery", "Sci-fi"] , datetime( 2023, 1, 1, 14, 0, 0 ), 7, "REGULER")
    MovieB7 = Movie("Mad Max: Fury Road", ["Action", "Adventure", "Sci-fi"] , datetime( 2023, 1, 1, 16, 0, 0 ), 1, "VIP")
    MovieB8 = Movie("Dunkirk", ["Action", "Drama", "History"] , datetime( 2023, 1, 1, 11, 0, 0 ), 7, "REGULER")
    MovieB9 = Movie("The Revenant", ["Adventure", "Drama", "Thriller"] , datetime( 2023, 1, 1, 5, 0, 0 ), 7, "REGULER")

    RestrictedMovie = InterfaceMovie("Restricted Movie", "B")
    RestrictedMovie.MovieList = [ MovieB0, MovieB1, MovieB2, MovieB3, MovieB4, MovieB5, MovieB6, MovieB7, MovieB8, MovieB9 ] 





    ListDataPembelian = []




    # Main Program
    while( True ) :
        os.system("cls")
        print("Log In\n")
        Username = str(input("Username \t: "))
        Password = str(input("Password \t: "))
        print()

        if ( DataManager.isValid(Username, Password) ) :
            os.system("cls")
            while( True ) :
                title = 'Menu Manager : '
                options = ["1. Data Makanan", "2. Data Makanan Bersize", "3. Data Minuman", "4. Data Minuman Bersize", "5. Data All Ages Movie", "6. Data Restricted Movie", "0. Log Out"]
                option, index = pick(options, title, "->")
                if ( option == "1. Data Makanan" ) :
                    Makanan.RunInterface()
                elif ( option == "2. Data Makanan Bersize" ) :
                    MakananBersize.RunInterface()
                elif ( option == "3. Data Minuman" ) :
                    Minuman.RunInterface()
                elif ( option == "4. Data Minuman Bersize" ) :
                    MinumanBersize.RunInterface()
                elif ( option == "5. Data All Ages Movie" ) :
                    AllAgesMovie.RunInterface()
                elif ( option == "6. Data Restricted Movie" ) :
                    RestrictedMovie.RunInterface()
                elif ( option == "0. Log Out" ) :
                    break


        elif ( DataStaff.isValid(Username, Password) ) :
            DataPembelian = Pembelian()
            while( True ) :
                os.system("cls")
                title = "Penjualan : "
                options = ["1. Makanan", "2. Minuman", "3. Tiket Film", "4. Next Customer", "0. Log Out"]
                option, index = pick(options, title, "->")

                os.system("cls")
                if ( option == "1. Makanan" ) :
                    DataStaff.InterfaceMakanan()
                    
                elif ( option == "2. Minuman" ) :
                    DataStaff.InterfaceMinuman()

                elif ( option == "3. Tiket Film" ) :
                    DataStaff.InterfaceTiket()

                elif ( option == "4. Next Customer" ) :
                    if ( DataPembelian.CheckBeli() ) :
                        DataPembelian.RunInterface()
                        ListDataPembelian.append(DataPembelian)
                        DataPembelian = Pembelian()
                    else :
                        print("\nCustomer belum membeli apapun.")
                        input("\nTekan Enter untuk melanjutkan ...")

                elif ( option == "0. Log Out" ) :
                    break

                
        else :
            print("User tidak ditemukan !")
            input("\nTekan Enter untuk melanjutkan ...")

        





