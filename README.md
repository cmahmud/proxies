# SyndProxy validated proxy pool

## Current pool

- Alive now: 532
- Gold now: 403
- HTTP: 87 alive / 57 gold
- HTTPS: 90 alive / 24 gold
- SOCKS4: 178 alive / 162 gold
- SOCKS5: 177 alive / 160 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42982
- Ever gold: 1365

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
