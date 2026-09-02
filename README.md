# SyndProxy validated proxy pool

## Current pool

- Alive now: 576
- Gold now: 452
- HTTP: 100 alive / 77 gold
- HTTPS: 107 alive / 33 gold
- SOCKS4: 179 alive / 165 gold
- SOCKS5: 190 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47428
- Ever gold: 1468

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
