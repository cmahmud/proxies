# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 428
- HTTP: 99 alive / 71 gold
- HTTPS: 59 alive / 28 gold
- SOCKS4: 171 alive / 160 gold
- SOCKS5: 195 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45480
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
