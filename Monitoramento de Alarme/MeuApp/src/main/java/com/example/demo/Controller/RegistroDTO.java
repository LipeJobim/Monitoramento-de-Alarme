package com.example.demo.Controller;


import java.util.Date;

import com.example.demo.Models.Alarme;
import com.example.demo.Models.Vigilante;

public class RegistroDTO {
    private Long id;
    private Alarme idAlarme;
    private Vigilante idVigilante;
    private String descricao;
    private Date horarioRegistro;
    private String motivoAcionamento;
    
	public Long getId() {
		return id;
	}
	public void setId(Long id) {
		this.id = id;
	}
	public Alarme getIdAlarme() {
		return idAlarme;
	}
	public void setIdAlarme(Alarme idAlarme) {
		this.idAlarme = idAlarme;
	}
	public Vigilante getIdVigilante() {
		return idVigilante;
	}
	public void setIdVigilante(Vigilante idVigilante) {
		this.idVigilante = idVigilante;
	}
	public String getDescricao() {
		return descricao;
	}
	public void setDescricao(String descricao) {
		this.descricao = descricao;
	}
	public Date getHorarioRegistro() {
		return horarioRegistro;
	}
	public void setHorarioRegistro(Date horarioRegistro) {
		this.horarioRegistro = horarioRegistro;
	}
	public String getMotivoAcionamento() {
		return motivoAcionamento;
	}
	public void setMotivoAcionamento(String motivoAcionamento) {
		this.motivoAcionamento = motivoAcionamento;
	}
	public RegistroDTO(Long id, Alarme idAlarme, Vigilante idVigilante, String descricao, Date horarioRegistro,
			String motivoAcionamento) {
		super();
		this.id = id;
		this.idAlarme = idAlarme;
		this.idVigilante = idVigilante;
		this.descricao = descricao;
		this.horarioRegistro = horarioRegistro;
		this.motivoAcionamento = motivoAcionamento;
	}
    

    
}