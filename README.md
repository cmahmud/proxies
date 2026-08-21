# SyndProxy private pool

## Current pool

- Alive now: 1110
- Gold now: 441
- HTTP: 372 alive / 106 gold
- HTTPS: 272 alive / 28 gold
- SOCKS4: 200 alive / 151 gold
- SOCKS5: 266 alive / 156 gold

## Historical pool

- Discovered: 153726
- Ever alive: 28574
- Ever gold: 1110

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
