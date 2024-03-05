
import java.util.Scanner;

public class Estacionamiento {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int capacidad = 10;
        int[] lugares = new int[capacidad];

        while (true) {
            System.out.println("1. Estacionar un auto");
            System.out.println("2. Retirar un auto");
            System.out.println("3. Mostrar los lugares ocupados");
            System.out.println("4. Salir");

            int opcion = sc.nextInt();

            if (opcion == 1) {
                estacionarAuto(lugares);
            } else if (opcion == 2) {
                retirarAuto(lugares);
            } else if (opcion == 3) {
                mostrarLugaresOcupados(lugares);
            } else if (opcion == 4) {
                break;
            } else {
                System.out.println("Opción inválida. Por favor, elija una opción válida.");
            }
        }
    }

    public static void estacionarAuto(int[] lugares) {
        for (int i = 0; i < lugares.length; i++) {
            if (lugares[i] == 0) {
                lugares[i] = 1;
                System.out.println("Auto estacionado en el lugar " + (i + 1));
                break;
            }
        }
    }

    public static void retirarAuto(int[] lugares) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Ingrese el número de lugar a retirar:");
        int numeroLugar = sc.nextInt();

        if (numeroLugar < 1 || numeroLugar > lugares.length) {
            System.out.println("Lugar inválido. Por favor, ingrese un número de lugar válido.");
            return;
        }

        if (lugares[numeroLugar - 1] == 1) {
            lugares[numeroLugar - 1] = 0;
            System.out.println("Auto retirado del lugar " + numeroLugar);
        } else {
            System.out.println("No hay ningún auto estacionado en ese lugar.");
        }
    }

    public static void mostrarLugaresOcupados(int[] lugares) {
        for (int i = 0; i < lugares.length; i++) {
            if (lugares[i] == 1) {
                System.out.println("Lugar " + (i + 1) + ": Ocupado");
            }
        }
    }
}

``` 
"""
        
Este programa
Java simula
un estacionamiento
con una
capacidad fija de 10
lugares. Permite estacionar autos,
retirar autos, mostrar
los lugares
ocupados y
salir del
programa.Cada lugar
en el
estacionamiento está
representado por
un número, 
donde 0 significa que está vacío y 1 significa que está ocupado.
""";
