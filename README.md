# SyndProxy validated proxy pool

## Current pool

- Alive now: 366
- Gold now: 192
- HTTP: 114 alive / 40 gold
- HTTPS: 65 alive / 8 gold
- SOCKS4: 70 alive / 61 gold
- SOCKS5: 117 alive / 83 gold

## Historical pool

- Discovered: 169863
- Ever alive: 32716
- Ever gold: 1207

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
