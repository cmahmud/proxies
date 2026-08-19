# SyndProxy private pool

## Current pool

- Alive now: 1270
- Gold now: 365
- HTTP: 459 alive / 91 gold
- HTTPS: 272 alive / 21 gold
- SOCKS4: 234 alive / 116 gold
- SOCKS5: 305 alive / 137 gold

## Historical pool

- Discovered: 134552
- Ever alive: 22079
- Ever gold: 893

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
