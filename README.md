# SyndProxy validated proxy pool

## Current pool

- Alive now: 629
- Gold now: 470
- HTTP: 131 alive / 95 gold
- HTTPS: 123 alive / 39 gold
- SOCKS4: 178 alive / 160 gold
- SOCKS5: 197 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46367
- Ever gold: 1444

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
