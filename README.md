# SyndProxy validated proxy pool

## Current pool

- Alive now: 553
- Gold now: 420
- HTTP: 97 alive / 75 gold
- HTTPS: 105 alive / 21 gold
- SOCKS4: 172 alive / 159 gold
- SOCKS5: 179 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42003
- Ever gold: 1348

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
