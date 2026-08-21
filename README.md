# SyndProxy private pool

## Current pool

- Alive now: 800
- Gold now: 417
- HTTP: 220 alive / 83 gold
- HTTPS: 115 alive / 23 gold
- SOCKS4: 222 alive / 152 gold
- SOCKS5: 243 alive / 159 gold

## Historical pool

- Discovered: 157420
- Ever alive: 29748
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
