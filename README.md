# SyndProxy validated proxy pool

## Current pool

- Alive now: 490
- Gold now: 379
- HTTP: 109 alive / 61 gold
- HTTPS: 55 alive / 18 gold
- SOCKS4: 154 alive / 146 gold
- SOCKS5: 172 alive / 154 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38927
- Ever gold: 1294

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
