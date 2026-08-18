# SyndProxy private pool

## Current pool

- Alive now: 873
- Gold now: 336
- HTTP: 255 alive / 66 gold
- HTTPS: 194 alive / 13 gold
- SOCKS4: 219 alive / 141 gold
- SOCKS5: 205 alive / 116 gold

## Historical pool

- Discovered: 109955
- Ever alive: 15217
- Ever gold: 491

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
