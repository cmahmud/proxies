# SyndProxy private pool

## Current pool

- Alive now: 765
- Gold now: 408
- HTTP: 180 alive / 82 gold
- HTTPS: 140 alive / 24 gold
- SOCKS4: 219 alive / 141 gold
- SOCKS5: 226 alive / 161 gold

## Historical pool

- Discovered: 151059
- Ever alive: 27309
- Ever gold: 1094

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
