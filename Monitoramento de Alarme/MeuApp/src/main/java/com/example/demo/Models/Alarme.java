package com.example.demo.Models;

import java.time.LocalDate;
import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;

@Entity
public class Alarme {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false)
    private String locala = "";

    @Column
    private LocalDate diadoalarme;

    @Column(nullable = false)
    private Boolean ativo = false;

    @Column
    private String status;

    public Alarme() {
    }

    // getters e setters
    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getLocala() {
        return locala;
    }

    public void setLocala(String locala) {
        this.locala = locala;
    }

    public LocalDate getDiadoalarme() {
        return diadoalarme;
    }

    public void setDiadoalarme(LocalDate diadoalarme) {
        this.diadoalarme = diadoalarme;
    }

    public Boolean getAtivo() {
        return ativo;
    }

    public void setAtivo(Boolean ativo) {
        this.ativo = ativo;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
}
