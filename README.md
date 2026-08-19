# SyndProxy private pool

## Current pool

- Alive now: 1365
- Gold now: 382
- HTTP: 492 alive / 83 gold
- HTTPS: 336 alive / 13 gold
- SOCKS4: 238 alive / 146 gold
- SOCKS5: 299 alive / 140 gold

## Historical pool

- Discovered: 134448
- Ever alive: 21792
- Ever gold: 887

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
