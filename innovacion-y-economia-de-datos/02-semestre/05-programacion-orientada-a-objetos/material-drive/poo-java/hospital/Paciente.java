package hospital;

public class Paciente {

    private String nombre;
    private String enfermedad;
    private int edad;
    private int gradoDoctor;

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
     * @return the enfermedad
     */
    public String getEnfermedad() {
        return enfermedad;
    }

    /**
     * @param enfermedad the enfermedad to set
     */
    public void setEnfermedad(String enfermedad) {
        this.enfermedad = enfermedad;
    }

    /**
     * @return the edad
     */
    public int getEdad() {
        return edad;
    }

    /**
     * @param edad the edad to set
     */
    public void setEdad(int edad) {
        this.edad = edad;
    }

    /**
     * @return the gradoDoctor
     */
    public int getGradoDoctor() {
        return gradoDoctor;
    }

    /**
     * @param gradoDoctor the gradoDoctor to set
     */
    public void setGradoDoctor(int gradoDoctor) {
        this.gradoDoctor = gradoDoctor;
    }
}
