class Distribuir(object):
    def __init__(self, dosis, duracion):
        self.duracion = duracion
        self.dosis = dosis
        self.distribucion = []
        self.distribuir()
        if (dosis % duracion != 0):
            self.Bjorklund()

    def distribuir(self):
        # '//' obtiene la parte de entera del cociente
        dosis_dia = self.dosis // self.duracion
        for i in range(0, self.duracion):
            self.distribucion.append(dosis_dia)
    
    def flatten(self, l):
        while (1 < len(l)):
            l[0].extend(l.pop(1))
        l = l[0]
        for i in range(len(l)):
            self.distribucion[i] += l[i]

    def Bjorklund(self):
        samples = self.dosis % self.duracion
        interval = self.duracion
        distributed_strings = []
        remaining_strings = []
        for i in range(0, samples):
            distributed_strings.append([1])
        for i in range(0, interval - samples):
            remaining_strings.append([0])
        
        while(1 < len(remaining_strings)):
            make_new_remaining_strings = \
                len(remaining_strings) < len(distributed_strings)
            former_remaining_strings_length = len(remaining_strings)
            elements_to_join = \
                min(len(distributed_strings), len(remaining_strings))
            for i in range(0, elements_to_join):
                distributed_strings[i].extend(remaining_strings[0])
                remaining_strings.pop(0)
            if (make_new_remaining_strings):
                remaining_strings = distributed_strings[former_remaining_strings_length:]
                distributed_strings = \
                    distributed_strings[0: former_remaining_strings_length]
        if len(remaining_strings) > 0 :
            distributed_strings[0].extend(remaining_strings.pop(0))
        self.flatten(distributed_strings)
