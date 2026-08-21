# SyndProxy private pool

## Current pool

- Alive now: 822
- Gold now: 405
- HTTP: 224 alive / 89 gold
- HTTPS: 147 alive / 25 gold
- SOCKS4: 209 alive / 147 gold
- SOCKS5: 242 alive / 144 gold

## Historical pool

- Discovered: 154723
- Ever alive: 29134
- Ever gold: 1123

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
