# SyndProxy validated proxy pool

## Current pool

- Alive now: 572
- Gold now: 451
- HTTP: 102 alive / 77 gold
- HTTPS: 102 alive / 33 gold
- SOCKS4: 179 alive / 165 gold
- SOCKS5: 189 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47428
- Ever gold: 1468

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
