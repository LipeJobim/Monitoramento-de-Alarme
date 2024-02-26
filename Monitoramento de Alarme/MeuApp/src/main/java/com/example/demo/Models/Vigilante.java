package com.example.demo.Models;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;

@Entity
public class Vigilante {

	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private Long idVigilante;

	@Column(unique = true)
	private String nome;

	@Column(nullable = false, unique = false)
	private String status;

	public Long getIdVigilante() {
		return idVigilante;
	}

	public void setIdVigilante(Long idVigilante) {
		this.idVigilante = idVigilante;
	}

	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public String getStatus() {
		return status;
	}

	public void setStatus(String status) {
		this.status = status;
	}

	@Override
	public String toString() {
		return "Vigilante [idVigilante=" + idVigilante + ", nome=" + nome + ", status=" + status + ", getIdVigilante()="
				+ getIdVigilante() + ", getNome()=" + getNome() + ", getStatus()=" + getStatus() + ", getClass()="
				+ getClass() + ", hashCode()=" + hashCode() + ", toString()=" + super.toString() + "]";
	}

	public Long getId() {
		// TODO Auto-generated method stub
		return null;
	}
	
	
}
