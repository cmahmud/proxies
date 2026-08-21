# SyndProxy private pool

## Current pool

- Alive now: 860
- Gold now: 409
- HTTP: 262 alive / 94 gold
- HTTPS: 136 alive / 24 gold
- SOCKS4: 222 alive / 142 gold
- SOCKS5: 240 alive / 149 gold

## Historical pool

- Discovered: 155807
- Ever alive: 29407
- Ever gold: 1126

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
