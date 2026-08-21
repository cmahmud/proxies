# SyndProxy private pool

## Current pool

- Alive now: 1078
- Gold now: 367
- HTTP: 388 alive / 82 gold
- HTTPS: 288 alive / 21 gold
- SOCKS4: 181 alive / 116 gold
- SOCKS5: 221 alive / 148 gold

## Historical pool

- Discovered: 158226
- Ever alive: 29881
- Ever gold: 1138

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
