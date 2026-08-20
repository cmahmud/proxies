# SyndProxy private pool

## Current pool

- Alive now: 718
- Gold now: 387
- HTTP: 177 alive / 69 gold
- HTTPS: 112 alive / 17 gold
- SOCKS4: 212 alive / 146 gold
- SOCKS5: 217 alive / 155 gold

## Historical pool

- Discovered: 146604
- Ever alive: 25692
- Ever gold: 1071

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
