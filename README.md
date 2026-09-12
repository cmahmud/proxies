# SyndProxy validated proxy pool

## Current pool

- Alive now: 533
- Gold now: 423
- HTTP: 117 alive / 79 gold
- HTTPS: 43 alive / 21 gold
- SOCKS4: 184 alive / 159 gold
- SOCKS5: 189 alive / 164 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49474
- Ever gold: 1584

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
