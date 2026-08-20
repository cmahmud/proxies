# SyndProxy private pool

## Current pool

- Alive now: 1638
- Gold now: 635
- HTTP: 654 alive / 236 gold
- HTTPS: 514 alive / 113 gold
- SOCKS4: 208 alive / 142 gold
- SOCKS5: 262 alive / 144 gold

## Historical pool

- Discovered: 142746
- Ever alive: 24607
- Ever gold: 1029

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
