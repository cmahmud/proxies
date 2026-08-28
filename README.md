# SyndProxy validated proxy pool

## Current pool

- Alive now: 621
- Gold now: 432
- HTTP: 110 alive / 81 gold
- HTTPS: 135 alive / 22 gold
- SOCKS4: 184 alive / 160 gold
- SOCKS5: 192 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42352
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
