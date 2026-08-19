# SyndProxy private pool

## Current pool

- Alive now: 1375
- Gold now: 392
- HTTP: 489 alive / 93 gold
- HTTPS: 346 alive / 18 gold
- SOCKS4: 223 alive / 130 gold
- SOCKS5: 317 alive / 151 gold

## Historical pool

- Discovered: 134551
- Ever alive: 22020
- Ever gold: 890

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
