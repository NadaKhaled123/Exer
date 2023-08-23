# EOP هو اختصار لـ Event-Driven Programming
#  أو البرمجة المستندة إلى الأحداث. في هذا النمط من البرمجة،
#  يتم تعريف وتنفيذ البرنامج بناءً على حدوث أحداث معينة.
# فيما يلي مثال بسيط للبرمجة المستندة إلى الأحداث باستخدام لغة برمجة Python:
from tkinter import *

def button_click():
    label.config(text="Hello, World!")

root = Tk()
root.title("Event-Driven Programming Example")

label = Label(root, text="Click the button!")
label.pack()

button = Button(root, text="Click Me", command=button_click)
button.pack()

root.mainloop()

# في هذا المثال، 
# يتم استيراد واجهة برمجة التطبيقات 
# (Tkinter) لإنشاء واجهة المستخدم الرسومية.
#  تُعرف دالة `button_click()`
#  التي ستُطلب عند الضغط على زر "Click Me".
#  عند حدوث هذا الحدث، 
# ستقوم الدالة بتغيير نص التسمية (label) إلى "Hello, World!".

# باستخدام هذا المثال، ستظهر نافذة تحتوي على تسمية وزر. عند النقر فوق الزر،
#  سيتم تغيير نص التسمية إلى "Hello, World!".

# هذا هو مثال بسيط يوضح كيفية استخدام البرمجة المستندة إلى الأحداث في إنشاء تطبيقات تفاعلية.
