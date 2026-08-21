# SyndProxy private pool

## Current pool

- Alive now: 812
- Gold now: 423
- HTTP: 186 alive / 81 gold
- HTTPS: 155 alive / 25 gold
- SOCKS4: 223 alive / 148 gold
- SOCKS5: 248 alive / 169 gold

## Historical pool

- Discovered: 155791
- Ever alive: 29332
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
