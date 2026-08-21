# SyndProxy private pool

## Current pool

- Alive now: 1112
- Gold now: 446
- HTTP: 350 alive / 96 gold
- HTTPS: 259 alive / 32 gold
- SOCKS4: 246 alive / 163 gold
- SOCKS5: 257 alive / 155 gold

## Historical pool

- Discovered: 159260
- Ever alive: 30261
- Ever gold: 1144

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
