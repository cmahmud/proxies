# SyndProxy private pool

## Current pool

- Alive now: 877
- Gold now: 319
- HTTP: 291 alive / 49 gold
- HTTPS: 189 alive / 11 gold
- SOCKS4: 207 alive / 132 gold
- SOCKS5: 190 alive / 127 gold

## Historical pool

- Discovered: 128086
- Ever alive: 20030
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
