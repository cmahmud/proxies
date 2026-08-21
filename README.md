# SyndProxy private pool

## Current pool

- Alive now: 828
- Gold now: 396
- HTTP: 245 alive / 88 gold
- HTTPS: 157 alive / 21 gold
- SOCKS4: 194 alive / 132 gold
- SOCKS5: 232 alive / 155 gold

## Historical pool

- Discovered: 151681
- Ever alive: 27674
- Ever gold: 1102

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
