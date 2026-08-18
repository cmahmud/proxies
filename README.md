# SyndProxy private pool

## Current pool

- Alive now: 1340
- Gold now: 235
- HTTP: 618 alive / 32 gold
- HTTPS: 252 alive / 9 gold
- SOCKS4: 237 alive / 111 gold
- SOCKS5: 233 alive / 83 gold

## Historical pool

- Discovered: 86746
- Ever alive: 7591
- Ever gold: 335

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
