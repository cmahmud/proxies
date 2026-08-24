# SyndProxy validated proxy pool

## Current pool

- Alive now: 543
- Gold now: 387
- HTTP: 113 alive / 52 gold
- HTTPS: 45 alive / 14 gold
- SOCKS4: 183 alive / 156 gold
- SOCKS5: 202 alive / 165 gold

## Historical pool

- Discovered: 178697
- Ever alive: 33406
- Ever gold: 1235

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
