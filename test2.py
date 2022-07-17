from multiprocessing import Process

import matlab.engine

def proc1():
    print("1")
    eng_names = matlab.engine.find_matlab()
    eng = matlab.engine.connect_matlab(eng_names[0])
    print(eng)
    return eng

def proc2():
    print("2")


if __name__ == "__main__":
    job1 = Process(target=proc1)
    job2 = Process(target=proc1)

    job1.start()
    job2.start()

    job1.join()


