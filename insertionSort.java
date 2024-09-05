import java.lang.Math;

public class insertionSort {
    public static int geradorDeNumerosAleatorios() {
        int numAleatorio = (int)(Math.random() * 10) + 1;
        return numAleatorio;
    }

    public static int[] insersorDeNumerosAleatoriosEmUmArrayDe500Elementos() {
        int dataset[] = new int[500];

        for(int i = 0; i < 500; i++) {
            dataset[i] = geradorDeNumerosAleatorios();
        }

        return dataset;
    }

    public static int[] aplicacaoInsertionSort() {
        int dataset[] = insersorDeNumerosAleatoriosEmUmArrayDe500Elementos();
        int n = dataset.length;
        int movimentacoes = 0;

        for(int i = 1; i < n; i++) {
            int key = dataset[i];
            int j = i - 1;

            while (j >= 0 && dataset[j] > key) {
                dataset[j + 1] = dataset[j];
                j = j - 1;
                movimentacoes++;
            }

            dataset[j + 1] = key;
            movimentacoes++;
        } 

        System.out.println("Número de movimentações: " + movimentacoes + "\n");
        return dataset;
    }

    public static void printarDatasetOrdenado(int arr[])
    {
        int n = arr.length;
        for (int i = 0; i < n; ++i)
            System.out.print(arr[i] + " ");

        System.out.println();
    }

    public static void main(String[] args) {
        int datasetOrdenado[] = aplicacaoInsertionSort();

        printarDatasetOrdenado(datasetOrdenado);
    }
}