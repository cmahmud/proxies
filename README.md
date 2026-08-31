# SyndProxy validated proxy pool

## Current pool

- Alive now: 732
- Gold now: 475
- HTTP: 199 alive / 98 gold
- HTTPS: 126 alive / 39 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 231 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45294
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
