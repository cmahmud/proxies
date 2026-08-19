# SyndProxy private pool

## Current pool

- Alive now: 1318
- Gold now: 400
- HTTP: 447 alive / 90 gold
- HTTPS: 302 alive / 16 gold
- SOCKS4: 243 alive / 147 gold
- SOCKS5: 326 alive / 147 gold

## Historical pool

- Discovered: 133966
- Ever alive: 21672
- Ever gold: 886

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
