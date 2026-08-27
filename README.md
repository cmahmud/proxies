# SyndProxy validated proxy pool

## Current pool

- Alive now: 498
- Gold now: 404
- HTTP: 77 alive / 55 gold
- HTTPS: 61 alive / 20 gold
- SOCKS4: 180 alive / 163 gold
- SOCKS5: 180 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41599
- Ever gold: 1341

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
