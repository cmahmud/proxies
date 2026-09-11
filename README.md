# SyndProxy validated proxy pool

## Current pool

- Alive now: 534
- Gold now: 427
- HTTP: 99 alive / 73 gold
- HTTPS: 66 alive / 25 gold
- SOCKS4: 184 alive / 166 gold
- SOCKS5: 185 alive / 163 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49060
- Ever gold: 1570

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
