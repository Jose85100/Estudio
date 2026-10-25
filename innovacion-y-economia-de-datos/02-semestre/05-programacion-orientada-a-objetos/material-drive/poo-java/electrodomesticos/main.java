package personas;

import java.util.Random;

public class main {

    public static void main(String[] args) {
        Electrodomesticos aparatos[]=new Electrodomesticos[10];
        
        //Aspiradora samsung1=new Aspiradora();
        //samsung1.encender();
        
        for (int i=0; i<aparatos.length;i++){
            aparatos[i]=new Electrodomesticos();
            Random u=new Random();
            
            int o=u.nextInt(10);
            
            //tipo de electrodomestico 
            if(o>=0 && o<=3){
                aparatos[i].setNombre("Aspiradora "+o);
            }
            if(o>=4&& o<=6){
                aparatos[i].setNombre("Brilladora "+o);
            }
            if(o>=7&& o<=10){
                aparatos[i].setNombre("Ventilador "+o);
            }
            //marcas
            if(o==1||o==4||o==8){
                aparatos[i].setMarca("Samgung "+i);
            }
            if(o==2||o==5||o==9){
                aparatos[i].setMarca("Lg "+i);
            }
            if(o==3||o==6||o==10){
                aparatos[i].setMarca("Whirlpool "+i);
            }
            if(o==0||o==4||o==7){
                aparatos[i].setMarca("Bosch "+i);
            }
            
        }
        
        for (int i=0; i<aparatos.length;i++){
            System.out.println("El electrodomestico es "+ aparatos[i].getNombre()+" la marca es "+aparatos[i].getMarca());
            aparatos[i].encender();
        }
    }

}
