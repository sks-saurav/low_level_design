'''
REQUIREMENT:
1. Schedule a meeting if room is available of desired capacity
2. All attendies should be available in time period
3. Employee can accept or decline a meeting
4. n avilable meeting room
5. Abaility of add attendied in scheduled meeting
6. Is meeting reoccuring
7. User will get notification of meeting invite
8. he can accept or decline a meting invite
9. User will be able to cancel scheduled meeting
10. User will able to access calendar which have all meeting time and date
'''

class MeetingStatus(Enum):
    SCHEDULED = 1
    ACCEPTED = 2
    DECLINED = 3
    
class RoomStatus(Enum):
    BOOKED = 1
    AVAILABLE = 2

class Employee:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name
        self.__meetings = []
        self.__meeting_status = {}
        
class Meeting:
    def __init__(self, id, name, host, start_time, end_time) -> None:
        self.__id = id
        self.__name = name
        self.__host = host
        self.start = start_time
        self.end = end_time
        self.attendies = []
        
class Room:
    def __init__(self, id, location, capacity) -> None:
        self.__id = id
        self.__location = location
        self.__capacitiy = capacity
        self.__type = None
        self.__scheduled_meetings = []
        
class Calendar:
    def __init__(self) -> None:
        self.meetings = []

        
class Singleton(object):
    __instances = None
    
    def __new__(cls):
        if cls.__instances is None:
            cls.__instances = super(Singleton, cls).__new__(cls)
        return cls.__instances
    
class Scheduler(Singleton):
    def __init__(self, room_count) -> None:
        self.__number_of_rooms = room_count
        self.__rooms = {}
        
    def schedule_new_meeting(self):
        pass
    
    def cancel_meeting(self):
        pass
        

        
        