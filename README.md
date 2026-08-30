# SyndProxy validated proxy pool

## Current pool

- Alive now: 645
- Gold now: 485
- HTTP: 142 alive / 101 gold
- HTTPS: 124 alive / 45 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 202 alive / 177 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44933
- Ever gold: 1420

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
