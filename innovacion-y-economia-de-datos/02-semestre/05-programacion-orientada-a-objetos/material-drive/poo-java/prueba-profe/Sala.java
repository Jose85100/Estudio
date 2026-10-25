package prueba;

/**
 *
 * @author red
 */
public class Sala {

    private boolean[][] sillas = new boolean[10][10];

    private Pelicula pelicula;

    public Sala(Pelicula p) {
        this.pelicula=p;
        
        for (int i = 0; i < sillas.length; i++) {
            for (int j = 0; j < sillas[i].length; j++) {
                sillas[i][j] = false;
            }
        }
    }

    public boolean validarSillaLibre(int x, int y) {
        return !sillas[x][y];
    }

    public void reservarSilla(int x, int y) {
        sillas[x][y] = true;
    }

    /**
     * @return the pelicula
     */
    public Pelicula getPelicula() {
        return pelicula;
    }

    /**
     * @param pelicula the pelicula to set
     */
    public void setPelicula(Pelicula pelicula) {
        this.pelicula = pelicula;
    }

}
