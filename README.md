# SyndProxy private pool

## Current pool

- Alive now: 817
- Gold now: 405
- HTTP: 208 alive / 90 gold
- HTTPS: 166 alive / 29 gold
- SOCKS4: 213 alive / 133 gold
- SOCKS5: 230 alive / 153 gold

## Historical pool

- Discovered: 163842
- Ever alive: 31944
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
