# SyndProxy private pool

## Current pool

- Alive now: 1309
- Gold now: 238
- HTTP: 589 alive / 34 gold
- HTTPS: 242 alive / 9 gold
- SOCKS4: 244 alive / 113 gold
- SOCKS5: 234 alive / 82 gold

## Historical pool

- Discovered: 86746
- Ever alive: 7591
- Ever gold: 336

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
