# SyndProxy private pool

## Current pool

- Alive now: 1106
- Gold now: 540
- HTTP: 411 alive / 154 gold
- HTTPS: 271 alive / 106 gold
- SOCKS4: 216 alive / 138 gold
- SOCKS5: 208 alive / 142 gold

## Historical pool

- Discovered: 127353
- Ever alive: 19837
- Ever gold: 803

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
