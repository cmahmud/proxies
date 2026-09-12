# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 422
- HTTP: 106 alive / 77 gold
- HTTPS: 44 alive / 21 gold
- SOCKS4: 180 alive / 158 gold
- SOCKS5: 184 alive / 166 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49469
- Ever gold: 1584

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
