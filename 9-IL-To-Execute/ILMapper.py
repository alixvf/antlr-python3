class ILMapper:

    @staticmethod
    def is_temp_reg(code):
        return str.startswith(code, "T")
    @staticmethod
    def get_msil_header(used_regs):
        result = (".assembly extern mscorlib {}\n"
                ".assembly a {}\n"
                ".module a.exe\n"
                ".class private auto ansi beforefieldinit ConsoleApp1.Program extends [mscorlib]System.Object\n"
                "{\n"
                ".method private hidebysig static void  Main(string[] args) cil managed\n"
                "{\n"
                ".entrypoint\n"
                ".maxstack  100\n")

        for i in range(used_regs):
            result += f".locals init ([{i}] int64 T{i})\n"

        result += ("nop\n"
                "///////////////////////// IL CODE\n")

        return result

    @staticmethod
    def get_msil_footer():
        return ("\n///////////////////////// IL CODE\n"
                "ldloca.s   T0\n"
                "call       instance string [mscorlib]System.Int64::ToString()\n"
                "call       void [mscorlib]System.Console::WriteLine(string)\n"
                "nop\n"
                "ret\n"
                "} // end of method Program::Main\n"
                ".method public hidebysig specialname rtspecialname instance void  .ctor() cil managed\n"
                "{\n"
                ".maxstack  8\n"
                "ldarg.0\n"
                "call       instance void [mscorlib]System.Object::.ctor()\n"
                "nop\n"
                "ret\n"
                "} // end of method Program::.ctor\n"
                "} // end of class\n")

    @staticmethod
    def mul(result_reg, a, b):
        if ILMapper.is_temp_reg(a):
            if ILMapper.is_temp_reg(b):
                return f"ldloc {a}\nldloc {b}\nmul\nstloc {result_reg}\n"
            else:
                return f"ldloc {a}\nldc.i8 {b}\nmul\nstloc {result_reg}\n"
        else:
            if ILMapper.is_temp_reg(b):
                return f"ldc.i8 {a}\nldloc {b}\nmul\nstloc {result_reg}\n"
            else:
                return f"ldc.i8 {a}\nldc.i8 {b}\nmul\nstloc {result_reg}\n"

    @staticmethod
    def div(result_reg, a, b):
        if ILMapper.is_temp_reg(a):
            if ILMapper.is_temp_reg(b):
                return f"ldloc {a}\nldloc {b}\ndiv\nstloc {result_reg}\n"
            else:
                return f"ldloc {a}\nldc.i8 {b}\ndiv\nstloc {result_reg}\n"
        else:
            if ILMapper.is_temp_reg(b):
                return f"ldc.i8 {a}\nldloc {b}\ndiv\nstloc {result_reg}\n"
            else:
                return f"ldc.i8 {a}\nldc.i8 {b}\ndiv\nstloc {result_reg}\n"

    @staticmethod
    def add(result_reg, a, b):
        if ILMapper.is_temp_reg(a):
            if ILMapper.is_temp_reg(b):
                return f"ldloc {a}\nldloc {b}\nadd\nstloc {result_reg}\n"
            else:
                return f"ldloc {a}\nldc.i8 {b}\nadd\nstloc {result_reg}\n"
        else:
            if ILMapper.is_temp_reg(b):
                return f"ldc.i8 {a}\nldloc {b}\nadd\nstloc {result_reg}\n"
            else:
                return f"ldc.i8 {a}\nldc.i8 {b}\nadd\nstloc {result_reg}\n"

    @staticmethod
    def sub(result_reg, a, b):
        if ILMapper.is_temp_reg(a):
            if ILMapper.is_temp_reg(b):
                return f"ldloc {a}\nldloc {b}\nsub\nstloc {result_reg}\n"
            else:
                return f"ldloc {a}\nldc.i8 {b}\nsub\nstloc {result_reg}\n"
        else:
            if ILMapper.is_temp_reg(b):
                return f"ldc.i8 {a}\nldloc {b}\nsub\nstloc {result_reg}\n"
            else:
                return f"ldc.i8 {a}\nldc.i8 {b}\nsub\nstloc {result_reg}\n"
