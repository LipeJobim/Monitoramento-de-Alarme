package com.example.demo.Controller;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import com.example.demo.Models.Cliente;

@RestController
@CrossOrigin("*")
public class ClienteController {

	@Autowired
	private ClienteRepository cr;

//	@PostMapping("/cadastrar/cliente")
//    public Cliente cadastrarCliente(@RequestParam Long id, @RequestParam String nome, @RequestParam String email,
//            @RequestParam LocalDate dataNascimento, @RequestParam String endereco, @RequestParam String telefone,
//            @RequestParam String cep, @RequestParam String cpf) {
//        // Crie um objeto Cliente com os dados do formulário
//        Cliente cliente = new Cliente();
//        cliente.setId(id);
//        cliente.setNome(nome);
//        cliente.setEmail(email);
//        cliente.setCEP(cep);
//        cliente.setCPF(cpf);
//        cliente.setTelefone(telefone);
//        cliente.setEndereco(endereco);
//        cliente.setDataNascimento(dataNascimento);
//        
//        return cliente;
//    }

	// Lista clientes por id
	@GetMapping("/clientes/{id}")
	public Cliente findById(@PathVariable Long id) {
		Cliente result = cr.findById(id).get();
		return result;
	}

	// Cadastra clientes

	@PostMapping("/cadastrar/cliente")
	public Cliente cadastrarCliente(@RequestBody Cliente novocliente) {
		Cliente newcliente = new Cliente();
		newcliente.setId(novocliente.getId());
		newcliente.setNome(novocliente.getNome());
		newcliente.setDataNascimento(novocliente.getDataNascimento());
		newcliente.setCEP(novocliente.getCEP());
		newcliente.setCPF(novocliente.getCPF());
		newcliente.setTelefone(novocliente.getTelefone());
		newcliente.setEmail(novocliente.getEmail());
		newcliente.setEndereco(novocliente.getEndereco());
		Cliente result = cr.save(newcliente);
		return result;
	}

	// Lista clientes
	@GetMapping("/clientes")
	public List<Cliente> findAll() {
		List<Cliente> result = cr.findAll();
		return result;
	}

	// Deleta pelo id
	@DeleteMapping("/clientes/apagar/{id}")
	public ResponseEntity<Void> deletarPorId(@PathVariable Long id) {
		if (cr.existsById(id)) {
			cr.deleteById(id);
			return new ResponseEntity<>(HttpStatus.NO_CONTENT);
		} else {
			return new ResponseEntity<>(HttpStatus.NOT_FOUND);
		}
	}

	// Atualiza cliente
	@PutMapping("/clientes/atualizar{id}")
	public ResponseEntity<Cliente> atualizarCliente( @PathVariable Long id, @RequestBody Cliente novoCliente) {
		if (id != null) {
			Optional<Cliente> clienteExistente = cr.findById(id);

			if (clienteExistente.isPresent()) {
				// Atualiza os campos do cliente com os valores do novoCliente
				Cliente cliente = clienteExistente.get();
				cliente.setNome(novoCliente.getNome());
				cliente.setEmail(novoCliente.getEmail());
				cliente.setDataNascimento(novoCliente.getDataNascimento());
				cliente.setCEP(novoCliente.getCEP());
				cliente.setCPF(novoCliente.getCPF());
				cliente.setEndereco(novoCliente.getEndereco());
				cliente.setTelefone(novoCliente.getTelefone());
				// Adicione outros campos que deseja atualizar

				Cliente clienteAtualizado = cr.save(cliente);
				return new ResponseEntity<>(clienteAtualizado, HttpStatus.OK); // Retorna o cliente atualizado com
																				// status 200 OK
			} else {
				return new ResponseEntity<>(HttpStatus.NOT_FOUND); // Retorna 404 Not Found se o cliente não existir
			}
		} else {
			return new ResponseEntity<>(HttpStatus.BAD_REQUEST); // Retorna 400 Bad Request se o ID não for fornecido na
																	// URL
		}
	}
}