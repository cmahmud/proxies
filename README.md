# SyndProxy private pool

## Current pool

- Alive now: 1936
- Gold now: 655
- HTTP: 759 alive / 222 gold
- HTTPS: 613 alive / 121 gold
- SOCKS4: 252 alive / 146 gold
- SOCKS5: 312 alive / 166 gold

## Historical pool

- Discovered: 142699
- Ever alive: 24359
- Ever gold: 983

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
