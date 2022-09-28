**0x0B. Python - Input/Output**


**In this project, I learned how to open a file, read from it, and aslo write to to it.**

* When opening a textfile for reading or writing always include the encoding type.

* It's considered good practice to use the open call with a "with" statement.

* The "with" statement handles exceptions/ errors in the course of using your file i.e if an error occurs, it still
closes the file.

* When used with a textfile, the read() method reads characters.

* Never forget to close a file after using it, especially in cases where it is not used wit a "with" statement.

* Binary files do not have an encoding attribute.

* When used with a binary file, the read() function method bytes.

* The seek() and tell() methods works differently for textfiles and binary files:
      . For text files => The seek() method returns the file offset to the specified byte
        and the tell() method returns the current file position in a file stream.
      . For binary files => the seek() and tell() method does the same as above. The only difference is in its
        behavior with the two kinds of file. Because some characters in a textfile accounts for more than one byte
	using seek() to traverse to a specified byte may cause unpredictable outcomes.