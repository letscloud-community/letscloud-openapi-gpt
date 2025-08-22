# 🔧 Guia Completo: Como Duplicar seu GPT Actions e Torná-lo Privado

## 🎯 **Objetivo**

Este guia mostra como criar uma **versão privada** do seu GPT Actions para uso pessoal, mantendo a **versão pública** segura para outros usuários.

## 📋 **Pré-requisitos**

- ✅ GPT Actions já criado e funcionando
- ✅ Acesso ao GPT Builder
- ✅ API key da LetsCloud para uso pessoal

## 🚀 **Passo a Passo Detalhado**

### **Passo 1: Acessar o GPT Builder**

1. **Abra o ChatGPT**
2. **Vá para GPTs** (menu lateral)
3. **Encontre seu GPT** "LetsCloud Infrastructure Manager"
4. **Clique em "Editar"** (ou ⋮ → Editar GPT)

### **Passo 2: Fazer uma Cópia**

1. **No topo direito**, clique em **⋮ Mais opções**
2. **Selecione "Duplicar"**
3. **Aguarde** a criação da cópia
4. **Confirme** que a cópia foi criada

### **Passo 3: Configurar como Privado**

1. **Na cópia criada**, vá em **Configurações**
2. **Encontre "Visibilidade"**
3. **Selecione "Somente eu"**
4. **Isso garante** que só você terá acesso

### **Passo 4: Configurar a API Key**

1. **Vá para a aba "Actions"**
2. **Abra a Action** que conecta ao `core_letscloud_io__jit_plugin`
3. **Encontre "Autenticação"**
4. **Configure a Environment Variable:**
   - **Nome**: `LETSCLOUD_API_TOKEN`
   - **Valor**: Sua API key da LetsCloud
5. **Salve as alterações**

### **Passo 5: Testar a Configuração**

1. **Clique em "Salvar"** ou "Publicar"
2. **Teste a versão privada:**
   ```
   "Show me my account information"
   ```
3. **Verifique** se funciona sem solicitar API key

## 🎯 **Resultado Final**

### **✅ Versão Pública (Original)**
- **Visibilidade**: Pública
- **API Key**: Não configurada
- **Uso**: Para clientes da LetsCloud
- **Segurança**: Solicita API key quando necessário

### **🔒 Versão Privada (Cópia)**
- **Visibilidade**: Privada (só você)
- **API Key**: Configurada
- **Uso**: Para seu gerenciamento pessoal
- **Segurança**: Acesso direto sem configuração

## 🔍 **Verificação**

### **Teste da Versão Pública:**
```
Usuário: "Show me my account information"
GPT: "I need your API key to access your account..."
```

### **Teste da Versão Privada:**
```
Você: "Show me my account information"
GPT: "Here's your account information: [dados da conta]"
```

## 🛡️ **Segurança**

### **✅ Benefícios:**
- **API key protegida**: Não exposta publicamente
- **Controle de acesso**: Versão privada só para você
- **Conformidade**: Segue melhores práticas de segurança
- **Flexibilidade**: Duas versões para diferentes usos

### **⚠️ Lembretes:**
- **Nunca compartilhe** a versão privada
- **Mantenha a API key** segura
- **Use a versão pública** para demonstrações
- **Use a versão privada** para gerenciamento pessoal

## 🚀 **Comandos Úteis para Testar**

### **Versão Pública (para clientes):**
```
"List my servers"
"Create a new server"
"Show me my SSH keys"
"Get my account balance"
```

### **Versão Privada (para você):**
```
"Show me my account information"
"List all my servers"
"Create a new Ubuntu server"
"Take a snapshot of server-123"
```

## 📞 **Suporte**

Se encontrar problemas:

1. **Verifique** se a API key está correta
2. **Confirme** que a visibilidade está como "Somente eu"
3. **Teste** com comandos simples primeiro
4. **Consulte** a documentação da LetsCloud

## 🎉 **Parabéns!**

Agora você tem:
- ✅ **Versão pública** para clientes
- ✅ **Versão privada** para uso pessoal
- ✅ **Segurança** garantida
- ✅ **Funcionalidade** completa

**Seu setup está perfeito!** 🚀
