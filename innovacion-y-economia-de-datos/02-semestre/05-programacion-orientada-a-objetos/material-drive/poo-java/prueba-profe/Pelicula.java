
package prueba;

/**
 *
 * @author red
 */
public class Pelicula {
    private String nombre;
    private int clasificacion;

    public Pelicula(String nombre,int clasificacion){
        this.nombre=nombre;
        this.clasificacion=clasificacion;
    }
    
    /**
     * @return the nombre
     */
    public String getNombre() {
        return nombre;
    }

    /**
     * @param nombre the nombre to set
     */
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    /**
     * @return the clasificacion
     */
    public int getClasificacion() {
        return clasificacion;
    }

    /**
     * @param clasificacion the clasificacion to set
     */
    public void setClasificacion(int clasificacion) {
        this.clasificacion = clasificacion;
    }
    
    
    
}
