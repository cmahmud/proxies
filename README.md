# SyndProxy private pool

## Current pool

- Alive now: 1396
- Gold now: 589
- HTTP: 531 alive / 191 gold
- HTTPS: 373 alive / 97 gold
- SOCKS4: 224 alive / 137 gold
- SOCKS5: 268 alive / 164 gold

## Historical pool

- Discovered: 138940
- Ever alive: 23128
- Ever gold: 914

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
