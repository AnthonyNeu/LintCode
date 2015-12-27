"""
Singleton is a most widely used design pattern. If a class has and only has one instance at every moment, we call this design as singleton. For example, for class Mouse (not a animal mouse), we should design it in singleton.

You job is to implement a getInstance method for given class, return the same instance of this class every time you call this method.

Example
In Java:

A a = A.getInstance();
A b = A.getInstance();
a should equal to b.

Challenge
If we call getInstance concurrently, can you make sure your code could run correctly?
"""

class Solution:
    obj = None
    # @return: The same instance of this class every time

    @classmethod
    def getInstance(cls):
        # write your code here
        if not Solution.obj:
            Solution.obj = cls()
        return Solution.obj

# thread safe
import threading
class Solution:
    __lock = threading.Lock()
    __obj = None
    # @return: The same instance of this class every time

    @classmethod
    def getInstance(cls):
        # write your code here
        if not cls.__obj:
            with cls.__lock:
                if not cls.__obj:
                    cls.__obj = cls()

        return cls.__obj
