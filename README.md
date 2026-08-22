# SyndProxy private pool

## Current pool

- Alive now: 1034
- Gold now: 411
- HTTP: 363 alive / 94 gold
- HTTPS: 244 alive / 31 gold
- SOCKS4: 192 alive / 127 gold
- SOCKS5: 235 alive / 159 gold

## Historical pool

- Discovered: 163242
- Ever alive: 31700
- Ever gold: 1164

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
