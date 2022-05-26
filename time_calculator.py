def add_time(start, duration, day = False):

  DAYS_WEEK_INDEX = {"monday" : 0, "tuesday" : 1, "wednesday" : 2, "thursday" : 3, "friday" : 4, "saturday" : 5, "sunday" : 6}

  DAYS_WEEK_ARRAY = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

  duration_tup = duration.partition(":")
  duration_hours = int(duration_tup[0])
  duration_mins = int(duration_tup[2])

  start_tup = start.partition(":")
  start_mins_tup = start_tup[2].partition(" ")
  start_hours = int(start_tup[0])
  start_mins = int(start_mins_tup[0])
  
  am_pm = start_mins_tup[2]
  am_pm_flip = {"AM": "PM", "PM": "AM"}

  amt_days = int(duration_hours / 24)

  end_mins = duration_mins + start_mins 
  if end_mins >= 60:
    start_hours += 1
    end_mins = end_mins % 60
    
  end_hours = (start_hours + duration_hours) % 12
  amt_of_am_pm_flips = int((start_hours + duration_hours) / 12)
  
  if end_mins > 9:
    end_mins = end_mins
  else:
    end_mins = "0" + str(end_mins)

  if end_hours == 0:
    end_hours = 12
  else:
    end_hours = end_hours

  if am_pm == "PM" and start_hours + (duration_hours % 12) >= 12:
    amt_days += 1

  if amt_of_am_pm_flips % 2 == 1:
    am_pm = am_pm_flip[am_pm]
  else:
    am_pm = am_pm

  returnTime = str(end_hours) + ":" + str(end_mins) + " " + am_pm

  if day:
    day = day.lower()
    index = int((DAYS_WEEK_INDEX[day]) + amt_days) % 7
    new_day = DAYS_WEEK_ARRAY[index]
    returnTime += ", " + new_day

  if amt_days == 1:
    return returnTime + " " + "(next day)"
  elif amt_days > 1:
    return returnTime + " (" + str(amt_days) + " days later)"

  return returnTime