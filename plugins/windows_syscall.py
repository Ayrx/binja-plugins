"""
This plugin extends the x86_64 architecture to lift "int 0x2e" to the
LLIL_SYSCALL instruction.

As there is currently no way in Binary Ninja's API to apply architecture hooks
to only specific platforms, this will affect non-Windows platforms as well.
Hopefully "int 0x2e" is not used anywhere else...
"""
from binaryninja.architecture import Architecture, ArchitectureHook


class WindowsX86SyscallHook(ArchitectureHook):
    def get_instruction_low_level_il(self, data, addr, il):
        result, length = super().get_instruction_text(data, addr)

        if len(result) > 0 and result[0].text == "int" and result[2].value == 0x2E:
            il.append(il.system_call())
            return True

        return super().get_instruction_low_level_il(data, addr, il)


WindowsX86SyscallHook(Architecture["x86_64"]).register()
