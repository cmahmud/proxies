# SyndProxy validated proxy pool

## Current pool

- Alive now: 506
- Gold now: 403
- HTTP: 79 alive / 57 gold
- HTTPS: 69 alive / 19 gold
- SOCKS4: 175 alive / 165 gold
- SOCKS5: 183 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41602
- Ever gold: 1341

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
