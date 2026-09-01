# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 416
- HTTP: 98 alive / 65 gold
- HTTPS: 66 alive / 24 gold
- SOCKS4: 173 alive / 159 gold
- SOCKS5: 178 alive / 168 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47036
- Ever gold: 1463

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
