# SyndProxy validated proxy pool

## Current pool

- Alive now: 530
- Gold now: 417
- HTTP: 100 alive / 70 gold
- HTTPS: 69 alive / 17 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 192 alive / 171 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34826
- Ever gold: 1258

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
