# SyndProxy private pool

## Current pool

- Alive now: 979
- Gold now: 255
- HTTP: 366 alive / 32 gold
- HTTPS: 174 alive / 4 gold
- SOCKS4: 213 alive / 115 gold
- SOCKS5: 226 alive / 104 gold

## Historical pool

- Discovered: 99105
- Ever alive: 11765
- Ever gold: 389

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
