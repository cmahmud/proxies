# SyndProxy validated proxy pool

## Current pool

- Alive now: 578
- Gold now: 434
- HTTP: 104 alive / 77 gold
- HTTPS: 102 alive / 22 gold
- SOCKS4: 183 alive / 162 gold
- SOCKS5: 189 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47581
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
