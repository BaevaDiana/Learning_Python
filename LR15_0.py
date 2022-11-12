import sqlite3
from sqlite3 import Error

'''#создание базы данных
def sql_connection():
    try:
        con = sqlite3.connect('mydatabase0.db')
        print("Connection is established: Database is created in memory")
        return con
    except Error:
        print(Error)'''

'''def sql_table(con):
    cursorObj = con.cursor()
    cursorObj.execute("CREATE TABLE SubFaculties(SubFacultiesID int PRIMARY KEY,SubFacultiesName text,EmployeeList text,SalaryeEmployee text,GroupList text)")
    cursorObj.execute("CREATE TABLE Lecturer(LectID int PRIMARY KEY,SubFacultiesID int,FullNameLecturer text,ScienceDegree text,SubFaculties text,Discipline text,WorkExperience int)")
    cursorObj.execute("CREATE TABLE Subject(SubID int PRIMARY KEY,LectID int,TypeSubject text)")
    cursorObj.execute("CREATE TABLE Lesson(LectID int,SubID int,NumberOfGroups int,NumberOfStudents int)")
    cursorObj.execute("CREATE TABLE LoadLog(JournalPersonnelNumber int PRIMARY KEY,SubFacultiesID int,NameSubject text,NumberOfHours int,NumberOfGroups int)")
    con.commit()'''

'''def sql_insert_1(con):
    cursorObj = con.cursor()
    cursorObj.execute(
        "INSERT INTO SubFaculties(SubFacultiesID,SubFacultiesName,EmployeeList,SalaryeEmployee,GroupList) VALUES(1,'Кафедра вычислительных технологий','Шиян В.И.,Жук А.С.Приходько Т.А.','50000-100000','36,39')")
    cursorObj.execute(
        "INSERT INTO SubFaculties(SubFacultiesID,SubFacultiesName,EmployeeList,SalaryeEmployee,GroupList) VALUES(2,'Кафедра информационных технологий','Гаркуша О.В.,Добровольская Н.Ю.,Михайличенко А.А.','50000-100000','36,39')")
    cursorObj.execute(
        "INSERT INTO SubFaculties(SubFacultiesID,SubFacultiesName,EmployeeList,SalaryeEmployee,GroupList) VALUES(3,'Кафедра математического моделирования','Евдокимов А.А.,Истомин Н.К.,Рубцов С.Е.','50000-10000','37,38')")
    cursorObj.execute(
        "INSERT INTO SubFaculties(SubFacultiesID,SubFacultiesName,EmployeeList,SalaryeEmployee,GroupList) VALUES(4,'Кафедра прикладной математики','Колотий А.Д.,Калайдин Е.Н.,Александров А.А.','50000-70000','34,35')")
    cursorObj.execute(
        "INSERT INTO SubFaculties(SubFacultiesID,SubFacultiesName,EmployeeList,SalaryeEmployee,GroupList) VALUES(5,'Кафедра анализа данных и искуственного интеллекта','Калайдина Г.В.,Коваленко А.А.,Акиньшина В.А.','50000-70000','31,32,33')")
    cursorObj.execute(
        "INSERT INTO SubFaculties(SubFacultiesID,SubFacultiesName,EmployeeList,SalaryeEmployee,GroupList) VALUES(6,'Кафедра английской филологии','Зиньковская А.В.,Шершнева Н.Б.,Сахно А.А.','30000-50000','335,336')")
    cursorObj.execute(
        "INSERT INTO SubFaculties(SubFacultiesID,SubFacultiesName,EmployeeList,SalaryeEmployee,GroupList) VALUES(7,'Кафедра немецкой филологии','Белокопытова И.А.,Нечай Ю.П.,Бычков С.С.','30000-50000','335,336')")
    cursorObj.execute(
        "INSERT INTO SubFaculties(SubFacultiesID,SubFacultiesName,EmployeeList,SalaryeEmployee,GroupList) VALUES(8,'Кафедра францусской филологии','Грушевская Т.М.,Фанян Н.Ю.,Метелева В.В.','30000-50000','121,122,123')")
    cursorObj.execute(
        "INSERT INTO SubFaculties(SubFacultiesID,SubFacultiesName,EmployeeList,SalaryeEmployee,GroupList) VALUES(9,'Английского языка в профессиональной сфере','Баклагова Ю.В.,Лопатина Н.В.,Семерджиди В.Н.','30000-50000','36,39')")
    cursorObj.execute(
        "INSERT INTO SubFaculties(SubFacultiesID,SubFacultiesName,EmployeeList,SalaryeEmployee,GroupList) VALUES(10,'Кафедра теории и практики перевода','Шершнева Н.Б.,Бычков С.С.,Прима А.М.','30000-50000','221,235,236')")
    con.commit()'''

