# SyndProxy validated proxy pool

## Current pool

- Alive now: 372
- Gold now: 208
- HTTP: 108 alive / 46 gold
- HTTPS: 66 alive / 8 gold
- SOCKS4: 73 alive / 69 gold
- SOCKS5: 125 alive / 85 gold

## Historical pool

- Discovered: 169854
- Ever alive: 32708
- Ever gold: 1206

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
