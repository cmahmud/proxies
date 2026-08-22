# SyndProxy private pool

## Current pool

- Alive now: 882
- Gold now: 435
- HTTP: 248 alive / 92 gold
- HTTPS: 149 alive / 30 gold
- SOCKS4: 226 alive / 152 gold
- SOCKS5: 259 alive / 161 gold

## Historical pool

- Discovered: 163284
- Ever alive: 31813
- Ever gold: 1167

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
