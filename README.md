# SyndProxy validated proxy pool

## Current pool

- Alive now: 582
- Gold now: 449
- HTTP: 112 alive / 78 gold
- HTTPS: 108 alive / 30 gold
- SOCKS4: 173 alive / 163 gold
- SOCKS5: 189 alive / 178 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47370
- Ever gold: 1467

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
