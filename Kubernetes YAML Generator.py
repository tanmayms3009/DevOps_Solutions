#   Kubernetes YAML Generator

comp = ""

#1. API Server:
def apiVersion():
    api_v = input("Enter apiVersion for the specified Kubernetes Component: ")
    file.write("apiVersion: " + str(api_v) + "\n")


#2. Kind:
def kind():
    #Create a code to auto fill kind section:
    kind = component
    file.write("kind: " + str(kind) + "\n")


#3. Metadata:
def metadata():
    #Add name for component:
    #i is the indent factor metadata indentation in case of metadata section in the deployment, replicaset kind of components under spec:
    #set value for i in case of building such kind of components
    #i=0
    md_name = input("Enter metadata name: ")
    file.write(i*"   " + "metadata: \n" +
               i*"   " + "   name: " + str(md_name) + "\n")
    ns_perm = input("Is namespace to be added ? (y/N): ").lower()
    if ns_perm == "y":
        ns_name = input("Enter namespace: ")
        file.write(i*"   " + "   namespace: " + str(ns_name) + "\n")
    else:
        exit 
    #Add labels:
    md_l_perm = input("Are labels to be added ? (y/N): ").lower()
    if md_l_perm == "y":
        file.write(i*"   " + "   labels: \n")
        md_l_n = int(input("Enter number of labels to be added: "))
        for mdl in range(0, md_l_n):
            md_l_k = input("Enter label key: ")
            md_l_v = input("Enter label value for " + str(md_l_k) + ": ")
            file.write(i*"   " + "      " + str(md_l_k) + ": " + str(md_l_v) + "\n")
    elif md_l_perm == "n":
        exit
    else:
        exit
    #Add annotations:
    md_a_perm = input("Are Annotations to be added ? (y/N): ").lower()
    if md_a_perm == "y":
        file.write(i*"   " + "   annotations: \n")
        md_a_n = int(input("Enter number of annotations to be added: "))
        for mda in range(0, md_a_n):
            md_a_k = input("Enter annotation key: ")
            md_a_v = input("Enter annotation value for " + str(md_a_k) + ": ")
            file.write(i*"   " + "      " + str(md_a_k) + ": " + str(md_a_v) + "\n")
    elif md_a_perm == "n":
        exit
    else:
        exit    


#4. Data:
def data():
    data_kvp_n = int(input("Enter number of key value pairs to be added under data section: "))
    file.write("data: \n")
    for dkvp in range(0, data_kvp_n):
        d_k = input("Enter key for data: ")
        d_v = input("Enter value for " + d_k + ": ")
        file.write("   " + str(d_k) + ": " + str(d_v) + "\n")      


#5. Specifications:
def spec():
    #j=0
    #j is indentation factor for spec section under spec section of components like deployment and repicaset
    #set value for j while building such components
    file.write(j*"   " + "spec: \n")


#6. Template
def template():
    #k=0
    #j is indentation factor for spec section under spec section of components like deployment and repicaset
    #set value for j while building such components
    file.write(k*"   " + "   template: \n")


#7. Containers:

def containers():
    #k=0
    #k is for indentation factor, depending on the components selected it will change (default k = 0):
    #mention k while creating program for each component
    file.write(k*"   " + "   containers: \n")
    c_image = input("Enter container image name: ")
    c_name = input("Enter container name: ")
    c_port = int(input("Enter container port number: "))
    c_prot = input("Enter protocol: ").upper()
    c_h_perm = input("Is host port enabled or disabled ? (e/D): ").lower()
    file.write(k*"   " + "     - image: " + str(c_image) + "\n" +
               k*"   " + "       name: " + str(c_name) + "\n" +
               k*"   " + "       ports: \n" +
               k*"   " + "        - containerPort: " + str(c_port) + "\n" +
               k*"   " + "          protocol: " + str(c_prot) + "\n")
    if c_h_perm == "e":
        c_h_port = int(input("Enter host port number: "))
        file.write(k*"   " + "          hostPort: " + str(c_h_port) + "\n")
    else: 
        exit


#8. Command:
def command():
    cmd_perm = input("Is any command to be added ? (y/N): ").lower()
    if cmd_perm == "y":
        cmd = input("Enter command inside of square brackets and double quotes: ")
        file.write(k*"   " + "       command: " + cmd + "\n")
    else:
        exit


#9. Arguments:
def args():
    arg_perm = input("Is any argument to be added ? (y/N): ").lower()
    if arg_perm == "y":
        arg = input("Enter argument inside of square brackets and double quotes: ")
        file.write(k*"   " + "       args: " + arg + "\n")
    else:
        exit


