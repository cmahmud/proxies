# SyndProxy validated proxy pool

## Current pool

- Alive now: 628
- Gold now: 453
- HTTP: 131 alive / 86 gold
- HTTPS: 136 alive / 33 gold
- SOCKS4: 174 alive / 160 gold
- SOCKS5: 187 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46847
- Ever gold: 1452

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
