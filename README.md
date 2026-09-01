# SyndProxy validated proxy pool

## Current pool

- Alive now: 500
- Gold now: 418
- HTTP: 95 alive / 67 gold
- HTTPS: 58 alive / 24 gold
- SOCKS4: 170 alive / 159 gold
- SOCKS5: 177 alive / 168 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47035
- Ever gold: 1463

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
