# SyndProxy private pool

## Current pool

- Alive now: 701
- Gold now: 357
- HTTP: 212 alive / 68 gold
- HTTPS: 128 alive / 20 gold
- SOCKS4: 183 alive / 133 gold
- SOCKS5: 178 alive / 136 gold

## Historical pool

- Discovered: 147175
- Ever alive: 25783
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
