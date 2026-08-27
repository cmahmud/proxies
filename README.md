# SyndProxy validated proxy pool

## Current pool

- Alive now: 594
- Gold now: 395
- HTTP: 108 alive / 58 gold
- HTTPS: 124 alive / 13 gold
- SOCKS4: 178 alive / 160 gold
- SOCKS5: 184 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41343
- Ever gold: 1325

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
