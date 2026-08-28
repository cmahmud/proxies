# SyndProxy validated proxy pool

## Current pool

- Alive now: 504
- Gold now: 403
- HTTP: 80 alive / 61 gold
- HTTPS: 76 alive / 16 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 176 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42916
- Ever gold: 1364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
