# SyndProxy private pool

## Current pool

- Alive now: 684
- Gold now: 360
- HTTP: 169 alive / 69 gold
- HTTPS: 118 alive / 20 gold
- SOCKS4: 193 alive / 132 gold
- SOCKS5: 204 alive / 139 gold

## Historical pool

- Discovered: 147168
- Ever alive: 25761
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
