# SyndProxy validated proxy pool

## Current pool

- Alive now: 488
- Gold now: 419
- HTTP: 92 alive / 67 gold
- HTTPS: 51 alive / 24 gold
- SOCKS4: 168 alive / 159 gold
- SOCKS5: 177 alive / 169 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47034
- Ever gold: 1463

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
