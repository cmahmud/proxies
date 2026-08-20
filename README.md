# SyndProxy private pool

## Current pool

- Alive now: 870
- Gold now: 381
- HTTP: 221 alive / 77 gold
- HTTPS: 213 alive / 17 gold
- SOCKS4: 218 alive / 150 gold
- SOCKS5: 218 alive / 137 gold

## Historical pool

- Discovered: 149510
- Ever alive: 26860
- Ever gold: 1088

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
