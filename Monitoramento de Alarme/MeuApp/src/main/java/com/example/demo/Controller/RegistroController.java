package com.example.demo.Controller;

import java.util.List;
import java.util.stream.Collectors;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import com.example.demo.Models.Registro;

@RestController
@CrossOrigin("*")
public class RegistroController {
    
        @Autowired
        private RegistroService rs;
        
        @Autowired
        private RegistroRepository registror;

        @GetMapping("/listarTodos")
        public List<RegistroDTO> listarTodosRegistros() {
            List<Registro> registros = rs.listarTodosRegistros();

            
            List<RegistroDTO> registrosDTO = registros.stream()
                    .map(registro -> new RegistroDTO(
                            registro.getId(),
                            registro.getAlarme(),
                            registro.getVigilante(),
                            registro.getDescricao(),
                            registro.getHorarioRegistro(),
                            registro.getMotivo_acionamento()
                    ))
                    .collect(Collectors.toList());

            return registrosDTO;
        }
        
        //Lista alarmes
        @GetMapping("/listarAndamento")
        public List<Registro> listarAndamento() {
        	return registror.findByDescricao("Em Andamento");
        }
}
