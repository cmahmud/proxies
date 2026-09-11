# SyndProxy validated proxy pool

## Current pool

- Alive now: 401
- Gold now: 346
- HTTP: 95 alive / 73 gold
- HTTPS: 44 alive / 20 gold
- SOCKS4: 85 alive / 82 gold
- SOCKS5: 177 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48685
- Ever gold: 1564

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