#10. Replicas and selectors:
def rep_sel():
    replicas = int(input("Enter number of pod replicas to be added: "))
    file.write(k*"   " + "   replicas: " + str(replicas) + "\n" +
               k*"   " + "   selector: \n" + 
               k*"   " + "      matchLabels: \n")
    ml_no = int(input("Enter number of match labels to be added: "))
    for ml in range(0, ml_no):
        ml_k = input("Enter match label key: ").lower()
        ml_v = input("Enter match label value for " + str(ml_k) + ": ").lower()
        file.write(k*"   " + "         " +  str(ml_k) + ": " + str(ml_v) + "\n")


#11. Environment variables: 
def env_var():
    env_perm = input("Is environment variable to be added ? (y/N): ").lower()    
    if env_perm == "y":
        env_ref_method=input("Method of Injecting environment variables to file (d: Direct, yr: YAML file reference, ser: Single Environment Variable Reference) :" )
        if env_ref_method == "d":
            file.write(k*"   " + "       env: \n")
            env_no = int(input("Enter number of environment variables to be added: "))
            for env in range(0, env_no):
                env_k = input("Enter environment variable key: ")
                env_v = input("Enter environment variable value for " + str(env_k) + ": ")
                file.write(k*"   " + "          " + str(env_k) + ": " + str(env_v) + "\n")
        elif env_ref_method == "yr":
            file.write(k*"   " + "       envFrom: \n")
            env_ref_file = input("Value is to be injected from (CM: ConfigMap or S: Secret)? ").lower()
            if env_ref_file == "cm":
                env_ref_file_name = input("Enter ConfigMap Environment reference file name: ")
                file.write(k*"   " + "          configMapRef: \n" + 
                           k*"   " + "             - name: " + env_ref_file_name + "\n")
            elif env_ref_file == "s":
                env_ref_file_name = input("Enter Secret Environment reference file name: ")
                file.write.write(k*"   " + "          secretRef: \n" +
                                 k*"   " + "             - name: " + env_ref_file_name + "\n")
            else:
                exit
        elif env_ref_method == "ser":
            file.write(k*"   " + "       env: \n")
            env_ref_file = input("Value is to be injected from (CM: ConfigMap or S: Secret)? ").lower()
            if env_ref_file == "cm":
                env_no = int(input("Enter number of environment variables to be added: "))
                for env_no in range(0, env_no):
                    env_var_name = input("Enter environment variable name: ")
                    env_ref_file_name = input("Enter ConfigMap Environment reference file name: ")
                    env_ref_key_name = input("Enter ConfigMap Environment reference key name: ")
                    file.write(k*"   " + "          - name: " +  str(env_var_name) + "\n" + 
                               k*"   " + "             valueFrom: \n" + 
                               k*"   " + "                configMapRef: \n" + 
                               k*"   " + "                   name: " + str(env_ref_file_name) +"\n" + 
                               k*"   " + "                   key: " + str(env_ref_key_name) +"\n")
            elif env_ref_file == "s":
                env_no = int(input("Enter number of environment variables to be added: "))
                for env_no in range(0, env_no):
                    env_var_name = input("Enter environment variable name: ")
                    env_ref_file_name = input("Enter Secret Environment reference file name: ")
                    env_ref_key_name = input("Enter Secret Environment reference key name: ")
                    file.write(k*"   " + "          - name: " +  str(env_var_name) + "\n" + 
                               k*"   " + "             valueFrom: \n" + 
                               k*"   " + "                secretKeyRef: \n" + 
                               k*"   " + "                   name: " + str(env_ref_file_name) +"\n" + 
                               k*"   " + "                   key: " + str(env_ref_key_name) +"\n")
            else:
                exit
    else:
        exit


#12. Service Account:
def service_acc():
    sa_perm = input("Is service account to be added ? (y/N): ").lower()
    if sa_perm == "y":
        sa_name = input("Enter Service Account name: ")
        file.write(k*"   " + "   serviceAccount: " + str(sa_name) + "\n")
    else:
        exit
    sa_aa_perm = input("Is auto assigning of service accunt policy to be changes ? (y/N):").lower()
    if sa_aa_perm == "y":
        sa_aa = input("Enter policy for Auto Assigning Service Account to be set to True or False: ").lower()
        file.write(k*"   " + "   automountServiceAccountToken: " + str(sa_aa) + "\n")
    else:
        exit


