# SyndProxy validated proxy pool

## Current pool

- Alive now: 541
- Gold now: 439
- HTTP: 101 alive / 79 gold
- HTTPS: 85 alive / 24 gold
- SOCKS4: 169 alive / 163 gold
- SOCKS5: 186 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47673
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
