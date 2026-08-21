# SyndProxy private pool

## Current pool

- Alive now: 924
- Gold now: 408
- HTTP: 263 alive / 96 gold
- HTTPS: 219 alive / 33 gold
- SOCKS4: 213 alive / 150 gold
- SOCKS5: 229 alive / 129 gold

## Historical pool

- Discovered: 160997
- Ever alive: 30958
- Ever gold: 1152

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
