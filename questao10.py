import datetime
import pandas as pd
import psutil
import time
import threading
from matplotlib import style
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from cycler import cycler

style.use('dark_background')
mpl.rcParams['lines.linewidth'] = 1
mpl.rcParams['lines.linestyle'] = '--'
mpl.rcParams['axes.prop_cycle'] = cycler(color=['r', 'g', 'b', 'y'])
fig = plt.figure()

ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)

def thr_gerar_csv(int):
    for i in range(0, int):
        pmem, pcpu = pegar_dados()
        list_data = [pmem, pcpu]
        fazer_csv(list_data)
        time.sleep(5)

def pegar_dados():
    memoria = psutil.virtual_memory()
    mem_percem = str(memoria.percent)
    cpu_percem = str(psutil.cpu_percent(interval=1))

    return mem_percem, cpu_percem

def fazer_csv(list_data):
    time_stamp = datetime.datetime.now()
    time_stamp = time_stamp.strftime('%d/%m/%Y %H:%M:%S')
    col = [time_stamp]
    col.extend(list_data)
    col.extend(list_data)
    df = pd.DataFrame(col)
    df = df.T
    df.to_csv('questao10_info.csv', mode='a', header=False)
    print('Dado adicionado no csv.')

def loop_grafico(i):
    df = pd.read_csv('questao10_info.csv')

    ys = df.iloc[1:, 2].values
    xs = list(range(1, len(ys)+1))
    ax1.clear()
    ax1.plot(xs, ys)
    ax1.set_title('Memoria', fontsize=10)

    ys = df.iloc[1:, 3].values
    ax2.clear()
    ax2.plot(xs, ys)
    ax2.set_title('CPU', fontsize=10)


def main():
    t1 = threading.Thread(target=thr_gerar_csv, args=[101])
    t1.start()
    ani = animation.FuncAnimation(fig, loop_grafico, interval=1000)
    plt.tight_layout()
    plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,
                    wspace=0.35)
    plt.show()

if __name__ == '__main__':
    main()