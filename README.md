# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 421
- HTTP: 106 alive / 76 gold
- HTTPS: 46 alive / 24 gold
- SOCKS4: 179 alive / 159 gold
- SOCKS5: 182 alive / 162 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49477
- Ever gold: 1584

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
