# SyndProxy private pool

## Current pool

- Alive now: 996
- Gold now: 428
- HTTP: 308 alive / 99 gold
- HTTPS: 215 alive / 27 gold
- SOCKS4: 232 alive / 152 gold
- SOCKS5: 241 alive / 150 gold

## Historical pool

- Discovered: 144747
- Ever alive: 25188
- Ever gold: 1057

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
