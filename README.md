# SyndProxy private pool

## Current pool

- Alive now: 1197
- Gold now: 501
- HTTP: 394 alive / 123 gold
- HTTPS: 295 alive / 75 gold
- SOCKS4: 235 alive / 152 gold
- SOCKS5: 273 alive / 151 gold

## Historical pool

- Discovered: 114412
- Ever alive: 17028
- Ever gold: 629

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
