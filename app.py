from flask import Flask, render_template, url_for, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "performance_eval_db"

mysql = MySQL(app)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/get-started')
def get_started():
   return render_template('get-started.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/register')
def register():
    return render_template('register.html')  

@app.route('/login')
def login():
    return render_template('login.html') 

@app.route('/login/admin', methods=['GET', 'POST'])
def admin_login():
    error1 = ""
    error2 = ""
    if request.method == 'POST':
      empid = request.form['empid']
      pw = request.form['pw']

      cur = mysql.connection.cursor()
      cur.execute("select emp_id, pw from admin_tbl where emp_id = %s",(str(empid),))

      users = cur.fetchall()
      cur.close()
      if users:
         if users[0][1] == pw:
            return redirect(url_for('admin'))
         else:
            error1 = "Invalid Password."
            return render_template('admin-login.html', error1=error1)
      else:
        error2 = "ID doesn't exist."
        return render_template('admin-login.html', error2=error2)

    return render_template('admin-login.html') 

@app.route('/admin')
def admin():
  return render_template('admin/admin-dashboard-home.html')

@app.route('/admin/school-admin')
def admin_school_admin():
  return render_template('admin/admin-dashboard-admin.html')

@app.route('/admin/form')
def admin_form():
  return render_template('admin/admin-dashboard-form.html')

@app.route('/admin/inbox')
def admin_inbox():
  return render_template('admin/admin-dashboard-inbox.html')

@app.route('/admin/request')
def admin_request():
  return render_template('admin/admin-dashboard-request.html')

@app.route('/admin/school')
def admin_school():
  return render_template('admin/admin-dashboard-school.html')



@app.route('/login/school-admin', methods=['GET', 'POST'])
def school_admin_login():
    error1 = ""
    error2 = ""
    if request.method == 'POST':
      empid = request.form['empid']
      pw = request.form['pw']

      cur = mysql.connection.cursor()
      cur.execute("select emp_id, pw from school_admin_tbl where emp_id = %s",(str(empid),))

      users = cur.fetchall()
      cur.close()
      if users:
         if users[0][1] == pw:
            return redirect(url_for('school_admin'))
         else:
            error1 = "Invalid Password."
            return render_template('school-admin-login.html', error1=error1)
      else:
        error2 = "ID doesn't exist."
        return render_template('school-admin-login.html', error2=error2)

    return render_template('school-admin-login.html') 

@app.route('/school-admin')
def school_admin():
  return render_template('school-admin/schooladmin_home.html')

@app.route('/school-admin/faculty')
def school_admin_faculty():
  return render_template('school-admin/faculty.html')

@app.route('/school-admin/faculty/add-people')
def school_admin_faculty_add():
  return render_template('school-admin/add_people_faculty.html')

@app.route('/school-admin/faculty/status')
def school_admin_faculty_status():
  return render_template('school-admin/status.html')

@app.route('/school-admin/faculty/assigned')
def school_admin_faculty_assigned():
  return render_template('school-admin/assigned.html')

@app.route('/school-admin/faculty/deactivated')
def school_admin_faculty_deactivated():
  return render_template('school-admin/deactivated.html')

@app.route('/school-admin/faculty/summary')
def school_admin_faculty_summary():
  return render_template('school-admin/faculty_view_summary.html')

@app.route('/school-admin/results')
def school_admin_results():
  return render_template('school-admin/results.html')

@app.route('/school-admin/records')
def school_admin_records():
  return render_template('school-admin/records.html')

@app.route('/login/teacher', methods=['GET', 'POST'])
def teacher_login():
    error1 = ""
    error2 = ""
    if request.method == 'POST':
      empid = request.form['empid']
      pw = request.form['pw']

      cur = mysql.connection.cursor()
      cur.execute("select emp_id, pw from faculty_tbl where emp_id = %s",(str(empid),))

      users = cur.fetchall()
      cur.close()
      if users:
         if users[0][1] == pw:
            return redirect(url_for('teacher'))
         else:
            error1 = "Invalid Password."
            return render_template('teacher.html', error1=error1)
      else:
        error2 = "ID doesn't exist."
        return render_template('teacher.html', error2=error2)

    return render_template('teacher.html') 

@app.route('/teacher')
def teacher():
  return render_template('teacher/teacher_home.html')

@app.route('/teacher/evaluation')
def teacher_evaluation():
  return render_template('teacher/teacher_evaluation.html')

@app.route('/teacher/forms')
def teacher_forms():
  return render_template('teacher/teacher_forms.html')

@app.route('/teacher/summary')
def teacher_summary():
  return render_template('teacher/teacher_summary.html')

@app.route('/teacher/profile')
def teacher_profile():
  return render_template('teacher/teacher_profile.html')

@app.route('/login/evaluator')
def evaluator_login():
    return render_template('evaluator-login.html') 

if __name__ == "__main__":
  app.run(debug=True)

