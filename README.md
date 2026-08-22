# SyndProxy private pool

## Current pool

- Alive now: 798
- Gold now: 388
- HTTP: 225 alive / 92 gold
- HTTPS: 163 alive / 27 gold
- SOCKS4: 209 alive / 138 gold
- SOCKS5: 201 alive / 131 gold

## Historical pool

- Discovered: 162762
- Ever alive: 31601
- Ever gold: 1164

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
