# SyndProxy validated proxy pool

## Current pool

- Alive now: 464
- Gold now: 377
- HTTP: 86 alive / 65 gold
- HTTPS: 44 alive / 22 gold
- SOCKS4: 148 alive / 120 gold
- SOCKS5: 186 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48735
- Ever gold: 1564

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
