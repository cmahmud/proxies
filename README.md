# SyndProxy validated proxy pool

## Current pool

- Alive now: 601
- Gold now: 449
- HTTP: 100 alive / 79 gold
- HTTPS: 122 alive / 31 gold
- SOCKS4: 187 alive / 162 gold
- SOCKS5: 192 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47538
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
