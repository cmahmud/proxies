# SyndProxy validated proxy pool

## Current pool

- Alive now: 512
- Gold now: 407
- HTTP: 101 alive / 73 gold
- HTTPS: 79 alive / 17 gold
- SOCKS4: 161 alive / 156 gold
- SOCKS5: 171 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43095
- Ever gold: 1365

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
