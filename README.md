# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 407
- HTTP: 100 alive / 63 gold
- HTTPS: 73 alive / 19 gold
- SOCKS4: 166 alive / 161 gold
- SOCKS5: 178 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41735
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
