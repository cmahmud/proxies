# SyndProxy validated proxy pool

## Current pool

- Alive now: 563
- Gold now: 423
- HTTP: 126 alive / 83 gold
- HTTPS: 90 alive / 30 gold
- SOCKS4: 160 alive / 151 gold
- SOCKS5: 187 alive / 159 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44039
- Ever gold: 1391

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
