# SyndProxy private pool

## Current pool

- Alive now: 723
- Gold now: 399
- HTTP: 164 alive / 80 gold
- HTTPS: 129 alive / 20 gold
- SOCKS4: 222 alive / 152 gold
- SOCKS5: 208 alive / 147 gold

## Historical pool

- Discovered: 144750
- Ever alive: 25217
- Ever gold: 1057

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
