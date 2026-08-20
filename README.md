# SyndProxy private pool

## Current pool

- Alive now: 798
- Gold now: 405
- HTTP: 195 alive / 76 gold
- HTTPS: 171 alive / 22 gold
- SOCKS4: 224 alive / 150 gold
- SOCKS5: 208 alive / 157 gold

## Historical pool

- Discovered: 149514
- Ever alive: 26945
- Ever gold: 1089

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
