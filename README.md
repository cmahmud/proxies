# SyndProxy private pool

## Current pool

- Alive now: 950
- Gold now: 255
- HTTP: 401 alive / 27 gold
- HTTPS: 136 alive / 2 gold
- SOCKS4: 197 alive / 120 gold
- SOCKS5: 216 alive / 106 gold

## Historical pool

- Discovered: 99104
- Ever alive: 11737
- Ever gold: 389

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
