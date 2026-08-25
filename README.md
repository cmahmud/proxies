# SyndProxy validated proxy pool

## Current pool

- Alive now: 547
- Gold now: 416
- HTTP: 105 alive / 67 gold
- HTTPS: 84 alive / 20 gold
- SOCKS4: 170 alive / 160 gold
- SOCKS5: 188 alive / 169 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34819
- Ever gold: 1258

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
