# SyndProxy validated proxy pool

## Current pool

- Alive now: 629
- Gold now: 430
- HTTP: 119 alive / 78 gold
- HTTPS: 143 alive / 24 gold
- SOCKS4: 168 alive / 160 gold
- SOCKS5: 199 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42402
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
