# SyndProxy validated proxy pool

## Current pool

- Alive now: 601
- Gold now: 449
- HTTP: 98 alive / 80 gold
- HTTPS: 125 alive / 31 gold
- SOCKS4: 186 alive / 162 gold
- SOCKS5: 192 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47538
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
