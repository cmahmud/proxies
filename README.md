# SyndProxy private pool

## Current pool

- Alive now: 924
- Gold now: 447
- HTTP: 245 alive / 103 gold
- HTTPS: 186 alive / 28 gold
- SOCKS4: 226 alive / 153 gold
- SOCKS5: 267 alive / 163 gold

## Historical pool

- Discovered: 163327
- Ever alive: 31823
- Ever gold: 1167

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
