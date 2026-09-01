# SyndProxy validated proxy pool

## Current pool

- Alive now: 522
- Gold now: 409
- HTTP: 82 alive / 63 gold
- HTTPS: 97 alive / 21 gold
- SOCKS4: 166 alive / 158 gold
- SOCKS5: 177 alive / 167 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47203
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
