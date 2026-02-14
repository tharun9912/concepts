""" Single Responsibility principle , a class should perform single functionality.
In this example, each class performing single functionality,otherwise it voilates this principle.
"""

class Report :                     
    def generate(self):
        print("generating report")

class FileSaver:
    def save(self):
        print("saving report")

class Send:
    def send_report(self):
        print("sending report")

if __name__=="__main__":
    report = Report()
    report.generate()

    file_saving=FileSaver()
    file_saving.save()

    send_file=Send()
    send_file.send_report()    

