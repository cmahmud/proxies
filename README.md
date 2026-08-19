# SyndProxy private pool

## Current pool

- Alive now: 1145
- Gold now: 467
- HTTP: 424 alive / 122 gold
- HTTPS: 261 alive / 73 gold
- SOCKS4: 231 alive / 140 gold
- SOCKS5: 229 alive / 132 gold

## Historical pool

- Discovered: 113536
- Ever alive: 16583
- Ever gold: 621

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
