# SyndProxy private pool

## Current pool

- Alive now: 1908
- Gold now: 660
- HTTP: 740 alive / 223 gold
- HTTPS: 601 alive / 123 gold
- SOCKS4: 252 alive / 149 gold
- SOCKS5: 315 alive / 165 gold

## Historical pool

- Discovered: 142699
- Ever alive: 24359
- Ever gold: 983

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
