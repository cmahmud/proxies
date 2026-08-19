# SyndProxy private pool

## Current pool

- Alive now: 927
- Gold now: 322
- HTTP: 328 alive / 49 gold
- HTTPS: 192 alive / 11 gold
- SOCKS4: 203 alive / 131 gold
- SOCKS5: 204 alive / 131 gold

## Historical pool

- Discovered: 128143
- Ever alive: 20034
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
