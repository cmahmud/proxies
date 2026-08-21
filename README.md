# SyndProxy private pool

## Current pool

- Alive now: 968
- Gold now: 454
- HTTP: 297 alive / 99 gold
- HTTPS: 190 alive / 36 gold
- SOCKS4: 201 alive / 149 gold
- SOCKS5: 280 alive / 170 gold

## Historical pool

- Discovered: 153740
- Ever alive: 28692
- Ever gold: 1112

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
