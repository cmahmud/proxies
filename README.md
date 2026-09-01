# SyndProxy validated proxy pool

## Current pool

- Alive now: 655
- Gold now: 463
- HTTP: 150 alive / 92 gold
- HTTPS: 134 alive / 36 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 195 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46872
- Ever gold: 1452

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