#13. Resource Assignment:
def resources():
    resc_perm=("Is resource assignment to be added? (y/N) : ").lower()
    if resc_perm == "y":
        file.write(k*"   " + "   resources: \n")
        mem_perm=("Is memory resource to be assigned? (y/N) : ").lower()
        if mem_perm == "y":
            mem_req = input("Enter minimum memory request inside double quotes with size (Ki, Mi, Gi, K, M, G): ")
            mem_lim = input("Enter memory limit inside double quotes with size (Ki, Mi, Gi, K, M, G): ")
            def mem_request():
                file.write(k*"   " + "         memory: " + str(mem_req) + "\n")
            def mem_limit():
                file.write(k*"   " + "         memory: " + str(mem_lim) + "\n")
        else:
            exit
        cpu_perm=("Is memory resource to be assigned? (y/N) : ").lower()
        if cpu_perm == "y":
            cpu_req = input("Enter minimum CPU request inside double quotes with size (Ki, Mi, Gi, K, M, G): ")
            cpu_lim = input("Enter CPU limit inside double quotes with size (Ki, Mi, Gi, K, M, G): ")
            def cpu_request():
                file.write(k*"   " + "      memory: " + str(cpu_req) + "\n")
            def cpu_limit():
                file.write(k*"   " + "      memory: " + str(cpu_lim) + "\n")
        else:
            exit
        if mem_perm == "y" and cpu_perm == "y":
            file.write(k*"   " + "      requests: ")
            mem_request()
            cpu_request()
            file.write(k*"   " + "      limts: ")
            mem_lim()
            cpu_lim()
        elif mem_perm == "y" and cpu_perm == "n":
            file.write(k*"   " + "      requests: ")
            mem_request()
            file.write(k*"   " + "      limts: ")
            mem_lim()
        elif mem_perm == "n" and cpu_perm == "y":
            file.write(k*"   " + "      requests: ")
            cpu_request()
            file.write(k*"   " + "      limts: ")
            cpu_lim()


#14. Taints and Tolerations: 
def tolerations():
    tol_perm = input("Is any toleration to be added to pod ? (y/n): ").lower()
    if tol_perm == "y":
        file.write(k*"   " + "   tolerations: \n")
        tol_k = input("Enter key for toleration in double quotes: ")
        file.write(k*"   " + "      - key: " + str(tol_k) + "\n")
        tol_o = input('Enter operator for toleration in double quotes ("Equal", "Exists") > Copy with quotes: ')
        file.write(k*"   " + "        operator: " + str(tol_o) + "\n")
        if tol_o == '"Equal"' :
            tol_v = input("Enter value for toleration in double quotes: ")
            file.write(k*"   " + "        value: " + str(tol_v) + "\n")
        else:
            exit
        tol_e = input('Enter toleration effect in double quotes ("NoSchedule", "PreferNoSchedule", "NoExecute") > Copy with quotes: ')
        file.write(k*"   " + "        effect: " + str(tol_e) + "\n")


#15. Node Selector:
def node_sel():
    node_sel_perm = input("Is node selector to be added ? (y/N): ").lower()
    if node_sel_perm == "y":
        file.write(k*"   " + "   nodeSelector: \n")
        node_sel_no = int(input("Enter number of node selectors to be added: "))
        for nsn in range(0, node_sel_no):
            node_sel_k = input("Enter node selector key: ")
            node_sel_v = input("Enter node selector value for" + str(node_sel_k) + ": ")
            file.write(k*"   " + "      " + str(node_sel_k) + ": " + str(node_sel_v) + " \n") 
    else:
        exit


#16. Node Affinity (Match expression based):
def node_aff():
    node_aff_perm = input("Is node affinity to be added ? (y/N): ").lower()
    if node_aff_perm == "y":
        node_aff_policy = input("Enter policy to be applied from below: \n" 
                                "rdside = requiredDuringSchedulingIgnoredDuringExecution \n"
                                "pdside = preferredDuringSchedulingIgnoredDuringExecution \n"
                                "rdsrde = requiredDuringSchedulingRequiredDuringExecution : ")
        if node_aff_policy == "rdside" or node_aff_policy == "requiredDuringSchedulingIgnoredDuringExecution":
            node_aff_policy = "requiredDuringSchedulingIgnoredDuringExecution"
            file.write(k*"   " + "   affinity: \n" + 
                       k*"   " + "      nodeAffinity: \n" +
                       k*"   " + "         " + str(node_aff_policy) + ": \n")
        elif node_aff_policy == "pdside" or node_aff_policy == "preferredDuringSchedulingIgnoredDuringExecution":
            node_aff_policy = "preferredDuringSchedulingIgnoredDuringExecution"
            file.write(k*"   " + "   affinity: \n" + 
                       k*"   " + "      nodeAffinity: \n" +
                       k*"   " + "         " + str(node_aff_policy) + ": \n")   
        elif node_aff_policy == "rdsrde" or node_aff_policy == "preferredDuringSchedulingIgnoredDuringExecution":
            node_aff_policy = "requiredDuringSchedulingRequiredDuringExecution"
            file.write(k*"   " + "   affinity: \n" + 
                       k*"   " + "      nodeAffinity: \n" +
                       k*"   " + "         " + str(node_aff_policy) + ": \n")               
        na_mexp_perm = input("Is node affinity to be set using match expressions ? (y/N): ").lower()
        if na_mexp_perm == "y":
            na_mxp_k = input("Enter match expression key for node affinity: ")
            na_mxp_op = input("Enter operator for relating key value pairs (In | NotIn) :")
            na_mxp_v_no = int(input("Enter number of match expression value for node affinity key " + str(na_mxp_k) + ": "))
            file.write(k*"   " + "            nodeSelectorTerms: \n" + 
                       k*"   " + "               - matchExpressions: \n" +
                       k*"   " + "                    - key: " + str(na_mxp_k) + "\n" +
                       k*"   " + "                      operator: " + str(na_mxp_op) + "\n" + 
                       k*"   " + "                      value: \n")
            for na_mx_v_no in range(0, na_mxp_v_no):
                na_mxp_v = input("Enter value for given match expression node affinity key: ")
                file.write(k*"   " + "                         - " + str(na_mxp_v) + "\n")
    else:
        exit


