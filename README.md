# SyndProxy private pool

## Current pool

- Alive now: 1074
- Gold now: 525
- HTTP: 375 alive / 164 gold
- HTTPS: 281 alive / 90 gold
- SOCKS4: 196 alive / 123 gold
- SOCKS5: 222 alive / 148 gold

## Historical pool

- Discovered: 124834
- Ever alive: 19199
- Ever gold: 731

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
