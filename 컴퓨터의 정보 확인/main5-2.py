import psutil

cpu = psutil.cpu_freq()
cpu_current_ghz = round(cpu.current / 1000, 2) # CPU 사용량을 1000으로 나눈 값에서 소숫점 둘째자리 반올림
print(f"CPU 속도 : {cpu_current_ghz}GHz")

cpu_core = psutil.cpu_count(logical=False)
print(f"코어 : {cpu_core} 개")

memory = psutil.virtual_memory()
memory_total = round(memory.total / 1024**3) # Memory 총량에서 1024**3, GB 값으로 표기하기 위해 나눔
print(f"메모리 : {memory_total}GB")

disk = psutil.disk_partitions()
for p in disk :
    print(p.mountpoint, p.fstype, end=' ')
    du = psutil.disk_usage(p.mountpoint)
    disk_total = round(du.total / 1024**3) # Disk 총량에서 1024**3, GB 값으로 표기하기 위해 나눔
    print(f"디스크 크기 : {disk_total}GB")


net = psutil.net_io_counters()
sent = round(net.bytes_sent / 1024**2, 1) # 데이터 량에서 1024**2, MB 값으로 표기하기 위해 나눔
recv = round(net.bytes_recv / 1024**2, 1)
print(f"보내는 량 : {sent}MB / 받는 량 : {recv}MB")