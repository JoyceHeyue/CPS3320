from main import *
from normal import *
from package import *
from activity import *
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PIL import Image
from PyQt5.QtCore import *

class Ve_Main(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.main_ui = Ui_MainWindow()
        self.main_ui.setupUi(self)

        btn_del = self.main_ui.pushButton_5
        btn_del.clicked.connect(self.order_del)
        btn_num = self.main_ui.pushButton_6
        btn_num.clicked.connect(self.order_num)
        self.btn_tip = self.main_ui.pushButton_7
        self.btn_tip.clicked.connect(self.order_tip)
        self.btn_tip.setEnabled(False)
        self.num = []
        self.new_num = []

    def person(self):
        self.balance = 200
        self.coupons = 1
        self.main_ui.label_2.setText(str(self.balance))
        self.main_ui.label_5.setText(str(self.coupons))
        main.show()

    def order_del(self):
        row_index = main.main_ui.tableWidget.currentRow()
        if row_index != -1:
            main.main_ui.tableWidget.removeRow(row_index)

    def order_num(self):
        self.btn_tip.setEnabled(True)
        for row_index in range(main.main_ui.tableWidget.rowCount()):
            self.num.append(main.main_ui.tableWidget.item(row_index, 2).text())

        self.new_num = eval('[' + (','.join(self.num)) + ']')
        self.money = sum(self.new_num)

        if self.coupons >= 1:
            button = QMessageBox.information(self, "Tips", "Use coupons or not?", QMessageBox.Yes | QMessageBox.No)
            if button == QMessageBox.Yes:
                self.coupons = self.coupons -1
                self.main_ui.label_5.setText(str(self.coupons))

                if self.balance >= (self.money - self.coupons * 20):
                    QMessageBox.information(self, "Congratulation!", "Payment successfully!", QMessageBox.Yes)
                    self.balance = self.balance - self.money - self.coupons * 20
                    self.main_ui.label_2.setText(str(self.balance))
                else:
                    QMessageBox.information(self, "Sorry", "Your balance is insufficient!", QMessageBox.Yes)
            else:
                if self.balance >= self.money:
                    QMessageBox.information(self, "Congratulation!", "Payment successfully!", QMessageBox.Yes)
                    self.balance = self.balance - self.money
                    self.main_ui.label_2.setText(str(self.balance))
                else:
                    QMessageBox.information(self, "Sorry", "Your balance is insufficient!", QMessageBox.Yes)
        else:
            if self.balance >= self.money:
                QMessageBox.information(self, "Congratulation!", "Payment successfully!", QMessageBox.Yes)
                self.balance = self.balance - self.money
                self.main_ui.label_2.setText(str(self.balance))
            else:
                QMessageBox.information(self, "Sorry", "Your balance is insufficient!", QMessageBox.Yes)
    def order_tip(self):
        with open("kfctip.txt", "w") as f:
            for row_index in range(main.main_ui.tableWidget.rowCount()):
                for column_index in range(main.main_ui.tableWidget.columnCount()):
                    f.write(main.main_ui.tableWidget.item(row_index, column_index).text() + "\n")
            f.write("Sum: " + str(self.money) + "Dollars")
        f.close()

class Normal(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.normal_ui = Ui_Normal()
        self.normal_ui.setupUi(self)
        self.bt1 = 0
        self.bt2 = 0
        self.bt3 = 0
        self.bt4 = 0
        self.bt6 = 0
        self.bt5 = 0
        btn_spinach = self.normal_ui.pushButton
        btn_spinach.clicked.connect(self.order_spinach)
        btn_kale = self.normal_ui.pushButton_2
        btn_kale.clicked.connect(self.order_kale)
        btn_broccoli = self.normal_ui.pushButton_3
        btn_broccoli.clicked.connect(self.order_broccoli)
        btn_pea = self.normal_ui.pushButton_4
        btn_pea.clicked.connect(self.order_pea)
        btn_carrot = self.normal_ui.pushButton_6
        btn_carrot.clicked.connect(self.order_carrot)
        btn_return = self.normal_ui.pushButton_5
        btn_return.clicked.connect(self.nor_show)

    def nor_order(self):
        self.price_spinach = 3.5
        self.price_kale = 4.0
        self.price_broccoli = 2.8
        self.price_pea = 13.2
        self.price_carrot = 3.4
        self.normal_ui.label.setText(str(self.price_spinach)+"Dollars")
        self.normal_ui.label_4.setText(str(self.price_kale)+"Dollars")
        self.normal_ui.label_7.setText(str(self.price_broccoli)+"Dollars")
        self.normal_ui.label_10.setText(str(self.price_pea)+"Dollars")
        self.normal_ui.label_13.setText(str(self.price_carrot)+"Dollars")
        normal.show()

    def order_spinach(self):
        self.bt1 += 1

    def order_kale(self):
        self.bt2 += 1

    def order_broccoli(self):
        self.bt3 += 1

    def order_pea(self):
        self.bt4 += 1

    def order_carrot(self):
        self.bt6 += 1

    def nor_show(self):
        self.bt5 += 1

        
        normal.hide()

        self.num_spinach = self.price_spinach * self.bt1
        self.num_kale = self.price_kale * self.bt2
        self.num_broccoli = self.price_broccoli * self.bt3
        self.num_pea = self.price_pea * self.bt4
        self.num_carrot = self.price_carrot * self.bt6

        if self.bt5 > 1:
            for row_index in range(main.main_ui.tableWidget.rowCount()):
                name.append(main.main_ui.tableWidget.item(row_index, 0).text())
            if 'Spinach' in name:
                main.main_ui.tableWidget.setItem(name.index('Spinach'), 1, QTableWidgetItem("×" + str(self.bt1)))
                main.main_ui.tableWidget.setItem(name.index('Spinach'), 2, QTableWidgetItem(str(self.num_spinach)))
            if 'Spinach' not in name:
                if self.bt1 != 0:
                    row_count = main.main_ui.tableWidget.rowCount()
                    main.main_ui.tableWidget.insertRow(row_count)
                    main.main_ui.tableWidget.setItem(row_count, 0, QTableWidgetItem(normal.normal_ui.label_2.text()))
                    main.main_ui.tableWidget.setItem(row_count, 1, QTableWidgetItem("×" + str(self.bt1)))
                    main.main_ui.tableWidget.setItem(row_count, 2, QTableWidgetItem(str(self.num_spinach)))
            if 'Kale' in name:
                main.main_ui.tableWidget.setItem(name.index('Kale'), 1, QTableWidgetItem("×" + str(self.bt2)))
                main.main_ui.tableWidget.setItem(name.index('Kale'), 2, QTableWidgetItem(str(self.num_kale)))
            if 'Kale' not in name:
                if self.bt2 != 0:
                    row_count = main.main_ui.tableWidget.rowCount()
                    main.main_ui.tableWidget.insertRow(row_count)
                    main.main_ui.tableWidget.setItem(row_count, 0, QTableWidgetItem(normal.normal_ui.label_5.text()))
                    main.main_ui.tableWidget.setItem(row_count, 1, QTableWidgetItem("×" + str(self.bt2)))
                    main.main_ui.tableWidget.setItem(row_count, 2, QTableWidgetItem(str(self.num_kale)))
            if 'Broccoli' in name:
                main.main_ui.tableWidget.setItem(name.index('Broccoli'), 1, QTableWidgetItem("×" + str(self.bt3)))
                main.main_ui.tableWidget.setItem(name.index('Broccoli'), 2, QTableWidgetItem(str(self.num_broccoli)))
            if 'Broccoli' not in name:
                if self.bt3 != 0:
                    row_count = main.main_ui.tableWidget.rowCount()
                    main.main_ui.tableWidget.insertRow(row_count)
                    main.main_ui.tableWidget.setItem(row_count, 0, QTableWidgetItem(normal.normal_ui.label_8.text()))
                    main.main_ui.tableWidget.setItem(row_count, 1, QTableWidgetItem("×" + str(self.bt3)))
                    main.main_ui.tableWidget.setItem(row_count, 2, QTableWidgetItem(str(self.num_broccoli)))
            if 'Pea'in name:
                main.main_ui.tableWidget.setItem(name.index('Pea'), 1, QTableWidgetItem("×" + str(self.bt4)))
                main.main_ui.tableWidget.setItem(name.index('Pea'), 2, QTableWidgetItem(str(self.num_pea)))
            if 'Pea' not in name:
                if self.bt4 != 0:
                    row_count = main.main_ui.tableWidget.rowCount()
                    main.main_ui.tableWidget.insertRow(row_count)
                    main.main_ui.tableWidget.setItem(row_count, 0, QTableWidgetItem(normal.normal_ui.label_11.text()))
                    main.main_ui.tableWidget.setItem(row_count, 1, QTableWidgetItem("×" + str(self.bt4)))
                    main.main_ui.tableWidget.setItem(row_count, 2, QTableWidgetItem(str(self.num_pea)))
            if 'Carrot' in name:
                main.main_ui.tableWidget.setItem(name.index('Carrot'), 1, QTableWidgetItem("×" + str(self.bt6)))
                main.main_ui.tableWidget.setItem(name.index('Carrot'), 2, QTableWidgetItem(str(self.num_carrot)))
            if 'Carrot' not in name:
                if self.bt6 != 0:
                    row_count = main.main_ui.tableWidget.rowCount()
                    main.main_ui.tableWidget.insertRow(row_count)
                    main.main_ui.tableWidget.setItem(row_count, 0, QTableWidgetItem(normal.normal_ui.label_14.text()))
                    main.main_ui.tableWidget.setItem(row_count, 1, QTableWidgetItem("×" + str(self.bt6)))
                    main.main_ui.tableWidget.setItem(row_count, 2, QTableWidgetItem(str(self.num_carrot)))
        else:
            if self.bt1 != 0:
                row_count = main.main_ui.tableWidget.rowCount()
                main.main_ui.tableWidget.insertRow(row_count)
                main.main_ui.tableWidget.setItem(row_count, 0, QTableWidgetItem(normal.normal_ui.label_2.text()))
                main.main_ui.tableWidget.setItem(row_count, 1, QTableWidgetItem("×" + str(self.bt1)))
                main.main_ui.tableWidget.setItem(row_count, 2, QTableWidgetItem(str(self.num_spinach)))
            if self.bt2 != 0:
                row_count = main.main_ui.tableWidget.rowCount()
                main.main_ui.tableWidget.insertRow(row_count)
                main.main_ui.tableWidget.setItem(row_count, 0, QTableWidgetItem(normal.normal_ui.label_5.text()))
                main.main_ui.tableWidget.setItem(row_count, 1, QTableWidgetItem("×" + str(self.bt2)))
                main.main_ui.tableWidget.setItem(row_count, 2, QTableWidgetItem(str(self.num_kale)))
            if self.bt3 != 0:
                row_count = main.main_ui.tableWidget.rowCount()
                main.main_ui.tableWidget.insertRow(row_count)
                main.main_ui.tableWidget.setItem(row_count, 0, QTableWidgetItem(normal.normal_ui.label_8.text()))
                main.main_ui.tableWidget.setItem(row_count, 1, QTableWidgetItem("×" + str(self.bt3)))
                main.main_ui.tableWidget.setItem(row_count, 2, QTableWidgetItem(str(self.num_broccoli)))
            if self.bt4 != 0:
                row_count = main.main_ui.tableWidget.rowCount()
                main.main_ui.tableWidget.insertRow(row_count)
                main.main_ui.tableWidget.setItem(row_count, 0, QTableWidgetItem(normal.normal_ui.label_11.text()))
                main.main_ui.tableWidget.setItem(row_count, 1, QTableWidgetItem("×" + str(self.bt4)))
                main.main_ui.tableWidget.setItem(row_count, 2, QTableWidgetItem(str(self.num_pea)))
            if self.bt6 != 0:
                row_count = main.main_ui.tableWidget.rowCount()
                main.main_ui.tableWidget.insertRow(row_count)
                main.main_ui.tableWidget.setItem(row_count, 0, QTableWidgetItem(normal.normal_ui.label_14.text()))
                main.main_ui.tableWidget.setItem(row_count, 1, QTableWidgetItem("×" + str(self.bt6)))
                main.main_ui.tableWidget.setItem(row_count, 2, QTableWidgetItem(str(self.num_carrot)))

class Package(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.package_ui = Ui_Package()
        self.package_ui.setupUi(self)
        self.bt1 = 0
        self.bt2 = 0
        self.bt3 = 0
        btn_pack1 = self.package_ui.pushButton
        btn_pack1.clicked.connect(self.order_pack1)
        btn_pack2 = self.package_ui.pushButton_2
        btn_pack2.clicked.connect(self.order_pack2)
        btn_return = self.package_ui.pushButton_3
        btn_return.clicked.connect(self.pac_show)

    def pac_order(self):
        self.price_pack1 = 19.9
        self.price_pack2 = 28.8
        self.package_ui.label.setText(str(self.price_pack1)+"Dollars")
        self.package_ui.label_2.setText(str(self.price_pack2)+"Dollars")
        package.show()

    def order_pack1(self):
        self.bt1 += 1

    def order_pack2(self):
        self.bt2 += 1

    def pac_show(self):
        self.bt3 += 1

        package.hide()

        self.num_pack1 = self.price_pack1 * self.bt1
        self.num_pack2 = self.price_pack2 * self.bt2

        if self.bt3 > 1:
            for row_index in range(main.main_ui.tableWidget.rowCount()):
                name.append(main.main_ui.tableWidget.item(row_index, 0).text())
            if 'Vegetable Combo' in name:
                main.main_ui.tableWidget.setItem(name.index('Vegetable Combo'), 1, QTableWidgetItem("×" + str(self.bt1)))
                main.main_ui.tableWidget.setItem(name.index('Vegetable Combo'), 2, QTableWidgetItem(str(self.num_pack1)))
            if 'Vegetable Combo' not in name:
                if self.bt1 != 0:
                    row_count = main.main_ui.tableWidget.rowCount()
                    main.main_ui.tableWidget.insertRow(row_count)
                    main.main_ui.tableWidget.setItem(row_count, 0, QTableWidgetItem(package.package_ui.label_3.text()))
                    main.main_ui.tableWidget.setItem(row_count, 1, QTableWidgetItem("×" + str(self.bt1)))
                    main.main_ui.tableWidget.setItem(row_count, 2, QTableWidgetItem(str(self.num_pack1)))
            if 'Fruit Combo' in name:
                main.main_ui.tableWidget.setItem(name.index('Fruit Combo'), 1, QTableWidgetItem("×" + str(self.bt2)))
                main.main_ui.tableWidget.setItem(name.index('Fruit Combo'), 2, QTableWidgetItem(str(self.num_pack2)))
            if 'Fruit Combo' not in name:
                if self.bt2 != 0:
                    row_count = main.main_ui.tableWidget.rowCount()
                    main.main_ui.tableWidget.insertRow(row_count)
                    main.main_ui.tableWidget.setItem(row_count, 0, QTableWidgetItem(package.package_ui.label_4.text()))
                    main.main_ui.tableWidget.setItem(row_count, 1, QTableWidgetItem("×" + str(self.bt2)))
                    main.main_ui.tableWidget.setItem(row_count, 2, QTableWidgetItem(str(self.num_pack2)))
        else:
            if self.bt1 != 0:
                row_count = main.main_ui.tableWidget.rowCount()
                main.main_ui.tableWidget.insertRow(row_count)
                main.main_ui.tableWidget.setItem(row_count, 0, QTableWidgetItem(package.package_ui.label_3.text()))
                main.main_ui.tableWidget.setItem(row_count, 1, QTableWidgetItem("×" + str(self.bt1)))
                main.main_ui.tableWidget.setItem(row_count, 2, QTableWidgetItem(str(self.num_pack1)))
            if self.bt2 != 0:
                row_count = main.main_ui.tableWidget.rowCount()
                main.main_ui.tableWidget.insertRow(row_count)
                main.main_ui.tableWidget.setItem(row_count, 0, QTableWidgetItem(package.package_ui.label_4.text()))
                main.main_ui.tableWidget.setItem(row_count, 1, QTableWidgetItem("×" + str(self.bt2)))
                main.main_ui.tableWidget.setItem(row_count, 2, QTableWidgetItem(str(self.num_pack2)))

class Activity(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.activity_ui = Ui_Activity()
        self.activity_ui.setupUi(self)

        self.bt1 = 0
        self.bt3 = 0
        btn_act1 = self.activity_ui.pushButton
        btn_act1.clicked.connect(self.order_act1)
        btn_act2 = self.activity_ui.pushButton_2
        btn_act2.clicked.connect(self.order_act2)
        btn_return = self.activity_ui.pushButton_3
        btn_return.clicked.connect(self.act_show)

    def act_order(self):
        self.price_act1 = 4.99
        self.price_act2 = 3.99
        self.activity_ui.label.setText("$" + str(self.price_act1) + "  Original Price:"+ "$" + str(self.price_act1 + 7))
        self.activity_ui.label_5.setText("$" + str(self.price_act2) + "  Original Price:"+"$" +str(self.price_act2 + 10))
        activity.show()

    def order_act1(self):
        self.bt1 += 1

    def order_act2(self):
        QMessageBox.information(self, "Sorry", "The promotion is not open!", QMessageBox.Yes)

    def act_show(self):
        self.bt3 += 1

        activity.hide()

        self.num_act1 = self.price_act1 * self.bt1

        if self.bt3 > 1:
            for row_index in range(main.main_ui.tableWidget.rowCount()):
                name.append(main.main_ui.tableWidget.item(row_index, 0).text())
            if 'Five Tomatoes' in name:
                main.main_ui.tableWidget.setItem(name.index('Five Tomatoes'), 1, QTableWidgetItem("×" + str(self.bt1)))
                main.main_ui.tableWidget.setItem(name.index('Five Tomatoes'), 2, QTableWidgetItem(str(self.num_act1)))
            if 'Five Tomatoes' not in name:
                if self.bt1 != 0:
                    row_count = main.main_ui.tableWidget.rowCount()
                    main.main_ui.tableWidget.insertRow(row_count)
                    main.main_ui.tableWidget.setItem(row_count, 0, QTableWidgetItem(activity.activity_ui.label_3.text()))
                    main.main_ui.tableWidget.setItem(row_count, 1, QTableWidgetItem("×" + str(self.bt1)))
                    main.main_ui.tableWidget.setItem(row_count, 2, QTableWidgetItem(str(self.num_act1)))
        else:
            if self.bt1 != 0:
                row_count = main.main_ui.tableWidget.rowCount()
                main.main_ui.tableWidget.insertRow(row_count)
                main.main_ui.tableWidget.setItem(row_count, 0, QTableWidgetItem(activity.activity_ui.label_3.text()))
                main.main_ui.tableWidget.setItem(row_count, 1, QTableWidgetItem("×" + str(self.bt1)))
                main.main_ui.tableWidget.setItem(row_count, 2, QTableWidgetItem(str(self.num_act1)))

if __name__=="__main__":
    app = QApplication(sys.argv)

    main = Ve_Main()
    normal = Normal()
    package = Package()
    activity = Activity()
    main.person()
    btn_normal = main.main_ui.pushButton_2
    btn_normal.clicked.connect(normal.nor_order)
    btn_package = main.main_ui.pushButton_3
    btn_package.clicked.connect(package.pac_order)
    btn_activity = main.main_ui.pushButton_4
    btn_activity.clicked.connect(activity.act_order)
    name = []

    sys.exit(app.exec_())

