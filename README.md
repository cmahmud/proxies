# SyndProxy validated proxy pool

## Current pool

- Alive now: 689
- Gold now: 465
- HTTP: 145 alive / 93 gold
- HTTPS: 133 alive / 34 gold
- SOCKS4: 179 alive / 162 gold
- SOCKS5: 232 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46216
- Ever gold: 1442

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
