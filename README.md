# SyndProxy validated proxy pool

## Current pool

- Alive now: 722
- Gold now: 346
- HTTP: 178 alive / 81 gold
- HTTPS: 114 alive / 39 gold
- SOCKS4: 102 alive / 53 gold
- SOCKS5: 328 alive / 173 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48552
- Ever gold: 1543

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
