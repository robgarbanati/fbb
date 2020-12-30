import math

jj_stdev = 1.684264101
stdev1 = 1.722482038
stdev2 = 1.63877096
d1 = 0.147162673
d2 = -0.130100334
sum = 61*(math.pow(stdev1,2)+d1)+69*(math.pow(stdev2,2) + d2)
print(sum)
var = sum/(61+69)
print(var)
stdevtot = math.sqrt(var)
print(stdevtot)

jj_games = 130
twojj_sum = jj_games*(math.pow(jj_stdev,2))+jj_games*(math.pow(stdev2,2))
print(twojj_sum)
twojj_var = twojj_sum/(jj_games*2)
print(twojj_var)
twojj_sd = math.sqrt(twojj_var)
print(twojj_sd)

jj_games = 130
tenjj_sum = 100*jj_games*(math.pow(jj_stdev,2))
print(tenjj_sum)
tenjj_var = tenjj_sum/(jj_games*100)
print(tenjj_var)
tenjj_sd = math.sqrt(tenjj_var)
print(tenjj_sd)
