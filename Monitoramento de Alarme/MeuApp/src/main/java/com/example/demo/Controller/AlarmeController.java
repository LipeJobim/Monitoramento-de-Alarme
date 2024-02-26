package com.example.demo.Controller;

import java.util.Date;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PatchMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import com.example.demo.Models.Alarme;
import com.example.demo.Models.Registro;
import com.example.demo.Models.Vigilante;

@RestController
public class AlarmeController {

    @Autowired
    private AlarmeRepository ar;

    @Autowired
    private RegistroRepository rr;

    @Autowired
    private VigilanteRepository vr;

    @GetMapping("/alarmes/{id}")
    public ResponseEntity<Alarme> findById(@PathVariable Long id) {
        Optional<Alarme> optionalAlarme = ar.findById(id);
        return optionalAlarme.map(alarme -> new ResponseEntity<>(alarme, HttpStatus.OK))
                .orElseGet(() -> new ResponseEntity<>(HttpStatus.NOT_FOUND));
    }

    @PostMapping("/cadastrar/alarme")
    public ResponseEntity<Alarme> cadastrarAlarme(@RequestBody Alarme alarme) {
        Alarme result = ar.save(alarme);
        return new ResponseEntity<>(result, HttpStatus.CREATED);
    }

    //Aciona Alarme
    @PatchMapping("/alarmes/{id}/modificar-status")
    public ResponseEntity<String> modificarStatus(@PathVariable Long id, @RequestBody ModificarStatusRequest request) {
        Optional<Alarme> optionalAlarme = ar.findById(id);

        if (optionalAlarme.isPresent()) {
            Alarme alarme = optionalAlarme.get();
            alarme.setStatus("Disparado");
            ar.save(alarme);

            Registro registro = new Registro();
            registro.setAlarme(alarme);
            registro.setHorarioRegistro(new Date());
            registro.setMotivo_acionamento("");
            registro.setDescricao("Em aberto");
            rr.save(registro);
            
           
            Map<String, String> response = new HashMap<>();
            response.put("message", "Status modificado com sucesso!");
            ResponseEntity.ok(response);
            return new ResponseEntity<>("Status modificado e registro criado com sucesso.", HttpStatus.OK);
        } else {
            return new ResponseEntity<>("Alarme não encontrado.", HttpStatus.NOT_FOUND);
        }
    }

    //Termina ocorrencia
    @PatchMapping("/vigilante/{idVigilante}/terminar/{idAlarme}")
    public ResponseEntity<String> acionarVigilante(@PathVariable Long idVigilante, @PathVariable Long idAlarme,
            @RequestBody MotivoAcionamentoRequest motivoAcionamentoRequest) {
        Optional<Vigilante> optionalVigilante = vr.findById(idVigilante);
        Optional<Alarme> optionalAlarme = ar.findById(idAlarme);

        if (optionalVigilante.isPresent() && optionalAlarme.isPresent()) {
            Vigilante vigilante = optionalVigilante.get();
            vigilante.setStatus("Disponível");
            vr.save(vigilante);
            if (optionalAlarme.isPresent() && optionalVigilante.isPresent()) {
            	Alarme alarme = optionalAlarme.get();
            	alarme.setStatus("Funcionando");
            	ar.save(alarme);
            }
            Alarme alarme = optionalAlarme.get();
           

            Registro novoRegistro = new Registro();
            novoRegistro.setAlarme(alarme);
            novoRegistro.setVigilante(vigilante);
            novoRegistro.setHorarioRegistro(new Date());
            novoRegistro.setDescricao("Finalizado");
            novoRegistro.setMotivo_acionamento(motivoAcionamentoRequest.getMotivo_acionamento());
            rr.save(novoRegistro);

            return new ResponseEntity<>("Vigilante acionado com sucesso e status atualizado.", HttpStatus.OK);
        } else {
            return new ResponseEntity<>("Vigilante ou Alarme não encontrado.", HttpStatus.NOT_FOUND);
        }
    }

    //Aciona Vigilante
    @PatchMapping("/vigilante/{idVigilante}/acionar/{idAlarme}")
    public ResponseEntity<String> acionarVigilante(@PathVariable Long idVigilante, @PathVariable Long idAlarme) {
        Optional<Vigilante> optionalVigilante = vr.findById(idVigilante);
        Optional<Alarme> optionalAlarme = ar.findById(idAlarme);

        if (optionalVigilante.isPresent() && optionalAlarme.isPresent()) {
            Vigilante vigilante = optionalVigilante.get();
            vigilante.setStatus("Ocupado");
            vr.save(vigilante);
            if (optionalAlarme.isPresent() && optionalVigilante.isPresent()) {
            	Alarme alarme = optionalAlarme.get();
            	alarme.setStatus("Em manutenção");
            	ar.save(alarme);
            }

            Alarme alarme = optionalAlarme.get();

            Registro novoRegistro = new Registro();
            novoRegistro.setAlarme(alarme);
            novoRegistro.setVigilante(vigilante);
            novoRegistro.setHorarioRegistro(new Date());
            novoRegistro.setDescricao("Em Andamento");
            novoRegistro.setMotivo_acionamento("");
            rr.save(novoRegistro);

            return new ResponseEntity<>("Vigilante acionado com sucesso e status atualizado.", HttpStatus.OK);
        } else {
            return new ResponseEntity<>("Vigilante ou Alarme não encontrado.", HttpStatus.NOT_FOUND);
        }
    }

    @GetMapping("/alarmes")
    public List<Alarme> findAll() {
        return ar.findAll();
    }

    @DeleteMapping("/alarmes/{id}")
    public ResponseEntity<Void> deletarPorId(@PathVariable Long id) {
        if (ar.existsById(id)) {
            ar.deleteById(id);
            return new ResponseEntity<>(HttpStatus.NO_CONTENT);
        } else {
            return new ResponseEntity<>(HttpStatus.NOT_FOUND);
        }
    }

    @PutMapping("/alarmes/atualizar")
    public ResponseEntity<Alarme> atualizarAlarme(@RequestBody Alarme novoAlarme) {
        if (novoAlarme.getId() != null) {
            Optional<Alarme> alarmeExistente = ar.findById(novoAlarme.getId());

            if (alarmeExistente.isPresent()) {
                Alarme alarme = alarmeExistente.get();
                alarme.setLocala(novoAlarme.getLocala());
                alarme.setDiadoalarme(novoAlarme.getDiadoalarme());
                alarme.setAtivo(novoAlarme.getAtivo());

                Alarme clienteAtualizado = ar.save(alarme);
                return new ResponseEntity<>(clienteAtualizado, HttpStatus.OK);
            } else {
                return new ResponseEntity<>(HttpStatus.NOT_FOUND);
            }
        } else {
            return new ResponseEntity<>(HttpStatus.BAD_REQUEST);
        }
    }
}