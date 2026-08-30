# SyndProxy validated proxy pool

## Current pool

- Alive now: 545
- Gold now: 442
- HTTP: 122 alive / 83 gold
- HTTPS: 72 alive / 32 gold
- SOCKS4: 166 alive / 160 gold
- SOCKS5: 185 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44297
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
