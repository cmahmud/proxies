# SyndProxy private pool

## Current pool

- Alive now: 833
- Gold now: 392
- HTTP: 245 alive / 86 gold
- HTTPS: 160 alive / 20 gold
- SOCKS4: 193 alive / 131 gold
- SOCKS5: 235 alive / 155 gold

## Historical pool

- Discovered: 151681
- Ever alive: 27674
- Ever gold: 1102

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
