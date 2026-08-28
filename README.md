# SyndProxy validated proxy pool

## Current pool

- Alive now: 542
- Gold now: 408
- HTTP: 84 alive / 62 gold
- HTTPS: 104 alive / 22 gold
- SOCKS4: 180 alive / 162 gold
- SOCKS5: 174 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42980
- Ever gold: 1364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
