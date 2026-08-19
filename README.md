# SyndProxy private pool

## Current pool

- Alive now: 1202
- Gold now: 477
- HTTP: 444 alive / 123 gold
- HTTPS: 284 alive / 72 gold
- SOCKS4: 239 alive / 141 gold
- SOCKS5: 235 alive / 141 gold

## Historical pool

- Discovered: 113536
- Ever alive: 16536
- Ever gold: 621

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
