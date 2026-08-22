# SyndProxy private pool

## Current pool

- Alive now: 840
- Gold now: 415
- HTTP: 216 alive / 90 gold
- HTTPS: 156 alive / 31 gold
- SOCKS4: 214 alive / 132 gold
- SOCKS5: 254 alive / 162 gold

## Historical pool

- Discovered: 162771
- Ever alive: 31641
- Ever gold: 1164

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
