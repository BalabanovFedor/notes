from PyQt5 import QtCore, QtGui

from design import Ui_MainWindow
from add_note import Ui_add_note
from del_note import Ui_Form
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QTableWidgetItem
import sys
import sqlite3


class Notes(QMainWindow, Ui_MainWindow):
    """класс главного окна, в котором происходит основная работа"""

    def __init__(self, db):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Notes")
        self.con = sqlite3.connect(db)
        self.initUI()

    def initUI(self):
        self.edit_flag = False
        self.table_init()
        self.print_notes('id > 0')
        self.plus_btn.clicked.connect(self.add_note)
        self.search_btn.clicked.connect(self.search)
        self.editmode_btn.clicked.connect(self.edit_mode)

    def edit_mode(self):
        """включение режима редактирования"""
        self.edit_flag = not self.edit_flag
        if self.edit_flag:
            self.editmode_btn.setStyleSheet("background-color: {}".format('#99ff99'))
            self.print_all_notes()

        else:
            self.editmode_btn.setStyleSheet("background-color: {}".format('white'))
            self.save_all()
            self.del_idcolumn()
            self.del_keyscolumn()
            self.print_all_notes()

    def save_all(self):
        """сохранение всех изменений в таблице"""
        for row in range(self.tableWidget.rowCount()):
            row_data = [self.tableWidget.item(row, i) for i in range(self.tableWidget.columnCount())]
            for i in range(len(row_data)):
                if row_data[i] is None:
                    row_data[i] = QTableWidgetItem('')
            row_data = list(map(lambda el: el.text(), row_data))
            t, c, dt, k = row_data[0], row_data[1], row_data[2], row_data[3]

            self.save_note(row_data[-1], title=t, comment=c, datetime=dt, keys=k)

    def save_note(self, id, title='', comment='', datetime='', keys=''):
        """сохранение одной заметки"""
        q1 = f"UPDATE notes SET title='{title}' WHERE id={id}"
        q2 = f"UPDATE notes SET comment='{comment}' WHERE id={id}"
        q3 = f"UPDATE notes SET datetime='{datetime}' WHERE id={id}"
        q4 = f"UPDATE notes SET keys='{keys}' WHERE id={id}"

        with self.con:
            cur = self.con.cursor()
            cur.execute(q1)
            cur.execute(q2)
            cur.execute(q3)
            cur.execute(q4)

    def table_init(self):
        """ инициализация таблицы """

        cur = self.con.execute('select * from notes')

        # titles = [description[0] for description in cur.description[1:-1]]
        titles = ['Заголовок', 'Заметка', 'Дата']
        self.tableWidget.setColumnCount(len(titles))
        self.tableWidget.setHorizontalHeaderLabels(titles)

        self.tableWidget.resizeColumnsToContents()

    def search(self):
        """ поиск заметок по словам """

        text = self.search_textedit.toPlainText().split()
        self.search_textedit.setPlainText('')
        cur = self.con.cursor()
        count_dict, fl = {}, True

        if text == []:
            self.print_all_notes()
            fl = False

        if fl:
            notes = list(cur.execute("SELECT id, title, comment, keys FROM notes WHERE id>0"))
            for note in notes:
                id, keys_ = note[0], note[1:]
                keys = []
                for s in keys_:
                    keys.extend(str(s).split())

                for sear_t in text:
                    for k in keys:
                        if sear_t.lower() in k.lower():
                            count_dict[id] = count_dict.get(id, 0) + 1

            self.clear_table()
            count_dict = dict(sorted(count_dict.items(), key=lambda x: x[1], reverse=True))
            q = list(map(lambda x: str(x), list(count_dict.keys())))
            if len(q) == 1:
                self.print_notes(f"id = {q[0]}")
            else:
                self.print_notes(f"id IN ({', '.join(q)})")

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Enter:
            self.search()

    def clear_table(self):
        """полная очистка таблицы(обнуление всех строк)"""
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(3)

    def print_all_notes(self):
        """печать всех заметок"""
        self.print_notes("id>0")

    def print_notes(self, *inquiry):
        """вывод заметок по запросу inquiry"""

        cur = self.con.cursor()
        self.clear_table()
        inquiry = ' AND '.join(inquiry)
        s = f"SELECT id FROM notes WHERE {inquiry}"

        IDs = list(map(lambda x: x[0], cur.execute(s)))
        self.ids_intable = IDs

        for row_numb, id in enumerate(IDs):
            row = cur.execute(f"SELECT * FROM notes WHERE id = {id}")
            row = list(*row)
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)

            for col_numb, elem in enumerate(row[1:-1]):
                self.print_totableWidget(row_numb, col_numb, elem)

        if self.edit_flag:
            self.print_keyscolumn(IDs)
            self.print_idcolumn(IDs)
            self.tableWidget.cellDoubleClicked.disconnect()
        else:
            self.tableWidget.cellDoubleClicked.connect(self.delete_note)

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

    def none(self):
        """ничего не делающая функция"""
        pass

    def print_keyscolumn(self, IDs):
        """печать колонки с ключами поиска"""
        col = 3
        self.tableWidget.setColumnCount(self.tableWidget.columnCount() + 1)
        self.tableWidget.setHorizontalHeaderLabels(['Заголовок', 'Заметка', 'Дата', 'Ключи'])

        cur = self.con.cursor()
        for row, id in enumerate(IDs):
            key = list(cur.execute(f"SELECT keys FROM notes WHERE id={str(id)}"))[0][0]
            self.tableWidget.setItem(row, col, QTableWidgetItem(str(key)))

    def del_keyscolumn(self):
        """удаление колонки с ключами поиска"""
        self.tableWidget.setColumnCount(self.tableWidget.columnCount() - 1)

    def print_idcolumn(self, IDs):
        """печать колонки с id"""
        col = 4
        self.tableWidget.setColumnCount(self.tableWidget.columnCount() + 1)

        for row, id in enumerate(IDs):
            el = QTableWidgetItem(str(id))
            el.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.tableWidget.setItem(row, col, el)

    def del_idcolumn(self):
        """удаление колонки с id"""
        self.tableWidget.setColumnCount(self.tableWidget.columnCount() - 1)

    def print_totableWidget(self, row, col, elem):
        """вывод в таблицу елементa"""

        elem = QTableWidgetItem(str(elem))
        if not self.edit_flag:
            elem.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(row, col, elem)

    def delete_note(self, row):
        """создание окна для удаления заметки"""
        self.w = DelNote(self.ids_intable[row], self)
        self.w.setGeometry(500, 500, 500, 500)
        self.w.show()

    def add_note(self):
        """создание и вывод окна для создания новой заметки"""

        self.addnote_widget = AddNote(self)
        self.addnote_widget.show()


