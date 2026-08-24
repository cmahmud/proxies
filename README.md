# SyndProxy validated proxy pool

## Current pool

- Alive now: 504
- Gold now: 388
- HTTP: 121 alive / 70 gold
- HTTPS: 43 alive / 14 gold
- SOCKS4: 161 alive / 152 gold
- SOCKS5: 179 alive / 152 gold

## Historical pool

- Discovered: 176564
- Ever alive: 33239
- Ever gold: 1231

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
