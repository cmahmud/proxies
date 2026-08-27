# SyndProxy validated proxy pool

## Current pool

- Alive now: 504
- Gold now: 407
- HTTP: 76 alive / 59 gold
- HTTPS: 63 alive / 18 gold
- SOCKS4: 175 alive / 165 gold
- SOCKS5: 190 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41571
- Ever gold: 1339

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
