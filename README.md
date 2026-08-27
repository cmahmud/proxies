# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 393
- HTTP: 95 alive / 64 gold
- HTTPS: 78 alive / 18 gold
- SOCKS4: 166 alive / 152 gold
- SOCKS5: 175 alive / 159 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41742
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
