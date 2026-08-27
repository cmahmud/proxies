# SyndProxy validated proxy pool

## Current pool

- Alive now: 498
- Gold now: 391
- HTTP: 77 alive / 49 gold
- HTTPS: 57 alive / 14 gold
- SOCKS4: 178 alive / 165 gold
- SOCKS5: 186 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41616
- Ever gold: 1341

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
