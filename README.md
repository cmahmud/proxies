# SyndProxy validated proxy pool

## Current pool

- Alive now: 466
- Gold now: 357
- HTTP: 82 alive / 39 gold
- HTTPS: 31 alive / 9 gold
- SOCKS4: 168 alive / 153 gold
- SOCKS5: 185 alive / 156 gold

## Historical pool

- Discovered: 173623
- Ever alive: 33013
- Ever gold: 1223

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
