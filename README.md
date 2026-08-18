# SyndProxy private pool

## Current pool

- Alive now: 885
- Gold now: 328
- HTTP: 249 alive / 38 gold
- HTTPS: 179 alive / 9 gold
- SOCKS4: 227 alive / 145 gold
- SOCKS5: 230 alive / 136 gold

## Historical pool

- Discovered: 102931
- Ever alive: 13995
- Ever gold: 435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
