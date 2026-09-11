# SyndProxy validated proxy pool

## Current pool

- Alive now: 439
- Gold now: 354
- HTTP: 110 alive / 72 gold
- HTTPS: 54 alive / 20 gold
- SOCKS4: 97 alive / 92 gold
- SOCKS5: 178 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48699
- Ever gold: 1564

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
