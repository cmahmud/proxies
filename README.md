# SyndProxy validated proxy pool

## Current pool

- Alive now: 525
- Gold now: 431
- HTTP: 114 alive / 78 gold
- HTTPS: 62 alive / 26 gold
- SOCKS4: 164 alive / 160 gold
- SOCKS5: 185 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44305
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
