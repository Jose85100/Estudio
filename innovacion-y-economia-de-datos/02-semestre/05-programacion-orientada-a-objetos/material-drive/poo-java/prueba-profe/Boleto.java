package prueba;

public class Boleto {

    private Persona p;
    private int sillaX;
    private int sillaY;
    private Sala sala;
    private long price =16000;

    
    public boolean comprar(Persona p, Sala s, int x, int y) {

        if (s.validarSillaLibre(x, y)) {
            if (p.getAge() >= s.getPelicula().getClasificacion()) {
                this.p = p;
                this.sala=s;
                sala.reservarSilla(x, y);
                return true;
            }

        }
       return false; 
    }

}
