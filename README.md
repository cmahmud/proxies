# SyndProxy private pool

## Current pool

- Alive now: 926
- Gold now: 386
- HTTP: 286 alive / 84 gold
- HTTPS: 189 alive / 24 gold
- SOCKS4: 216 alive / 136 gold
- SOCKS5: 235 alive / 142 gold

## Historical pool

- Discovered: 157419
- Ever alive: 29713
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