'''def sql_insert_2(con):
    cursorObj = con.cursor()
    cursorObj.execute(
        "INSERT INTO Lecturer(LectID,SubFacultiesID,FullNameLecturer,ScienceDegree,SubFaculties,Discipline,WorkExperience) VALUES(11,1,'Шиян Валерий Игоревич','Преподаватель','Кафедра вычислительных технологий','Интерпретируемые языки программирования',5)")
    cursorObj.execute(
        "INSERT INTO Lecturer(LectID,SubFacultiesID,FullNameLecturer,ScienceDegree,SubFaculties,Discipline,WorkExperience) VALUES(21,1,'Жук Арсений Сергеевич','Старший преподаватель','Кафедра вычислительных технологий','Информационная безопасность',8)")
    cursorObj.execute(
        "INSERT INTO Lecturer(LectID,SubFacultiesID,FullNameLecturer,ScienceDegree,SubFaculties,Discipline,WorkExperience) VALUES(31,1,'Приходько Татьяна Александровна','Доцент','Кафедра вычислительных технологий','Компьютерные сети',10)")
    cursorObj.execute(
        "INSERT INTO Lecturer(LectID,SubFacultiesID,FullNameLecturer,ScienceDegree,SubFaculties,Discipline,WorkExperience) VALUES(41,1,'Усов Павел Евгеньевич','Ассистент','Кафедра вычислительных технологий','Инфомационная безопасность',1)")
    cursorObj.execute(
        "INSERT INTO Lecturer(LectID,SubFacultiesID,FullNameLecturer,ScienceDegree,SubFaculties,Discipline,WorkExperience) VALUES(12,2,'Гаркуша Олег Васильевич','Доцент','Кафедра информационных технологий','Операционные системы',42)")
    cursorObj.execute(
        "INSERT INTO Lecturer(LectID,SubFacultiesID,FullNameLecturer,ScienceDegree,SubFaculties,Discipline,WorkExperience) VALUES(22,2,'Добровольская Наталья Юрьевна','Доцент','Кафедра информационных технологий','Основы программирования',28)")
    cursorObj.execute(
        "INSERT INTO Lecturer(LectID,SubFacultiesID,FullNameLecturer,ScienceDegree,SubFaculties,Discipline,WorkExperience) VALUES(32,2,'Михайличенко Анна Александровна','Старший препоаватель','Кафедра информационных технологий','Основы компьютерной графики',15)")
    cursorObj.execute(
        "INSERT INTO Lecturer(LectID,SubFacultiesID,FullNameLecturer,ScienceDegree,SubFaculties,Discipline,WorkExperience) VALUES(13,3,'Евдокимов Александр Александрович','Доцент','Кафедра математического моделирования','Управление информацией',5)")
    cursorObj.execute(
        "INSERT INTO Lecturer(LectID,SubFacultiesID,FullNameLecturer,ScienceDegree,SubFaculties,Discipline,WorkExperience) VALUES(23,3,'Истомин Никита Константинович','Ассистент','Кафедра математического моделирования','Управление информацией',1)")
    cursorObj.execute(
        "INSERT INTO Lecturer(LectID,SubFacultiesID,FullNameLecturer,ScienceDegree,SubFaculties,Discipline,WorkExperience) VALUES(33,3,'Рубцов Сергей Евгеньевич','Доцент','Кафедра математического моделирования','Физические основы построения ЭВМ',35)")
    con.commit()'''

