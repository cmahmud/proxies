# SyndProxy validated proxy pool

## Current pool

- Alive now: 571
- Gold now: 413
- HTTP: 96 alive / 71 gold
- HTTPS: 124 alive / 19 gold
- SOCKS4: 168 alive / 159 gold
- SOCKS5: 183 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41919
- Ever gold: 1344

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
