# SyndProxy validated proxy pool

## Current pool

- Alive now: 654
- Gold now: 294
- HTTP: 267 alive / 75 gold
- HTTPS: 37 alive / 19 gold
- SOCKS4: 167 alive / 65 gold
- SOCKS5: 183 alive / 135 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47819
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
