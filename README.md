# SyndProxy validated proxy pool

## Current pool

- Alive now: 533
- Gold now: 423
- HTTP: 94 alive / 69 gold
- HTTPS: 68 alive / 25 gold
- SOCKS4: 187 alive / 165 gold
- SOCKS5: 184 alive / 164 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49061
- Ever gold: 1570

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
