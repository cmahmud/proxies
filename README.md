# SyndProxy private pool

## Current pool

- Alive now: 733
- Gold now: 362
- HTTP: 205 alive / 69 gold
- HTTPS: 115 alive / 15 gold
- SOCKS4: 214 alive / 148 gold
- SOCKS5: 199 alive / 130 gold

## Historical pool

- Discovered: 145561
- Ever alive: 25478
- Ever gold: 1060

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
