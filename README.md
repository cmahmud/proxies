# SyndProxy private pool

## Current pool

- Alive now: 838
- Gold now: 383
- HTTP: 236 alive / 79 gold
- HTTPS: 181 alive / 26 gold
- SOCKS4: 214 alive / 148 gold
- SOCKS5: 207 alive / 130 gold

## Historical pool

- Discovered: 163331
- Ever alive: 31864
- Ever gold: 1168

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
