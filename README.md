# SyndProxy private pool

## Current pool

- Alive now: 924
- Gold now: 251
- HTTP: 312 alive / 34 gold
- HTTPS: 224 alive / 7 gold
- SOCKS4: 236 alive / 143 gold
- SOCKS5: 152 alive / 67 gold

## Historical pool

- Discovered: 102887
- Ever alive: 13770
- Ever gold: 429

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
