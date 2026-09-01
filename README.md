# SyndProxy validated proxy pool

## Current pool

- Alive now: 526
- Gold now: 426
- HTTP: 107 alive / 67 gold
- HTTPS: 74 alive / 30 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 172 alive / 167 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47056
- Ever gold: 1463

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
