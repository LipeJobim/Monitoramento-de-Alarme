package com.example.demo.Controller;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;


import com.example.demo.Models.Vigilante;

@RestController
public class VigilanteController {
	
	@Autowired
	private VigilanteRepository vr;

	// Lista clientes por id
	@GetMapping("/vigilantes/{id}")
	public Vigilante findById(@PathVariable Long id) {
		Vigilante result = vr.findById(id).get();
		return result;
	}
	
	// Cadastra clientes
	@PostMapping("/cadastrar/vigilante")
	public Vigilante cadastrarCliente(@RequestBody Vigilante vigilante) {
		Vigilante result = vr.save(vigilante);
	    return result;
	}
	
	// Lista clientes
	@GetMapping("/vigilantes")
	public List<Vigilante> findAll() {
		List<Vigilante> result = vr.findAll();
		return result;
	}
	
	// Deleta pelo id
	@DeleteMapping("/vigilantes/{id}")
    public ResponseEntity<Void> deletarPorId(@PathVariable Long id) {
        if (vr.existsById(id)) {
            vr.deleteById(id);
            return new ResponseEntity<>(HttpStatus.NO_CONTENT); 
        } else {
            return new ResponseEntity<>(HttpStatus.NOT_FOUND);
        }
    }
	
	// Atualiza cliente
    @PutMapping("/vigilantes/atualizar")
    public ResponseEntity<Vigilante> atualizarCliente(@RequestBody Vigilante novoVigilante) {
        if (novoVigilante.getIdVigilante() != null) {
            Optional<Vigilante> vigilanteExistente = vr.findById(novoVigilante.getIdVigilante());

            if (vigilanteExistente.isPresent()) {
                // Atualiza os campos do cliente com os valores do novoCliente
            	Vigilante vigilante = vigilanteExistente.get();
                vigilante.setNome(novoVigilante.getNome());
                vigilante.setStatus(novoVigilante.getStatus());
                // Adicione outros campos que deseja atualizar
                
                Vigilante vigilanteAtualizado = vr.save(vigilante);
                return new ResponseEntity<>(vigilanteAtualizado, HttpStatus.OK); // Retorna o cliente atualizado com status 200 OK
            } else {
                return new ResponseEntity<>(HttpStatus.NOT_FOUND); // Retorna 404 Not Found se o cliente não existir
            }
        } else {
            return new ResponseEntity<>(HttpStatus.BAD_REQUEST); // Retorna 400 Bad Request se o ID não for fornecido no corpo
        }
    }
}
