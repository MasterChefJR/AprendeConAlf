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



void pass() {
    string usuario;
    string contrasenia;
    string usuario_correcto = "admin";
    string Password = "1234";

    cout << "\nIngrese su usuario: ";
    cin >> usuario;
    cout << "Clave de seguridad: ";
    cin >> Password;

    if (usuario == usuario_correcto && Password == Password) {
        cout << "\nBienvenido, acceso concedido." << endl;
    }
    else {
        cout << "\nUsuario y/o contraseña incorrectos. Acceso denegado." << endl;
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

void menuVentas() {
    int opcion = 0;

    do {
        cout << "----- VENTAS -----" << endl;
        cout << "1. Agregar auto" << endl;
        cout << "2. Mostrar autos" << endl;
        cout << "3. Pagina anterior" << endl;
        cout << "Ingrese una opcion: ";
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
            menu();
            break;
        }


        default: {
            cout << "Opcion invalida. Intente de nuevo" << endl;
            menuVentas();
            break;
        }
        }
    } while (opcion != 3);
            system("cls");
}


void ventas() {
    char respuestaProducto;
    string nombreProducto;
    float precio, cantidad, subtotal, subtotalVenta = 0, iva, total, totalVentasDia = 0, pago, cambio, ventaCliente;
    int contadorClientes = 0;

    cout << "Ventas De Carros" << endl;
    cout << endl;

    while (contadorClientes < 3) {
        cout << " - - - - - - - - - - - - - - " << endl;

        contadorClientes = contadorClientes + 1;
        ventaCliente = 0;
        respuestaProducto = 's';

        cout << ":::::: Capturar la venta del CLIENTE " << contadorClientes << " ::::::" << endl;
        do {
            cout << "-- Ingrese el NOMBRE del producto: ";
            getline(cin, nombreProducto);

            cout << "-- Ingrese el PRECIO del producto: ";
            cin >> precio;

            cout << "-- Ingrese la CANTIDAD de productos: ";
            cin >> cantidad;
            cin.ignore();

            // Costos por producto
            subtotal = precio * cantidad;
            subtotalVenta = subtotalVenta + subtotal;
            iva = subtotalVenta * 0.16;
            total = subtotalVenta + iva;

            ventaCliente = total;

            cout << ":::::: CONTINUAR ::::::" << endl;
            cout << "¿Desea capturar otro producto? (s/n): ";
            cin >> respuestaProducto;
            cin.ignore();
        } while (respuestaProducto == 's' || respuestaProducto == 'S');

        cout << "::::::::: CLIENTE " << contadorClientes << ":::::::::" << endl;
        cout << "Subtotal:  $ " << subtotalVenta << endl;
        cout << "IVA:       $ " << iva << endl;
        cout << "Total:     $ " << ventaCliente << endl;
        cout << "::::::::::::::::::::::::::" << endl;
        cout << endl;
        cout << "Ingrese el monto de pago del CLIENTE " << contadorClientes << endl;
        cout << "Debe ser mayor o igual al total a PAGAR ($ " << ventaCliente << ")" << endl;
        cin >> pago;

        cambio = pago - ventaCliente;
        cout << "::::::::::::::::::::::::::" << endl;
        cout << "El cambio que se le dará al CLIENTE " << contadorClientes << " es de: $ " << cambio << endl;
        cout << "::::::::::::::::::::::::::" << endl;
        cout << endl;
        cout << endl;

        totalVentasDia = totalVentasDia + ventaCliente;
        subtotalVenta = 0;
    }

    cout << "El total de las ventas del día fue de: $ " << totalVentasDia << endl;
}

int main() {
    ventas();
    return 0;
}

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
    cout << "1. Ventas" << endl;
    gotoxy(10, 10);
    cout << "2. Inventario" << endl;
    gotoxy(10, 11);
    cout << "3. Salir" << endl;
    gotoxy(10, 13);
}

void Ventas() {
    gotoxy(10, 14);
    cout << "Ingrese una opcion: ";
    int opcionVentas;
    cin >> opcionVentas;
    system("cls");

    switch (opcionVentas) {
    case 1:
        menuVentas();
        break;

    case 2:
        ventas();
        break;

    case 3:
        // Salir del programa 
        exit;
        break;

    default:
        cout << "Opción inválida. Intente de nuevo." << endl;
        Ventas();
        break;
    }
}

int main() {
    marco();
    bienvenida();
    pass();

    if (cin.fail()) {
        cin.clear();
        cin.ignore(1);
        return main();
    }
    else {
        marco2();
        menu();
        Ventas();
    }

    return 0;
}
