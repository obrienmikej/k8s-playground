metadata:
  creationTimestamp: 2019-01-12T20:29:11Z
  name: k8s.mikejobrien.com
spec:
  api:
    dns: {}
  authorization:
    rbac: {}
  channel: stable
  cloudProvider: aws
  clusterDNSDomain: cluster.local
  configBase: s3://k8s-mikejobrien-com-state-store/k8s.mikejobrien.com
  configStore: s3://k8s-mikejobrien-com-state-store/k8s.mikejobrien.com
  dnsZone: Z2UH0OY9ST4TG6
  docker:
    ipMasq: false
    ipTables: false
    logDriver: json-file
    logLevel: warn
    logOpt:
    - max-size=10m
    - max-file=5
    storage: overlay2,overlay,aufs
    version: 17.03.2
  etcdClusters:
  - etcdMembers:
    - instanceGroup: master-us-west-1a
      name: a
    image: k8s.gcr.io/etcd:2.2.1
    name: main
    provider: Legacy
    version: 2.2.1
  - etcdMembers:
    - instanceGroup: master-us-west-1a
      name: a
    image: k8s.gcr.io/etcd:2.2.1
    name: events
    provider: Legacy
    version: 2.2.1
  iam:
    allowContainerRegistry: true
    legacy: false
  keyStore: s3://k8s-mikejobrien-com-state-store/k8s.mikejobrien.com/pki
  kubeAPIServer:
    allowPrivileged: true
    anonymousAuth: false
    apiServerCount: 1
    authorizationMode: RBAC
    bindAddress: 0.0.0.0
    cloudProvider: aws
    enableAdmissionPlugins:
    - Initializers
    - NamespaceLifecycle
    - LimitRanger
    - ServiceAccount
    - PersistentVolumeLabel
    - DefaultStorageClass
    - DefaultTolerationSeconds
    - MutatingAdmissionWebhook
    - ValidatingAdmissionWebhook
    - NodeRestriction
    - ResourceQuota
    etcdQuorumRead: false
    etcdServers:
    - http://127.0.0.1:4001
    etcdServersOverrides:
    - /events#http://127.0.0.1:4002
    image: k8s.gcr.io/kube-apiserver:v1.11.6
    insecureBindAddress: 127.0.0.1
    insecurePort: 8080
    kubeletPreferredAddressTypes:
    - InternalIP
    - Hostname
    - ExternalIP
    logLevel: 2
    requestheaderAllowedNames:
    - aggregator
    requestheaderExtraHeaderPrefixes:
    - X-Remote-Extra-
    requestheaderGroupHeaders:
    - X-Remote-Group
    requestheaderUsernameHeaders:
    - X-Remote-User
    securePort: 443
    serviceClusterIPRange: 100.64.0.0/13
    storageBackend: etcd2
  kubeControllerManager:
    allocateNodeCIDRs: true
    attachDetachReconcileSyncPeriod: 1m0s
    cloudProvider: aws
    clusterCIDR: 100.96.0.0/11
    clusterName: k8s.mikejobrien.com
    configureCloudRoutes: true
    image: k8s.gcr.io/kube-controller-manager:v1.11.6
    leaderElection:
      leaderElect: true
    logLevel: 2
    useServiceAccountCredentials: true
  kubeDNS:
    cacheMaxConcurrent: 150
    cacheMaxSize: 1000
    domain: cluster.local
    replicas: 2
    serverIP: 100.64.0.10
  kubeProxy:
    clusterCIDR: 100.96.0.0/11
    cpuRequest: 100m
    hostnameOverride: '@aws'
    image: k8s.gcr.io/kube-proxy:v1.11.6
    logLevel: 2
  kubeScheduler:
    image: k8s.gcr.io/kube-scheduler:v1.11.6
    leaderElection:
      leaderElect: true
    logLevel: 2
  kubelet:
    allowPrivileged: true
    anonymousAuth: false
    cgroupRoot: /
    cloudProvider: aws
    clusterDNS: 100.64.0.10
    clusterDomain: cluster.local
    enableDebuggingHandlers: true
    evictionHard: memory.available<100Mi,nodefs.available<10%,nodefs.inodesFree<5%,imagefs.available<10%,imagefs.inodesFree<5%
    featureGates:
      ExperimentalCriticalPodAnnotation: "true"
    hostnameOverride: '@aws'
    kubeconfigPath: /var/lib/kubelet/kubeconfig
    logLevel: 2
    networkPluginMTU: 9001
    networkPluginName: kubenet
    nonMasqueradeCIDR: 100.64.0.0/10
    podInfraContainerImage: k8s.gcr.io/pause-amd64:3.0
    podManifestPath: /etc/kubernetes/manifests
  kubernetesApiAccess:
  - 0.0.0.0/0
  kubernetesVersion: 1.11.6
  masterInternalName: api.internal.k8s.mikejobrien.com
  masterKubelet:
    allowPrivileged: true
    anonymousAuth: false
    cgroupRoot: /
    cloudProvider: aws
    clusterDNS: 100.64.0.10
    clusterDomain: cluster.local
    enableDebuggingHandlers: true
    evictionHard: memory.available<100Mi,nodefs.available<10%,nodefs.inodesFree<5%,imagefs.available<10%,imagefs.inodesFree<5%
    featureGates:
      ExperimentalCriticalPodAnnotation: "true"
    hostnameOverride: '@aws'
    kubeconfigPath: /var/lib/kubelet/kubeconfig
    logLevel: 2
    networkPluginMTU: 9001
    networkPluginName: kubenet
    nonMasqueradeCIDR: 100.64.0.0/10
    podInfraContainerImage: k8s.gcr.io/pause-amd64:3.0
    podManifestPath: /etc/kubernetes/manifests
    registerSchedulable: false
  masterPublicName: api.k8s.mikejobrien.com
  networkCIDR: 172.20.0.0/16
  networking:
    kubenet: {}
  nonMasqueradeCIDR: 100.64.0.0/10
  secretStore: s3://k8s-mikejobrien-com-state-store/k8s.mikejobrien.com/secrets
  serviceClusterIPRange: 100.64.0.0/13
  sshAccess:
  - 0.0.0.0/0
  subnets:
  - cidr: 172.20.32.0/19
    name: us-west-1a
    type: Public
    zone: us-west-1a
  topology:
    dns:
      type: Public
    masters: public
    nodes: public
