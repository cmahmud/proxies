# SyndProxy private pool

## Current pool

- Alive now: 1015
- Gold now: 428
- HTTP: 321 alive / 108 gold
- HTTPS: 205 alive / 35 gold
- SOCKS4: 245 alive / 145 gold
- SOCKS5: 244 alive / 140 gold

## Historical pool

- Discovered: 160278
- Ever alive: 30785
- Ever gold: 1148

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
