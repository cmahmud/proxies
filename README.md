# SyndProxy validated proxy pool

## Current pool

- Alive now: 494
- Gold now: 399
- HTTP: 78 alive / 54 gold
- HTTPS: 56 alive / 19 gold
- SOCKS4: 182 alive / 161 gold
- SOCKS5: 178 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41584
- Ever gold: 1339

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
