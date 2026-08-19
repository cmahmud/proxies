# SyndProxy private pool

## Current pool

- Alive now: 1298
- Gold now: 519
- HTTP: 489 alive / 185 gold
- HTTPS: 349 alive / 52 gold
- SOCKS4: 213 alive / 122 gold
- SOCKS5: 247 alive / 160 gold

## Historical pool

- Discovered: 125671
- Ever alive: 19656
- Ever gold: 774

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
