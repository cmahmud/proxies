# SyndProxy validated proxy pool

## Current pool

- Alive now: 608
- Gold now: 442
- HTTP: 120 alive / 77 gold
- HTTPS: 117 alive / 27 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 194 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47563
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
