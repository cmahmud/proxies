# SyndProxy validated proxy pool

## Current pool

- Alive now: 538
- Gold now: 422
- HTTP: 96 alive / 65 gold
- HTTPS: 86 alive / 25 gold
- SOCKS4: 166 alive / 160 gold
- SOCKS5: 190 alive / 172 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35647
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
