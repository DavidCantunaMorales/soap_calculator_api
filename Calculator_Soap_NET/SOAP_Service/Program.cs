using System;
using System.Threading.Tasks;
using ServiceCalculator;

namespace SoapClientExample
{
    class Program
    {
        static async Task Main(string[] args)
        {
            // Se crea una instancia del cliente SOAP
            var client = new CalculatorSoapClient(CalculatorSoapClient.EndpointConfiguration.CalculatorSoap);

            try
            {
                // Realizar operaciones asíncronas con el servicio web
                int resultadoSuma = await client.AddAsync(8, 8);
                Console.WriteLine("Resultado de la suma: " + resultadoSuma);

                int resultadoResta = await client.SubtractAsync(48, 8);
                Console.WriteLine("Resultado de la resta: " + resultadoResta);

                int resultadoMultiplicacion = await client.MultiplyAsync(8, 8);
                Console.WriteLine("Resultado de la multiplicación: " + resultadoMultiplicacion);

                int resultadoDivision = await client.DivideAsync(8, 2);
                Console.WriteLine("Resultado de la división: " + resultadoDivision);
            }
            catch (Exception ex)
            {
                Console.WriteLine("Error: " + ex.Message);
            }
            finally
            {
                // Cerrar el cliente para liberar los recursos
                await client.CloseAsync();
            }
        }
    }
}
