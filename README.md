# SyndProxy private pool

## Current pool

- Alive now: 1909
- Gold now: 656
- HTTP: 747 alive / 221 gold
- HTTPS: 607 alive / 122 gold
- SOCKS4: 243 alive / 146 gold
- SOCKS5: 312 alive / 167 gold

## Historical pool

- Discovered: 142699
- Ever alive: 24353
- Ever gold: 983

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
