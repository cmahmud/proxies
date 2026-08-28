# SyndProxy validated proxy pool

## Current pool

- Alive now: 623
- Gold now: 433
- HTTP: 118 alive / 81 gold
- HTTPS: 137 alive / 22 gold
- SOCKS4: 167 alive / 160 gold
- SOCKS5: 201 alive / 170 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42407
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
