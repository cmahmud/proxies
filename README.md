# SyndProxy validated proxy pool

## Current pool

- Alive now: 457
- Gold now: 372
- HTTP: 94 alive / 59 gold
- HTTPS: 30 alive / 8 gold
- SOCKS4: 159 alive / 151 gold
- SOCKS5: 174 alive / 154 gold

## Historical pool

- Discovered: 174309
- Ever alive: 33083
- Ever gold: 1225

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
