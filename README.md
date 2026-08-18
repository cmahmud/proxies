# SyndProxy private pool

## Current pool

- Alive now: 1084
- Gold now: 290
- HTTP: 345 alive / 30 gold
- HTTPS: 250 alive / 4 gold
- SOCKS4: 242 alive / 140 gold
- SOCKS5: 247 alive / 116 gold

## Historical pool

- Discovered: 100167
- Ever alive: 12669
- Ever gold: 399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
