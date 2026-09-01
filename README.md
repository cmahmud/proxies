# SyndProxy validated proxy pool

## Current pool

- Alive now: 650
- Gold now: 463
- HTTP: 130 alive / 91 gold
- HTTPS: 119 alive / 37 gold
- SOCKS4: 179 alive / 160 gold
- SOCKS5: 222 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46501
- Ever gold: 1445

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
