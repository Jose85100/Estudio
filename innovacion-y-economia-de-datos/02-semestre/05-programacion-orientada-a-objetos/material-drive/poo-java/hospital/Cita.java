package hospital;

public class Cita {

    private Paciente p;
    private Doctor d;
    private int dia;
    private int mes;
    private int hora;

    public String asignarCita(Paciente p, Doctor d) {
        return null;
    }

    public String establecerHora(int dia, int mes, int hora) {
        return null;
    }

    public String imprimir() {
        return null;
    }

    /**
     * @return the p
     */
    public Paciente getP() {
        return p;
    }

    /**
     * @param p the p to set
     */
    public void setP(Paciente p) {
        this.p = p;
    }

    /**
     * @return the d
     */
    public Doctor getD() {
        return d;
    }

    /**
     * @param d the d to set
     */
    public void setD(Doctor d) {
        this.d = d;
    }

    /**
     * @return the dia
     */
    public int getDia() {
        return dia;
    }

    /**
     * @param dia the dia to set
     */
    public void setDia(int dia) {
        this.dia = dia;
    }

    /**
     * @return the mes
     */
    public int getMes() {
        return mes;
    }

    /**
     * @param mes the mes to set
     */
    public void setMes(int mes) {
        this.mes = mes;
    }

    /**
     * @return the hora
     */
    public int getHora() {
        return hora;
    }

    /**
     * @param hora the hora to set
     */
    public void setHora(int hora) {
        this.hora = hora;
    }
}
