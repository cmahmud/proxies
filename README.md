# SyndProxy validated proxy pool

## Current pool

- Alive now: 614
- Gold now: 444
- HTTP: 122 alive / 81 gold
- HTTPS: 127 alive / 35 gold
- SOCKS4: 170 alive / 160 gold
- SOCKS5: 195 alive / 168 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44720
- Ever gold: 1411

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
