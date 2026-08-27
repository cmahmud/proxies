# SyndProxy validated proxy pool

## Current pool

- Alive now: 593
- Gold now: 419
- HTTP: 100 alive / 77 gold
- HTTPS: 124 alive / 16 gold
- SOCKS4: 180 alive / 159 gold
- SOCKS5: 189 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42149
- Ever gold: 1351

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
