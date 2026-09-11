# SyndProxy validated proxy pool

## Current pool

- Alive now: 488
- Gold now: 377
- HTTP: 92 alive / 66 gold
- HTTPS: 48 alive / 25 gold
- SOCKS4: 157 alive / 115 gold
- SOCKS5: 191 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48729
- Ever gold: 1564

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
