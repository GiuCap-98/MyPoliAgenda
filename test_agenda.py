import datetime
import unittest
from agenda import Agenda, Event

class TestAgenda(unittest.TestCase):
    def setUp(self):
        self.agenda = Agenda()

    def test_add_event(self):
        title = "Meeting"
        date = datetime.datetime(2024, 7, 16)
        description = "Project meeting with team"

        self.agenda.add_event(title, date, description)

        self.assertIn(title, self.agenda.temporary_db)
        self.assertEqual(self.agenda.temporary_db[title], [date, description])
        print("test_add_event passed")

    def test_remove_event(self):
        title = "Meeting"
        date = datetime.datetime(2024, 7, 16)
        description = "Project meeting with team"

        self.agenda.add_event(title, date, description)
        self.agenda.remove_event(title)

        self.assertNotIn(title, self.agenda.temporary_db)
        print("test_remove_event passed")

    def test_list_events(self):
        title1 = "Meeting"
        date1 = datetime.datetime(2024, 7, 16)
        description1 = "Project meeting with team"

        title2 = "Doctor's Appointment"
        date2 = datetime.datetime(2024, 7, 17)
        description2 = "Annual check-up"

        self.agenda.add_event(title1, date1, description1)
        self.agenda.add_event(title2, date2, description2)

        events = self.agenda.list_events()
        self.assertEqual(events, [
            f"Title: {title1}, Date: {date1}, Description: {description1}",
            f"Title: {title2}, Date: {date2}, Description: {description2}"
        ])
        print("test_list_events passed")

if __name__ == "__main__":
    unittest.main()