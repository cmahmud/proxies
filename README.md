# SyndProxy private pool

## Current pool

- Alive now: 960
- Gold now: 419
- HTTP: 300 alive / 91 gold
- HTTPS: 192 alive / 25 gold
- SOCKS4: 211 alive / 141 gold
- SOCKS5: 257 alive / 162 gold

## Historical pool

- Discovered: 154719
- Ever alive: 29043
- Ever gold: 1119

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
