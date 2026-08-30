# SyndProxy validated proxy pool

## Current pool

- Alive now: 540
- Gold now: 429
- HTTP: 119 alive / 74 gold
- HTTPS: 68 alive / 26 gold
- SOCKS4: 167 alive / 162 gold
- SOCKS5: 186 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44376
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
