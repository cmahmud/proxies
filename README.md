# SyndProxy private pool

## Current pool

- Alive now: 680
- Gold now: 394
- HTTP: 188 alive / 68 gold
- HTTPS: 96 alive / 20 gold
- SOCKS4: 187 alive / 150 gold
- SOCKS5: 209 alive / 156 gold

## Historical pool

- Discovered: 146668
- Ever alive: 25753
- Ever gold: 1075

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
