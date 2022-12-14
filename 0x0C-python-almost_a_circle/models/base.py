#!/usr/bin/python3
"""
create a class base that has a private class attribute __nb_objects
and public instance attribute id
"""
import json


class Base:
    """
    Attributes:
        __nb_objects
        id
    Methods:
        __init__()
        to_json_string(list_dictionaries)
        save_to_file(cls, list_objs)
        from_json_string(json_string)
        create(cls, **dictionary)
        load_from_file(cls)
        save_to_file_csv(cls, list_objs)
        load_from_file_csv(cls)
    """
    __nb_objects = 0  # public class attribute

    def __init__(self, id=None):
        # if id is given by user, assign id to the value
        if id is not None:
            self.id = id
        else:  # else assign it to an increment of the public class attribute
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the json rep of list_dictionaries"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes an object to a
            textfile using json string
        Args:
            list_objs - objects to convert
            cls - filename
        """
        if cls is None:
            return
        if list_objs is not None:
            list_objs = [obj.to_dictionary() for obj in list_objs]
        filename = "{}.json".format(cls.__name__)
        with open(filename, mode="w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation """
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes set """
        from models.rectangle import Rectangle
        from models.square import Square

        if cls is Rectangle:
            new = Rectangle(1, 2)
        elif cls is Square:
            new = Square(3)
        else:
            new = None
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances """
        from os import path
        file = "{}.json".format(cls.__name__)
        if not path.isfile(file):
            return []
        with open(file, "r", encoding="utf-8") as f:
            return [cls.create(**arg) for arg in
                    cls.from_json_string(f.read())]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes in csv format
            Args:
                cls - filename
                list_objs - object to convert
        """
        import csv
        from models.rectangle import Rectangle
        from models.square import Square

        if cls is None:
            return
        if list_objs is not None:
            list_objs = [obj.to_dictionary() for obj in list_objs]
        filename = "{}.csv".format(cls.__name__)  # create filename
        with open(filename, mode="w", encoding="utf-8") as csv_file:
            # open the file in csv format using the filename created
            # create field names
            if cls is Rectangle:
                fieldnames = ["id", "width", "height", "x", "y"]
            elif cls is Square:
                fieldnames = ["id", "size", "x", "y"]
            # write fieldnames into the csv file
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()
            # write each element of every dictionary under their
            # respective columns
            for dic in list_objs:
                writer.writerow(dic)

    @classmethod
    def load_from_file_csv(cls):
        """ deserializes in csv format
            Args:
                cls - filename
        """
        import csv
        from models.rectangle import Rectangle
        from models.square import Square

        if cls is None:
            return
        filename = "{}.csv".format(cls.__name__)  # create filename
        with open(filename, mode="r", encoding="utf-8") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0
            list_objs = []
            attr = []
            for row in csv_reader:
                attr_dic = {}
                if line_count == 0:
                    for key in row:
                        attr.append(key)
                    line_count += 1
                for key, value in row.items():
                    attr_dic[key] = int(value)
                line_count += 1
                list_objs.append(cls.create(**attr_dic))
            return list_objs


if __name__ == "__main__":
    Base()
