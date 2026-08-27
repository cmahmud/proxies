# SyndProxy validated proxy pool

## Current pool

- Alive now: 562
- Gold now: 403
- HTTP: 96 alive / 63 gold
- HTTPS: 103 alive / 14 gold
- SOCKS4: 173 alive / 163 gold
- SOCKS5: 190 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41438
- Ever gold: 1328

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
