class MyClass:
    # Instance Method
    def instance_method(self):
        print("This is an instance method")
    
    # Class Method
    @classmethod
    def class_method(cls):
        print("This is a class method")
    
    # Static Method
    @staticmethod
    def static_method():
        print("This is a static method")

# تجربة الـ methods

# إنشاء كائن من الـ class
obj = MyClass()

# استدعاء الـ instance method على الكائن
obj.instance_method()

# استدعاء الـ class method على الكلاس نفسه (بدون إنشاء كائن)
MyClass.class_method()

# استدعاء الـ static method على الكلاس نفسه (بدون إنشاء كائن)
MyClass.static_method()
