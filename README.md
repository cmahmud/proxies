# SyndProxy private pool

## Current pool

- Alive now: 734
- Gold now: 362
- HTTP: 164 alive / 67 gold
- HTTPS: 153 alive / 17 gold
- SOCKS4: 216 alive / 138 gold
- SOCKS5: 201 alive / 140 gold

## Historical pool

- Discovered: 148336
- Ever alive: 26278
- Ever gold: 1080

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
