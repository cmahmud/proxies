# SyndProxy validated proxy pool

## Current pool

- Alive now: 501
- Gold now: 392
- HTTP: 76 alive / 54 gold
- HTTPS: 76 alive / 14 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 177 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42870
- Ever gold: 1364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
