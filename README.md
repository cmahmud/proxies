# SyndProxy private pool

## Current pool

- Alive now: 803
- Gold now: 412
- HTTP: 215 alive / 84 gold
- HTTPS: 151 alive / 28 gold
- SOCKS4: 194 alive / 131 gold
- SOCKS5: 243 alive / 169 gold

## Historical pool

- Discovered: 162742
- Ever alive: 31497
- Ever gold: 1160

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
