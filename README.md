# SyndProxy validated proxy pool

## Current pool

- Alive now: 593
- Gold now: 434
- HTTP: 110 alive / 75 gold
- HTTPS: 104 alive / 23 gold
- SOCKS4: 182 alive / 161 gold
- SOCKS5: 197 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47571
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
