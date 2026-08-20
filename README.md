# SyndProxy private pool

## Current pool

- Alive now: 1211
- Gold now: 566
- HTTP: 432 alive / 186 gold
- HTTPS: 329 alive / 93 gold
- SOCKS4: 200 alive / 127 gold
- SOCKS5: 250 alive / 160 gold

## Historical pool

- Discovered: 138813
- Ever alive: 22944
- Ever gold: 910

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
