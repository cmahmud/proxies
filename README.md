# SyndProxy private pool

## Current pool

- Alive now: 828
- Gold now: 285
- HTTP: 229 alive / 27 gold
- HTTPS: 137 alive / 5 gold
- SOCKS4: 242 alive / 143 gold
- SOCKS5: 220 alive / 110 gold

## Historical pool

- Discovered: 99552
- Ever alive: 12361
- Ever gold: 396

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
