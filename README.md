# SyndProxy private pool

## Current pool

- Alive now: 1080
- Gold now: 412
- HTTP: 338 alive / 95 gold
- HTTPS: 265 alive / 36 gold
- SOCKS4: 237 alive / 147 gold
- SOCKS5: 240 alive / 134 gold

## Historical pool

- Discovered: 160998
- Ever alive: 30980
- Ever gold: 1153

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
