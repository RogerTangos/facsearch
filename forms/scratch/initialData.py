from forms.models import Visitor, Host, Assistant

host = Host(
fName = "Munther",
lName = "Dahleh",
email = "dahleh@mit.edu",
officeNumber = "38-435",
officePhone = "617-251-3893",
mitId = "12345")

host.save();

assistant = Assistant(
fName = "Albert",
lName = "Carter",
officePhone = "8-8773",
officeNumber = "38-409C",
email = "arcarter@mit.edu",
mitId = "12345"
)

assistant.save();
assistant.facMembers.add(host);


visitor = Visitor(
fName = "Sample",
lName = "Visitor",
email = "arcarter@mit.edu",
address1 = "1 sample drive",
address2 = "#2",
city = "anywhereTown",
state = "MA",
zipcode = "02138",
country = "USA",

officePhone = "123-456-7890",
cellPhone = "123-456-7890",
dietary = "no",
videoRecording = True
	)

visitor.save()
visitor.hosts.add(host)