#17. CronJobs:
def cron_jobs():
    cj_perm=input("Is cron job to be added ? (y/N):").lower()
    if cj_perm == "y":
        cj_sch = input("Enter job schedule (* * * * * / min hr dom m dow) : ")
        cj_sch = '"' + cj_sch + '"'
        file.write(k*"   " + "   schedule: "+ str(cj_sch) + "\n" +
                   k*"   " + "   jobTemplate: \n")


#18. Jobs:
def jobs():
    c_job_perm = input("Is completion to be added ? (y/N):").lower()
    if c_job_perm == "y":
        c_job = int(input("Enter number of times the job is to be completed: "))
        file.write(k*"   " + "   completion: "+ str(c_job) + "\n")
    else:
        exit
    p_job_perm = input("Are parellel pods to be added ? (y/N):").lower()
    if p_job_perm == "y":
        p_job = int(input("Enter number of parallel jobs/pods to be initiated: "))
        file.write(k*"   " + "   parallelism: "+ str(p_job) + "\n")
    else:
        exit


#19. Restart Policy:
def restart_policy():
    rp_perm=input("Is restart policy to be added ? (y/N):").lower()
    if rp_perm == "y":
        rp_sel = input("Enter restart policy from (Never | OnFailure | Always): ")
        file.write(k*"   " + "   restartPolicy: " + str(rp_sel) + "\n")
    else:
        exit


#20. Readiness Probe:
def readiness_probe():
    red_prob_perm = input("Is readiness probe to be added ? (y/N): ").lower()
    if red_prob_perm == "y":
        red_prob_kind = input("Enter type of readiness probe (http | tcp | exec): ")
        if red_prob_kind == "http":
            #Make the following questions more descriptive:
            rp_path = input("Enter path: ")
            rp_ids = int(input("Enter Initial delay in seconds: "))
            rp_ps = int(input("Enter time interval in seconds after which pod has to be started: "))
            file.write(k*"   " + "        readinessProbe: \n" + 
                       k*"   " + "           httpGet: \n" + 
                       k*"   " + "              path: " + str(rp_path) + "\n" +
                       k*"   " + "              port: 8080 \n" +
                       k*"   " + "           initialDelaySeconds: " + str(rp_ids) + "\n" +
                       k*"   " + "           periodSeconds: " + str(rp_ps) + "\n")
        elif red_prob_kind == "tcp":
            #Make the following questions more descriptive:
            rp_ids = int(input("Enter Initial delay in seconds: "))
            rp_ps = int(input("Enter time interval in seconds after which pod has to be started: "))
            file.write(k*"   " + "        readinessProbe: \n" + 
                       k*"   " + "           tcpSocket: \n" +
                       k*"   " + "              port: 3306 \n" +
                       k*"   " + "           initialDelaySeconds: " + str(rp_ids) + "\n" +
                       k*"   " + "           periodSeconds: " + str(rp_ps) + "\n")
        elif red_prob_kind == "exec":
            #Make the following questions more descriptive:
            
            file.write(k*"   " + "        exec: \n" + 
                       k*"   " + "           command: \n")
            rp_cmd_no = int(input("Enter number of command to be added: "))
            for rp_cmd_no in range(0, rp_cmd_no):
                rp_cmd = input("Enter command: ")
                file.write(k*"   " + "            - " + str(rp_cmd) + "\n")           
            rp_ids = int(input("Enter Initial delay in seconds: "))
            rp_ps = int(input("Enter time interval in seconds after which pod has to be started: "))
            file.write(k*"   " + "           initialDelaySeconds: " + str(rp_ids) + "\n" +
                       k*"   " + "           periodSeconds: " + str(rp_ps) + "\n")
        else:
            exit


