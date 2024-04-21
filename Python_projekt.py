import matplotlib.pyplot as plt

def stat(file):
    """Podatke o izpustu toplogrednih plinov držav v EU med leti 1990-2022,
    iz spletne strani 'https://ec.europa.eu/eurostat/web/environment/database' uredi.
                Urejene podatke prikaže z nekaj grafi"""
    
    info_I= []
    info_II = []
    drzave = []
    leta = list(range(1990,2023)) 
    file = open(f"{file}","r")
    plt.figure(figsize = [15,15]) #format grafa
    
    #grupa 1: TOTX4_MEMONIA - total, 
    #excluding LULUCF and memo items, including international aviation
    
    #grupa 2: TOTXMEMONIA - total,
    #excluding memo items, including international aviation

    #LULUCF - Land Use, Land Use Change and Forestry
    #memo items - international bunkers : which represent consumption of ships and aircraft on international routes. 

    for vrstica in file: #gremo skozi datoteko
        vrstica = vrstica.strip() 
        
        l = vrstica.split("\t") #locimo in shranimo v tab
        kl = l[0].split(",") #ime države
        
        if kl[3] == "I90" or l[0][-2:] == "20": #nepotrebno info. izpustimo 
            continue
        
        elif kl[2] == "TOTX4_MEMONIA": #prva grupa podatkov 
            drzave.append(l[0][-2:]) #shranimo ime države
            stevila = []
            for st in l[1:]:
                if "b" in st or "e" in st or "p" in st: #znebimo se crk 
                    st = st.strip("bep") 
                    stevila.append(float(st)) #pretvorimo v float()
                else:
                    stevila.append(float(st))
                
            info_I.append(stevila)
            
            
        elif kl[2] == "TOTXMEMONIA": #druga grupa podatkov
            stevila = []
            for st in l[1:]:
                if "b" in st or "e" in st or "p" in st:#znebimo se crk 
                    st = st.strip("bep")
                    stevila.append(float(st)) #pretvorimo v float()
                else:
                    stevila.append(float(st))
            info_II.append(stevila)
     
    explode=[]
    n = 0 
    povprecje_I = []
    for drzava in info_I:
        povp = sum(drzava)/len(drzava) #izračunamo povprečje izpusta drzave med 1990-2022 za 2 grupo
        povprecje_I.append(povp)
        if drzave[n] == "SI": #Slovenijo izpostavimo 
            plt.plot(leta, drzava, color = 'k', linestyle = 'dashed',label = f"{drzave[n]}",linewidth = 3)
            n += 1 
            explode.append(0.3) #za tortni diagram 
        else:
            plt.plot(leta, drzava, label = f"{drzave[n]}")
            n += 1
            explode.append(0) #za tortni diagram 
        
    plt.yticks(range(0,50,4))
    plt.xlabel("LETA")
    plt.ylabel("TONNES PER CAPITA")
    plt.title("Net greenhouse gas emissions \n (excluding memo items, including international aviation)")
    plt.legend()
    plt.show()
    
    plt.figure(figsize = [15,15]) #format grafa
    n = 0
    povprecje_II = []
    for drzava in info_II:
        povp = sum(drzava)/len(drzava) #izračunamo povprečje izpusta drzave med 1990-2022 za 2 grupo
        povprecje_II.append(povp)
        if drzave[n] == "SI": #Slovenijo izpostavimo
            plt.plot(leta, drzava, color = 'k', linestyle = 'dashed',label = f"{drzave[n]}",linewidth = 3)
            n += 1
        else:
            plt.plot(leta, drzava, label = f"{drzave[n]}")
            n += 1
        
    n = 0
    
    
    plt.yticks(range(0,50,4))
    plt.xlabel("LETA")
    plt.ylabel("TONNES PER CAPITA")
    plt.title("Net greenhouse gas emissions \n (excluding LULUCF and memo items, including international aviation)")
    plt.legend()
    plt.show()
    
    
    #Povprecja 1990-2022(histrogram)
    
    #grupa 1
    plt.figure(figsize = [15,15])
    bar = plt.bar(drzave, povprecje_I, color ='b', alpha=.5)
    plt.xlabel("Drzave")
    plt.ylabel("TONNES PER CAPITA")
    plt.title("Average greenhouse gas emissions by country between 1990-2022 \n (excluding memo items, including international aviation)")
    bar[28].set_color('r') #stolpček za slo obarvamo rdeče
    plt.show()
    
    #grupa 2
    plt.figure(figsize = [15,15])
    bar = plt.bar(drzave, povprecje_II, color ='b', alpha=.5)
    plt.xlabel("Drzave")
    plt.ylabel("TONNES PER CAPITA")
    plt.title("Average greenhouse gas emissions by country between 1990-2022 \n (excluding LULUCF and memo items, including international aviation)")
    bar[28].set_color('r')  #stolpček za slo obarvamo rdeče
    plt.show()

    #Tortni diagram
    
    #grupa 1
    plt.figure(figsize = [15,15])
    delez_I = []
    n = 0
    for st in povprecje_I:
        r = round(((100 * st) / sum(povprecje_I)),2)
        delez_I.append(f"{drzave[n]} {r}%")
        n += 1
    
    plt.pie(povprecje_I, labels=delez_I,explode=explode,wedgeprops = {'linewidth':1,'edgecolor':'white'})
    plt.title("Average greenhouse gas emissions by country in % between 1990-2022 \n (excluding memo items, including international aviation)")
    centre_circle = plt.Circle((0,0),0.70,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    plt.show()
    
    #grupa 2
    plt.figure(figsize = [15,15])
    delez_II = []
    n = 0
    for st in povprecje_II:
        r = round(((100 * st) / sum(povprecje_II)),2)
        delez_II.append(f"{drzave[n]} {r}%")
        n += 1
    
    plt.pie(povprecje_II, labels=delez_II,explode=explode,wedgeprops = {'linewidth':1,'edgecolor':'white'})
    plt.title("Average greenhouse gas emissions by country in % btween 1990-2022\n (excluding LULUCF and memo items, including international aviation)")
    centre_circle = plt.Circle((0,0),0.70,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    plt.show()

    #Povprečni izpust toplogrednih plinov v evropi ter primerjava s Slovenijo 

    
    plt.figure(figsize = [15,15])
    
    skupaj_letno_I = [round(sum(st)/len(info_I),2) for st in zip(*info_I)] #izra
    skupaj_letno_II = [round(sum(st)/len(info_II),2) for st in zip(*info_II)]
    
    #grupa 1
    plt.plot(leta, skupaj_letno_I, label = "Povprecje",color="r")
    plt.plot(leta, info_I[28], color = 'b', linestyle = '-',label = f"SLO",linewidth = 2)
    plt.title("Slovenia compared to avarage greenhouse gas emissions in EU 1990-2022 \n (excluding memo items, including international aviation)")
    plt.fill_between(leta,skupaj_letno_I,color="red", alpha=.5)
    plt.fill_between(leta,info_I[28],color="blue", alpha=.5)
    plt.xlabel("LETA")
    plt.ylabel("TONNES PER CAPITA")
    plt.legend()
    plt.show()
    
    #grupa 2
    plt.figure(figsize = [15,15])
    plt.plot(leta, skupaj_letno_II, label = "Povprecje",color="r")
    plt.plot(leta, info_II[28], color = 'b', linestyle = '-',label = f"SLO",linewidth = 2)
    plt.title("Slovenia compared to avarage greenhouse gas emissions in EU 1990-2022\n (excluding LULUCF and memo items, including international aviation)")
    plt.fill_between(leta,skupaj_letno_II,color="red", alpha=.5)
    plt.fill_between(leta,info_II[28],color="blue", alpha=.5)
    plt.xlabel("LETA")
    plt.ylabel("TONNES PER CAPITA")
    plt.legend()
    plt.show()

stat(r"c:\Users\zagil\Downloads\other stuff\sola\študij\leto2\PRO_2\python_projekt_PRO2_2024\estat_sdg_13_10.tsv") 