# UTOPIA BOMBSQUAD SERVER

Modded server scripts to host Ballistica (BombSquad) dedicated servers. Running on Ballistica API 9 (server manager v1.3.5).

> **Migrated from API 7 to API 9.** Some features may be unstable or missing.
> For the previous API 7 build, see the [API 7 release](https://github.com/imayushsaini/Bombsquad-Ballistica-Modded-Server/releases/tag/1.7.26).

## Prerequisites
- Basic knowledge of Linux
- A VPS (e.g. [Amazon Web Services](https://aws.amazon.com/), [Microsoft Azure](https://portal.azure.com/))
- Any Linux distribution (Ubuntu 22+ recommended)
- Python 3.13
- 1 GB free memory (2 GB recommended)

## Getting Started
This assumes you are on Ubuntu or an Ubuntu-based distribution.

### Install `software-properties-common`
```sh
sudo apt install software-properties-common -y
```

### Add Python Deadsnakes PPA
```sh
sudo add-apt-repository ppa:deadsnakes/ppa
```

### Install Python 3.13
```sh
sudo apt install python3.13 python3.13-dev python3.13-venv python3-pip -y
```

### Update installed packages
```sh
sudo apt update && sudo apt upgrade
```

### Create a tmux session
```sh
tmux new -s 43210
```

### Clone & configure
```sh
git clone --depth=1 https://github.com/Yuma-desu/UTOPIA-BOMBSQUAD-SERVER
cd UTOPIA-BOMBSQUAD-SERVER
```

### Edit the server config
Edit `config.json` in the root directory to set server name, port, admins, playlist, team names, team colors, etc.

```sh
nano config.json
```

### Make binaries executable
```sh
chmod 777 bombsquad_server
chmod 777 dist/bombsquad_headless
chmod 777 dist/bombsquad_headless_aarch64
```

### Start the server
```sh
./bombsquad_server
```

If your ports are open, you can connect to your server now.

---

## More Configuration

Open `dist/ba_root/mods/setting.json` in your preferred editor and change values to match your setup.

See the wiki for details:
- [How to edit settings.json](https://github.com/Yuma-desu/UTOPIA-BOMBSQUAD-SERVER/wiki/Server-Settings)
- [Available chat commands](https://github.com/Yuma-desu/UTOPIA-BOMBSQUAD-SERVER/wiki/Chat-commands)

---

## Adding yourself as Owner
- Open `dist/ba_root/mods/playersData/roles.json` in your preferred editor.
- Add your PB-ID to the owner ID list.
- Restart the server.

---

## Managing Players
Open `dist/ba_root/mods/playersData/profiles.json` in your preferred editor.

Here you can ban players, mute them, or disable their kick votes.

---

## Features
- **Rank System** — persistent player ranks and stats tracking
- **[Chat Commands](https://github.com/Yuma-desu/UTOPIA-BOMBSQUAD-SERVER/wiki/Chat-commands)** — extensive set of in-game commands
- **V2 Account** — cloud console support for server management
- **Ping check** — `/ping` chat command to check any player's latency via `_ba.get_client_ping()`
- **Hide/show player specs** — `/hideid` and `/showid` chat commands
- **[Role management](https://github.com/Yuma-desu/UTOPIA-BOMBSQUAD-SERVER/wiki/Chat-commands#role-management-system)** — create custom roles with specific command access and tags
- **Rejoin cooldown** — configurable delay before a player can rejoin
- **Leaderboard** — top 3 ranked players displayed top-right corner
- **Kick vote restrictions** — limit which players can start kick votes
- **Owner priority join** — server owners can join even when full (bypasses queue via IP recognition)
- **Auto-kick fake accounts** — unsigned/unverified accounts kicked automatically
- **Auto public queue** — queue mode toggles on/off when server is full
- **Auto night mode** — scheduled day/night visuals with fireflies
- **Transparent kick votes** — see who started a kick vote and against whom
- **Kick vote announcements** — configurable as chat message or screen message
- **IP & Device UUID tracking** — ban by IP or device
- **Team Chat** — prefix messages with `,` (comma) to send to teammates only
- **In-game popup chat** — prefix messages with `.` (dot) to send popup messages
- **Custom Voting System** — type `end`, `sm`, `nv`, or `dv` in chat for votes
- **Ballistica Web Stats** — support for [ballistica-web-stats](https://github.com/imayushsaini/ballistica-web-stats)
- **Discord Bot** — live sync of players, chats, and logs to Discord; execute chat commands remotely
- **Many mini-games & maps** — 40+ custom game modes
- **Colorful bomb explosions** — custom explosion colors
- **Floater** — floating effect support
- **Auto stats reset** — reset stats after a configurable number of days
- **Auto AFK/idle removal** — kick inactive players (configurable lobby and in-game thresholds)
- **Auto server update check** — checks for new server versions
- **All settings in one place** — no coding required, just edit `setting.json`
- **Configurable server host name**
- **Character chooser** — players pick any character when joining
- **New account restrictions** — minimum account age to join or chat
- **Custom characters** — load characters made with the character maker
- **Auto Team Balance** — moves players to balance teams in dual-team modes
- **ElPatron Powerups** — integrated power-up system
- **Auto coop mode** — switches to coop when player count is below threshold
- **Playlist switching** — change playlists on the fly with `/playlist teams`, `/playlist coop`, `/playlist 34532`
- **Rotate prop nodes** — `node.changerotation(x, y, z)`
- **2D mode** — `_ba.set_2d_mode(true)` and `_ba.set_2d_plane(z)` (beta)
- **Splitted Team score screen** — new in-game score display
- **StumbledScoreScreen** — new final score screen
- **MFA support** — enforce multi-factor authentication for specific accounts or all players
- **Text on map** — configurable on-screen overlays (watermarks, highlight messages)
- **Profanity filter** — chat moderation
- **Whitelist mode** — restrict server access to whitelisted players only
- **Max accounts per IP** — prevent multi-accounting
- **Max players per device** — limit accounts per device
