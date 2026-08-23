# SyndProxy validated proxy pool

## Current pool

- Alive now: 459
- Gold now: 367
- HTTP: 96 alive / 47 gold
- HTTPS: 26 alive / 11 gold
- SOCKS4: 165 alive / 153 gold
- SOCKS5: 172 alive / 156 gold

## Historical pool

- Discovered: 173755
- Ever alive: 33025
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
