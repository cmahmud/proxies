# SyndProxy private pool

## Current pool

- Alive now: 1195
- Gold now: 410
- HTTP: 396 alive / 97 gold
- HTTPS: 284 alive / 23 gold
- SOCKS4: 197 alive / 125 gold
- SOCKS5: 318 alive / 165 gold

## Historical pool

- Discovered: 143501
- Ever alive: 24860
- Ever gold: 1051

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
