# SyndProxy private pool

## Current pool

- Alive now: 828
- Gold now: 413
- HTTP: 212 alive / 81 gold
- HTTPS: 140 alive / 25 gold
- SOCKS4: 217 alive / 146 gold
- SOCKS5: 259 alive / 161 gold

## Historical pool

- Discovered: 155799
- Ever alive: 29349
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
