# SyndProxy private pool

## Current pool

- Alive now: 840
- Gold now: 418
- HTTP: 270 alive / 96 gold
- HTTPS: 149 alive / 22 gold
- SOCKS4: 206 alive / 147 gold
- SOCKS5: 215 alive / 153 gold

## Historical pool

- Discovered: 152160
- Ever alive: 27822
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
