#include <iostream>
#include <cstdlib>
#include <string>
#include <fstream>
#include <conio.h>
#include <windows.h>
#include <vector>

using namespace std;

struct auto_t {
    string marca;
    string modelo;
    string descripcion;
    float precio;
    int cantidad;
};

void marco() {
    for (int i = 0; i < 80; i++) {
        cout << "-";
    }
    cout << endl;
}

void bienvenida() {
    marco();
    cout << "\t\t\t   BIENVENIDO A LA TIENDA DE AUTOS" << endl;
    marco();
}

void gotoxy(int x, int y) {
    HANDLE hCon;
    hCon = GetStdHandle(STD_OUTPUT_HANDLE);
    COORD dwPos;
    dwPos.X = x;
    dwPos.Y = y;
    SetConsoleCursorPosition(hCon, dwPos);
}

void marco1() {
    for (int i = 5; i <= 22; i++) {
        gotoxy(5, i);
        cout << "|";
        gotoxy(75, i);
        cout << "|";
    }
    for (int i = 5; i <= 75; i++) {
        gotoxy(i, 5);
        cout << "-";
        gotoxy(i, 22);
        cout << "-";
    }
}

void marco2() {
    for (int i = 5; i <= 20; i++) {
        gotoxy(5, i);
        cout << "|";
        gotoxy(75, i);
        cout << "|";
    }
    for (int i = 5; i <= 75; i++) {
        gotoxy(i, 5);
        cout << "-";
        gotoxy(i, 20);
        cout << "-";
    }
}

void menu() {
    system("cls");
    gotoxy(27, 7);
    cout << "MENU PRINCIPAL" << endl;
    gotoxy(10, 9);
    cout << "1. Cobros" << endl;
    gotoxy(10, 10);
    cout << "2. Inventario" << endl;
    gotoxy(10, 11);
    cout << "3. Salir" << endl;
    gotoxy(10, 13);
}

void pass() {
    string usuario;
    string contrasenia;
    string usuario_correcto = "admin";
    string password_correcto = "1234";

    cout << "\nIngrese su usuario: ";
    cin >> usuario;
    cout << "Clave de seguridad: ";
    cin >> contrasenia;

    if (usuario == usuario_correcto && contrasenia == password_correcto) {
        cout << "\nBienvenido, acceso concedido." << endl;
        system("pause");
    } else {
        cout << "\nUsuario y/o contraseña incorrectos. Acceso denegado." << endl;
        system("pause");
        exit(0);
    }
    system("cls");
}



void agregarAuto(ofstream& archivo, auto_t autoNuevo) {
    archivo << autoNuevo.marca << "," << autoNuevo.modelo << "," << autoNuevo.descripcion << "," << autoNuevo.precio << "," << autoNuevo.cantidad << endl;
}

void mostrarAutos(ifstream& archivo) {
    vector<auto_t> autos;
    auto_t autoActual;
    string linea;

    while (getline(archivo, linea)) {
        autoActual.marca = linea.substr(0, linea.find(","));
        linea.erase(0, linea.find(",") + 1);

        autoActual.modelo = linea.substr(0, linea.find(","));
        linea.erase(0, linea.find(",") + 1);

        autoActual.descripcion = linea.substr(0, linea.find(","));
        linea.erase(0, linea.find(",") + 1);

        autoActual.precio = stof(linea.substr(0, linea.find(",")));
        linea.erase(0, linea.find(",") + 1);

        autoActual.cantidad = stoi(linea);

        autos.push_back(autoActual);
    }




    for (auto autoActual : autos) {
        cout << "Marca: " << autoActual.marca << endl;
        cout << "Modelo: " << autoActual.modelo << endl;
        cout << "Descripción: " << autoActual.descripcion << endl;
        cout << "Precio: " << autoActual.precio << endl;
        cout << "Cantidad: " << autoActual.cantidad << endl;
        cout << endl;
    }
}

