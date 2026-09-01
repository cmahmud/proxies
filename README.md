# SyndProxy validated proxy pool

## Current pool

- Alive now: 560
- Gold now: 447
- HTTP: 93 alive / 74 gold
- HTTPS: 106 alive / 31 gold
- SOCKS4: 170 alive / 163 gold
- SOCKS5: 191 alive / 179 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47412
- Ever gold: 1468

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
