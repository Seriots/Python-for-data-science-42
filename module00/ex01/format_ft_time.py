import time

epoch_time = time.time()

print(f"Seconds since January 1, 1970: {int(epoch_time // 1000000000)},\
{int((epoch_time % 1000000000) // 1000000):03d},\
{int((epoch_time % 1000000) // 1000):03d},\
{epoch_time % 1000:.4f} \
or {epoch_time:.3} in scientific notation")

print(f"{time.strftime('%B %d %Y', time.localtime(epoch_time))}")
