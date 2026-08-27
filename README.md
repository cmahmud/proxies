# SyndProxy validated proxy pool

## Current pool

- Alive now: 605
- Gold now: 401
- HTTP: 103 alive / 60 gold
- HTTPS: 139 alive / 15 gold
- SOCKS4: 178 alive / 160 gold
- SOCKS5: 185 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41328
- Ever gold: 1324

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
