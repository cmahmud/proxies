# SyndProxy private pool

## Current pool

- Alive now: 849
- Gold now: 351
- HTTP: 303 alive / 88 gold
- HTTPS: 137 alive / 22 gold
- SOCKS4: 197 alive / 115 gold
- SOCKS5: 212 alive / 126 gold

## Historical pool

- Discovered: 167412
- Ever alive: 32583
- Ever gold: 1190

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
