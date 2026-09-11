# SyndProxy validated proxy pool

## Current pool

- Alive now: 400
- Gold now: 339
- HTTP: 100 alive / 73 gold
- HTTPS: 43 alive / 21 gold
- SOCKS4: 79 alive / 76 gold
- SOCKS5: 178 alive / 169 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48679
- Ever gold: 1564

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
