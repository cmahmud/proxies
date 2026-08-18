# SyndProxy private pool

## Current pool

- Alive now: 586
- Gold now: 219
- HTTP: 165 alive / 30 gold
- HTTPS: 73 alive / 7 gold
- SOCKS4: 174 alive / 107 gold
- SOCKS5: 174 alive / 75 gold

## Historical pool

- Discovered: 86711
- Ever alive: 6454
- Ever gold: 300

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
