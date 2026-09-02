# SyndProxy validated proxy pool

## Current pool

- Alive now: 606
- Gold now: 437
- HTTP: 111 alive / 75 gold
- HTTPS: 113 alive / 24 gold
- SOCKS4: 185 alive / 162 gold
- SOCKS5: 197 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47571
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
