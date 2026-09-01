# SyndProxy validated proxy pool

## Current pool

- Alive now: 659
- Gold now: 465
- HTTP: 131 alive / 92 gold
- HTTPS: 130 alive / 36 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 221 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46468
- Ever gold: 1444

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
