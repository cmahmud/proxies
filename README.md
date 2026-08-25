# SyndProxy validated proxy pool

## Current pool

- Alive now: 554
- Gold now: 419
- HTTP: 105 alive / 70 gold
- HTTPS: 89 alive / 18 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 191 alive / 171 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34826
- Ever gold: 1258

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
