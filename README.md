# SyndProxy validated proxy pool

## Current pool

- Alive now: 487
- Gold now: 376
- HTTP: 91 alive / 67 gold
- HTTPS: 49 alive / 25 gold
- SOCKS4: 155 alive / 114 gold
- SOCKS5: 192 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48729
- Ever gold: 1564

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
