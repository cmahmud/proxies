# SyndProxy private pool

## Current pool

- Alive now: 740
- Gold now: 392
- HTTP: 183 alive / 89 gold
- HTTPS: 132 alive / 26 gold
- SOCKS4: 209 alive / 127 gold
- SOCKS5: 216 alive / 150 gold

## Historical pool

- Discovered: 151059
- Ever alive: 27297
- Ever gold: 1094

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
