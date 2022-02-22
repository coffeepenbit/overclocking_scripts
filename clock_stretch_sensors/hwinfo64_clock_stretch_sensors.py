import pathlib

# Replace with your core clocks from HWiNFO64
# "<Core number>": "<name from HWiNFO64>"
CORE_PERF = {
    "0": "Core 0 Clock (perf #2/3)",
    "1": "Core 1 Clock (perf #1/1)",
    "2": "Core 2 Clock (perf #3/4)",
    "3": "Core 3 Clock (perf #1/2)",
    "4": "Core 4 Clock (perf #5/6)",
    "5": "Core 5 Clock (perf #4/5)",
}

# Replace with your total number of threads
NTHREADS = 12

# Location for saving the generated registry file
REG_FILE_PATH = pathlib.Path("~/Desktop/clock_stretch.reg").expanduser()


clock_stretch_names = []
with open(REG_FILE_PATH, "w") as reg:
    reg.write("Windows Registry Editor Version 5.00\n\n")

    for thread in range(NTHREADS):
        reg.write(f"[HKEY_CURRENT_USER\\SOFTWARE\\HWiNFO64\\Sensors\\Custom\\Clock Stretch\\Clock{thread}]\n")

        core = thread // 2
        core_thread = thread % 2
        clock_stretch_name = f"\"Clock Stretch Core {str(core)} T{core_thread}\""
        reg.write(f"\"Name\"={clock_stretch_name}\n")
        clock_stretch_names.append(clock_stretch_name)

        perf = CORE_PERF[str(core)]
        thread_usage = f"Core {core} T{core_thread} Effective Clock"

        reg.write(f"\"Value\"=\"\\\"{perf}\\\" - \\\"{thread_usage}\\\"\"\n\n")

    # Aggregate of other clocks
    reg.write(f"[HKEY_CURRENT_USER\\SOFTWARE\\HWiNFO64\\Sensors\\Custom\\Clock Stretch\\Clock{NTHREADS}]\n")
    reg.write(f"\"Name\"=\"Clock Stretch Aggregate Max\"\n")
    string_escaped_clock_stretch_names = [name.replace('"', '\\\"') for name in clock_stretch_names]
    reg.write(f"\"Value\"=\"max({', '.join(string_escaped_clock_stretch_names)})\"\n")
