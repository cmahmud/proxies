# SyndProxy private pool

## Current pool

- Alive now: 1108
- Gold now: 580
- HTTP: 352 alive / 188 gold
- HTTPS: 237 alive / 98 gold
- SOCKS4: 230 alive / 138 gold
- SOCKS5: 289 alive / 156 gold

## Historical pool

- Discovered: 138944
- Ever alive: 23231
- Ever gold: 915

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
