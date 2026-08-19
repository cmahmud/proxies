# SyndProxy private pool

## Current pool

- Alive now: 1428
- Gold now: 385
- HTTP: 527 alive / 86 gold
- HTTPS: 359 alive / 14 gold
- SOCKS4: 235 alive / 146 gold
- SOCKS5: 307 alive / 139 gold

## Historical pool

- Discovered: 134448
- Ever alive: 21797
- Ever gold: 887

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
