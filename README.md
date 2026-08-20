# SyndProxy private pool

## Current pool

- Alive now: 1273
- Gold now: 604
- HTTP: 474 alive / 207 gold
- HTTPS: 336 alive / 100 gold
- SOCKS4: 219 alive / 147 gold
- SOCKS5: 244 alive / 150 gold

## Historical pool

- Discovered: 138948
- Ever alive: 23396
- Ever gold: 920

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
