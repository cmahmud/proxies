# SyndProxy validated proxy pool

## Current pool

- Alive now: 545
- Gold now: 403
- HTTP: 95 alive / 62 gold
- HTTPS: 100 alive / 13 gold
- SOCKS4: 168 alive / 161 gold
- SOCKS5: 182 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43032
- Ever gold: 1365

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
