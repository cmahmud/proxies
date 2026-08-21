# SyndProxy private pool

## Current pool

- Alive now: 754
- Gold now: 402
- HTTP: 192 alive / 88 gold
- HTTPS: 116 alive / 23 gold
- SOCKS4: 204 alive / 146 gold
- SOCKS5: 242 alive / 145 gold

## Historical pool

- Discovered: 154723
- Ever alive: 29135
- Ever gold: 1123

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
