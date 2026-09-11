# SyndProxy validated proxy pool

## Current pool

- Alive now: 508
- Gold now: 421
- HTTP: 91 alive / 69 gold
- HTTPS: 52 alive / 24 gold
- SOCKS4: 189 alive / 167 gold
- SOCKS5: 176 alive / 161 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49039
- Ever gold: 1570

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
