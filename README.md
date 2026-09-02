# SyndProxy validated proxy pool

## Current pool

- Alive now: 568
- Gold now: 452
- HTTP: 102 alive / 78 gold
- HTTPS: 104 alive / 31 gold
- SOCKS4: 176 alive / 165 gold
- SOCKS5: 186 alive / 178 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47428
- Ever gold: 1468

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
