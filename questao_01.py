import psutil
import multiprocessing

class Program():
    list_proc = []

def gerar_lista():
    for proc in psutil.process_iter():
        info = proc.as_dict(attrs=['pid', 'name'])
        processo = psutil.Process(info['pid'])
        info['mem_percent'] = round(processo.memory_percent(),2)
        info['cpu_percent'] = round(processo.cpu_percent(interval=0.1)/multiprocessing.cpu_count(), 2)
        Program().list_proc.append(info)

    for element in Program().list_proc:
        print(element)

def main():
    while True:
        print('Lista sendo gerada, aguarde.')
        gerar_lista()
        print('------------')
        check = input('Atualizar a lista? S/N\n').upper()
        if check != 'S':
            #print(Program().list_proc)
            break


if __name__ == '__main__':
    main()