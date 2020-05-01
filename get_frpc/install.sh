main() {
  # frpc version: v0.33.0
  # todo 检测ssh端口
  if [ "$(id -u)" != "0" ]; then
    echo "Error: this script must be run as root" 1>&2
    exit 1
  fi
  lineIndex=$(awk '/^__PAYLOAD_BELOW__/ {print NR + 1; exit 0; }' "$0")
  tail -n+"$lineIndex" "$0" >payload.tar.gz
  tar -xvf payload.tar.gz
  cp payload/frpc /usr/bin/frpc
  #  cp payload/frps /usr/bin/frps
  mkdir -p /etc/frp/
  cp payload/*ini /etc/frp/
  # sshPort=$(netstat -apn | grep sshd | grep 0.0.0.0 | awk -F: '{print $2}' | awk '{print $1}')
  cp payload/systemd/*service /etc/systemd/system/
  systemctl enable frpc
  systemctl start frpc
  echo
  echo 'done'
  rm -f payload.tar.gz
  rm -rf payload/
  exit 0
}
main

__PAYLOAD_BELOW__
