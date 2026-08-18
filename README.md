# SyndProxy private pool

## Current pool

- Alive now: 924
- Gold now: 255
- HTTP: 324 alive / 33 gold
- HTTPS: 192 alive / 8 gold
- SOCKS4: 242 alive / 144 gold
- SOCKS5: 166 alive / 70 gold

## Historical pool

- Discovered: 102887
- Ever alive: 13723
- Ever gold: 429

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
