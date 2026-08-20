# SyndProxy private pool

## Current pool

- Alive now: 764
- Gold now: 356
- HTTP: 225 alive / 80 gold
- HTTPS: 167 alive / 18 gold
- SOCKS4: 203 alive / 143 gold
- SOCKS5: 169 alive / 115 gold

## Historical pool

- Discovered: 145543
- Ever alive: 25339
- Ever gold: 1057

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
