# SyndProxy validated proxy pool

## Current pool

- Alive now: 598
- Gold now: 400
- HTTP: 102 alive / 60 gold
- HTTPS: 134 alive / 15 gold
- SOCKS4: 178 alive / 160 gold
- SOCKS5: 184 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41328
- Ever gold: 1324

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
