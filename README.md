# SyndProxy private pool

## Current pool

- Alive now: 1362
- Gold now: 580
- HTTP: 572 alive / 192 gold
- HTTPS: 353 alive / 99 gold
- SOCKS4: 218 alive / 139 gold
- SOCKS5: 219 alive / 150 gold

## Historical pool

- Discovered: 136253
- Ever alive: 22780
- Ever gold: 909

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
