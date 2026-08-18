# SyndProxy private pool

## Current pool

- Alive now: 652
- Gold now: 250
- HTTP: 153 alive / 34 gold
- HTTPS: 87 alive / 7 gold
- SOCKS4: 213 alive / 125 gold
- SOCKS5: 199 alive / 84 gold

## Historical pool

- Discovered: 94326
- Ever alive: 9352
- Ever gold: 364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
