# SyndProxy private pool

## Current pool

- Alive now: 1013
- Gold now: 255
- HTTP: 395 alive / 32 gold
- HTTPS: 179 alive / 4 gold
- SOCKS4: 216 alive / 115 gold
- SOCKS5: 223 alive / 104 gold

## Historical pool

- Discovered: 99105
- Ever alive: 11773
- Ever gold: 389

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
