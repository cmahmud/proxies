# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 423
- HTTP: 108 alive / 79 gold
- HTTPS: 41 alive / 21 gold
- SOCKS4: 176 alive / 158 gold
- SOCKS5: 189 alive / 165 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49469
- Ever gold: 1584

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
