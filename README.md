# SyndProxy private pool

## Current pool

- Alive now: 617
- Gold now: 217
- HTTP: 192 alive / 29 gold
- HTTPS: 75 alive / 7 gold
- SOCKS4: 183 alive / 107 gold
- SOCKS5: 167 alive / 74 gold

## Historical pool

- Discovered: 86711
- Ever alive: 6454
- Ever gold: 300

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
