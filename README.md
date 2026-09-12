# SyndProxy validated proxy pool

## Current pool

- Alive now: 512
- Gold now: 423
- HTTP: 106 alive / 82 gold
- HTTPS: 41 alive / 22 gold
- SOCKS4: 178 alive / 158 gold
- SOCKS5: 187 alive / 161 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49470
- Ever gold: 1584

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
