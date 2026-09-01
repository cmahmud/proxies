# SyndProxy validated proxy pool

## Current pool

- Alive now: 495
- Gold now: 421
- HTTP: 93 alive / 68 gold
- HTTPS: 56 alive / 25 gold
- SOCKS4: 167 alive / 159 gold
- SOCKS5: 179 alive / 169 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47034
- Ever gold: 1463

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
