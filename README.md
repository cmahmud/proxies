# SyndProxy private pool

## Current pool

- Alive now: 1207
- Gold now: 475
- HTTP: 442 alive / 123 gold
- HTTPS: 286 alive / 73 gold
- SOCKS4: 243 alive / 146 gold
- SOCKS5: 236 alive / 133 gold

## Historical pool

- Discovered: 113536
- Ever alive: 16584
- Ever gold: 621

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
