# SyndProxy private pool

## Current pool

- Alive now: 929
- Gold now: 293
- HTTP: 304 alive / 26 gold
- HTTPS: 186 alive / 4 gold
- SOCKS4: 223 alive / 142 gold
- SOCKS5: 216 alive / 121 gold

## Historical pool

- Discovered: 102858
- Ever alive: 13515
- Ever gold: 417

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
