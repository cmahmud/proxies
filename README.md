# SyndProxy validated proxy pool

## Current pool

- Alive now: 568
- Gold now: 420
- HTTP: 102 alive / 73 gold
- HTTPS: 105 alive / 21 gold
- SOCKS4: 178 alive / 158 gold
- SOCKS5: 183 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42505
- Ever gold: 1358

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
