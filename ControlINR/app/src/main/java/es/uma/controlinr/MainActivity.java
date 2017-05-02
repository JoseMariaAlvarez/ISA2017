package es.uma.controlinr;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.widget.LinearLayout;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        /**
         * Indicamos el xml que se va a mostrar
         */
        setContentView(R.layout.activity_main);

    }

    /** Es llamado cuando el usuario hace click sobre la fila llamada Guías */
    public void abrirGuias(View v) {


        /**
         * Recogemos LinearLayout con id: id_expandable del xml activity_guia_desplegada
         * Recuperamos el LinearLayout con id: id_ del xml activity_main
         */
        LinearLayout row_expandible = (LinearLayout) findViewById(R.id.id_expandable);
        LinearLayout linearLayout_principal = (LinearLayout) findViewById(R.id.id_layout_principal);

        /**
         * Este if comprueba si el layout row_expandible está ya en el LinearLayout_principal
         */

        /**
         * Si no está (row_expandible == null), se crea.
         */
        if(row_expandible == null){
            /**
             * Creamos el LayoutInflater
             * Este inflater nos permitirá añadir nuevos layout al linearLayout_principal
             */
            LayoutInflater inflater = LayoutInflater.from(this);

            /**
             * Creamos la nueva vista view que contendrá al xml activity_guia_desplegada.
             */
            View view  =  getLayoutInflater().inflate(R.layout.activity_guia_desplegada, null);
            /**
             * Añadimos la vista view al linearLayout_principal en la fila 2
             */
            linearLayout_principal.addView(view, 2);

        /**
         * Si está (row_expandible != null) se destruye
         */
        }else {

            /**
             * Destruímos el layout row_expandible del linearLayout_principal.
             */
            linearLayout_principal.removeView(row_expandible);
        }
    }

    /** Es llamado cuando el usuario hace click sobre la fila "Para el Paciente" en el layout desplegado */
    public void abrirPaciente(View v) {
        Intent intent = new Intent(this, GuiaPaciente.class);
        startActivity(intent);
    }

    /** Es llamado cuando el usuario hace click sobre la fila "En caso de emergencia" en el layout desplegado */
    public void abrirEmergencia(View v) {
        Intent intent = new Intent(this, GuiaEmergencia.class);
        startActivity(intent);
    }
}
