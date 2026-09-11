# SyndProxy validated proxy pool

## Current pool

- Alive now: 543
- Gold now: 437
- HTTP: 111 alive / 74 gold
- HTTPS: 59 alive / 28 gold
- SOCKS4: 194 alive / 170 gold
- SOCKS5: 179 alive / 165 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49098
- Ever gold: 1573

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
