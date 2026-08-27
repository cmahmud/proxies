# SyndProxy validated proxy pool

## Current pool

- Alive now: 493
- Gold now: 404
- HTTP: 74 alive / 57 gold
- HTTPS: 58 alive / 19 gold
- SOCKS4: 180 alive / 163 gold
- SOCKS5: 181 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41598
- Ever gold: 1341

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
