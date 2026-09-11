# SyndProxy validated proxy pool

## Current pool

- Alive now: 500
- Gold now: 422
- HTTP: 102 alive / 74 gold
- HTTPS: 35 alive / 16 gold
- SOCKS4: 184 alive / 162 gold
- SOCKS5: 179 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48974
- Ever gold: 1569

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
