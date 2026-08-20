# SyndProxy private pool

## Current pool

- Alive now: 709
- Gold now: 388
- HTTP: 174 alive / 69 gold
- HTTPS: 110 alive / 17 gold
- SOCKS4: 211 alive / 147 gold
- SOCKS5: 214 alive / 155 gold

## Historical pool

- Discovered: 146604
- Ever alive: 25692
- Ever gold: 1071

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
