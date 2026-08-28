# SyndProxy validated proxy pool

## Current pool

- Alive now: 476
- Gold now: 398
- HTTP: 72 alive / 57 gold
- HTTPS: 58 alive / 17 gold
- SOCKS4: 168 alive / 158 gold
- SOCKS5: 178 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42757
- Ever gold: 1361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
