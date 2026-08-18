# SyndProxy private pool

## Current pool

- Alive now: 870
- Gold now: 274
- HTTP: 299 alive / 36 gold
- HTTPS: 161 alive / 8 gold
- SOCKS4: 241 alive / 137 gold
- SOCKS5: 169 alive / 93 gold

## Historical pool

- Discovered: 102899
- Ever alive: 13906
- Ever gold: 432

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
