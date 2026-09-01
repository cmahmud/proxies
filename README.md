# SyndProxy validated proxy pool

## Current pool

- Alive now: 630
- Gold now: 473
- HTTP: 131 alive / 93 gold
- HTTPS: 124 alive / 44 gold
- SOCKS4: 179 alive / 163 gold
- SOCKS5: 196 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46959
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
