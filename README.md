# SyndProxy validated proxy pool

## Current pool

- Alive now: 617
- Gold now: 448
- HTTP: 127 alive / 80 gold
- HTTPS: 130 alive / 36 gold
- SOCKS4: 166 alive / 159 gold
- SOCKS5: 194 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44652
- Ever gold: 1409

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
