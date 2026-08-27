# SyndProxy validated proxy pool

## Current pool

- Alive now: 668
- Gold now: 413
- HTTP: 126 alive / 68 gold
- HTTPS: 174 alive / 15 gold
- SOCKS4: 180 alive / 159 gold
- SOCKS5: 188 alive / 171 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40832
- Ever gold: 1313

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
