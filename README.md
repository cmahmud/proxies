# SyndProxy validated proxy pool

## Current pool

- Alive now: 598
- Gold now: 441
- HTTP: 114 alive / 77 gold
- HTTPS: 115 alive / 26 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 194 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47562
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
