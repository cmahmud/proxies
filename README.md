# SyndProxy private pool

## Current pool

- Alive now: 713
- Gold now: 395
- HTTP: 186 alive / 72 gold
- HTTPS: 118 alive / 19 gold
- SOCKS4: 199 alive / 149 gold
- SOCKS5: 210 alive / 155 gold

## Historical pool

- Discovered: 147183
- Ever alive: 25814
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
