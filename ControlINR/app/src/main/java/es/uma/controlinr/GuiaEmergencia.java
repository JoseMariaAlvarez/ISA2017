package es.uma.controlinr;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.widget.ExpandableListView;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

import com.example.juanignacio.controlinr.R;

/**
 * Created by Juan Ignacio on 25/04/2017.
 */
public class GuiaEmergencia extends AppCompatActivity {


    private List<String> listDataHeader;
    private HashMap<String,List<String>> listHash;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_guiaemergencia);
        initdata();
        ExpandableListView boton = (ExpandableListView) findViewById(R.id.ExpPaciente);
        ExpandableListAdapter expandable = new ExpandableListAdapter(this, listDataHeader, listHash);
        boton.setAdapter(expandable);
    }

    private void initdata(){
        listDataHeader = new ArrayList<>();
        listHash = new HashMap<>();

        listDataHeader.add(getString(R.string.cirugia));
        listDataHeader.add(getString(R.string.inyectar_heparina));
        listDataHeader.add(getString(R.string.ir_dentista));
        listDataHeader.add(getString(R.string.interacciones_anticoagulantes));
        listDataHeader.add(getString(R.string.heridas));
        listDataHeader.add(getString(R.string.mujer_anticonceptivos));
        listDataHeader.add(getString(R.string.embarazo));
        listDataHeader.add(getString(R.string.vacaciones));
        listDataHeader.add(getString(R.string.dolor));
        listDataHeader.add(getString(R.string.fiebre));
        listDataHeader.add(getString(R.string.diarrea));
        listDataHeader.add(getString(R.string.antibioticos));
        listDataHeader.add(getString(R.string.vacunas));

        List<String> cirugia = new ArrayList<>();
        cirugia.add(getString(R.string.texto_cirugia));

        List<String> inyectar_heparina = new ArrayList<>();
        inyectar_heparina.add(getString(R.string.texto_inyectar_heparina));

        List<String> ir_dentista = new ArrayList<>();
        ir_dentista.add(getString(R.string.texto_ir_dentista));

        List<String> interacciones_anticoagulantes = new ArrayList<>();
        interacciones_anticoagulantes.add(getString(R.string.texto_interacciones_anticoagulantes));

        List<String> heridas = new ArrayList<>();
        heridas.add(getString(R.string.texto_heridas));

        List<String> mujer_anticonceptivos = new ArrayList<>();
        mujer_anticonceptivos.add(getString(R.string.texto_mujer_anticonceptivos));

        List<String> embarazo = new ArrayList<>();
        embarazo.add(getString(R.string.texto_embarazo));

        List<String> vacaciones = new ArrayList<>();
        vacaciones.add(getString(R.string.texto_vacaiones));

        List<String> dolor = new ArrayList<>();
        dolor.add(getString(R.string.texto_dolor));

        List<String> fiebre = new ArrayList<>();
        fiebre.add(getString(R.string.texto_fiebre));

        List<String> diarrea = new ArrayList<>();
        diarrea.add(getString(R.string.texto_diarrea));

        List<String> antibioticos = new ArrayList<>();
        antibioticos.add(getString(R.string.texto_antibioticos));

        List<String> vacunas = new ArrayList<>();
        vacunas.add(getString(R.string.texto_vacunas));

        listHash.put(listDataHeader.get(0),cirugia);
        listHash.put(listDataHeader.get(1),inyectar_heparina);
        listHash.put(listDataHeader.get(2),ir_dentista);
        listHash.put(listDataHeader.get(3),interacciones_anticoagulantes);
        listHash.put(listDataHeader.get(4),heridas);
        listHash.put(listDataHeader.get(5),mujer_anticonceptivos);
        listHash.put(listDataHeader.get(6),embarazo);
        listHash.put(listDataHeader.get(7),vacaciones);
        listHash.put(listDataHeader.get(8),dolor);
        listHash.put(listDataHeader.get(9),fiebre);
        listHash.put(listDataHeader.get(10),diarrea);
        listHash.put(listDataHeader.get(11),antibioticos);
        listHash.put(listDataHeader.get(12),vacunas);

    }

}
