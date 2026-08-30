# SyndProxy validated proxy pool

## Current pool

- Alive now: 540
- Gold now: 430
- HTTP: 118 alive / 80 gold
- HTTPS: 62 alive / 23 gold
- SOCKS4: 167 alive / 160 gold
- SOCKS5: 193 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44322
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
