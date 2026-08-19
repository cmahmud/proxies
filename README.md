# SyndProxy private pool

## Current pool

- Alive now: 1294
- Gold now: 521
- HTTP: 493 alive / 178 gold
- HTTPS: 355 alive / 59 gold
- SOCKS4: 201 alive / 122 gold
- SOCKS5: 245 alive / 162 gold

## Historical pool

- Discovered: 125671
- Ever alive: 19664
- Ever gold: 775

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
