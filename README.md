# SyndProxy private pool

## Current pool

- Alive now: 910
- Gold now: 336
- HTTP: 294 alive / 44 gold
- HTTPS: 165 alive / 10 gold
- SOCKS4: 221 alive / 142 gold
- SOCKS5: 230 alive / 140 gold

## Historical pool

- Discovered: 107059
- Ever alive: 14588
- Ever gold: 465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
