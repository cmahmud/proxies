# SyndProxy validated proxy pool

## Current pool

- Alive now: 549
- Gold now: 405
- HTTP: 95 alive / 60 gold
- HTTPS: 105 alive / 18 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 178 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43022
- Ever gold: 1365

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
