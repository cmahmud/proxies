# SyndProxy validated proxy pool

## Current pool

- Alive now: 547
- Gold now: 411
- HTTP: 89 alive / 72 gold
- HTTPS: 101 alive / 17 gold
- SOCKS4: 178 alive / 158 gold
- SOCKS5: 179 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42025
- Ever gold: 1348

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
