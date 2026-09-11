# SyndProxy validated proxy pool

## Current pool

- Alive now: 465
- Gold now: 370
- HTTP: 95 alive / 69 gold
- HTTPS: 47 alive / 23 gold
- SOCKS4: 134 alive / 109 gold
- SOCKS5: 189 alive / 169 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48722
- Ever gold: 1564

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
