# SyndProxy private pool

## Current pool

- Alive now: 1318
- Gold now: 419
- HTTP: 409 alive / 93 gold
- HTTPS: 274 alive / 17 gold
- SOCKS4: 265 alive / 149 gold
- SOCKS5: 370 alive / 160 gold

## Historical pool

- Discovered: 133936
- Ever alive: 21462
- Ever gold: 881

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
