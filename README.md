# SyndProxy private pool

## Current pool

- Alive now: 696
- Gold now: 391
- HTTP: 171 alive / 74 gold
- HTTPS: 106 alive / 19 gold
- SOCKS4: 204 alive / 143 gold
- SOCKS5: 215 alive / 155 gold

## Historical pool

- Discovered: 145572
- Ever alive: 25520
- Ever gold: 1063

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
