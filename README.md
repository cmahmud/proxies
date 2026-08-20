# SyndProxy private pool

## Current pool

- Alive now: 810
- Gold now: 389
- HTTP: 236 alive / 83 gold
- HTTPS: 160 alive / 20 gold
- SOCKS4: 214 alive / 142 gold
- SOCKS5: 200 alive / 144 gold

## Historical pool

- Discovered: 144750
- Ever alive: 25232
- Ever gold: 1057

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
