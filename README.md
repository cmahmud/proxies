# SyndProxy validated proxy pool

## Current pool

- Alive now: 538
- Gold now: 405
- HTTP: 107 alive / 65 gold
- HTTPS: 95 alive / 19 gold
- SOCKS4: 161 alive / 156 gold
- SOCKS5: 175 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43067
- Ever gold: 1365

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
