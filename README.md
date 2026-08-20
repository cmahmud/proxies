# SyndProxy private pool

## Current pool

- Alive now: 1232
- Gold now: 566
- HTTP: 452 alive / 186 gold
- HTTPS: 321 alive / 95 gold
- SOCKS4: 206 alive / 127 gold
- SOCKS5: 253 alive / 158 gold

## Historical pool

- Discovered: 138813
- Ever alive: 22948
- Ever gold: 910

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
