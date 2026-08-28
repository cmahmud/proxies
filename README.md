# SyndProxy validated proxy pool

## Current pool

- Alive now: 535
- Gold now: 404
- HTTP: 88 alive / 67 gold
- HTTPS: 102 alive / 15 gold
- SOCKS4: 166 alive / 161 gold
- SOCKS5: 179 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43036
- Ever gold: 1365

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
