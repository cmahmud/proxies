# SyndProxy validated proxy pool

## Current pool

- Alive now: 624
- Gold now: 461
- HTTP: 133 alive / 87 gold
- HTTPS: 126 alive / 34 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 196 alive / 179 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46768
- Ever gold: 1451

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
