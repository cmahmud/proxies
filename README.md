# SyndProxy private pool

## Current pool

- Alive now: 891
- Gold now: 407
- HTTP: 255 alive / 73 gold
- HTTPS: 145 alive / 23 gold
- SOCKS4: 238 alive / 160 gold
- SOCKS5: 253 alive / 151 gold

## Historical pool

- Discovered: 156825
- Ever alive: 29613
- Ever gold: 1132

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
