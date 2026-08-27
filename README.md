# SyndProxy validated proxy pool

## Current pool

- Alive now: 508
- Gold now: 393
- HTTP: 93 alive / 64 gold
- HTTPS: 75 alive / 18 gold
- SOCKS4: 165 alive / 152 gold
- SOCKS5: 175 alive / 159 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41742
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
