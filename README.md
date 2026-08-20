# SyndProxy private pool

## Current pool

- Alive now: 784
- Gold now: 382
- HTTP: 217 alive / 75 gold
- HTTPS: 132 alive / 20 gold
- SOCKS4: 204 alive / 139 gold
- SOCKS5: 231 alive / 148 gold

## Historical pool

- Discovered: 147689
- Ever alive: 25961
- Ever gold: 1077

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
