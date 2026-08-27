# SyndProxy validated proxy pool

## Current pool

- Alive now: 610
- Gold now: 421
- HTTP: 101 alive / 70 gold
- HTTPS: 146 alive / 19 gold
- SOCKS4: 180 alive / 164 gold
- SOCKS5: 183 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41226
- Ever gold: 1319

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
