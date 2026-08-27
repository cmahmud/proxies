# SyndProxy validated proxy pool

## Current pool

- Alive now: 590
- Gold now: 422
- HTTP: 112 alive / 80 gold
- HTTPS: 112 alive / 19 gold
- SOCKS4: 178 alive / 158 gold
- SOCKS5: 188 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42093
- Ever gold: 1350

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
