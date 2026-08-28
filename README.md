# SyndProxy validated proxy pool

## Current pool

- Alive now: 516
- Gold now: 408
- HTTP: 98 alive / 72 gold
- HTTPS: 75 alive / 17 gold
- SOCKS4: 162 alive / 154 gold
- SOCKS5: 181 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43198
- Ever gold: 1366

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
