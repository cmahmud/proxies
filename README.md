# SyndProxy validated proxy pool

## Current pool

- Alive now: 503
- Gold now: 419
- HTTP: 82 alive / 62 gold
- HTTPS: 72 alive / 27 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 177 alive / 169 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47127
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
