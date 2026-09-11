# SyndProxy validated proxy pool

## Current pool

- Alive now: 695
- Gold now: 344
- HTTP: 200 alive / 80 gold
- HTTPS: 122 alive / 39 gold
- SOCKS4: 100 alive / 53 gold
- SOCKS5: 273 alive / 172 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48541
- Ever gold: 1543

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
