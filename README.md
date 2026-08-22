# SyndProxy private pool

## Current pool

- Alive now: 982
- Gold now: 395
- HTTP: 346 alive / 92 gold
- HTTPS: 185 alive / 25 gold
- SOCKS4: 227 alive / 147 gold
- SOCKS5: 224 alive / 131 gold

## Historical pool

- Discovered: 165831
- Ever alive: 32352
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
