# SyndProxy private pool

## Current pool

- Alive now: 822
- Gold now: 405
- HTTP: 246 alive / 91 gold
- HTTPS: 128 alive / 22 gold
- SOCKS4: 220 alive / 144 gold
- SOCKS5: 228 alive / 148 gold

## Historical pool

- Discovered: 155802
- Ever alive: 29405
- Ever gold: 1126

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
