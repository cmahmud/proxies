# SyndProxy private pool

## Current pool

- Alive now: 1002
- Gold now: 236
- HTTP: 298 alive / 33 gold
- HTTPS: 209 alive / 9 gold
- SOCKS4: 253 alive / 113 gold
- SOCKS5: 242 alive / 81 gold

## Historical pool

- Discovered: 86746
- Ever alive: 7591
- Ever gold: 336

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