void InventarioCarros() {
    int opcion = 0;
    do {
        cout << "----- INVENTARIO -----" << endl;
        cout << "1. Agregar auto" << endl;
        cout << "2. Mostrar autos" << endl;
        cout << "3. Guardar y salir." << endl;
        cout << "Ingrese una opción: ";
        cin >> opcion;

        switch (opcion) {
            case 1: {
                int cantidadMarcas, cantidadModelos;
                cout << "Ingrese cantidad de marcas: ";
                cin >> cantidadMarcas;

                ofstream archivo("autos.txt", ios::app);

                for (int i = 0; i < cantidadMarcas; i++) {
                    auto_t autoNuevo;
                    cout << "Ingrese marca " << i + 1 << ": ";
                    cin >> autoNuevo.marca;

                    cout << "Ingrese cantidad de modelos: ";
                    cin >> cantidadModelos;

                    for (int j = 0; j < cantidadModelos; j++) {
                        cout << "Ingrese modelo " << j + 1 << " de " << autoNuevo.marca << ": ";
                        cin >> autoNuevo.modelo;

                        cout << "Ingrese descripción: ";
                        cin.ignore();
                        getline(cin, autoNuevo.descripcion);

                        cout << "Ingrese precio: ";
                        cin >> autoNuevo.precio;

                        cout << "Ingrese cantidad: ";
                        cin >> autoNuevo.cantidad;

                        agregarAuto(archivo, autoNuevo);
                    }
                }
                archivo.close();
                break;
            }

            case 2: {
                ifstream archivo("autos.txt");
                mostrarAutos(archivo);
                archivo.close();
                break;
            }

            case 3: {
                cout << "Se cerrara el programa." << endl;
                system("pause");
                break;
                exit;
            }

            default: {
                cout << "Opción inválida. Intente de nuevo" << endl;
                break;
            }
        }
    } while (opcion != 3);


}

void ventas() {
    char respuestaProducto;
    string nombreProducto,pregunta;
    float precio, cantidad, subtotal, subtotalVenta = 0, iva, total, totalVentasDia = 0, pago, cambio, ventaCliente;
    int contadorClientes = 0;
    bool val = TRUE;

    cout << "Ventas De Carros" << endl;
    cout << endl;

    while (contadorClientes == val) {
        cout << " - - - - - - - - - - - - - - " << endl;

        contadorClientes = contadorClientes + 1;
        ventaCliente = 0;
        respuestaProducto = 's';


        cout << ":::::: Capturar la venta del CLIENTE " << contadorClientes << " ::::::" << endl;
        do {
            cout << "-- Ingrese el NOMBRE del producto: ";
            getline(cin, nombreProducto);
            cout << "-- Ingrese el PRECIO unitario del producto: $";
            cin >> precio;
            cout << "-- Ingrese la CANTIDAD de producto: ";
            cin >> cantidad;

            subtotal = precio * cantidad;
            iva = subtotal * 0.16;
            total = subtotal + iva;

            cout << endl;
            cout << "**** Venta del producto ****" << endl;
            cout << "Producto: " << nombreProducto << endl;
            cout << "Cantidad: " << cantidad << endl;
            cout << "Precio Unitario: $" << precio << endl;
            cout << "Subtotal: $" << subtotal << endl;
            cout << "IVA: $" << iva << endl;
            cout << "Total: $" << total << endl;

            ventaCliente = ventaCliente + total;

            cout << endl;
            cout << "Desea capturar otra venta para este CLIENTE (s/n)? ";
            cin >> respuestaProducto;
            cin.ignore();
            cout << endl;
        } while (val == TRUE);
            if (respuestaProducto == ('s') || respuestaProducto == 'S');
    
            subtotalVenta = subtotalVenta + ventaCliente;
    
            cout << "**** Venta del CLIENTE " << contadorClientes << " ****" << endl;
            cout << "Subtotal de la venta: $" << ventaCliente << endl;
    
            cout << endl;
            cout << "------------------------------------" << endl;
            cout << endl;

            if(respuestaProducto == ('n') || respuestaProducto == 'N'){
                cout << "==== Venta del día ====" << endl;
                cout << "Subtotal de todas las ventas: $" << subtotalVenta << endl;

                cout << endl;
                cout << "------------------------------------" << endl;
                cout << endl;

                cout << "Ingrese el PAGO del cliente: $";
                cin >> pago;

                cambio = pago - subtotalVenta;

                cout << "Cambio: $" << cambio << endl;

                cout << endl;
                cout << "===== FIN DE VENTAS =====" << endl;
                cout << endl;

                totalVentasDia = totalVentasDia + subtotalVenta;

                cout << "Ventas Totales: $" << totalVentasDia << endl;
                bool var = FALSE;
                    }
                }
}

int main() {
    marco();
    bienvenida();
    pass();

    marco2();
    menu();
    int opcion;
    cin >> opcion;

    switch (opcion) {
        case 1:
            ventas();
            break;
        case 2:
            InventarioCarros();
            break;
        case 3:
            cout << "Se cerrara el programa" << endl;
            system("pause");
            exit(0);
            break;
        default:
            cout << "Opción inválida. Intente de nuevo." << endl;
            break;
    }

    return 0;
}