#21 Liveness Probe:
def liveness_probe():
    liv_prob_perm = input("Is liveness probe to be added ? (y/N): ").lower()
    if liv_prob_perm == "y":
        liv_prob_kind = input("Enter type of liveness probe (http | tcp | exec): ")
        if liv_prob_kind == "http":
            #Make the following questions more descriptive:
            lp_path = input("Enter path: ")
            lp_ids = int(input("Enter Initial delay in seconds: "))
            lp_ps = int(input("Enter time interval in seconds after which pod has to be started: "))
            file.write(k*"   " + "        livenessProbe: \n" + 
                       k*"   " + "           httpGet: \n" + 
                       k*"   " + "              path: " + str(lp_path) + "\n" +
                       k*"   " + "              port: 8080 \n" +
                       k*"   " + "           initialDelaySeconds: " + str(lp_ids) + "\n" +
                       k*"   " + "           periodSeconds: " + str(lp_ps) + "\n")
        elif liv_prob_kind == "tcp":
            #Make the following questions more descriptive:
            lp_ids = int(input("Enter Initial delay in seconds: "))
            lp_ps = int(input("Enter time interval in seconds after which pod has to be started: "))
            file.write(k*"   " + "        livenessProbe: \n" + 
                       k*"   " + "           tcpSocket: \n" +
                       k*"   " + "              port: 3306 \n" +
                       k*"   " + "           initialDelaySeconds: " + str(lp_ids) + "\n" +
                       k*"   " + "           periodSeconds: " + str(lp_ps) + "\n")
        elif liv_prob_kind == "exec":
            #Make the following questions more descriptive:
            file.write(k*"   " + "        exec: \n" + 
                       k*"   " + "           command: \n")
            lp_cmd_no = int(input("Enter number of command to be added: "))
            for lp_cmd_no in range(0, lp_cmd_no):
                lp_cmd = input("Enter command: ")
                file.write(k*"   " + "            - " + str(lp_cmd) + "\n")           
            lp_ids = int(input("Enter Initial delay in seconds: "))
            lp_ps = int(input("Enter time interval in seconds after which pod has to be started: "))
            file.write(k*"   " + "           initialDelaySeconds: " + str(lp_ids) + "\n" +
                       k*"   " + "           periodSeconds: " + str(lp_ps) + "\n")
        else:
            exit

