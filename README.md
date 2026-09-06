# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 405
- HTTP: 110 alive / 74 gold
- HTTPS: 60 alive / 19 gold
- SOCKS4: 168 alive / 153 gold
- SOCKS5: 179 alive / 159 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48089
- Ever gold: 1518

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
