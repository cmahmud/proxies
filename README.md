# SyndProxy validated proxy pool

## Current pool

- Alive now: 629
- Gold now: 453
- HTTP: 128 alive / 85 gold
- HTTPS: 136 alive / 33 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 188 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46853
- Ever gold: 1452

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
