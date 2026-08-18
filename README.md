# SyndProxy private pool

## Current pool

- Alive now: 910
- Gold now: 332
- HTTP: 260 alive / 47 gold
- HTTPS: 204 alive / 10 gold
- SOCKS4: 206 alive / 134 gold
- SOCKS5: 240 alive / 141 gold

## Historical pool

- Discovered: 107059
- Ever alive: 14491
- Ever gold: 465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
