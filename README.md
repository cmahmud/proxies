# SyndProxy validated proxy pool

## Current pool

- Alive now: 552
- Gold now: 413
- HTTP: 105 alive / 72 gold
- HTTPS: 104 alive / 22 gold
- SOCKS4: 165 alive / 158 gold
- SOCKS5: 178 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41968
- Ever gold: 1346

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
