# SyndProxy validated proxy pool

## Current pool

- Alive now: 552
- Gold now: 436
- HTTP: 128 alive / 83 gold
- HTTPS: 70 alive / 28 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 185 alive / 166 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44301
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
