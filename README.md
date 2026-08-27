# SyndProxy validated proxy pool

## Current pool

- Alive now: 504
- Gold now: 403
- HTTP: 84 alive / 56 gold
- HTTPS: 60 alive / 19 gold
- SOCKS4: 177 alive / 163 gold
- SOCKS5: 183 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41599
- Ever gold: 1341

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