class DelNote(QWidget, Ui_Form):
    """класс в котором реализованно удаление заметки"""

    def __init__(self, id, MainWindow):
        super(DelNote, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Удаление')
        self.MainWindow, self.id = MainWindow, id
        self.setFixedSize(400, 200)
        self.initUI()

    def initUI(self):
        cur = self.MainWindow.con.cursor()
        note_data = list(list(cur.execute(f"SELECT title, comment, datetime FROM notes WHERE id={str(self.id)}"))[0])
        note_data = list(map(str, note_data))
        note = '\n'.join(note_data)
        self.label_2.setText(note)
        self.buttonBox.clicked.connect(self.run)

    def run(self, btn):
        if btn.text() == '&Yes':
            self.yes()
        else:
            self.no()

    def yes(self):
        """действия при нажатии пользователем клавиши 'Yes'"""
        q = f"DELETE from notes where id={str(self.id)}"
        cur = self.MainWindow.con.cursor()
        with self.MainWindow.con:
            cur.execute(q)

        self.MainWindow.print_all_notes()
        self.close()

    def no(self):
        """действия при нажатии пользователем клавиши 'No'"""
        self.close()


class AddNote(QWidget, Ui_add_note):
    """класс реализующий создание новой заметки"""

    def __init__(self, MainWindow):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Add note")
        self.MainWindow = MainWindow
        self.initUI()

    def initUI(self):
        self.buttonBox.clicked.connect(lambda btn: self.run(btn))

    def run(self, btn):
        if btn.text() == 'OK':
            self.ok()
        else:
            self.close()

    def ok(self):
        """действия при нажатии пользователем клавиши 'Ok'"""
        title = self.title_PTE.toPlainText()
        note_text = self.note_text_PTE.toPlainText()
        date = self.dateTimeEdit.dateTime()
        date = self.dateTimeEdit.textFromDateTime(date)
        keys = self.keys_PTE.toPlainText()

        self.addNoteToDB(title=title, comment=note_text, datetime=date, keys=keys)

        self.MainWindow.print_all_notes()
        self.close()

    def addNoteToDB(self, **kwargs):
        """добавление созданной пользователем заметки в БД"""
        # q = list(map(lambda s: "'" + s + "'", [title, note, dateTime, keys]))
        # q = f"INSERT INTO notes(title, comment,datetime, keys) VALUES ({', '.join(q)})"

        db_keys, db_vals = [], []
        for key, val in kwargs.items():
            db_keys.append(key)
            db_vals.append(val)

        db_vals = list(map(lambda s: "'" + s + "'", db_vals))
        q = f"INSERT INTO notes({', '.join(db_keys)}) VALUES ({', '.join(db_vals)})"

        con = self.MainWindow.con
        with con:
            cur = con.cursor()
            cur.execute(q)

    def cancel(self):
        """действия при нажатии пользователем клавиши 'Close'"""
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    notes = Notes("NotesData.db")
    notes.show()
    sys.exit(app.exec())
