# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 425
- HTTP: 110 alive / 72 gold
- HTTPS: 68 alive / 24 gold
- SOCKS4: 166 alive / 162 gold
- SOCKS5: 184 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44376
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
