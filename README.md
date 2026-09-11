# SyndProxy validated proxy pool

## Current pool

- Alive now: 469
- Gold now: 369
- HTTP: 97 alive / 69 gold
- HTTPS: 47 alive / 22 gold
- SOCKS4: 134 alive / 109 gold
- SOCKS5: 191 alive / 169 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48721
- Ever gold: 1564

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
