# SyndProxy validated proxy pool

## Current pool

- Alive now: 568
- Gold now: 469
- HTTP: 134 alive / 94 gold
- HTTPS: 65 alive / 37 gold
- SOCKS4: 179 alive / 162 gold
- SOCKS5: 190 alive / 176 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49377
- Ever gold: 1579

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
