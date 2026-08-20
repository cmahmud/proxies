# SyndProxy private pool

## Current pool

- Alive now: 717
- Gold now: 372
- HTTP: 164 alive / 69 gold
- HTTPS: 139 alive / 12 gold
- SOCKS4: 211 alive / 153 gold
- SOCKS5: 203 alive / 138 gold

## Historical pool

- Discovered: 147685
- Ever alive: 25895
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
