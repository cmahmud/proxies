# SyndProxy validated proxy pool

## Current pool

- Alive now: 559
- Gold now: 452
- HTTP: 90 alive / 77 gold
- HTTPS: 102 alive / 37 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 190 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47394
- Ever gold: 1468

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
