# SyndProxy validated proxy pool

## Current pool

- Alive now: 562
- Gold now: 463
- HTTP: 133 alive / 96 gold
- HTTPS: 64 alive / 33 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 190 alive / 172 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49340
- Ever gold: 1578

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
