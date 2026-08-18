# SyndProxy private pool

## Current pool

- Alive now: 678
- Gold now: 213
- HTTP: 183 alive / 25 gold
- HTTPS: 87 alive / 9 gold
- SOCKS4: 204 alive / 98 gold
- SOCKS5: 204 alive / 81 gold

## Historical pool

- Discovered: 86783
- Ever alive: 7960
- Ever gold: 343

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
