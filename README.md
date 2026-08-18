# SyndProxy private pool

## Current pool

- Alive now: 842
- Gold now: 220
- HTTP: 278 alive / 30 gold
- HTTPS: 140 alive / 10 gold
- SOCKS4: 206 alive / 98 gold
- SOCKS5: 218 alive / 82 gold

## Historical pool

- Discovered: 86777
- Ever alive: 7958
- Ever gold: 343

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
