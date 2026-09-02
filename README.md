# SyndProxy validated proxy pool

## Current pool

- Alive now: 607
- Gold now: 445
- HTTP: 129 alive / 82 gold
- HTTPS: 112 alive / 26 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 189 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47650
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
