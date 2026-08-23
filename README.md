# SyndProxy validated proxy pool

## Current pool

- Alive now: 510
- Gold now: 352
- HTTP: 112 alive / 41 gold
- HTTPS: 49 alive / 9 gold
- SOCKS4: 166 alive / 152 gold
- SOCKS5: 183 alive / 150 gold

## Historical pool

- Discovered: 171048
- Ever alive: 32848
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
