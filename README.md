# SyndProxy private pool

## Current pool

- Alive now: 880
- Gold now: 412
- HTTP: 265 alive / 84 gold
- HTTPS: 179 alive / 28 gold
- SOCKS4: 183 alive / 132 gold
- SOCKS5: 253 alive / 168 gold

## Historical pool

- Discovered: 162742
- Ever alive: 31483
- Ever gold: 1160

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