'''def sql_insert_3(con):
    cursorObj = con.cursor()
    cursorObj.execute(
        "INSERT INTO Subject(SubID,LectID,TypeSubject) VALUES(11,21,'Лекция')")
    cursorObj.execute(
        "INSERT INTO Subject(SubID,LectID,TypeSubject) VALUES(22,11,'Лабораторная работа')")
    cursorObj.execute(
        "INSERT INTO Subject(SubID,LectID,TypeSubject) VALUES(10,31,'Лекция')")
    cursorObj.execute(
        "INSERT INTO Subject(SubID,LectID,TypeSubject) VALUES(20,31,'Лабораторная работа')")
    cursorObj.execute(
        "INSERT INTO Subject(SubID,LectID,TypeSubject) VALUES(21,41,'Лабораторная работа')")
    cursorObj.execute(
        "INSERT INTO Subject(SubID,LectID,TypeSubject) VALUES(13,12,'Лекция')")
    cursorObj.execute(
        "INSERT INTO Subject(SubID,LectID,TypeSubject) VALUES(23,12,'Лабораторная работа')")
    cursorObj.execute(
        "INSERT INTO Subject(SubID,LectID,TypeSubject) VALUES(14,22,'Лекция')")
    cursorObj.execute(
        "INSERT INTO Subject(SubID,LectID,TypeSubject) VALUES(24,22,'Лабораторная работа')")
    cursorObj.execute(
        "INSERT INTO Subject(SubID,LectID,TypeSubject) VALUES(25,32,'Лабораторная работа')")
    con.commit()'''

'''def sql_insert_4(con):
    cursorObj = con.cursor()
    cursorObj.execute(
        "INSERT INTO Lesson(LectID,SubID,NumberOfGroups,NumberOfStudents) VALUES(11,22,1,15)")
    cursorObj.execute(
        "INSERT INTO Lesson(LectID,SubID,NumberOfGroups,NumberOfStudents) VALUES(21,11,3,50)")
    cursorObj.execute(
        "INSERT INTO Lesson(LectID,SubID,NumberOfGroups,NumberOfStudents) VALUES(31,10,1,15)")
    cursorObj.execute(
        "INSERT INTO Lesson(LectID,SubID,NumberOfGroups,NumberOfStudents) VALUES(31,10,3,50)")
    cursorObj.execute(
        "INSERT INTO Lesson(LectID,SubID,NumberOfGroups,NumberOfStudents) VALUES(41,21,1,15)")
    cursorObj.execute(
        "INSERT INTO Lesson(LectID,SubID,NumberOfGroups,NumberOfStudents) VALUES(12,13,3,45)")
    cursorObj.execute(
        "INSERT INTO Lesson(LectID,SubID,NumberOfGroups,NumberOfStudents) VALUES(12,23,1,15)")
    cursorObj.execute(
        "INSERT INTO Lesson(LectID,SubID,NumberOfGroups,NumberOfStudents) VALUES(22,14,3,75)")
    cursorObj.execute(
        "INSERT INTO Lesson(LectID,SubID,NumberOfGroups,NumberOfStudents) VALUES(11,24,1,15)")
    cursorObj.execute(
        "INSERT INTO Lesson(LectID,SubID,NumberOfGroups,NumberOfStudents) VALUES(32,25,1,15)")
    con.commit()'''

'''def sql_insert_5(con):
    cursorObj = con.cursor()
    cursorObj.execute(
        "INSERT INTO LoadLog(JournalPersonnelNumber,SubFacultiesID,NameSubject,NumberOfHours,NumberOfGroups) VALUES(1,1,'Интерпретируемые языки программирования',4,4)")
    cursorObj.execute(
        "INSERT INTO LoadLog(JournalPersonnelNumber,SubFacultiesID,NameSubject,NumberOfHours,NumberOfGroups) VALUES(2,1,'Информационная безопасность',2,4)")
    cursorObj.execute(
        "INSERT INTO LoadLog(JournalPersonnelNumber,SubFacultiesID,NameSubject,NumberOfHours,NumberOfGroups) VALUES(3,1,'Компьютерные сети',6,4)")
    cursorObj.execute(
        "INSERT INTO LoadLog(JournalPersonnelNumber,SubFacultiesID,NameSubject,NumberOfHours,NumberOfGroups) VALUES(4,1,'Информационная безопасность',2,3)")
    cursorObj.execute(
        "INSERT INTO LoadLog(JournalPersonnelNumber,SubFacultiesID,NameSubject,NumberOfHours,NumberOfGroups) VALUES(5,2,'Операционные системы',4,4)")
    cursorObj.execute(
        "INSERT INTO LoadLog(JournalPersonnelNumber,SubFacultiesID,NameSubject,NumberOfHours,NumberOfGroups) VALUES(6,2,'Основы компьютерной графики',2,2)")
    cursorObj.execute(
        "INSERT INTO LoadLog(JournalPersonnelNumber,SubFacultiesID,NameSubject,NumberOfHours,NumberOfGroups) VALUES(7,2,'Основы программирования',6,4)")
    cursorObj.execute(
        "INSERT INTO LoadLog(JournalPersonnelNumber,SubFacultiesID,NameSubject,NumberOfHours,NumberOfGroups) VALUES(8,3,'Управление информацией',4,4)")
    cursorObj.execute(
        "INSERT INTO LoadLog(JournalPersonnelNumber,SubFacultiesID,NameSubject,NumberOfHours,NumberOfGroups) VALUES(9,3,'Управление информацией',2,2)")
    cursorObj.execute(
        "INSERT INTO LoadLog(JournalPersonnelNumber,SubFacultiesID,NameSubject,NumberOfHours,NumberOfGroups) VALUES(10,3,'Физические основы ЭВМ',4,4)")
    con.commit()'''


