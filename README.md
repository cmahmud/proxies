# SyndProxy validated proxy pool

## Current pool

- Alive now: 466
- Gold now: 369
- HTTP: 101 alive / 48 gold
- HTTPS: 28 alive / 12 gold
- SOCKS4: 165 alive / 153 gold
- SOCKS5: 172 alive / 156 gold

## Historical pool

- Discovered: 173755
- Ever alive: 33025
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
