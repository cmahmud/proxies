# SyndProxy private pool

## Current pool

- Alive now: 908
- Gold now: 397
- HTTP: 297 alive / 95 gold
- HTTPS: 182 alive / 14 gold
- SOCKS4: 230 alive / 158 gold
- SOCKS5: 199 alive / 130 gold

## Historical pool

- Discovered: 119828
- Ever alive: 18236
- Ever gold: 717

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
