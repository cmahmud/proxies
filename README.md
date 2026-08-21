# SyndProxy private pool

## Current pool

- Alive now: 918
- Gold now: 422
- HTTP: 293 alive / 105 gold
- HTTPS: 169 alive / 35 gold
- SOCKS4: 218 alive / 137 gold
- SOCKS5: 238 alive / 145 gold

## Historical pool

- Discovered: 160257
- Ever alive: 30703
- Ever gold: 1146

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
