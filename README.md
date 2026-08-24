# SyndProxy validated proxy pool

## Current pool

- Alive now: 598
- Gold now: 437
- HTTP: 139 alive / 81 gold
- HTTPS: 92 alive / 23 gold
- SOCKS4: 173 alive / 160 gold
- SOCKS5: 194 alive / 173 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34535
- Ever gold: 1256

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
