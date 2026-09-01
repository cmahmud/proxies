# SyndProxy validated proxy pool

## Current pool

- Alive now: 616
- Gold now: 459
- HTTP: 130 alive / 87 gold
- HTTPS: 121 alive / 34 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 196 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46771
- Ever gold: 1451

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
