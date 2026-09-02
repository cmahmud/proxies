# SyndProxy validated proxy pool

## Current pool

- Alive now: 584
- Gold now: 449
- HTTP: 100 alive / 75 gold
- HTTPS: 110 alive / 30 gold
- SOCKS4: 184 alive / 164 gold
- SOCKS5: 190 alive / 180 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47436
- Ever gold: 1468

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
