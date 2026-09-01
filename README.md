# SyndProxy validated proxy pool

## Current pool

- Alive now: 639
- Gold now: 463
- HTTP: 141 alive / 92 gold
- HTTPS: 130 alive / 35 gold
- SOCKS4: 176 alive / 160 gold
- SOCKS5: 192 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46686
- Ever gold: 1446

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
