# SyndProxy validated proxy pool

## Current pool

- Alive now: 628
- Gold now: 454
- HTTP: 129 alive / 87 gold
- HTTPS: 135 alive / 32 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 187 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46853
- Ever gold: 1452

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
