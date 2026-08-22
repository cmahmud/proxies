# SyndProxy private pool

## Current pool

- Alive now: 852
- Gold now: 376
- HTTP: 230 alive / 87 gold
- HTTPS: 192 alive / 25 gold
- SOCKS4: 202 alive / 122 gold
- SOCKS5: 228 alive / 142 gold

## Historical pool

- Discovered: 164245
- Ever alive: 32068
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
