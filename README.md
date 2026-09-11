# SyndProxy validated proxy pool

## Current pool

- Alive now: 463
- Gold now: 361
- HTTP: 97 alive / 68 gold
- HTTPS: 55 alive / 23 gold
- SOCKS4: 124 alive / 101 gold
- SOCKS5: 187 alive / 169 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48713
- Ever gold: 1564

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
