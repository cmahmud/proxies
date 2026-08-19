# SyndProxy private pool

## Current pool

- Alive now: 980
- Gold now: 346
- HTTP: 323 alive / 68 gold
- HTTPS: 198 alive / 17 gold
- SOCKS4: 254 alive / 140 gold
- SOCKS5: 205 alive / 121 gold

## Historical pool

- Discovered: 109955
- Ever alive: 15343
- Ever gold: 495

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
