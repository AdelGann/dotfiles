#!/bin/sh

# Mensaje de despedida
echo "👋 Adiós! Desinstalando km_v2..."

# Función para desinstalar paquetes usando yay
uninstall_with_yay() {
  echo "🗑️  Desinstalando paquetes con yay..."
  yay -Rns ttf-firacode-nerd xdotool xclip dunst sxhkd feh blueman variety pamac-aur udiskie volumeicon kitty parcellite arandr xrandr qtile-extras pavucontrol rofi neovim ranger fd ripgrep bat duf fzf neofetch fastfetch lazygit thunar maim ark unrar
}

# Función para desinstalar paquetes usando dnf
uninstall_with_dnf() {
  echo "🗑️  Desinstalando paquetes con dnf..."
  sudo dnf remove sxhkd feh dunst xclip maim kitty rofi fastfetch unrar bat fd-find ranger neovim variety duf fzf xclipboard qtile-extras qtile lazygit ripgrep zsh picom lsd zsh-syntax-highlighting zsh-autosuggestions magick i3lock yazi -y
  
  # Deshabilitar repositorios copr
  sudo dnf copr disable atim/lazygit -y
  sudo dnf copr disable frostyx/qtile -y
  sudo dnf copr disable lihaohong/yazi -y
  
  # Restaurar qtile.desktop original si existe backup
  local config_dir="/usr/share/xsessions/qtile.desktop"
  local backup_dir="/usr/share/xsessions/qtile.desktop_bak"
  if [ -d "$backup_dir" ]; then
    sudo rm -rf "$config_dir"
    sudo mv "$backup_dir" "$config_dir"
    echo "✅ qtile.desktop original restaurado"
  else
    sudo rm -rf "$config_dir"
    echo "✅ qtile.desktop eliminado"
  fi
}

# Función para restaurar configuraciones de respaldo
restore_backup() {
  local config_dir="$1"
  local backup_dir="${config_dir}_bak"

  if [ -d "$backup_dir" ]; then
    echo "🔄 Restaurando $config_dir desde respaldo..."
    rm -rf "$config_dir"
    mv "$backup_dir" "$config_dir"
    echo "✅ $config_dir restaurado"
  else
    echo "🗑️  Eliminando $config_dir (sin respaldo encontrado)..."
    rm -rf "$config_dir"
    echo "✅ $config_dir eliminado"
  fi
}

# Función para restaurar zshrc
restore_zshrc() {
  local zshrc_backup="$HOME/.zshrc_bak"
  if [ -f "$zshrc_backup" ]; then
    echo "🔄 Restaurando .zshrc desde respaldo..."
    rm -f "$HOME/.zshrc"
    mv "$zshrc_backup" "$HOME/.zshrc"
    echo "✅ .zshrc restaurado"
  else
    echo "🗑️  Eliminando .zshrc (sin respaldo encontrado)..."
    rm -f "$HOME/.zshrc"
    echo "✅ .zshrc eliminado"
  fi
}

# Desinstalación de paquetes
if command -v yay >/dev/null 2>&1; then
  uninstall_with_yay
elif command -v dnf >/dev/null 2>&1; then
  uninstall_with_dnf
else
  echo "❌ No se encontró gestor de paquetes"
  exit 1
fi

# Restaurar configuraciones
echo "🔄 Restaurando configuraciones..."
restore_backup "$HOME/.config/nvim"
restore_backup "$HOME/.config/qtile"
restore_backup "$HOME/.config/kitty"
restore_backup "$HOME/.config/rofi"
restore_backup "$HOME/.config/picom"
restore_backup "$HOME/.config/yazi"
restore_backup "$HOME/.config/zellij"
restore_backup "$HOME/.config/fastfetch"
restore_backup "$HOME/.config/clipcat"

# Restaurar zshrc
restore_zshrc

# Limpiar archivos temporales y caché
echo "🧹 Limpiando caché y archivos temporales..."
if command -v yay >/dev/null 2>&1; then
  yay -Sc --noconfirm
elif command -v dnf >/dev/null 2>&1; then
  sudo dnf clean all
fi

echo "✅ ¡Desinstalación completada! km_v2 ha sido removido de tu sistema."
echo "💡 Recuerda reiniciar tu sesión para aplicar todos los cambios." 