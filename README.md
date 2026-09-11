# SyndProxy validated proxy pool

## Current pool

- Alive now: 475
- Gold now: 376
- HTTP: 90 alive / 67 gold
- HTTPS: 42 alive / 24 gold
- SOCKS4: 152 alive / 115 gold
- SOCKS5: 191 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48729
- Ever gold: 1564

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
