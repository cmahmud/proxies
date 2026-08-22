# SyndProxy private pool

## Current pool

- Alive now: 981
- Gold now: 422
- HTTP: 272 alive / 89 gold
- HTTPS: 193 alive / 22 gold
- SOCKS4: 225 alive / 141 gold
- SOCKS5: 291 alive / 170 gold

## Historical pool

- Discovered: 164956
- Ever alive: 32223
- Ever gold: 1175

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
