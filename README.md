# SyndProxy private pool

## Current pool

- Alive now: 1785
- Gold now: 649
- HTTP: 722 alive / 217 gold
- HTTPS: 508 alive / 120 gold
- SOCKS4: 222 alive / 151 gold
- SOCKS5: 333 alive / 161 gold

## Historical pool

- Discovered: 141249
- Ever alive: 24195
- Ever gold: 971

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
