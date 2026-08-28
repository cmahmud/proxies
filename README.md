# SyndProxy validated proxy pool

## Current pool

- Alive now: 509
- Gold now: 403
- HTTP: 81 alive / 60 gold
- HTTPS: 81 alive / 17 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 174 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42916
- Ever gold: 1364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
