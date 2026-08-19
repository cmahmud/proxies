# SyndProxy private pool

## Current pool

- Alive now: 1107
- Gold now: 467
- HTTP: 417 alive / 122 gold
- HTTPS: 244 alive / 73 gold
- SOCKS4: 226 alive / 140 gold
- SOCKS5: 220 alive / 132 gold

## Historical pool

- Discovered: 113536
- Ever alive: 16582
- Ever gold: 621

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
