# SyndProxy private pool

## Current pool

- Alive now: 1176
- Gold now: 405
- HTTP: 406 alive / 92 gold
- HTTPS: 241 alive / 15 gold
- SOCKS4: 227 alive / 148 gold
- SOCKS5: 302 alive / 150 gold

## Historical pool

- Discovered: 131842
- Ever alive: 21218
- Ever gold: 879

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
