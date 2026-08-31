# SyndProxy validated proxy pool

## Current pool

- Alive now: 666
- Gold now: 465
- HTTP: 141 alive / 94 gold
- HTTPS: 115 alive / 33 gold
- SOCKS4: 179 alive / 162 gold
- SOCKS5: 231 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46192
- Ever gold: 1442

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
