import network 
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True) 
sta_if.scan()
sta_if.connect("BROWAN_OFFICE","598dc25535")
sta_if.ifconfig()
