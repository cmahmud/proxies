# SyndProxy validated proxy pool

## Current pool

- Alive now: 625
- Gold now: 430
- HTTP: 119 alive / 79 gold
- HTTPS: 139 alive / 21 gold
- SOCKS4: 167 alive / 161 gold
- SOCKS5: 200 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42407
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
