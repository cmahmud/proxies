# SyndProxy private pool

## Current pool

- Alive now: 970
- Gold now: 392
- HTTP: 292 alive / 73 gold
- HTTPS: 208 alive / 11 gold
- SOCKS4: 243 alive / 152 gold
- SOCKS5: 227 alive / 156 gold

## Historical pool

- Discovered: 129331
- Ever alive: 20494
- Ever gold: 866

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
