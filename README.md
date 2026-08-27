# SyndProxy validated proxy pool

## Current pool

- Alive now: 512
- Gold now: 407
- HTTP: 94 alive / 61 gold
- HTTPS: 61 alive / 23 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 185 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41716
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
