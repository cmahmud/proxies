# SyndProxy private pool

## Current pool

- Alive now: 1071
- Gold now: 390
- HTTP: 348 alive / 87 gold
- HTTPS: 235 alive / 20 gold
- SOCKS4: 236 alive / 147 gold
- SOCKS5: 252 alive / 136 gold

## Historical pool

- Discovered: 158238
- Ever alive: 29991
- Ever gold: 1139

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
