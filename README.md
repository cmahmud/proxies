# SyndProxy validated proxy pool

## Current pool

- Alive now: 566
- Gold now: 416
- HTTP: 119 alive / 65 gold
- HTTPS: 87 alive / 21 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 185 alive / 169 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35407
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
