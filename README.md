# SyndProxy validated proxy pool

## Current pool

- Alive now: 535
- Gold now: 426
- HTTP: 107 alive / 74 gold
- HTTPS: 68 alive / 26 gold
- SOCKS4: 166 alive / 161 gold
- SOCKS5: 194 alive / 165 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44367
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
