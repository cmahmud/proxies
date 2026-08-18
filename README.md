# SyndProxy private pool

## Current pool

- Alive now: 1098
- Gold now: 276
- HTTP: 437 alive / 25 gold
- HTTPS: 213 alive / 5 gold
- SOCKS4: 219 alive / 125 gold
- SOCKS5: 229 alive / 121 gold

## Historical pool

- Discovered: 102838
- Ever alive: 13054
- Ever gold: 412

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
