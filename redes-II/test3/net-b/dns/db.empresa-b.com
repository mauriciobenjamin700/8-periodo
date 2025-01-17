// /etc/bind/db.empresa-b.com

$TTL    86400
@       IN      SOA     ns1.empresa-b.com. root.empresa-b.com. (
                      20250117    ; Serial
                      3600        ; Refresh
                      1800        ; Retry
                      1209600     ; Expire
                      86400 )     ; Minimum TTL

        IN      NS      ns1.empresa-b.com.
ns1     IN      A       20.0.0.20  ; IP do servidor DNS na Sub-rede B

www     IN      A       20.0.0.10  ; IP do container web-b
