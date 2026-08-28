# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 403
- HTTP: 90 alive / 58 gold
- HTTPS: 90 alive / 20 gold
- SOCKS4: 165 alive / 161 gold
- SOCKS5: 184 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42691
- Ever gold: 1360

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
