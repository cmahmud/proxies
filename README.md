# SyndProxy validated proxy pool

## Current pool

- Alive now: 553
- Gold now: 399
- HTTP: 96 alive / 59 gold
- HTTPS: 96 alive / 14 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 188 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39270
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
