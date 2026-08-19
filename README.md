# SyndProxy private pool

## Current pool

- Alive now: 1126
- Gold now: 509
- HTTP: 443 alive / 177 gold
- HTTPS: 307 alive / 115 gold
- SOCKS4: 196 alive / 104 gold
- SOCKS5: 180 alive / 113 gold

## Historical pool

- Discovered: 124841
- Ever alive: 19321
- Ever gold: 772

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
