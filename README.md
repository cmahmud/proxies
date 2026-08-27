# SyndProxy validated proxy pool

## Current pool

- Alive now: 493
- Gold now: 404
- HTTP: 77 alive / 57 gold
- HTTPS: 58 alive / 18 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 182 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41575
- Ever gold: 1339

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
