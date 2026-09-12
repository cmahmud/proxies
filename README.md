# SyndProxy validated proxy pool

## Current pool

- Alive now: 500
- Gold now: 414
- HTTP: 95 alive / 73 gold
- HTTPS: 46 alive / 18 gold
- SOCKS4: 178 alive / 158 gold
- SOCKS5: 181 alive / 165 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49463
- Ever gold: 1584

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
