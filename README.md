# SyndProxy validated proxy pool

## Current pool

- Alive now: 548
- Gold now: 413
- HTTP: 97 alive / 71 gold
- HTTPS: 109 alive / 23 gold
- SOCKS4: 166 alive / 159 gold
- SOCKS5: 176 alive / 160 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41833
- Ever gold: 1343

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
