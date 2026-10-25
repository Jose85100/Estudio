package personas;

public class Electrodomesticos {
    private String Nombre;
    private String Referencia;
    private String Marca;

    public void encender() {
        System.out.println("Hola, he encendido");
    }
    public String getNombre() {
        return Nombre;
    }
    public void setNombre(String Nombre) {
        this.Nombre = Nombre;
    }
    public String getReferencia() {
        return Referencia;
    }
    public void setReferencia(String Referencia) {
        this.Referencia = Referencia;
    }
    public String getMarca() {
        return Marca;
    }
    public void setMarca(String Marca) {
        this.Marca = Marca;
    }
}
