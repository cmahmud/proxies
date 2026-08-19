# SyndProxy private pool

## Current pool

- Alive now: 1071
- Gold now: 482
- HTTP: 341 alive / 123 gold
- HTTPS: 234 alive / 72 gold
- SOCKS4: 232 alive / 140 gold
- SOCKS5: 264 alive / 147 gold

## Historical pool

- Discovered: 113575
- Ever alive: 16886
- Ever gold: 626

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
