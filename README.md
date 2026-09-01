# SyndProxy validated proxy pool

## Current pool

- Alive now: 497
- Gold now: 418
- HTTP: 90 alive / 68 gold
- HTTPS: 62 alive / 23 gold
- SOCKS4: 167 alive / 159 gold
- SOCKS5: 178 alive / 168 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47030
- Ever gold: 1463

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
