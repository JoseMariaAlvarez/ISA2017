package com.example.juanignacio.controlinr;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.widget.ExpandableListView;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

/**
 * Created by Juan Ignacio on 25/04/2017.
 */
public class GuiaPaciente extends AppCompatActivity {

    private List<String> listDataHeader;
    private HashMap<String,List<String>> listHash;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_guiapaciente);
        initdata();
        ExpandableListView boton = (ExpandableListView) findViewById(R.id.ExpPaciente);
        ExpandableListAdapter expandable = new ExpandableListAdapter(this, listDataHeader, listHash);
        boton.setAdapter(expandable);
    }
    private void initdata(){
        listDataHeader = new ArrayList<>();
        listHash = new HashMap<>();

        listDataHeader.add(getString(R.string.pregunta_alcohol));
        listDataHeader.add(getString(R.string.pregunta_quien_medicamento));
        listDataHeader.add(getString(R.string.pregunta_otros_medicamentos));

        List<String> alcohol = new ArrayList<>();
        alcohol.add(getString(R.string.texto_alcohol));

        List<String> quienmedicamento = new ArrayList<>();
        quienmedicamento.add(getString(R.string.texto_quien_medicamento));

        List<String> otrosmedicamentos = new ArrayList<>();
        otrosmedicamentos.add(getString(R.string.texto_otros_medicamentos));

        listHash.put(listDataHeader.get(0),alcohol);
        listHash.put(listDataHeader.get(1),quienmedicamento);
        listHash.put(listDataHeader.get(2),otrosmedicamentos);
    }

}
