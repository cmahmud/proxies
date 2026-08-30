# SyndProxy validated proxy pool

## Current pool

- Alive now: 511
- Gold now: 416
- HTTP: 125 alive / 79 gold
- HTTPS: 53 alive / 28 gold
- SOCKS4: 163 alive / 150 gold
- SOCKS5: 170 alive / 159 gold

## Historical pool

- Discovered: 199830
- Ever alive: 43700
- Ever gold: 1379

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
