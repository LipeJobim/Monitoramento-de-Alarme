package com.example.demo.Models;

import java.util.Date;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.Temporal;
import jakarta.persistence.TemporalType;

@Entity
public class Registro {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @ManyToOne
    @JoinColumn(name = "idAlarme")
    private Alarme alarme;

    @ManyToOne
    @JoinColumn(name = "idVigilante")
    private Vigilante vigilante;
    
    @Column
    private String descricao;

    @Temporal(TemporalType.TIMESTAMP)
    @Column(columnDefinition = "TIMESTAMP DEFAULT CURRENT_TIMESTAMP")
    private Date horarioRegistro;
    
    @Column
    private String motivo_acionamento;

	public Long getId() {
		return id;
	}

	public void setId(Long id) {
		this.id = id;
	}

	public Alarme getAlarme() {
		return alarme;
	}

	public void setAlarme(Alarme alarme) {
		this.alarme = alarme;
	}

	public Vigilante getVigilante() {
		return vigilante;
	}

	public void setVigilante(Vigilante vigilante) {
		this.vigilante = vigilante;
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

	public String getMotivo_acionamento() {
		return motivo_acionamento;
	}

	public void setMotivo_acionamento(String motivo_acionamento) {
		this.motivo_acionamento = motivo_acionamento;
	}

	@Override
	public String toString() {
		return "Registro [id=" + id + ", alarme=" + alarme + ", vigilante=" + vigilante + ", descricao=" + descricao
				+ ", horarioRegistro=" + horarioRegistro + ", motivo_acionamento=" + motivo_acionamento + ", getId()="
				+ getId() + ", getAlarme()=" + getAlarme() + ", getVigilante()=" + getVigilante() + ", getDescricao()="
				+ getDescricao() + ", getHorarioRegistro()=" + getHorarioRegistro() + ", getMotivo_acionamento()="
				+ getMotivo_acionamento() + ", getClass()=" + getClass() + ", hashCode()=" + hashCode()
				+ ", toString()=" + super.toString() + "]";
	}

	
}
