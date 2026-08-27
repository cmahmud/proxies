# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 413
- HTTP: 93 alive / 71 gold
- HTTPS: 75 alive / 20 gold
- SOCKS4: 170 alive / 159 gold
- SOCKS5: 177 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41757
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
