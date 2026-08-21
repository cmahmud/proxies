# SyndProxy private pool

## Current pool

- Alive now: 816
- Gold now: 408
- HTTP: 258 alive / 90 gold
- HTTPS: 133 alive / 21 gold
- SOCKS4: 202 alive / 140 gold
- SOCKS5: 223 alive / 157 gold

## Historical pool

- Discovered: 156417
- Ever alive: 29454
- Ever gold: 1127

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
