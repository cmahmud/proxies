# SyndProxy private pool

## Current pool

- Alive now: 973
- Gold now: 395
- HTTP: 280 alive / 88 gold
- HTTPS: 209 alive / 28 gold
- SOCKS4: 243 alive / 146 gold
- SOCKS5: 241 alive / 133 gold

## Historical pool

- Discovered: 160993
- Ever alive: 30901
- Ever gold: 1152

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
