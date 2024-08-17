#print("TIME ON EARTH")

#take input as a time and calculate hours, minutes and seconds
#time = int(input("Input a time in Seconds:"))
#Hours = (time/3600)

#minutes = (Hours - int(Hours))
#Final_Minutes = (minutes*60)

#Seconds = (Final_Minutes - int(Final_Minutes))
#Final_Seconds = round(Seconds*60)

#print the result in the given format
#print('\n' "The time on Earth is" ,int(Hours),"hours",int(Final_Minutes),"minutes", "and",Final_Seconds,"seconds"'.')

# print ("TIME ON EARTH")
#
# Seconds =  int(input ("Input a time in seconds:"'\n'))
# tri_seconds = int(input("triseco:"))
# tri_min = int(input("trimin:"))
#
# #caclculate the hour, minutes and seconds
# hours = Seconds // (tri_seconds*tri_min)
# remain_seconds = Seconds % (tri_seconds*tri_min)
# minutes =  remain_seconds // tri_seconds
# Final_seconds = remain_seconds  % minutes
# #print the result in the given format
# print('\n' "The time on Earth is" ,hours,"hours",minutes,"minutes", "and",Final_seconds,"seconds"'.')

# print ("TIME ON EARTH")
#
# final_seconds =  int(input ("Input a time in seconds:"'\n'))
#
# #evaluating the hour, minutes and seconds
# final_hours = final_seconds // 3600
# sec_left = final_seconds % 3600
# final_min =  sec_left // 60
# sec_final = sec_left % 60
# #print the result in the given format
# print('\n' "The time on Earth is" ,final_hours,"hours",final_min,"minutes", "and",sec_final,"seconds"'.')
#
# print("\nTIME ON TRISOLARIS")
#
# trisolsec = int(input("Input the number of seconds in a minute on Trisolaris:\n"))
# trisolmin = int(input("Input the number of minutes in an hour on Trisolaris:\n"))
#
# trisolhours = final_seconds // (trisolsec * trisolmin)
# trisol_sec_left = final_seconds % (trisolsec * trisolmin)
# trisol_min = trisol_sec_left // trisolsec
# trisol_final_sec = trisol_sec_left % trisolsec
#
# print(f"\nThe time on Trisolaris is {trisolhours} hours {trisol_min} minutes and {trisol_final_sec} seconds.")

#earth
print ("TIME ON EARTH")

final_seconds =  int(input ("Input a time in seconds:"'\n'))

#evaluating the hour, minutes and seconds
final_hours = final_seconds // 3600
sec_left = final_seconds % 3600
final_min =  sec_left // 60
sec_final = sec_left % 60
#print the result in the given format
print('\n' "The time on Earth is" ,final_hours,"hours",final_min,"minutes", "and",sec_final,"seconds"'.')

#trisolaris
print("\nTIME ON TRISOLARIS")

trisolsec = int(input("Input the number of seconds in a minute on Trisolaris:\n"))
trisolmin = int(input("Input the number of minutes in an hour on Trisolaris:\n"))

trisolhours = final_seconds // (trisolsec * trisolmin)
trisol_sec_left = final_seconds % (trisolsec * trisolmin)
trisol_min = trisol_sec_left // trisolsec
trisol_final_sec = trisol_sec_left % trisolsec

print(f"\nThe time on Trisolaris is {trisolhours} hours {trisol_min} minutes and {trisol_final_sec} seconds.")

print("\nTIME AFTER WAITING ON TRISOLARIS")

#defining waiting seconds
waiting_seconds = int(input("Input a duration in seconds:\n"))
Final_waiting_seconds = final_seconds + waiting_seconds

#evaluating waiting time
trisol_waiting_hours = Final_waiting_seconds // (trisolsec * trisolmin)
trisol_waiting_secs_remaining = Final_waiting_seconds % (trisolsec * trisolmin)
trisol_waiting_min = trisol_waiting_secs_remaining // trisolsec
trisol_waiting_secs_finally_left = trisol_waiting_secs_remaining % trisolsec

print(f"\nThe time on Trisolaris after waiting is {trisol_waiting_hours} hours {trisol_waiting_min} minutes and {trisol_waiting_secs_finally_left} seconds.")