# SyndProxy validated proxy pool

## Current pool

- Alive now: 527
- Gold now: 391
- HTTP: 118 alive / 63 gold
- HTTPS: 60 alive / 15 gold
- SOCKS4: 163 alive / 151 gold
- SOCKS5: 186 alive / 162 gold

## Historical pool

- Discovered: 175458
- Ever alive: 33165
- Ever gold: 1228

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
