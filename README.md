# SyndProxy validated proxy pool

## Current pool

- Alive now: 490
- Gold now: 383
- HTTP: 95 alive / 67 gold
- HTTPS: 45 alive / 19 gold
- SOCKS4: 159 alive / 125 gold
- SOCKS5: 191 alive / 172 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48744
- Ever gold: 1564

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
