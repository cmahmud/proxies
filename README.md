# SyndProxy private pool

## Current pool

- Alive now: 724
- Gold now: 376
- HTTP: 166 alive / 71 gold
- HTTPS: 154 alive / 13 gold
- SOCKS4: 208 alive / 153 gold
- SOCKS5: 196 alive / 139 gold

## Historical pool

- Discovered: 147658
- Ever alive: 25892
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
