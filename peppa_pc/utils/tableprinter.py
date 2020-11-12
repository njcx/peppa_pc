import prettytable as pt


def data_table_printer(data):
    tb = pt.PrettyTable()
    tb.field_names = ["id", "target", "poc_name", "app_name", "app_version", "vul_type", "info", "mode", "status"]
    id_ = 0
    for data_ in data:
        id_ += 1
        tb.add_row([id_, data_["target"], data_["poc_name"], data_["app_name"], data_["app_version"],
                    data_["vul_type"], data_["info"], data_["mode"], data_["status"]])
    return tb

