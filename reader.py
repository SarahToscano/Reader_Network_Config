import logging
RED = "\x1b[31;1m"
GREEN = '\033[32m'
YELLOW = '\033[33m'
CIAN = '\033[36m'
MAGENTA = '\033[35m'
logging.getLogger().setLevel(logging.INFO)

def get_data():
    input_data = []
    for line in [l.strip() for l  in open('input_copy.txt') if not l.startswith('#')]:
        input_data.append(line.split())

    number_bars=int(input_data[0][0])
    num_bar_nodes = [int(array_list) for array_list in input_data[1]]
    components = int(input_data[2][0])
    max_nodes = max(num_bar_nodes)

    n = components
    m = max_nodes*number_bars + 2
    matrix = [[-1] * m for i in range(n)]
    j=3
    l=1
    i=0

    while (i<components):
        c_type = int(input_data[j][0])
        if(c_type==1):
            matrix[i][0] = int(input_data[j][0])
            for k in range (j+1, j+6+(max_nodes*2)):
                a=j            
                if(k==a+1 or k == a+2): #inductances
                    matrix[i][l] = complex(input_data[k][0])
                elif(k>=a+3 and k<=a+6): #Input Output bars and nodes
                    matrix[i][l] = int(input_data[k][0])
                    if(k==a+3 or k ==a+5):
                        bar_id = int(matrix[i][l]/10)
                        node_bar = num_bar_nodes[bar_id-1]
                    else:
                        if(matrix[i][l]>node_bar):#numero de nos na barra é maior do que o definido na linha 4 do script
                            logging.error(RED + f'THE NUMBER OF INPUT/OUTPUT NODES IN COMPONENT [{i+1}] IS GREATER THAN THE TOTAL OF NODES IN INPUT/OUTPUT BAR')
                            i+=components
                            break
                elif(k>=a+7 and k<a+7+matrix[i][4]+matrix[i][6]): #NodesID of bar [X] 
                    matrix[i][l] = int(input_data[k][0])
                else:
                    j+=6+matrix[i][4]+matrix[i][6]+1
                    k+=50
                l+=1
        elif(c_type==2):
            l=1
            matrix[i][0] = int(input_data[j][0])
            for k in range (j+1, j+10 +(max_nodes*2)):
                a=j
                if(k>=a+1 and k <= a+6): #inductances
                    matrix[i][l] =  complex(input_data[k][0])
                elif(k>=a+7 and k<=a+10): #Input Output bars and nodes
                    matrix[i][l] = int(input_data[k][0])
                    if(k==a+7 or k ==a+9):
                        bar_id = int(matrix[i][l]/10)
                        node_bar = num_bar_nodes[bar_id-1]
                    else:
                        if(matrix[i][l]>node_bar):#numero de nos na barra é maior do que o definido na linha 4 do script
                            logging.error(RED + f'THE NUMBER OF INPUT/OUTPUT NODES IN COMPONENT [{i+1}] IS GREATER THAN THE TOTAL OF NODES IN INPUT/OUTPUT BAR')
                            i+=components
                            break
                elif(k>=a+11 and k<a+11+matrix[i][8]+matrix[i][10]):
                    matrix[i][l] = int(input_data[k][0])
                else:
                    j+=10+matrix[i][8]+matrix[i][10]+1
                    continue
                l+=1
        elif(c_type==3):
            l=1
            matrix[i][0] = int(input_data[j][0])
            for k in range (j+1, j+9 +(max_nodes*2)):  
                a=j
                if(k>=a+1 and k <= a+4): ##Nominal Power, Power factor, Nominal Voltage, Load Type
                    matrix[i][l] = float(input_data[k][0])
                elif (k>=a+5 and k<= a+8): #Input Output bars and nodes
                    if(k==a+5):
                        matrix[i][l] = int(input_data[k][0])
                        bar_id = int(matrix[i][l]/10)
                        node_bar = num_bar_nodes[bar_id-1]
                    elif(k==a+6):
                        if(matrix[i][l]>node_bar):#numero de nos na barra é maior do que o definido na linha 4 do script
                            logging.error(RED + f'THE NUMBER OF INPUT/OUTPUT NODES IN COMPONENT [{i+1}] IS GREATER THAN THE TOTAL OF NODES IN INPUT/OUTPUT BAR')
                            i+=components
                            break
                        else:
                            matrix[i][l] = int(input_data[k][0])
                    elif(k>=a+7 and k<=a+8):
                        matrix[i][l] = 0
                elif(k>=a+9 and k<a+9+matrix[i][6]):#NodesID of bar [X] 
                    matrix[i][l] = int(input_data[k][0])
                else:
                    continue
                l+=1
        else:
            logging.error(RED + 'THERE IS NOT COMPONENT TYPE [ %s ]. THE ID MUST BE 1, 2 OR 3.', c_type)
            i+=components
            break
        i+=1
    size = len(input_data)
    time = [0]*3
    currents = [0]*(len(input_data[size-1]))
    time = [float(array_list) for array_list in input_data[size-2]]
    currents = [float(array_list) for array_list in input_data[size-1]]

    logging.info(GREEN)
    logging.info("DATASOURCE READ COMPLETED..." )
    logging.info(YELLOW)
    logging.info("Circuit Data:")
    for i in range(0, components):
        logging.info(f'{matrix[i]}')
    logging.info(CIAN)
    logging.info(f'Time: {time}')
    logging.info(f'Currents: {currents}')

    return (matrix, time, currents)

get_data()







