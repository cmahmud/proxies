# SyndProxy private pool

## Current pool

- Alive now: 1223
- Gold now: 393
- HTTP: 432 alive / 88 gold
- HTTPS: 326 alive / 15 gold
- SOCKS4: 220 alive / 129 gold
- SOCKS5: 245 alive / 161 gold

## Historical pool

- Discovered: 131850
- Ever alive: 21259
- Ever gold: 880

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
