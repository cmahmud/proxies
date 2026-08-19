# SyndProxy private pool

## Current pool

- Alive now: 1393
- Gold now: 414
- HTTP: 475 alive / 88 gold
- HTTPS: 371 alive / 17 gold
- SOCKS4: 237 alive / 155 gold
- SOCKS5: 310 alive / 154 gold

## Historical pool

- Discovered: 134448
- Ever alive: 21809
- Ever gold: 887

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