#22. Services:
def service():
    service_type=input("Enter Service Type (CI: Cluster IP, NP: Node Port, LB : Load Balancer,  I: Ingress): ").lower()
    if service_type == "ci":
        file.write(k*"   " + "   type: ClusterIP \n" +
                   k*"   " + "   selector: \n")
        service_selector_no=int(input("Enter number of selector labels to be added in: "))
        for ssn in range(0, service_selector_no):
            ssnk=input("Enter Service Label Key: ")
            ssnv=input("Enter Service Label Value for " + str(ssnk) + ": ")
            file.write("      " + str(ssnk) + ": " + str(ssnv) + "\n")
        service_port_no=input("Enter service port number: ")
        service_target_port_no=input("Enter Target port number for pod container: ")
        service_proto_type=input("Enter Service Protocol Type: ").upper()
        file.write(k*"   " + "   ports: \n" + 
                   k*"   " + "    - port: " + str(service_port_no) + "\n" +
                   k*"   " + "      targetPort: " + str(service_target_port_no) + "\n" +
                   k*"   " + "      protocol: " + str(service_proto_type) + "\n")
    elif service_type == "np":
        file.write(k*"   " + "   type: NodePort \n" +
                   k*"   " + "   selector: \n")
        service_selector_no=int(input("Enter number of selector labels to be added in: "))
        for ssn in range(0, service_selector_no):
            ssnk=input("Enter Service Label Key: ")
            ssnv=input("Enter Service Label Value for " + str(ssnk) + ": ")
            file.write("      " + str(ssnk) + ": " + str(ssnv) + "\n")
        service_port_no=int(input("Enter Service port number: "))
        service_target_port_no=int(input("Enter Target port number for Container in Pod: "))
        service_node_port_no=int(input("Enter Node port number: "))
        service_proto_type=input("Enter Service Protocol Type: ").upper()
        file.write(k*"   " + "   ports: \n" + 
                   k*"   " + "    - port: " + str(service_port_no) + "\n" +
                   k*"   " + "      targetPort: " + str(service_target_port_no) + "\n" + 
                   k*"   " + "      nodePort: " + str(service_node_port_no) + "\n" + 
                   k*"   " + "      protocol: " + str(service_proto_type) + "\n")
    elif service_type == "lb":
        file.write(k*"  " + "   type: LoadBalancer \n" +
                   k*"  " + "   selector: \n")
        service_selector_no=int(input("Enter number of selector labels to be added in: "))
        for ssn in range(0, service_selector_no):
            ssnk=input("Enter Service Label Key: ")
            ssnv=input("Enter Service Label Value for " + str(ssnk) + ": ")
            file.write("      " + str(ssnk) + ": " + str(ssnv) + "\n")
        service_port_no=int(input("Enter Service port number: "))
        service_target_port_no=int(input("Enter Target port number for Container in Pod: "))
        service_node_port_no=int(input("Enter Node port number: "))
        service_proto_type=input("Enter Service Protocol Type: ").upper()
        file.write(k*"   " + "   ports: \n" + 
                   k*"   " + "    - port: " + str(service_port_no) + "\n" +
                   k*"   " + "      targetPort: " + str(service_target_port_no) + "\n" + 
                   k*"   " + "      nodePort: " + str(service_node_port_no) + "\n" + 
                   k*"   " + "      protocol: " + str(service_proto_type) + "\n")
    elif service_type == "i":
        i_type = input("Enter which method is to be adopted to expose backend (D: Direct, P: Path Based, H: Host Based)").lower()
        if i_type == "d":
            i_s_n = input("Enter backend service name: ")
            i_s_p = int(input("Enter port in which backend service is to be exposed on: "))
            file.write(k*"   " + "   backend: \n" +
                       k*"   " + "      serviceName: " + str(i_s_n) + "\n" + 
                       k*"   " + "      servicePort: " + str(i_s_p) + "\n")
        elif i_type == "p":
            i_prot = input("Enter protocol for service (http | https ): ").lower()
            if i_prot == "http":
                file.write(k*"   " + "   rules: \n" + 
                           k*"   " + "      - http: \n" +
                           k*"   " + "           paths: \n")
                i_path_no = int(input("Enter number of paths to be added for backends: "))
                for i_path in range(0, i_path_no):
                    i_path_name = input("Enter backend path: ")
                    i_s_n = input("Enter backend service name: ")
                    i_s_p = int(input("Enter port in which backend service is to be exposed on: "))
                    file.write(k*"   " + "              - path: " + str(i_path_name) + "\n" +
                               k*"   " + "                backend: \n" +
                               k*"   " + "                   serviceName: " + str(i_s_n) + "\n" + 
                               k*"   " + "                   servicePort: " + str(i_s_p) + "\n")
            #Check if more configuration to be added or not for using https:
            if i_prot == "https":
                file.write(k*"   " + "   rules: \n" + 
                           k*"   " + "      - https: \n" +
                           k*"   " + "           paths: \n")
                i_path_no = int(input("Enter number of paths to be added for backends: "))
                for i_path in range(0, i_path_no):
                    i_path_name = input("Enter backend path: ")
                    i_s_n = input("Enter backend service name: ")
                    i_s_p = int(input("Enter port in which backend service is to be exposed on: "))
                    file.write(k*"   " + "              - path: " + str(i_path_name) + "\n" +
                               k*"   " + "                backend: \n" +
                               k*"   " + "                   serviceName: " + str(i_s_n) + "\n" + 
                               k*"   " + "                   servicePort: " + str(i_s_p) + "\n")
            else:
                exit
        elif i_type == "h":
            file.write(k*"   " + "   rules: \n")
            i_host_no = int(input("Enter number of hostnames to be added for backends: "))
            for i_host_no in range(0, i_host_no):
                i_host_name = input("Enter hostname: ")
                i_prot = input("Enter protocol for service (http | https ): ").lower()
                i_s_n = input("Enter backend service name: ")
                i_s_p = int(input("Enter port in which backend service is to be exposed on: "))
                file.write(k*"   " + "      - host: " + str(i_host_name) + "\n" + 
                           k*"   " + "        " + str(i_prot) + ": \n" + 
                           k*"   " + "           paths: \n" +
                           k*"   " + "              - backend: \n" +
                           k*"   " + "                   serviceName: " + str(i_s_n) + "\n" + 
                           k*"   " + "                   servicePort: " + str(i_s_p) + "\n")
        else:
            exit()


#23.1. Volume mounted on Container:
def vol_mount_cont():
    vol_mnt_perm = input("Is volume mount to be added ? (y/N) : ")
    if vol_mnt_perm == "y":
        c_mnt_path = input("Enter Path in Container/Pod where volume is to be mounted: ")
        c_mnt_name = input("Enter volume name for mounted volume: ")
        file.write(k*"   " + "        volumeMounts: \n" + 
                   k*"   " + "           - mountPath: " + str(c_mnt_path) + "\n" + 
                   k*"   " + "             name: " + str(c_mnt_name) + "\n")


