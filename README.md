# SyndProxy validated proxy pool

## Current pool

- Alive now: 597
- Gold now: 430
- HTTP: 102 alive / 80 gold
- HTTPS: 131 alive / 21 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 195 alive / 170 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42418
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
