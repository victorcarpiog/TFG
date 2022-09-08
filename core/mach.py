    #!/usr/bin/env python
    # coding: utf-8

    # In[1]:
    #pip install -U sentence-transformers


    # In[2]:


from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from pprint import pprint


def modelo(id, respuesta):
      

    # In[3]:


    model= SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')


# In[4]:

    # In[5]:

    if(id==1):
        
        respuestas1=['No me siento triste',
                    'Me siento triste gran parte del tiempo',
                    'Me siento triste todo el tiempo',
                    'Me siento tan triste o soy tan infeliz que no puedo soportarlo']
        preg1= respuesta
        embeddings1=model.encode(respuestas1)
        input1=model.encode(preg1)
        #variable sumatorio de puntuaciones


        largo1= len(embeddings1)
        r11=cosine_similarity(embeddings1[0].reshape(1,-1), input1.reshape(1,-1))
        r12=cosine_similarity(embeddings1[1].reshape(1,-1), input1.reshape(1,-1))
        r13=cosine_similarity(embeddings1[2].reshape(1,-1), input1.reshape(1,-1))
        r14=cosine_similarity(embeddings1[3].reshape(1,-1), input1.reshape(1,-1))

        lista_respuestas1=[r11, r12, r13, r14]

        aux=r11
        i=0
        punt1=0
        for i in range (largo1) :
            if (lista_respuestas1[i] > aux):
                
                aux= lista_respuestas1[i]
                punt1=i
                
     
        return punt1
    elif(id==2):
     
        respuestas2=['No estoy desalentado respecto del mi futuro.',
                    'Me siento más desalentado respecto de mi futuro que lo que solía estarlo. ',
                    'No espero que las cosas funcionen para mi.',
                    'Siento que no hay esperanza para mi futuro y que sólo puede empeorar.']
        preg2= respuesta
        embeddings2=model.encode(respuestas2)
        input2=model.encode(preg2)

        largo2= len(embeddings2)

        r21=cosine_similarity(embeddings2[0].reshape(1,-1), input2.reshape(1,-1))
        r22=cosine_similarity(embeddings2[1].reshape(1,-1), input2.reshape(1,-1))
        r23=cosine_similarity(embeddings2[2].reshape(1,-1), input2.reshape(1,-1))
        r24=cosine_similarity(embeddings2[3].reshape(1,-1), input2.reshape(1,-1))

        lista_respuestas2=[r21, r22, r23, r24]

        aux=r21
        i=0
        punt1=0
        for i in range (largo2) :
            if (lista_respuestas2[i] > aux):
                
                aux= lista_respuestas2[i]
                punt1=i
                
        
        return punt1
    elif(id==3):

    
        respuestas3=['No me siento como un fracasado.',
                    'He fracasado más de lo que hubiera debido.',
                    'Cuando miro hacia atrás, veo muchos fracasos.',
                    'Siento que como persona soy un fracaso total.']
        preg3= respuesta
        embeddings3=model.encode(respuestas3)
        input3=model.encode(preg3)

        largo3= len(embeddings3)

        r31=cosine_similarity(embeddings3[0].reshape(1,-1), input3.reshape(1,-1))
        r32=cosine_similarity(embeddings3[1].reshape(1,-1), input3.reshape(1,-1))
        r33=cosine_similarity(embeddings3[2].reshape(1,-1), input3.reshape(1,-1))
        r34=cosine_similarity(embeddings3[3].reshape(1,-1), input3.reshape(1,-1))

        lista_respuestas3=[r31, r32, r33, r34]


        aux=r31
        i=0
        punt1=0
        for i in range (largo3) :
            if (lista_respuestas3[i] > aux):
                
                aux= lista_respuestas3[i]
                punt1=i
        return punt1
  


    elif(id==4):
        respuestas4=['Obtengo tanto placer como siempre por las cosas de las que disfruto.',
                    'No disfruto tanto de las cosas como solía hacerlo.',
                    'Obtengo muy poco placer de las cosas que solía disfrutar. ',
                    'No puedo obtener ningún placer de las cosas de las que solía disfrutar.']
        preg4= respuesta
        embeddings4=model.encode(respuestas4)
        input4=model.encode(preg4)

        largo4= len(embeddings4)
  
        r41=cosine_similarity(embeddings4[0].reshape(1,-1), input4.reshape(1,-1))
        r42=cosine_similarity(embeddings4[1].reshape(1,-1), input4.reshape(1,-1))
        r43=cosine_similarity(embeddings4[2].reshape(1,-1), input4.reshape(1,-1))
        r44=cosine_similarity(embeddings4[3].reshape(1,-1), input4.reshape(1,-1))
        lista_respuestas4=[r41, r42, r43, r44]

        aux=r41
        i=0
        punt1=0
        for i in range (largo4) :
            if (lista_respuestas4[i] > aux):
                
                aux= lista_respuestas4[i]
                punt1=i
        return punt1       
 
    elif(id==5):
 
        respuestas5=['No me siento particularmente culpable.',
                    'Me siento culpable respecto de varias cosas que he hecho o que debería haber hecho.',
                    'Me siento bastante culpable la mayor parte del tiempo.',
                    'Me siento culpable todo el tiempo.']
        preg5= respuesta
        embeddings5=model.encode(respuestas5)
        input5=model.encode(preg5)

        largo5= len(embeddings5)

        r51=cosine_similarity(embeddings5[0].reshape(1,-1), input5.reshape(1,-1))
        r52=cosine_similarity(embeddings5[1].reshape(1,-1), input5.reshape(1,-1))
        r53=cosine_similarity(embeddings5[2].reshape(1,-1), input5.reshape(1,-1))
        r54=cosine_similarity(embeddings5[3].reshape(1,-1), input5.reshape(1,-1))

        lista_respuestas5=[r51, r52, r53, r54]


        aux=r51
        i=0
        punt1=0
        for i in range (largo5) :
            if (lista_respuestas5[i] > aux):
                
                aux= lista_respuestas5[i]
                punt1=i
                
        return punt1

    elif(id==6):
    
        respuestas6=['No siento que este siendo castigado',
                    'Siento que tal vez pueda ser castigado. ',
                    'Espero ser castigado.',
                    'Siento que estoy siendo castigado.']
        preg6= respuesta
        embeddings6=model.encode(respuestas6)
        input6=model.encode(preg6)

        largo6= len(embeddings6)

        r61=cosine_similarity(embeddings6[0].reshape(1,-1), input6.reshape(1,-1))
        r62=cosine_similarity(embeddings6[1].reshape(1,-1), input6.reshape(1,-1))
        r63=cosine_similarity(embeddings6[2].reshape(1,-1), input6.reshape(1,-1))
        r64=cosine_similarity(embeddings6[3].reshape(1,-1), input6.reshape(1,-1))

        lista_respuestas6=[r61, r62, r63, r64]

        aux=r61
        i=0
        punt1=0
        for i in range (largo6) :
            if (lista_respuestas6[i] > aux):
                
                aux= lista_respuestas6[i]
                punt1=i
        return punt1

    elif(id==7):
    
        respuestas7=['Siento acerca de mi lo mismo que siempre.',
                    'He perdido la confianza en mí mismo. ',
                    'Estoy decepcionado conmigo mismo.',
                    'No me gusto a mí mismo.']
        preg7= respuesta
        embeddings7=model.encode(respuestas7)
        input7=model.encode(preg7)

        largo7= len(embeddings7)

        r71=cosine_similarity(embeddings7[0].reshape(1,-1), input7.reshape(1,-1))
        r72=cosine_similarity(embeddings7[1].reshape(1,-1), input7.reshape(1,-1))
        r73=cosine_similarity(embeddings7[2].reshape(1,-1), input7.reshape(1,-1))
        r74=cosine_similarity(embeddings7[3].reshape(1,-1), input7.reshape(1,-1))

        lista_respuestas7=[r71, r72, r73, r74]

        aux=r71
        i=0
        punt1=0
        for i in range (largo7) :
            if (lista_respuestas7[i] > aux):
                
                aux= lista_respuestas7[i]
                punt1=i
                
        return punt1

    elif(id==8):
    
        respuestas8=['No me critico ni me culpo más de lo habitual.',
                    'Estoy más crítico conmigo mismo de lo que solía estarlo.',
                    'Me critico a mí mismo por todos mis errores.',
                    'Me culpo a mí mismo por todo lo malo que sucede.']
        preg8= respuesta
        embeddings8=model.encode(respuestas8)
        input8=model.encode(preg8)

        largo8= len(embeddings8)

        r81=cosine_similarity(embeddings8[0].reshape(1,-1), input8.reshape(1,-1))
        r82=cosine_similarity(embeddings8[1].reshape(1,-1), input8.reshape(1,-1))
        r83=cosine_similarity(embeddings8[2].reshape(1,-1), input8.reshape(1,-1))
        r84=cosine_similarity(embeddings8[3].reshape(1,-1), input8.reshape(1,-1))
    
        lista_respuestas8=[r81, r82, r83, r84]

        aux=r81
        i=0
        punt1=0
        for i in range (largo8) :
            if (lista_respuestas8[i] > aux):
                
                aux= lista_respuestas8[i]
                punt1=i
        return punt1


    elif(id==9):
     
        respuestas9=['No tengo ningún pensamiento de matarme.',
                    'He tenido pensamientos de matarme, pero no lo haría',
                    'Querría matarme ',
                    'Me mataría si tuviera la oportunidad de hacerlo.']
        preg9= respuesta
        embeddings9=model.encode(respuestas9)
        input9=model.encode(preg9)

        largo9= len(embeddings9)

        r91=cosine_similarity(embeddings9[0].reshape(1,-1), input9.reshape(1,-1))
        r92=cosine_similarity(embeddings9[1].reshape(1,-1), input9.reshape(1,-1))
        r93=cosine_similarity(embeddings9[2].reshape(1,-1), input9.reshape(1,-1))
        r94=cosine_similarity(embeddings9[3].reshape(1,-1), input9.reshape(1,-1))

        lista_respuestas9=[r91, r92, r93, r94]

        aux=r91
        i=0
        punt1=0
        for i in range (largo9) :
            if (lista_respuestas9[i] > aux):
                
                aux= lista_respuestas9[i]
                punt1=i
                
        return punt1

    elif(id==10):
        
        respuestas10=['No lloro más de lo que solía hacerlo.',
                    'Lloro más de lo que solía hacerlo',
                    'Lloro por cualquier pequeñez.',
                    'Siento ganas de llorar pero no puedo.']
        preg10= respuesta
        embeddings10=model.encode(respuestas10)
        input10=model.encode(preg10)

        largo10= len(embeddings10)

        r101=cosine_similarity(embeddings10[0].reshape(1,-1), input10.reshape(1,-1))
        r102=cosine_similarity(embeddings10[1].reshape(1,-1), input10.reshape(1,-1))
        r103=cosine_similarity(embeddings10[2].reshape(1,-1), input10.reshape(1,-1))
        r104=cosine_similarity(embeddings10[3].reshape(1,-1), input10.reshape(1,-1))

        lista_respuestas10=[r101, r102, r103, r104]

        aux=r101
        i=0
        punt1=0
        for i in range (largo10) :
            if (lista_respuestas10[i] > aux):
                
                aux= lista_respuestas10[i]
                punt1=i
        return punt1       

    elif(id==11):
    
        respuestas11=['No estoy más inquieto o tenso que lo habitual.',
                    'Me siento más inquieto o tenso que lo habitual.',
                    'Estoy tan inquieto o agitado que me es difícil quedarme quieto ',
                    'Estoy tan inquieto o agitado que tengo que estar siempre en movimiento o haciendo algo.']
        preg11= respuesta
        embeddings11=model.encode(respuestas11)
        input11=model.encode(preg11)

        largo11= len(embeddings11)

        r111=cosine_similarity(embeddings11[0].reshape(1,-1), input11.reshape(1,-1))
        r112=cosine_similarity(embeddings11[1].reshape(1,-1), input11.reshape(1,-1))
        r113=cosine_similarity(embeddings11[2].reshape(1,-1), input11.reshape(1,-1))
        r114=cosine_similarity(embeddings11[3].reshape(1,-1), input11.reshape(1,-1))

        lista_respuestas11=[r111, r112, r113, r114]


        aux=r111
        i=0
        punt1=0
        for i in range (largo11) :
            if (lista_respuestas11[i] > aux):
                
                aux= lista_respuestas11[i]
                punt1=i
                
        return punt1

    elif(id==12):

        respuestas12=['No he perdido el interés en otras actividades o personas.',
                    'Estoy menos interesado que antes en otras personas o cosas.',
                    'He perdido casi todo el interés en otras personas o cosas.',
                    'Me es difícil interesarme por algo.']
        preg12 = respuesta
        embeddings12=model.encode(respuestas12)
        input12=model.encode(preg12)


        largo12= len(embeddings12)

        r121=cosine_similarity(embeddings12[0].reshape(1,-1), input12.reshape(1,-1))
        r122=cosine_similarity(embeddings12[1].reshape(1,-1), input12.reshape(1,-1))
        r123=cosine_similarity(embeddings12[2].reshape(1,-1), input12.reshape(1,-1))
        r124=cosine_similarity(embeddings12[3].reshape(1,-1), input12.reshape(1,-1))

        lista_respuestas12=[r121, r122, r123, r124]

        aux=r121
        i=0
        punt1=0
        for i in range (largo12) :
            if (lista_respuestas12[i] > aux):
                
                aux= lista_respuestas12[i]
                punt1=i
                
        return punt1

    elif(id==13):
    
        respuestas13=['Tomo mis propias decisiones tan bien como siempre.',
                    'Me resulta más difícil que de costumbre tomar decisiones.',
                    'Encuentro mucha más dificultad que antes para tomar decisiones.',
                    'Tengo problemas para tomar cualquier decisión.']
        preg13= respuesta
        embeddings13=model.encode(respuestas13)
        input13=model.encode(preg13)

        largo13= len(embeddings13)

        r131=cosine_similarity(embeddings13[0].reshape(1,-1), input13.reshape(1,-1))
        r132=cosine_similarity(embeddings13[1].reshape(1,-1), input13.reshape(1,-1))
        r133=cosine_similarity(embeddings13[2].reshape(1,-1), input13.reshape(1,-1))
        r134=cosine_similarity(embeddings13[3].reshape(1,-1), input13.reshape(1,-1))

        lista_respuestas13=[r131, r132, r133, r134]

        aux=r131
        i=0
        punt1=0
        for i in range (largo13) :
            if (lista_respuestas13[i] > aux):
                
                aux= lista_respuestas13[i]
                punt1=i
                
        return punt1

    elif(id==14):
  
        respuestas14=['No siento que yo no sea valioso',
                    'No me considero a mi mismo tan valioso y útil como solía considerarme',
                    'Me siento menos valioso cuando me comparo con otros',
                    'Siento que no valgo nada.']
        preg14= respuesta
        embeddings14=model.encode(respuestas14)
        input14=model.encode(preg14)

        largo14= len(embeddings14)

        r141=cosine_similarity(embeddings14[0].reshape(1,-1), input14.reshape(1,-1))
        r142=cosine_similarity(embeddings14[1].reshape(1,-1), input14.reshape(1,-1))
        r143=cosine_similarity(embeddings14[2].reshape(1,-1), input14.reshape(1,-1))
        r144=cosine_similarity(embeddings14[3].reshape(1,-1), input14.reshape(1,-1))

        lista_respuestas14=[r141, r142, r143, r144]

        aux=r141
        i=0
        punt1=0
        for i in range (largo14) :
            if (lista_respuestas14[i] > aux):
                
                aux= lista_respuestas14[i]
                punt1=i
                
        return punt1

    elif(id==15):

        respuestas15=['Tengo tanta energía como siempre.',
                    'Tengo menos energía que la que solía tener. ',
                    'No tengo suficiente energía para hacer demasiado. ',
                    'No tengo energía suficiente para hacer nada. ']
        preg15= respuesta
        embeddings15=model.encode(respuestas15)
        input15=model.encode(preg15)

        largo15= len(embeddings15)

        r151=cosine_similarity(embeddings15[0].reshape(1,-1), input15.reshape(1,-1))
        r152=cosine_similarity(embeddings15[1].reshape(1,-1), input15.reshape(1,-1))
        r153=cosine_similarity(embeddings15[2].reshape(1,-1), input15.reshape(1,-1))
        r154=cosine_similarity(embeddings15[3].reshape(1,-1), input15.reshape(1,-1))

        lista_respuestas15=[r151, r152, r153, r154]

        aux=r151
        i=0
        punt1=0
        for i in range (largo15) :
            if (lista_respuestas15[i] > aux):
                
                aux= lista_respuestas15[i]
                punt1=i
                
        return punt1

    elif(id==16):
 
        respuestas16=['No he experimentado ningún cambio en mis hábitos de sueño.',
                    'Duermo un poco más o un poco menos de lo habitual',
                    'Duermo mucho más o mucho menos de lo habitual',
                    'Me despierto 1-2 horas más temprano y no puedo volver a dormirme']
        preg16= respuesta
        embeddings16=model.encode(respuestas16)
        input16=model.encode(preg16)

        largo16= len(embeddings16)

        r161=cosine_similarity(embeddings16[0].reshape(1,-1), input16.reshape(1,-1))
        r162=cosine_similarity(embeddings16[1].reshape(1,-1), input16.reshape(1,-1))
        r163=cosine_similarity(embeddings16[2].reshape(1,-1), input16.reshape(1,-1))
        r164=cosine_similarity(embeddings16[3].reshape(1,-1), input16.reshape(1,-1))



        lista_respuestas16=[r161, r162, r163, r164]



        aux=r161
        i=0
        punt1=0
        for i in range (largo16) :
            if (lista_respuestas16[i] > aux):
                
                aux= lista_respuestas16[i]
                punt1=i
                    
        return punt1


    elif(id==17):
        respuestas17=['No estoy tan irritable que lo habitual.',
                    'Estoy más irritable que lo habitual.',
                    'Estoy mucho más irritable que lo habitual.',
                    'Estoy irritable todo el tiempo.']
        preg17= respuesta
        embeddings17=model.encode(respuestas17)
        input17=model.encode(preg17)


        largo17= len(embeddings17)

        r171=cosine_similarity(embeddings17[0].reshape(1,-1), input17.reshape(1,-1))
        r172=cosine_similarity(embeddings17[1].reshape(1,-1), input17.reshape(1,-1))
        r173=cosine_similarity(embeddings17[2].reshape(1,-1), input17.reshape(1,-1))
        r174=cosine_similarity(embeddings17[3].reshape(1,-1), input17.reshape(1,-1))


        lista_respuestas17=[r171, r172, r173, r174]


        aux=r171
        i=0
        punt1=0
        for i in range (largo17) :
            if (lista_respuestas17[i] > aux):
                
                aux= lista_respuestas17[i]
                punt1=i
                
        return punt1

    elif(id==18):

        respuestas18=['No he experimentado ningún cambio en mi apetito. ',
                    'Mi apetito es un poco menor o mayor de lo habitual',
                    'mi apetito es mucho menor o mucho mayor que antes',
                    'No tengo apetito en absoluto.']
        preg18= respuesta
        embeddings18=model.encode(respuestas18)
        input18=model.encode(preg18)

        largo18= len(embeddings18)

        r181=cosine_similarity(embeddings18[0].reshape(1,-1), input18.reshape(1,-1))
        r182=cosine_similarity(embeddings18[1].reshape(1,-1), input18.reshape(1,-1))
        r183=cosine_similarity(embeddings18[2].reshape(1,-1), input18.reshape(1,-1))
        r184=cosine_similarity(embeddings18[3].reshape(1,-1), input18.reshape(1,-1))


        lista_respuestas18=[r181, r182, r183, r184]

        aux=r181
        i=0
        punt1=0
        for i in range (largo18) :
            if (lista_respuestas18[i] > aux):
                
                aux= lista_respuestas18[i]
                punt1=i
                    
        return punt1


    elif(id==19):
        respuestas19=['Puedo concentrarme tan bien como siempre.',
                    'No puedo concentrarme tan bien como habitualmente',
                    'Me es difícil mantener la mente en algo por mucho tiempo.',
                    'Encuentro que no puedo concentrarme en nada.']
        preg19= respuesta
        embeddings19=model.encode(respuestas19)
        input19=model.encode(preg19)

        largo19= len(embeddings19)

        r191=cosine_similarity(embeddings19[0].reshape(1,-1), input19.reshape(1,-1))
        r192=cosine_similarity(embeddings19[1].reshape(1,-1), input19.reshape(1,-1))
        r193=cosine_similarity(embeddings19[2].reshape(1,-1), input19.reshape(1,-1))
        r194=cosine_similarity(embeddings19[3].reshape(1,-1), input19.reshape(1,-1))


        lista_respuestas19=[r191, r192, r193, r194]


        aux=r191
        i=0
        punt1=0
        for i in range (largo19) :
            if (lista_respuestas19[i] > aux):
                
                aux= lista_respuestas19[i]
                punt1=i
                
        return punt1


    elif(id==20):
        respuestas20=['No estoy más cansado o fatigado que lo habitual.',
                    'Me fatigo o me canso más fácilmente que lo habitual.',
                    'Estoy demasiado fatigado o cansado para hacer muchas de las cosas que solía hacer.',
                    'Estoy demasiado fatigado o cansado para hacer la mayoría de las cosas que solía hacer']
        preg20= respuesta
        embeddings20=model.encode(respuestas20)
        input20=model.encode(preg20)

        largo20= len(embeddings20)

        r201=cosine_similarity(embeddings20[0].reshape(1,-1), input20.reshape(1,-1))
        r202=cosine_similarity(embeddings20[1].reshape(1,-1), input20.reshape(1,-1))
        r203=cosine_similarity(embeddings20[2].reshape(1,-1), input20.reshape(1,-1))
        r204=cosine_similarity(embeddings20[3].reshape(1,-1), input20.reshape(1,-1))

        lista_respuestas20=[r201, r202, r203, r204]


        aux=r201
        i=0
        punt1=0
        for i in range (largo20) :
            if (lista_respuestas20[i] > aux):
                
                aux= lista_respuestas20[i]
                punt1=i
                
        return punt1

    elif(id==21):

        respuestas21=['No he notado ningún cambio reciente en mi interés por el sexo.',
                    'Estoy menos interesado en el sexo de lo que solía estarlo. ',
                    'Estoy mucho menos interesado en el sexo. ',
                    'He perdido completamente el interés en el sexo.']
        preg21 = respuesta
        embeddings21=model.encode(respuestas21)
        input21=model.encode(preg21)

        largo21= len(embeddings21)

        r211=cosine_similarity(embeddings21[0].reshape(1,-1), input21.reshape(1,-1))
        r212=cosine_similarity(embeddings21[1].reshape(1,-1), input21.reshape(1,-1))
        r213=cosine_similarity(embeddings21[2].reshape(1,-1), input21.reshape(1,-1))
        r214=cosine_similarity(embeddings21[3].reshape(1,-1), input21.reshape(1,-1))

        lista_respuestas21=[r211, r212, r213, r214]


        aux=r211
        i=0
        punt1=0
        for i in range (largo21) :
            if (lista_respuestas21[i] > aux):
                
                aux= lista_respuestas21[i]
                punt1=i
                
        return punt1


   # if(sumatorio< 14):
    #    pprint("Usted padece depresión mínima")
    #elif( 13< sumatorio <20 ):
     #   pprint("Usted padece depresión leve")
    #elif (19< sumatorio <29):
     #   pprint("Usted padece depresión moderada")
    #else:
     #   pprint("Usted padece depresión grave")
        


# In[ ]:




