# SyndProxy validated proxy pool

## Current pool

- Alive now: 561
- Gold now: 388
- HTTP: 116 alive / 70 gold
- HTTPS: 98 alive / 14 gold
- SOCKS4: 165 alive / 151 gold
- SOCKS5: 182 alive / 153 gold

## Historical pool

- Discovered: 176564
- Ever alive: 33235
- Ever gold: 1231

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
