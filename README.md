# SyndProxy validated proxy pool

## Current pool

- Alive now: 535
- Gold now: 426
- HTTP: 119 alive / 72 gold
- HTTPS: 67 alive / 25 gold
- SOCKS4: 166 alive / 162 gold
- SOCKS5: 183 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44376
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
