# SyndProxy private pool

## Current pool

- Alive now: 1587
- Gold now: 584
- HTTP: 645 alive / 185 gold
- HTTPS: 429 alive / 91 gold
- SOCKS4: 244 alive / 142 gold
- SOCKS5: 269 alive / 166 gold

## Historical pool

- Discovered: 138940
- Ever alive: 23165
- Ever gold: 915

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
