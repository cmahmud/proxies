# SyndProxy validated proxy pool

## Current pool

- Alive now: 568
- Gold now: 468
- HTTP: 139 alive / 99 gold
- HTTPS: 61 alive / 37 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 191 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49373
- Ever gold: 1579

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
