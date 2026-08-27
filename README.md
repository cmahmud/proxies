# SyndProxy validated proxy pool

## Current pool

- Alive now: 596
- Gold now: 420
- HTTP: 113 alive / 81 gold
- HTTPS: 117 alive / 16 gold
- SOCKS4: 177 alive / 158 gold
- SOCKS5: 189 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42092
- Ever gold: 1350

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
