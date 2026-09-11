# SyndProxy validated proxy pool

## Current pool

- Alive now: 535
- Gold now: 425
- HTTP: 93 alive / 73 gold
- HTTPS: 60 alive / 26 gold
- SOCKS4: 200 alive / 167 gold
- SOCKS5: 182 alive / 159 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49076
- Ever gold: 1571

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
