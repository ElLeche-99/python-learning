lines = int(input())
messages = []
friends = []
friends_messages = []
friends_total_time = []
for line in range(lines):
    message = input()
    messages.append(message.split(' ')) # Creating events list


for message in messages:
    if(message[0] != 'T') and (message[0] != 't'):
        if int(message[1]) not in friends:
            friends.append(int(message[1]))

#print("messages: {}".format(messages))
#print("friends: {}".format(friends))



for friend in friends:
    count = 0
    for message in messages:
        if int(message[1]) == int(friend):
            count += 1
    indices = [indice for indice, message in enumerate(messages) if int(message[1]) == int(friend)] # Counting 
    #print("The Friend: {} is called on messages index : {}".format(friend, indices))
    
    friends_messages.append({'friend': friend, 'total_messages': count, 'messages_indices': indices}) # Creating an dictionary to count friends messages

#print("Friends messages details: {}".format(friends_messages))
for events in friends_messages:

    beginning = events['messages_indices'][0]
    ending = events['messages_indices'][-1]
    index_range = range(beginning, ending)
    count = 0

    for verify_spent in index_range:
 
        #if (messages[verify_spent] == beginning): # Verificando no começo da lista
         # if(messages[verify_spent+1][0] == 'T' and messages[verify_spent+1][0] == 't'): # Se o próximo elemento não for o T/t conta mais 1 salto
           #     
            #    count += int(messages[verify_spent+1][1])
            
            #else:
             #   count += 1
                
        
            if(messages[verify_spent+1][0] != 'T' and messages[verify_spent+1][0] != 't'):
                if(messages[verify_spent-1][0] != 'T' and messages[verify_spent-1][0] != 't'):
                 count +=1
            else:
                count += int(messages[verify_spent+1][1])
    print("Friend: {}, time: {}".format(events['friend'], count))
    ...
'''



for data in friends_messages:
    beginning = data['messages_indices'][0]
    ending = data['messages_indices'][-1]
    time_count = 0
    for index in range(beginning, ending):
        if(messages[index][0] == 'T' or messages[index][0] == 't'):
            time_count += int(messages[index][2])-1
        else:
            time_count += 1
    print("For friend {}, the sum of response time is: {}".format(data['friend'], time_count))
'''