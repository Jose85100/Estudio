package hospital;

public class Asignador {

    private Doctor[] doctores;
    private Paciente[] pacientes;
    private Cita[] citas;

    public String validar() {
        return null;
    }

    public String crearCita() {
        return null;
    }

    public String imprimirCitas() {
        return null;
    }

    /**
     * @return the doctores
     */
    public Doctor[] getDoctores() {
        return doctores;
    }

    /**
     * @param doctores the doctores to set
     */
    public void setDoctores(Doctor[] doctores) {
        this.doctores = doctores;
    }

    /**
     * @return the pacientes
     */
    public Paciente[] getPacientes() {
        return pacientes;
    }

    /**
     * @param pacientes the pacientes to set
     */
    public void setPacientes(Paciente[] pacientes) {
        this.pacientes = pacientes;
    }

    /**
     * @return the citas
     */
    public Cita[] getCitas() {
        return citas;
    }

    /**
     * @param citas the citas to set
     */
    public void setCitas(Cita[] citas) {
        this.citas = citas;
    }
}
