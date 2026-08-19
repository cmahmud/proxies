# SyndProxy private pool

## Current pool

- Alive now: 1365
- Gold now: 363
- HTTP: 444 alive / 81 gold
- HTTPS: 307 alive / 14 gold
- SOCKS4: 265 alive / 135 gold
- SOCKS5: 349 alive / 133 gold

## Historical pool

- Discovered: 133938
- Ever alive: 21472
- Ever gold: 882

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
