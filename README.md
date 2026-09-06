# SyndProxy validated proxy pool

## Current pool

- Alive now: 479
- Gold now: 395
- HTTP: 91 alive / 67 gold
- HTTPS: 31 alive / 14 gold
- SOCKS4: 173 alive / 152 gold
- SOCKS5: 184 alive / 162 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48242
- Ever gold: 1526

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
