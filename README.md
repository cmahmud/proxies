# SyndProxy private pool

## Current pool

- Alive now: 636
- Gold now: 217
- HTTP: 203 alive / 29 gold
- HTTPS: 76 alive / 7 gold
- SOCKS4: 184 alive / 107 gold
- SOCKS5: 173 alive / 74 gold

## Historical pool

- Discovered: 86711
- Ever alive: 6454
- Ever gold: 300

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