#23.2. Volume to be mounted from Host: 
def vol_mount_host():
    vol_mnt_host_perm = input("Is host volume to be specified (y : If Volume is mounted, n: If Volume is not mounted :)")
    if vol_mnt_host_perm == "y":
        h_vol_name = input("Enter volume name for host volume: ")
        h_mnt_vol = input("Enter path for volume on host which is to be mounted on container: ")
        #Check the actual types of paths:
        h_vol_type = input("Enter type of volume (Directory | File | etc)")
        #Check if there are other options than host Path:
        file.write(k*"   " + "   volumes: \n" + 
                   k*"   " + "      - name: " + str(h_vol_name) + "\n" + 
                   k*"   " + "        hostPath: \n" + 
                   k*"   " + "           path: " + str(h_mnt_vol) + "\n" + 
                   k*"   " + "           type: " + str(h_vol_type) + "\n")


#23.3. Volume to be mounted from Host for ConfigMap and Secret Injections: 
def vol_mount_host_cms():
    vol_mount_host_cms_perm = input("Is Config Map or Secret to be Injected using Volumes ? (y/N) :").lower()
    if vol_mount_host_cms_perm == "y":
        h_vol_name = input("Enter volume name for host volume: ")
        v_ask_cm_s = input("Is mounted volume is ConfigMap or Secret ?  ").lower()
        v_cm_s_name = input("Enter " + str(v_ask_cm_s) + " name : ")
        #Check if there are other options than host Path:
        file.write(k*"   " + "   volumes: \n" + 
                   k*"   " + "      - name: " + str(h_vol_name) + "\n" + 
                   k*"   " + "        " + str(v_ask_cm_s) +  ": \n" + 
                   k*"   " + "           name: " + str(v_cm_s_name) + "\n")


#24.1. Persistant Volume Create: 
def persistant_vol_cr():
    pv_am = input("Enter access mode for the volume (): ")
    pv_cap = input("Enter capacity of the host volume (Ki, Mi, Gi, K, , G): ")
    pv_hp = input("Enter Host Volume Path: ")
    file.write(k*"   " + "   accessModes: \n" + 
               k*"   " + "      - " + str(pv_am) + "\n" + 
               k*"   " + "   capacity: \n" + 
               k*"   " + "        storage: " + str(pv_cap) + "\n" +
               k*"   " + "   hostPath: \n" + 
               k*"   " + "        path: " + str(pv_hp) + "\n")
    #More additions are necessary for this field


#24.2. Persistant Volume Claim: 
def persistant_vol_cl():
    pv_am = input("Enter access mode for the volume (): ")
    pv_resc_req = input("Enter request storage capacity from the host volume (Ki, Mi, Gi, K, , G): ")
    file.write(k*"   " + "   accessModes: \n" + 
               k*"   " + "      - " + str(pv_am) + "\n" + 
               k*"   " + "   resources: \n" + 
               k*"   " + "        requests: \n" +
               k*"   " + "           storage: " + str(pv_resc_req) + "\n")
    #More additions are necessary for this field


#25. Resource Quota:
def resourcequota():
    file.write(k*"   " + "   hard: \n")
    resources_no = int(input("Enter number of resources to be added: "))
    for rqn in range(0, resources_no):
        rq_type_key=input("Enter type of resource quota as key: ")
        rq_type_value=input("Enter value for " + str(rq_type_key) + ": ")
        file.write(k*"   " + "      " + str(rq_type_key) + ": " + str(rq_type_value) + "\n")


##################################################################################################


comp = input("Enter Component to be created from following list: "
             "ConfigMap, Secret, Namespace , Pod "
             "Deployment, Ingress Controller, Service,"
             "Persistant Volume, Persistant Volume Claim, Resource Quota :").lower()
#ConfigMap
if comp == "configmap":
    component = "ConfigMap"
    file_name = input("Enter file name: ")
    file_name = file_name + ".yaml"
    file = open(file_name,"w")
    apiVersion()
    kind()
    i=0
    metadata()
    data()
#Secret
elif comp == "secret":
    component = "Secret"
    file_name = input("Enter file name: ")
    file_name = file_name + ".yaml"
    file = open(file_name,"w")
    apiVersion()
    kind()
    i=0
    metadata()
    data()
#Namespace:
elif comp == "namespace":
    component = "Namespace"
    file_name = input("Enter file name: ")
    file_name = file_name + ".yaml"
    file = open(file_name,"w")
    apiVersion()
    kind()
    i=0
    metadata()
#Pod:
elif comp == "pod":
    component = "Pod"
    file_name = input("Enter file name: ")
    file_name = file_name + ".yaml"
    file = open(file_name,"w")
    apiVersion()
    kind()
    i=0
    metadata()
    j=0
    spec()
    k=0
    containers()
    env_inject_type = input("Is env variable to be injected using file or volume ? (f/V) :").lower()
    if env_inject_type == "f":
        env_var()
    elif env_inject_type == "v":
        vol_mount_host_cms()
    else:
        exit
    command()
    args()
    service_acc()
    resources()
    tolerations()
    node_sel()
    node_aff()
    restart_policy()
    readiness_probe()
    liveness_probe()
    vol_mount_cont()
    vol_mount_host()
