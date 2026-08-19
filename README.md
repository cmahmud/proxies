# SyndProxy private pool

## Current pool

- Alive now: 1277
- Gold now: 385
- HTTP: 433 alive / 88 gold
- HTTPS: 281 alive / 21 gold
- SOCKS4: 254 alive / 138 gold
- SOCKS5: 309 alive / 138 gold

## Historical pool

- Discovered: 133938
- Ever alive: 21502
- Ever gold: 884

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
