# SyndProxy private pool

## Current pool

- Alive now: 955
- Gold now: 497
- HTTP: 316 alive / 149 gold
- HTTPS: 221 alive / 90 gold
- SOCKS4: 200 alive / 122 gold
- SOCKS5: 218 alive / 136 gold

## Historical pool

- Discovered: 117156
- Ever alive: 17580
- Ever gold: 690

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
