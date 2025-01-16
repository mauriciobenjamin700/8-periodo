# Informações Obtidas Durante o Desenvolvimento

## Switchs

No contexto do Docker, os **switches virtuais** não precisam ser explicitamente criados como serviços. Isso porque o Docker já utiliza redes **bridge** ou outras configurações de rede para simular o comportamento de switches e roteadores.

### **Como o Docker gerencia os switches?**

1. **Cada subrede (`subnet-A` e `subnet-B`) em seu `docker-compose.yml` já atua como um switch virtual.**
   - Containers conectados a uma mesma subrede podem se comunicar diretamente, como se estivessem conectados a um switch físico.
   - A configuração `networks` no `docker-compose.yml` já cria essas pontes automaticamente.

2. **Papel do Roteador (`router`):**
   - O roteador conecta as duas subredes e encaminha pacotes entre elas.
   - Sem o roteador, as subredes seriam isoladas e não poderiam trocar informações.

---

### **Como configurar um switch explícito?**

Se, por algum motivo, você deseja representar um switch de forma explícita no Docker (ex.: para simular comportamento real de rede), isso pode ser feito adicionando serviços "neutros" ou bridges manuais. Um exemplo seria adicionar um container "dummy" que atua como switch.

#### **Simulação de um Switch com Docker**

```yaml
services:
  switchA:
    image: alpine
    container_name: switchA
    command: sh -c "tail -f /dev/null"
    networks:
      subnet-A: {}

  switchB:
    image: alpine
    container_name: switchB
    command: sh -c "tail -f /dev/null"
    networks:
      subnet-B: {}
```

- Esses "switches" seriam contêineres neutros que não fazem nada diretamente, mas permitem representar fisicamente o papel dos switches na infraestrutura.

---

### **Conclusão**

- Para a simulação básica que você descreveu, **os switches estão implícitos no Docker**, já que as redes bridge em Docker gerenciam essa funcionalidade automaticamente.
- Se quiser representar switches explicitamente por questões educacionais ou visuais, você pode criar contêineres "dummy" como mostrado acima, mas eles não são necessários para o funcionamento da infraestrutura.
