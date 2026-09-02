# SyndProxy validated proxy pool

## Current pool

- Alive now: 593
- Gold now: 440
- HTTP: 113 alive / 77 gold
- HTTPS: 113 alive / 25 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 195 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47561
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
