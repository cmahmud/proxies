# SyndProxy private pool

## Current pool

- Alive now: 807
- Gold now: 388
- HTTP: 234 alive / 77 gold
- HTTPS: 143 alive / 22 gold
- SOCKS4: 216 alive / 143 gold
- SOCKS5: 214 alive / 146 gold

## Historical pool

- Discovered: 144750
- Ever alive: 25263
- Ever gold: 1057

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
