# SyndProxy validated proxy pool

## Current pool

- Alive now: 492
- Gold now: 418
- HTTP: 88 alive / 69 gold
- HTTPS: 57 alive / 23 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 178 alive / 167 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47034
- Ever gold: 1463

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
