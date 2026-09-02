# SyndProxy validated proxy pool

## Current pool

- Alive now: 591
- Gold now: 435
- HTTP: 110 alive / 74 gold
- HTTPS: 97 alive / 24 gold
- SOCKS4: 187 alive / 162 gold
- SOCKS5: 197 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47569
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
