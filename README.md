# SyndProxy validated proxy pool

## Current pool

- Alive now: 521
- Gold now: 425
- HTTP: 103 alive / 71 gold
- HTTPS: 67 alive / 27 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 179 alive / 167 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47048
- Ever gold: 1463

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
