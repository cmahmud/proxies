# SyndProxy private pool

## Current pool

- Alive now: 717
- Gold now: 366
- HTTP: 164 alive / 65 gold
- HTTPS: 141 alive / 12 gold
- SOCKS4: 211 alive / 151 gold
- SOCKS5: 201 alive / 138 gold

## Historical pool

- Discovered: 147685
- Ever alive: 25898
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
