# SyndProxy validated proxy pool

## Current pool

- Alive now: 526
- Gold now: 435
- HTTP: 104 alive / 78 gold
- HTTPS: 57 alive / 27 gold
- SOCKS4: 187 alive / 168 gold
- SOCKS5: 178 alive / 162 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49092
- Ever gold: 1573

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
