# SyndProxy validated proxy pool

## Current pool

- Alive now: 666
- Gold now: 349
- HTTP: 213 alive / 39 gold
- HTTPS: 45 alive / 10 gold
- SOCKS4: 181 alive / 154 gold
- SOCKS5: 227 alive / 146 gold

## Historical pool

- Discovered: 171094
- Ever alive: 32870
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
