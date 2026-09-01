# SyndProxy validated proxy pool

## Current pool

- Alive now: 503
- Gold now: 418
- HTTP: 87 alive / 63 gold
- HTTPS: 71 alive / 27 gold
- SOCKS4: 164 alive / 159 gold
- SOCKS5: 181 alive / 169 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47162
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
