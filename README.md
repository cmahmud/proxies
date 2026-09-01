# SyndProxy validated proxy pool

## Current pool

- Alive now: 533
- Gold now: 421
- HTTP: 106 alive / 70 gold
- HTTPS: 74 alive / 25 gold
- SOCKS4: 173 alive / 160 gold
- SOCKS5: 180 alive / 166 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47047
- Ever gold: 1463

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
