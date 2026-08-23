# SyndProxy validated proxy pool

## Current pool

- Alive now: 380
- Gold now: 208
- HTTP: 110 alive / 46 gold
- HTTPS: 76 alive / 8 gold
- SOCKS4: 74 alive / 68 gold
- SOCKS5: 120 alive / 86 gold

## Historical pool

- Discovered: 169854
- Ever alive: 32705
- Ever gold: 1206

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
