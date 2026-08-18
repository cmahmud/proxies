# SyndProxy private pool

## Current pool

- Alive now: 714
- Gold now: 212
- HTTP: 194 alive / 25 gold
- HTTPS: 106 alive / 9 gold
- SOCKS4: 206 alive / 97 gold
- SOCKS5: 208 alive / 81 gold

## Historical pool

- Discovered: 86780
- Ever alive: 7959
- Ever gold: 343

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
