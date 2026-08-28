# SyndProxy validated proxy pool

## Current pool

- Alive now: 564
- Gold now: 421
- HTTP: 90 alive / 72 gold
- HTTPS: 108 alive / 20 gold
- SOCKS4: 181 alive / 161 gold
- SOCKS5: 185 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42523
- Ever gold: 1358

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
