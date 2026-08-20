# SyndProxy private pool

## Current pool

- Alive now: 859
- Gold now: 371
- HTTP: 252 alive / 77 gold
- HTTPS: 159 alive / 21 gold
- SOCKS4: 207 alive / 136 gold
- SOCKS5: 241 alive / 137 gold

## Historical pool

- Discovered: 144770
- Ever alive: 25288
- Ever gold: 1057

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
