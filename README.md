# SyndProxy validated proxy pool

## Current pool

- Alive now: 631
- Gold now: 457
- HTTP: 129 alive / 88 gold
- HTTPS: 139 alive / 33 gold
- SOCKS4: 176 alive / 161 gold
- SOCKS5: 187 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46855
- Ever gold: 1452

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
