# SyndProxy private pool

## Current pool

- Alive now: 645
- Gold now: 236
- HTTP: 174 alive / 29 gold
- HTTPS: 77 alive / 8 gold
- SOCKS4: 191 alive / 109 gold
- SOCKS5: 203 alive / 90 gold

## Historical pool

- Discovered: 86775
- Ever alive: 7596
- Ever gold: 339

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
