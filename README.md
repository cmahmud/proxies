# SyndProxy validated proxy pool

## Current pool

- Alive now: 504
- Gold now: 404
- HTTP: 81 alive / 56 gold
- HTTPS: 60 alive / 18 gold
- SOCKS4: 178 alive / 163 gold
- SOCKS5: 185 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41575
- Ever gold: 1339

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
