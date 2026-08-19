# SyndProxy private pool

## Current pool

- Alive now: 997
- Gold now: 522
- HTTP: 346 alive / 153 gold
- HTTPS: 241 alive / 91 gold
- SOCKS4: 204 alive / 144 gold
- SOCKS5: 206 alive / 134 gold

## Historical pool

- Discovered: 127362
- Ever alive: 19896
- Ever gold: 803

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
