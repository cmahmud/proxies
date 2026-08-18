# SyndProxy private pool

## Current pool

- Alive now: 957
- Gold now: 316
- HTTP: 332 alive / 40 gold
- HTTPS: 160 alive / 10 gold
- SOCKS4: 240 alive / 139 gold
- SOCKS5: 225 alive / 127 gold

## Historical pool

- Discovered: 107013
- Ever alive: 14369
- Ever gold: 440

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
