import screens

if __name__ == '__main__':

    def setscreen(screencode):
        if screencode == 1:
            loginscreen = screens.loginScreen()
            loginscreen.mainloop()
        elif screencode == 2:
            userscreen = screens.userScreen()
            userscreen.mainloop()
        elif screencode == 3:
            withdrawmoneyscreen = screens.withdrawMoneyScreen()
            withdrawmoneyscreen.mainloop()
        elif screencode == 4:
            depositemoneyscreen = screens.depositeMoneyScreen()
            depositemoneyscreen.mainloop()
        elif screencode == 5:
            changepassword = screens.changePasswordScreen()
            changepassword.mainloop()
        elif screencode == 6:
            transactionhistory = screens.transactionHistoryScreen()
            transactionhistory.mainloop()
        elif screencode == 7:
            anotheramount = screens.anotherAmountScreen()
            anotheramount.mainloop()
    setscreen(1)
