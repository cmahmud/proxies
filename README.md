# SyndProxy private pool

## Current pool

- Alive now: 934
- Gold now: 391
- HTTP: 316 alive / 79 gold
- HTTPS: 189 alive / 23 gold
- SOCKS4: 192 alive / 126 gold
- SOCKS5: 237 alive / 163 gold

## Historical pool

- Discovered: 151047
- Ever alive: 27130
- Ever gold: 1092

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
