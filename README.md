# SyndProxy private pool

## Current pool

- Alive now: 931
- Gold now: 281
- HTTP: 314 alive / 28 gold
- HTTPS: 123 alive / 5 gold
- SOCKS4: 254 alive / 140 gold
- SOCKS5: 240 alive / 108 gold

## Historical pool

- Discovered: 99165
- Ever alive: 12274
- Ever gold: 396

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
