# SyndProxy validated proxy pool

## Current pool

- Alive now: 411
- Gold now: 350
- HTTP: 105 alive / 77 gold
- HTTPS: 48 alive / 25 gold
- SOCKS4: 80 alive / 76 gold
- SOCKS5: 178 alive / 172 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48677
- Ever gold: 1564

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
