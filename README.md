# SyndProxy private pool

## Current pool

- Alive now: 1229
- Gold now: 498
- HTTP: 408 alive / 147 gold
- HTTPS: 345 alive / 91 gold
- SOCKS4: 214 alive / 124 gold
- SOCKS5: 262 alive / 136 gold

## Historical pool

- Discovered: 117110
- Ever alive: 17318
- Ever gold: 663

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
