# SyndProxy private pool

## Current pool

- Alive now: 1659
- Gold now: 619
- HTTP: 663 alive / 232 gold
- HTTPS: 517 alive / 101 gold
- SOCKS4: 213 alive / 142 gold
- SOCKS5: 266 alive / 144 gold

## Historical pool

- Discovered: 142740
- Ever alive: 24607
- Ever gold: 1029

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
