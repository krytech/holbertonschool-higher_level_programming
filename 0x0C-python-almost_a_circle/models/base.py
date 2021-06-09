#!/usr/bin/python3
"""
class Base
"""
import json
import csv


class Base:
    """ Define class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns JSON string representation of list_dictionaries """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string representation json_string """
        if json_string is None or len(json_string) == 0:
            json_string = "[]"
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes JSON string representation of list_objs to a file """
        list_dict = []
        if list_objs is not None:
            for i in list_objs:
                list_dict.append(cls.to_dictionary(i))
        with open(cls.__name__ + ".json", "w") as f:
            f.write(cls.to_json_string(list_dict))

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes already set """
        if cls.__name__ == "Square":
            dummy = cls(1)
        elif cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances """
        try:
            with open(cls.__name__ + ".json", "r") as f:
                content = cls.from_json_string(f.read())
                instances = []
                for i, c in enumerate(content):
                    instances.append(cls.create(**content[i]))
                return instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Serializes data to CSV file """
        with open(cls.__name__ + ".csv", "w") as f:
            write = csv.writer(f)
            for i in list_objs:
                if cls.__name__ == "Rectangle":
                    write.writerow([i.id, i.width, i.height, i.x, i.y])
                if cls.__name__ == "Square":
                    write.writerow([i.id, i.size, i.x, i.y])

    @classmethod
    def load_from_file_csv(cls):
        """ Deserializes data from a CSV file """
        objs = []
        with open(cls.__name__ + ".csv", "r") as f:
            read = csv.reader(f)
            for row in read:
                if cls.__name__ == "Rectangle":
                    dict = {"id": int(row[0]),
                            "width": int(row[1]),
                            "height": int(row[2]),
                            "x": int(row[3]),
                            "y": int(row[4])}
                if cls.__name__ == "Square":
                    dict = {"id": int(row[0]),
                            "size": int(row[1]),
                            "x": int(row[2]),
                            "y": int(row[3])}
                o = cls.create(**dict)
                objs.append(o)
        return objs
