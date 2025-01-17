$TTL    86400
@       IN      SOA     ns1.empresa-a.com. root.empresa-a.com. (
                      20250117    ; Serial
                      3600        ; Refresh
                      1800        ; Retry
                      1209600     ; Expire
                      86400 )     ; Minimum TTL

        IN      NS      ns1.empresa-a.com.
ns1     IN      A       10.0.0.20  ; IP do servidor DNS na Sub-rede A

www     IN      A       10.0.0.10  ; IP do container web-a
