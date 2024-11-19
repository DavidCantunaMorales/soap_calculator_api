/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package calculatorClient;

import calculator.Calculator;
import calculator.CalculatorSoap;

/**
 *
 * @author Vivobook Oled
 */
public class CalculatorClient {

    public static void main(String[] args) {
        try {
            Calculator calculadora = new Calculator();
            CalculatorSoap calculadoraSoap = calculadora.getCalculatorSoap();

            int num1 = 1;
            int num2 = 5;

            int suma = calculadoraSoap.add(num1, num2);
            int resta = calculadoraSoap.subtract(num1, num2);
            int multiplicacion = calculadoraSoap.multiply(num1, num2);
            int division = calculadoraSoap.divide(num1, num2);

            System.out.println("Suma es: " + suma);
            System.out.println("Resta es: " + resta);
            System.out.println("Multiplicación es: " + multiplicacion);
            System.out.println("División es: " + division);

        } catch (Exception e) {
            System.err.println("Error al consumir el servicio: " + e.getMessage());
        }

    }
}
