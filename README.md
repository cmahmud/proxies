# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 420
- HTTP: 95 alive / 76 gold
- HTTPS: 75 alive / 22 gold
- SOCKS4: 168 alive / 161 gold
- SOCKS5: 175 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41764
- Ever gold: 1343

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
