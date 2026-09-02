# SyndProxy validated proxy pool

## Current pool

- Alive now: 581
- Gold now: 451
- HTTP: 103 alive / 77 gold
- HTTPS: 112 alive / 30 gold
- SOCKS4: 180 alive / 165 gold
- SOCKS5: 186 alive / 179 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47431
- Ever gold: 1468

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
