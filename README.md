# SyndProxy validated proxy pool

## Current pool

- Alive now: 560
- Gold now: 463
- HTTP: 131 alive / 93 gold
- HTTPS: 57 alive / 28 gold
- SOCKS4: 179 alive / 165 gold
- SOCKS5: 193 alive / 177 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49424
- Ever gold: 1582

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