#Deployment:
elif comp == "deployment" or comp == "ingresscontroller" or comp == "ingress controller" :
    component = "Deployment"
    file_name = input("Enter file name: ")
    file_name = file_name + ".yaml"
    file = open(file_name,"w")
    cron_jb_perm_1 = input("Is Cron Job to be added ? (y/N) : ").lower()
    if cron_jb_perm_1 == "y":
            apiVersion()
            kind()
            i=0
            metadata()
            j=0
            spec()
            k=0
            cron_jobs()
            job_perm = input("Is Job to be added ? (y/N) : ").lower()
            if job_perm == "y":
                j=2
                spec()
                k=2
                jobs()
                rep_sel()
                template()
                i=3
                metadata()
                j=3
                spec()
                k=3
                containers()
                env_inject_type = input("Is env variable to be injected using file or volume ? (f/V) :").lower()
                if env_inject_type == "f":
                    env_var()
                elif env_inject_type == "v":
                    vol_mount_host_cms()
                else:
                    exit
                command()
                args()
                service_acc()
                resources()
                tolerations()
                node_sel()
                node_aff()
                restart_policy()
                readiness_probe()
                liveness_probe()
                vol_mount_cont()
                vol_mount_host()    
            elif job_perm == "n":
                k=2
                rep_sel()
                template()
                i=3
                metadata()
                j=3
                spec()
                k=3
                containers()
                env_inject_type = input("Is env variable to be injected using file or volume ? (f/V) :").lower()
                if env_inject_type == "f":
                    env_var()
                elif env_inject_type == "v":
                    vol_mount_host_cms()
                else:
                    exit
                command()
                args()
                service_acc()
                resources()
                tolerations()
                node_sel()
                node_aff()
                restart_policy()
                readiness_probe()
                liveness_probe()
                vol_mount_cont()
                vol_mount_host()    
    elif cron_jb_perm_1 == "n":
        job_perm = input("Is Job to be added ? (y/N) : ").lower()
        if job_perm == "y":
            apiVersion()
            kind()
            i=0
            metadata()
            j=0
            spec()
            jobs()
            rep_sel()
            template()
            i=2
            metadata()
            j=2
            spec()
            k=2
            containers()
            env_inject_type = input("Is env variable to be injected using file or volume ? (f/V) :").lower()
            if env_inject_type == "f":
                env_var()
            elif env_inject_type == "v":
                vol_mount_host_cms()
            else:
                exit
            command()
            args()
            service_acc()
            resources()
            tolerations()
            node_sel()
            node_aff()
            restart_policy()
            readiness_probe()
            liveness_probe()
            vol_mount_cont()
            vol_mount_host()    
        elif job_perm == "n":
            apiVersion()
            kind()
            i=0
            metadata()
            j=0
            spec()
            rep_sel()
            template()
            i=2
            metadata()
            j=2
            spec()
            k=2
            containers()
            env_inject_type = input("Is env variable to be injected using file or volume ? (f/V) :").lower()
            if env_inject_type == "f":
                env_var()
            elif env_inject_type == "v":
                vol_mount_host_cms()
            else:
                exit
            command()
            args()
            service_acc()
            resources()
            tolerations()
            node_sel()
            node_aff()
            restart_policy()
            readiness_probe()
            liveness_probe()
            vol_mount_cont()
            vol_mount_host()
#Service:
elif comp == "service":
    component = "Service"
    file_name = input("Enter file name: ")
    file_name = file_name + ".yaml"
    file = open(file_name,"w")
    apiVersion()
    kind()
    i = 0
    metadata()
    j = 0
    spec()
    k = 0
    service()
#Persistant Volume Create:
elif comp == "persistantvolume" or comp == "persistant volume":
    component = "PersistantVolume"
    file_name = input("Enter file name: ")
    file_name = file_name + ".yaml"
    file = open(file_name,"w")
    apiVersion()
    kind()
    i = 0
    metadata()
    j = 0
    spec()
    k=0
    persistant_vol_cr()
#Persistant Volume Claim:
elif comp == "persistantvolumeclaim" or comp == "persistant volume claim":
    component = "PersistantVolumeClaim"
    file_name = input("Enter file name: ")
    file_name = file_name + ".yaml"
    file = open(file_name,"w")
    apiVersion()
    kind()
    i = 0
    metadata()
    j = 0
    spec()
    k=0
    persistant_vol_cl()
#Resource Quota:
elif comp == "resourcequota" or comp == "resource quota":
    component = "ResourceQuota"
    file_name = input("Enter file name: ")
    file_name = file_name + ".yaml"
    file = open(file_name,"w")
    apiVersion()
    kind()
    i = 0
    metadata()
    j = 0
    spec()
    k=0
    resourcequota()





