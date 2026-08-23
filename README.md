# SyndProxy validated proxy pool

## Current pool

- Alive now: 552
- Gold now: 352
- HTTP: 130 alive / 40 gold
- HTTPS: 54 alive / 10 gold
- SOCKS4: 176 alive / 153 gold
- SOCKS5: 192 alive / 149 gold

## Historical pool

- Discovered: 171048
- Ever alive: 32848
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
