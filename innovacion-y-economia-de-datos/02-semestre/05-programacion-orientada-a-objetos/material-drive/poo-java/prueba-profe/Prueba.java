package prueba;

import javax.swing.JOptionPane;

/**
 *
 * @author red
 */
public class Prueba {

    
    public static void main(String[] args) {
        
        Pelicula batman=new Pelicula("THE BATMAN",12);
        
        Pelicula padrino=new Pelicula("The Godfather",15);
        
        Sala sala1=new Sala(padrino);
        Sala sala2=new Sala(padrino);
        Sala sala3=new Sala(batman);
        Sala sala4=new Sala(batman);
        
        Persona p1=new Persona("Gabriel",14);
        Persona p2=new Persona("Apolonia",17);
        
        String k=JOptionPane.showInputDialog("ASDFASDFASDF");
        int j=Integer.parseInt(k);  
        Boleto b=new Boleto();
        if(b.comprar(p2, sala4, 5, 5)){
            System.out.println("Compra exitosa");
        }else{
            System.out.println("Compra NO exitosa");
        }
        
        Boleto b1=new Boleto();
        if(b1.comprar(p1, sala2, 8, 6)){
            System.out.println("Compra exitosa");
        }else{
            System.out.println("Compra NO exitosa");
        }

        
    }
    
}
