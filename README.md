# SyndProxy private pool

## Current pool

- Alive now: 827
- Gold now: 399
- HTTP: 230 alive / 87 gold
- HTTPS: 149 alive / 29 gold
- SOCKS4: 210 alive / 130 gold
- SOCKS5: 238 alive / 153 gold

## Historical pool

- Discovered: 163842
- Ever alive: 31927
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
