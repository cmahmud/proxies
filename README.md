# SyndProxy private pool

## Current pool

- Alive now: 797
- Gold now: 410
- HTTP: 215 alive / 74 gold
- HTTPS: 134 alive / 19 gold
- SOCKS4: 215 alive / 156 gold
- SOCKS5: 233 alive / 161 gold

## Historical pool

- Discovered: 146130
- Ever alive: 25611
- Ever gold: 1069

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
