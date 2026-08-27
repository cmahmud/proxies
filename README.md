# SyndProxy validated proxy pool

## Current pool

- Alive now: 560
- Gold now: 407
- HTTP: 95 alive / 70 gold
- HTTPS: 119 alive / 16 gold
- SOCKS4: 168 alive / 158 gold
- SOCKS5: 178 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42046
- Ever gold: 1348

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
