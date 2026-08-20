# SyndProxy private pool

## Current pool

- Alive now: 1349
- Gold now: 599
- HTTP: 513 alive / 194 gold
- HTTPS: 367 alive / 98 gold
- SOCKS4: 230 alive / 147 gold
- SOCKS5: 239 alive / 160 gold

## Historical pool

- Discovered: 138957
- Ever alive: 23418
- Ever gold: 920

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
