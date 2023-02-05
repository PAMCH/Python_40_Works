import psutil # 컴퓨터의 정보를 확인하기 위한 모듈

cpu = psutil.cpu_freq() # CPU 속도 확인
print(cpu)

cpu_core = psutil.cpu_count(logical=False) # CPU 물리 코어 수 확인
print(cpu_core)

memory = psutil.virtual_memory() # 메모리 정보 확인
print(memory)

disk = psutil.disk_partitions() # 디스크 정보 확인
print(disk)

net = psutil.net_io_counters() #네트워크를 통해 주고받는 데이터량 확인
print(net)