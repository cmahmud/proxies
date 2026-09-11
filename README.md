# SyndProxy validated proxy pool

## Current pool

- Alive now: 533
- Gold now: 424
- HTTP: 95 alive / 72 gold
- HTTPS: 58 alive / 26 gold
- SOCKS4: 199 alive / 167 gold
- SOCKS5: 181 alive / 159 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49076
- Ever gold: 1571

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
