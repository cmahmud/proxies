# SyndProxy validated proxy pool

## Current pool

- Alive now: 497
- Gold now: 401
- HTTP: 93 alive / 61 gold
- HTTPS: 50 alive / 19 gold
- SOCKS4: 174 alive / 160 gold
- SOCKS5: 180 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41705
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
