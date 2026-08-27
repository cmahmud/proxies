# SyndProxy validated proxy pool

## Current pool

- Alive now: 558
- Gold now: 420
- HTTP: 92 alive / 67 gold
- HTTPS: 108 alive / 22 gold
- SOCKS4: 173 alive / 165 gold
- SOCKS5: 185 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41465
- Ever gold: 1332

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
