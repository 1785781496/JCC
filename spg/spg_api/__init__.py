# -*- coding: utf-8 -*-


def spg_create_project(pcode, pname, ptype=0):
    if pcode not in list(project_dict.keys()):
        project_dict[pcode] = [pname, ptype, []]
        print(pcode, pname, ptype)
        return True
    else:
        return False


def spg_get_projects():
    return list(project_dict.keys())


if __name__ == '__main__':
    project_dict = {}
    spg_create_project("AAA", "Projaaa")
    print(spg_create_project("AAA", "Projaaa"))
    spg_create_project("BBB", "Projbbb")
    print(project_dict)
    print(spg_get_projects())

