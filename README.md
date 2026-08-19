# SyndProxy private pool

## Current pool

- Alive now: 1044
- Gold now: 421
- HTTP: 326 alive / 91 gold
- HTTPS: 205 alive / 20 gold
- SOCKS4: 240 alive / 149 gold
- SOCKS5: 273 alive / 161 gold

## Historical pool

- Discovered: 136206
- Ever alive: 22327
- Ever gold: 896

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
