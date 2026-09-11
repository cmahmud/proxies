# SyndProxy validated proxy pool

## Current pool

- Alive now: 406
- Gold now: 347
- HTTP: 98 alive / 72 gold
- HTTPS: 45 alive / 20 gold
- SOCKS4: 87 alive / 84 gold
- SOCKS5: 176 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48686
- Ever gold: 1564

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
