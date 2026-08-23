# SyndProxy validated proxy pool

## Current pool

- Alive now: 522
- Gold now: 351
- HTTP: 113 alive / 40 gold
- HTTPS: 46 alive / 9 gold
- SOCKS4: 172 alive / 152 gold
- SOCKS5: 191 alive / 150 gold

## Historical pool

- Discovered: 171048
- Ever alive: 32848
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
