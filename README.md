# SyndProxy private pool

## Current pool

- Alive now: 982
- Gold now: 405
- HTTP: 265 alive / 79 gold
- HTTPS: 205 alive / 12 gold
- SOCKS4: 263 alive / 153 gold
- SOCKS5: 249 alive / 161 gold

## Historical pool

- Discovered: 131115
- Ever alive: 20568
- Ever gold: 868

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
