# SyndProxy validated proxy pool

## Current pool

- Alive now: 488
- Gold now: 403
- HTTP: 99 alive / 65 gold
- HTTPS: 31 alive / 20 gold
- SOCKS4: 167 alive / 146 gold
- SOCKS5: 191 alive / 172 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48788
- Ever gold: 1567

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
