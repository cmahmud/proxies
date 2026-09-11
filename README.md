# SyndProxy validated proxy pool

## Current pool

- Alive now: 534
- Gold now: 430
- HTTP: 96 alive / 74 gold
- HTTPS: 59 alive / 26 gold
- SOCKS4: 195 alive / 169 gold
- SOCKS5: 184 alive / 161 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49089
- Ever gold: 1573

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
