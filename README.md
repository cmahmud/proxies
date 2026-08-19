# SyndProxy private pool

## Current pool

- Alive now: 1011
- Gold now: 520
- HTTP: 350 alive / 150 gold
- HTTPS: 253 alive / 95 gold
- SOCKS4: 196 alive / 133 gold
- SOCKS5: 212 alive / 142 gold

## Historical pool

- Discovered: 127357
- Ever alive: 19895
- Ever gold: 803

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
