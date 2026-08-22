# SyndProxy private pool

## Current pool

- Alive now: 1024
- Gold now: 372
- HTTP: 332 alive / 81 gold
- HTTPS: 252 alive / 25 gold
- SOCKS4: 206 alive / 136 gold
- SOCKS5: 234 alive / 130 gold

## Historical pool

- Discovered: 165841
- Ever alive: 32372
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
