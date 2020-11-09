import prettytable as pt

# tb = pt.PrettyTable( ["City name", "Area", "Population", "Annual Rainfall"])
tb = pt.PrettyTable()
tb.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
tb.add_row(["Adelaide",1295, 1158259, 600.5])
tb.add_row(["Brifasdfae",5905, 1857594, 1146.4])
tb.add_row(["Darwin", 112, 120900, 171423423423423424.7])
tb.add_row(["Hobart", 1357, 205556,619.5])

print(tb)