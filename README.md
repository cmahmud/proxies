# SyndProxy validated proxy pool

## Current pool

- Alive now: 553
- Gold now: 413
- HTTP: 88 alive / 66 gold
- HTTPS: 107 alive / 20 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 183 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42585
- Ever gold: 1358

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
