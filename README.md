# SyndProxy validated proxy pool

## Current pool

- Alive now: 536
- Gold now: 376
- HTTP: 200 alive / 90 gold
- HTTPS: 41 alive / 32 gold
- SOCKS4: 96 alive / 76 gold
- SOCKS5: 199 alive / 178 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48631
- Ever gold: 1562

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
