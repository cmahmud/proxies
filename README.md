# SyndProxy private pool

## Current pool

- Alive now: 884
- Gold now: 322
- HTTP: 297 alive / 57 gold
- HTTPS: 195 alive / 9 gold
- SOCKS4: 197 alive / 127 gold
- SOCKS5: 195 alive / 129 gold

## Historical pool

- Discovered: 129258
- Ever alive: 20141
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
