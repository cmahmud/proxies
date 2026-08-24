# SyndProxy validated proxy pool

## Current pool

- Alive now: 557
- Gold now: 392
- HTTP: 109 alive / 55 gold
- HTTPS: 64 alive / 15 gold
- SOCKS4: 185 alive / 156 gold
- SOCKS5: 199 alive / 166 gold

## Historical pool

- Discovered: 178697
- Ever alive: 33385
- Ever gold: 1235

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
