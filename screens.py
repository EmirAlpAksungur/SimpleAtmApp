import datetime
import tkinter
from tkinter import messagebox
from tkinter import *

import __main__

import pyodbc

import dbTransactions as Db


class loginScreen(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('200x120')
        self.protocol('WM_DELETE_WINDOW', self.cls)

        self.lblCardno = tkinter.Label(text="Card No :")
        self.lblCardno.grid(pady=4, row=0, sticky=W)

        self.txtCardNo = tkinter.Entry(bd=2)
        self.txtCardNo.grid(pady=4, row=0, column=1, sticky=E)

        self.lblPassword = tkinter.Label(text="Password :")
        self.lblPassword.grid(pady=10, row=1, sticky=W)

        self.txtPassword = tkinter.Entry(bd=2)
        self.txtPassword.grid(pady=10, row=1, column=1, sticky=E)

        self.btnLogin = tkinter.Button(text="Login", width=10, height=2, command=self.btnLogin)
        self.btnLogin.grid(row=2, column=1, sticky=E)

    def btnLogin(self):
        text = "SELECT [password] FROM [card] WHERE cardNo = "+self.txtCardNo.get()
        try:
            password = Db.returnSingleValue(text)
        except pyodbc.ProgrammingError:
            tkinter.messagebox.showerror("Warning", "Card number cannot be blank")
        except IndexError:
            tkinter.messagebox.showerror("Warning", "Card not found")
        else:
            if password == self.txtPassword.get():
                global instantCardNo
                instantCardNo = self.txtCardNo.get()
                self.destroy()
                __main__.setscreen(2)
            else:
                tkinter.messagebox.showerror("Warning", "Wrong password")

    def cls(self):
        msgbox = tkinter.messagebox.askquestion("askquestion", "Are you sure?")
        if msgbox == 'yes':
            self.destroy()
        else:
            pass


class userScreen(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('275x385')
        self.protocol('WM_DELETE_WINDOW', self.cls)

        self.btnWithdrawMoney = tkinter.Button(text="Withdraw money", font="Verdana 14", width=10, height=2,
                                               command=self.withdrawMoney)
        self.btnWithdrawMoney.pack(side=TOP, fill=X, ipadx=15, ipady=8)

        self.btnDepositeMoney = tkinter.Button(text="Deposite money", font="Verdana 14", width=10, height=2,
                                               command=self.depositeMoney)
        self.btnDepositeMoney.pack(side=TOP, fill=X, ipadx=15, ipady=8)

        self.btnChangePassword = tkinter.Button(text="Change password", font="Verdana 14", width=10, height=2,
                                                command=self.changePassword)
        self.btnChangePassword.pack(side=TOP, fill=X, ipadx=15, ipady=8)

        self.btnTransactionHistory = tkinter.Button(text="Transaction history", font="Verdana 14", width=10, height=2,
                                                    command=self.transactionHistory)
        self.btnTransactionHistory.pack(side=TOP, fill=X, ipadx=15, ipady=8)

        self.btnBack = tkinter.Button(text="Back", font="Verdana 14",  width=10, height=2, command=self.back)
        self.btnBack.pack(side=TOP, fill=X, ipadx=15, ipady=8)

    def cls(self):
        msgbox = tkinter.messagebox.askquestion("askquestion", "Are you sure?")
        if msgbox == 'yes':
            self.destroy()
        else:
            pass

    def withdrawMoney(self):
        self.destroy()
        __main__.setscreen(3)

    def depositeMoney(self):
        self.destroy()
        __main__.setscreen(4)

    def changePassword(self):
        self.destroy()
        __main__.setscreen(5)

    def transactionHistory(self):
        self.destroy()
        __main__.setscreen(6)

    def back(self):
        self.destroy()
        __main__.setscreen(1)


class withdrawMoneyScreen(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.protocol('WM_DELETE_WINDOW', self.cls)

        self.btnhundredCash = tkinter.Button(text="100", font="Verdana 14", width=10, height=2,
                                             command=lambda: self.withdrawMoney(100))
        self.btnhundredCash.pack(side=TOP, fill=X, ipadx=15, ipady=8)

        self.btntwohundredCash = tkinter.Button(text="200", font="Verdana 14", width=10, height=2,
                                                command=lambda: self.withdrawMoney(200))
        self.btntwohundredCash.pack(side=TOP, fill=X, ipadx=15, ipady=8)

        self.btnthreehundredCash = tkinter.Button(text="300", font="Verdana 14", width=10, height=2,
                                                  command=lambda: self.withdrawMoney(300))
        self.btnthreehundredCash.pack(side=TOP, fill=X, ipadx=15, ipady=8)

        self.btnfourhundredCash = tkinter.Button(text="400", font="Verdana 14", width=10, height=2,
                                                 command=lambda: self.withdrawMoney(400))
        self.btnfourhundredCash.pack(side=TOP, fill=X, ipadx=15, ipady=8)

        self.btnfivehundredCash = tkinter.Button(text="500", font="Verdana 14", width=10, height=2,
                                                 command=lambda: self.withdrawMoney(500))
        self.btnfivehundredCash.pack(side=TOP, fill=X, ipadx=15, ipady=8)

        self.btnanotheramount = tkinter.Button(text="Another amount", font="Verdana 14", width=10, height=2,
                                               command=self.anotherAmount)
        self.btnanotheramount.pack(side=TOP, fill=X, ipadx=15, ipady=8)

        self.btnBack = tkinter.Button(text="Back", font="Verdana 14", width=10, height=2, command=self.back)
        self.btnBack.pack(side=TOP, fill=X, ipadx=15, ipady=8)

    def cls(self):
        msgbox = tkinter.messagebox.askquestion("askquestion", "Are you sure?")
        if msgbox == 'yes':
            self.destroy()

    def anotherAmount(self):
        self.destroy()
        __main__.setscreen(7)

    def back(self):
        self.destroy()
        __main__.setscreen(2)

    def withdrawMoney(self, amount):
        text = "SELECT [money] FROM [card] WHERE cardNo = " + instantCardNo
        usermoney = Db.returnSingleValue(text)
        usercurrentmoney = int(usermoney) - amount
        text = "UPDATE [card] SET [money] = " + str(usercurrentmoney) + "WHERE cardNo = " + instantCardNo
        Db.addInfo(text)
        text = "SELECT MAX(transactionId) FROM pastTransactions"
        lastaddedtransaction = int(Db.returnSingleValue(text))
        text = "SELECT cardId FROM [card] WHERE cardNo = " + instantCardNo
        cardid = Db.returnSingleValue(text)
        date = datetime.datetime.now()
        year = date.year
        mount = date.month
        day = date.day
        text = "INSERT INTO pastTransactions (transactionId,cardId,[date],[description],amount)" \
               "VALUES ("+str(lastaddedtransaction+1)+","+str(cardid)+",'"+str(year)+"-"+str(mount)+"-"+str(day) +\
               "','Withdrawal made', -"+str(amount)+" )"
        Db.addInfo(text)
        tkinter.messagebox.showinfo("Info", "Transaction successful")


class anotherAmountScreen(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.protocol('WM_DELETE_WINDOW', self.cls)

        self.lblAmount = tkinter.Label(text="Amount :")
        self.lblAmount.grid(pady=4, row=0, sticky=W)

        self.txtAmount = tkinter.Entry(bd=2)
        self.txtAmount.grid(pady=4, row=0, column=1, sticky=E)

        self.btnback = tkinter.Button(text="Back", width=10, height=2, command=self.back)
        self.btnback.grid(row=2, column=0, sticky=E)

        self.btnamountConfirm = tkinter.Button(text="Confirm", width=10, height=2, command=self.amountConfirm)
        self.btnamountConfirm.grid(row=2, column=1, sticky=E)

    def cls(self):
        msgbox = tkinter.messagebox.askquestion("askquestion", "Are you sure?")
        if msgbox == 'yes':
            self.destroy()

    def back(self):
        self.destroy()
        __main__.setscreen(3)

    def amountConfirm(self):
        text = "SELECT [money] FROM [card] WHERE cardNo = " + instantCardNo
        usermoney = Db.returnSingleValue(text)
        try:
            usercurrentmoney = int(usermoney)-int(self.txtAmount.get())
            text = "UPDATE [card] SET [money] = " + str(usercurrentmoney) + "WHERE cardNo = " + instantCardNo
            Db.addInfo(text)
            text = "SELECT MAX(transactionId) FROM pastTransactions"
            lastaddedtransaction = int(Db.returnSingleValue(text))
            text = "SELECT cardId FROM [card] WHERE cardNo = " + instantCardNo
            cardid = Db.returnSingleValue(text)
            date = datetime.datetime.now()
            year = date.year
            mount = date.month
            day = date.day
            text = "INSERT INTO pastTransactions (transactionId,cardId,[date],[description],amount)" \
                   "VALUES (" + str(lastaddedtransaction + 1) + "," + str(cardid) + ",'" + str(year) + "-" + str(
                    mount) + "-" + str(day) + \
                   "','Withdrawal made', -" + str(self.txtAmount.get()) + " )"
            Db.addInfo(text)
            tkinter.messagebox.showinfo("Info", "Transaction successful")
        except ValueError:
            tkinter.messagebox.showinfo("Info", "Lütfen bir sayı giriniz.")


class depositeMoneyScreen(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.protocol('WM_DELETE_WINDOW', self.cls)

        self.lblAmount = tkinter.Label(text="Amount :")
        self.lblAmount.grid(pady=4, row=0, sticky=W)

        self.txtAmount = tkinter.Entry(bd=2)
        self.txtAmount.grid(pady=4, row=0, column=1, sticky=E)

        self.btnback = tkinter.Button(text="Back", width=10, height=2, command=self.back)
        self.btnback.grid(row=2, column=0, sticky=E)

        self.btnamountConfirm = tkinter.Button(text="Confirm", width=10, height=2, command=self.amountConfirm)
        self.btnamountConfirm.grid(row=2, column=1, sticky=E)

    def cls(self):
        msgbox = tkinter.messagebox.askquestion("askquestion", "Are you sure?")
        if msgbox == 'yes':
            self.destroy()

    def back(self):
        self.destroy()
        __main__.setscreen(2)

    def amountConfirm(self):
        try:
            text = "SELECT [money] FROM [card] WHERE cardNo = " + instantCardNo
            usermoney = Db.returnSingleValue(text)
            usercurrentmoney = int(usermoney) + int(self.txtAmount.get())
            text = "UPDATE [card] SET [money] = " + str(usercurrentmoney) + "WHERE cardNo = " + instantCardNo
            Db.addInfo(text)
            text = "SELECT MAX(transactionId) FROM pastTransactions"
            lastaddedtransaction = int(Db.returnSingleValue(text))
            text = "SELECT cardId FROM [card] WHERE cardNo = " + instantCardNo
            cardid = Db.returnSingleValue(text)
            date = datetime.datetime.now()
            year = date.year
            mount = date.month
            day = date.day
            text = "INSERT INTO pastTransactions (transactionId,cardId,[date],[description],amount)" \
                   "VALUES ("+str(lastaddedtransaction+1)+","+str(cardid)+",'"+str(year)+"-"+str(mount)+"-"+str(day) +\
                   "','The deposit has been made', "+str(self.txtAmount.get())+" )"
            Db.addInfo(text)
            tkinter.messagebox.showinfo("Info", "Transaction successful")
        except ValueError:
            tkinter.messagebox.showinfo("Info", "Lütfen bir sayı giriniz.")


class changePasswordScreen(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.protocol('WM_DELETE_WINDOW', self.cls)

        self.lblOldPassword = tkinter.Label(text="Old password :")
        self.lblOldPassword.grid(pady=4, row=0, sticky=W)

        self.txtOldPassword = tkinter.Entry(bd=2)
        self.txtOldPassword.grid(pady=4, row=0, column=1, sticky=E)

        self.lblNewPassword = tkinter.Label(text="New password :")
        self.lblNewPassword.grid(pady=4, row=1, sticky=W)

        self.txtNewPassword = tkinter.Entry(bd=2)
        self.txtNewPassword.grid(pady=4, row=1, column=1, sticky=E)

        self.btnback = tkinter.Button(text="Back", width=10, height=2, command=self.back)
        self.btnback.grid(row=2, column=0, sticky=E)

        self.btnamountConfirm = tkinter.Button(text="Confirm", width=10, height=2, command=self.confirm)
        self.btnamountConfirm.grid(row=2, column=1, sticky=E)

    def confirm(self):
        try:
            text = "SELECT [password] FROM [card] WHERE cardId =" + instantCardNo
            oldpassword = Db.returnSingleValue(text)
            if oldpassword == self.txtOldPassword.get():
                if 999 < int(self.txtNewPassword.get()) < 10000:
                    text = "UPDATE [card] SET [password] = " + self.txtNewPassword.get() +\
                           "WHERE cardId = " + instantCardNo
                    Db.addInfo(text)
                    tkinter.messagebox.showinfo("Info", "Your password has been successfully changed")
                else:
                    tkinter.messagebox.showerror("Warning", "Your password must be a 4 digit number")
            else:
                tkinter.messagebox.showerror("Warning", "Wrong old password")
        except ValueError:
            tkinter.messagebox.showinfo("Info", "Password must be a number")

    def back(self):
        self.destroy()
        __main__.setscreen(2)

    def cls(self):
        msgbox = tkinter.messagebox.askquestion("askquestion", "Are you sure?")
        if msgbox == 'yes':
            self.destroy()


class transactionHistoryScreen(tkinter.Tk):
    def __init__(self):
        super().__init__()

        self.protocol('WM_DELETE_WINDOW', self.cls)

        text = "SELECT [date],[description],amount FROM pastTransactions WHERE cardId = " + instantCardNo
        counter = 0
        for i in Db.returnLargeValue(text):
            b = tkinter.Label(self, text=i)
            b.grid(row=counter, columnspan=2)
            counter += 1

        self.btnback = tkinter.Button(text="Back", width=10, height=2, command=self.back)
        self.btnback.grid(row=(counter+1), column=0, sticky=W)

    def cls(self):
        msgbox = tkinter.messagebox.askquestion("askquestion", "Are you sure?")
        if msgbox == 'yes':
            self.destroy()

    def back(self):
        self.destroy()
        __main__.setscreen(2)

