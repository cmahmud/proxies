# SyndProxy validated proxy pool

## Current pool

- Alive now: 476
- Gold now: 396
- HTTP: 75 alive / 55 gold
- HTTPS: 54 alive / 20 gold
- SOCKS4: 166 alive / 159 gold
- SOCKS5: 181 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42796
- Ever gold: 1361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
