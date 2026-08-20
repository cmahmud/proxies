# SyndProxy private pool

## Current pool

- Alive now: 1617
- Gold now: 583
- HTTP: 635 alive / 183 gold
- HTTPS: 510 alive / 90 gold
- SOCKS4: 223 alive / 144 gold
- SOCKS5: 249 alive / 166 gold

## Historical pool

- Discovered: 141229
- Ever alive: 24022
- Ever gold: 967

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
