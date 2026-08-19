# SyndProxy private pool

## Current pool

- Alive now: 921
- Gold now: 462
- HTTP: 296 alive / 117 gold
- HTTPS: 212 alive / 86 gold
- SOCKS4: 217 alive / 141 gold
- SOCKS5: 196 alive / 118 gold

## Historical pool

- Discovered: 117130
- Ever alive: 17493
- Ever gold: 664

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
