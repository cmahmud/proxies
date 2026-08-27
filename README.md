# SyndProxy validated proxy pool

## Current pool

- Alive now: 490
- Gold now: 390
- HTTP: 74 alive / 48 gold
- HTTPS: 50 alive / 16 gold
- SOCKS4: 178 alive / 163 gold
- SOCKS5: 188 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41668
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
