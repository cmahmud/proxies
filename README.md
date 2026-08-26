# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 403
- HTTP: 111 alive / 67 gold
- HTTPS: 53 alive / 16 gold
- SOCKS4: 171 alive / 156 gold
- SOCKS5: 182 alive / 164 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38942
- Ever gold: 1295

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
