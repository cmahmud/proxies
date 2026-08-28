# SyndProxy validated proxy pool

## Current pool

- Alive now: 574
- Gold now: 413
- HTTP: 98 alive / 65 gold
- HTTPS: 118 alive / 21 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 183 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43002
- Ever gold: 1365

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
