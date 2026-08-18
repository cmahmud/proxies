# SyndProxy private pool

## Current pool

- Alive now: 843
- Gold now: 268
- HTTP: 216 alive / 28 gold
- HTTPS: 150 alive / 5 gold
- SOCKS4: 235 alive / 121 gold
- SOCKS5: 242 alive / 114 gold

## Historical pool

- Discovered: 99165
- Ever alive: 12140
- Ever gold: 392

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
