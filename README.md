# SyndProxy private pool

## Current pool

- Alive now: 1217
- Gold now: 399
- HTTP: 423 alive / 101 gold
- HTTPS: 309 alive / 28 gold
- SOCKS4: 225 alive / 127 gold
- SOCKS5: 260 alive / 143 gold

## Historical pool

- Discovered: 152746
- Ever alive: 28115
- Ever gold: 1104

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
