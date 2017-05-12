''' CALL CENTER '''

class call(object):
    def __init__(self, unique_id, caller_name, caller_number, time_of_call, reason_for_call):
        self.unique_id = unique_id
        self.caller_name = caller_name
        self.caller_number = caller_number
        self.time_of_call = time_of_call
        self.reason_for_call = reason_for_call
    def displayCall(self):
        print "ID:",self.unique_id
        print "Name:",self.caller_name,": #:",self.caller_number
        print "Time:",self.time_of_call,": Reason for call:",self.reason_for_call
        return self

class callCenter(object):
    def __init__(self):
        self.calls = []
        self.queue = 0
    def addCall(self, call):
        self.calls.append(call)
        self.queue += 1
        return self
    def removeCall(self):
        self.calls.pop(0)
        self.queue -= 1
        return self
    def removeCallbyNum(self, num):
        for caller in range(len(self.calls)):
            if self.calls[caller].caller_number == num:
                self.calls.pop(caller)
                break
        self.queue -= 1
        return self
    def sort(self):
        self.calls.sort(key=lambda caller: caller.time_of_call)
        return self
    def callInfo(self):
        print "Current queue size:", self.queue
        for caller in range(len(self.calls)):
            print "Queue Position:", (caller+1), "Name:", self.calls[caller].caller_name, ": #:", self.calls[caller].caller_number
        return self

call1 = call(1, "Bob", "555-111-2222", "9:00AM", "Lonely")
call2 = call(2, "Lisa", "555-222-3333", "9:30AM", "Broken")
call3 = call(3, "Albert", "555-333-4444", "10:00AM", "Refund")
call4 = call(4, "Natalie", "555-444-5555", "7:30AM", "Angry")
call5 = call(4, "Marge", "555-555-6666", "11:30AM", "Weird")

#call1.displayCall()

callCenter1 = callCenter().addCall(call1).addCall(call2).addCall(call3).addCall(call4).callInfo().removeCall().callInfo().removeCallbyNum("555-333-4444").callInfo().addCall(call5).callInfo().removeCallbyNum("555-555-6666").callInfo().addCall(call1).addCall(call5).sort().callInfo()
