# SyndProxy private pool

## Current pool

- Alive now: 1106
- Gold now: 417
- HTTP: 466 alive / 90 gold
- HTTPS: 170 alive / 25 gold
- SOCKS4: 225 alive / 142 gold
- SOCKS5: 245 alive / 160 gold

## Historical pool

- Discovered: 155807
- Ever alive: 29419
- Ever gold: 1126

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
