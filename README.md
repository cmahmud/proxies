# SyndProxy validated proxy pool

## Current pool

- Alive now: 604
- Gold now: 444
- HTTP: 130 alive / 82 gold
- HTTPS: 107 alive / 25 gold
- SOCKS4: 179 alive / 162 gold
- SOCKS5: 188 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47652
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
