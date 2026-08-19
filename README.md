# SyndProxy private pool

## Current pool

- Alive now: 991
- Gold now: 368
- HTTP: 321 alive / 77 gold
- HTTPS: 223 alive / 13 gold
- SOCKS4: 220 alive / 126 gold
- SOCKS5: 227 alive / 152 gold

## Historical pool

- Discovered: 129304
- Ever alive: 20389
- Ever gold: 865

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
