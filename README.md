# SyndProxy private pool

## Current pool

- Alive now: 1589
- Gold now: 580
- HTTP: 626 alive / 193 gold
- HTTPS: 415 alive / 94 gold
- SOCKS4: 238 alive / 140 gold
- SOCKS5: 310 alive / 153 gold

## Historical pool

- Discovered: 136248
- Ever alive: 22739
- Ever gold: 909

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
