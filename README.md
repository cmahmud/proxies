# SyndProxy validated proxy pool

## Current pool

- Alive now: 663
- Gold now: 413
- HTTP: 114 alive / 67 gold
- HTTPS: 180 alive / 17 gold
- SOCKS4: 183 alive / 163 gold
- SOCKS5: 186 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41190
- Ever gold: 1318

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
