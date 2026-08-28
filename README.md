# SyndProxy validated proxy pool

## Current pool

- Alive now: 574
- Gold now: 413
- HTTP: 101 alive / 67 gold
- HTTPS: 112 alive / 18 gold
- SOCKS4: 178 alive / 161 gold
- SOCKS5: 183 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42550
- Ever gold: 1358

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
