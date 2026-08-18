# SyndProxy private pool

## Current pool

- Alive now: 774
- Gold now: 213
- HTTP: 217 alive / 26 gold
- HTTPS: 133 alive / 9 gold
- SOCKS4: 205 alive / 97 gold
- SOCKS5: 219 alive / 81 gold

## Historical pool

- Discovered: 86777
- Ever alive: 7959
- Ever gold: 343

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
