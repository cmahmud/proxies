# SyndProxy validated proxy pool

## Current pool

- Alive now: 640
- Gold now: 488
- HTTP: 148 alive / 100 gold
- HTTPS: 124 alive / 47 gold
- SOCKS4: 170 alive / 163 gold
- SOCKS5: 198 alive / 178 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44993
- Ever gold: 1422

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
