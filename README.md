# SyndProxy private pool

## Current pool

- Alive now: 803
- Gold now: 318
- HTTP: 225 alive / 61 gold
- HTTPS: 175 alive / 8 gold
- SOCKS4: 209 alive / 118 gold
- SOCKS5: 194 alive / 131 gold

## Historical pool

- Discovered: 129264
- Ever alive: 20142
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
