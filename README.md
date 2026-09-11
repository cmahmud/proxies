# SyndProxy validated proxy pool

## Current pool

- Alive now: 573
- Gold now: 372
- HTTP: 222 alive / 88 gold
- HTTPS: 41 alive / 30 gold
- SOCKS4: 102 alive / 76 gold
- SOCKS5: 208 alive / 178 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48620
- Ever gold: 1560

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
