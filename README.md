# SyndProxy private pool

## Current pool

- Alive now: 1251
- Gold now: 489
- HTTP: 420 alive / 119 gold
- HTTPS: 314 alive / 70 gold
- SOCKS4: 230 alive / 152 gold
- SOCKS5: 287 alive / 148 gold

## Historical pool

- Discovered: 116452
- Ever alive: 17103
- Ever gold: 629

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
