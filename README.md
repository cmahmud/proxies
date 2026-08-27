# SyndProxy validated proxy pool

## Current pool

- Alive now: 508
- Gold now: 402
- HTTP: 83 alive / 56 gold
- HTTPS: 61 alive / 19 gold
- SOCKS4: 186 alive / 162 gold
- SOCKS5: 178 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41584
- Ever gold: 1339

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
