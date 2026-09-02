# SyndProxy validated proxy pool

## Current pool

- Alive now: 594
- Gold now: 431
- HTTP: 122 alive / 73 gold
- HTTPS: 103 alive / 22 gold
- SOCKS4: 177 alive / 165 gold
- SOCKS5: 192 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47601
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
