# SyndProxy private pool

## Current pool

- Alive now: 1403
- Gold now: 415
- HTTP: 465 alive / 88 gold
- HTTPS: 386 alive / 17 gold
- SOCKS4: 239 alive / 155 gold
- SOCKS5: 313 alive / 155 gold

## Historical pool

- Discovered: 134448
- Ever alive: 21818
- Ever gold: 887

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