def select1(con):
   cursorObj = con.cursor()
   cursorObj.execute('''select FullNameLecturer,ScienceDegree
    from Lecturer where Lecturer.SubFacultiesID==1   ''')
   rows = cursorObj.fetchall()
   cursorObj.close()
   print('\nВсе преподаватели с кафедры КВТ:')
   for row in rows:
      print(row)

def select2(con):
   cursorObj = con.cursor()
   cursorObj.execute('''select FullNameLecturer,ScienceDegree,Discipline
    from Lecturer inner join SubFaculties on Lecturer.SubFacultiesID=SubFaculties.SubFacultiesID where SubFaculties.GroupList='36,39' ''')
   rows = cursorObj.fetchall()
   cursorObj.close()
   print('\nФИО преподавателей,преподающих в группах 36 и 39:')
   for row in rows:
      print(row)

def select3(con):
   cursorObj = con.cursor()
   cursorObj.execute('''select FullNameLecturer,ScienceDegree
    from Lecturer inner join Lesson on Lecturer.LectID=Lesson.LectID group by NumberOfGroups ''')
   rows = cursorObj.fetchall()
   cursorObj.close()
   print('\nСортировка преподавателей по числу групп,в которых они преподают(в порядке возрастания):')
   for row in rows:
      print(row)


def select4(con):
   cursorObj = con.cursor()
   cursorObj.execute('''select Discipline
    from Lecturer inner join SubFaculties on Lecturer.SubFacultiesID=SubFaculties.SubFacultiesID where SubFaculties.GroupList='36,39' ''')
   rows = cursorObj.fetchall()
   cursorObj.close()
   print('\nПредметы кафедры КВТ в группах 36,39:')
   for row in rows:
      print(row)

def select5(con):
   cursorObj = con.cursor()
   cursorObj.execute('''select FullNameLecturer,ScienceDegree,TypeSubject
    from Lecturer inner join Subject on Lecturer.LectID=Subject.LectID where Lecturer.LectID=Subject.LectID ''')
   rows = cursorObj.fetchall()
   cursorObj.close()
   print('\nФИО преподавателя и вид занятия,который он проводит:')
   for row in rows:
      print(row)

def sql_delete(con):
   cursorObj = con.cursor()
   cursorObj.execute('DELETE FROM Lecturer where SubFacultiesID == 3')
   cursorObj.execute('DELETE FROM Lesson where NumberOfGroups == 50')
   cursorObj.execute('DELETE FROM SubFaculties  where SubFacultiesID == 9')
   cursorObj.execute('DELETE FROM Subject  where TypeSubject = "Лекция"')
   cursorObj.execute('DELETE FROM LoadLog  where NumberOfGroups == 2 and NumberOfHours == 2')
   con.commit()


def sql_update(con):
   cursorObj = con.cursor()
   cursorObj.execute('UPDATE Lesson SET NumberOfStudents = 30  where NumberOfGroups == 1')
   cursorObj.execute('UPDATE LoadLog SET NumberOfHours = 4  where NumberOfGroups == 3')
   cursorObj.execute('UPDATE Lecturer SET ScienceDegree = "Доцент" where LectID == 11')
   con.commit()



#con = sql_connection()
#sql_table(con)

con = sqlite3.connect('mydatabase0.db')
#sql_insert_1(con)
#sql_insert_2(con)
#sql_insert_3(con)
#sql_insert_4(con)
#sql_insert_5(con)
select1(con)
select2(con)
select3(con)
select4(con)
select5(con)
sql_delete(con)
sql_update(con)