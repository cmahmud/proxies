# SyndProxy validated proxy pool

## Current pool

- Alive now: 520
- Gold now: 391
- HTTP: 116 alive / 53 gold
- HTTPS: 52 alive / 14 gold
- SOCKS4: 171 alive / 156 gold
- SOCKS5: 181 alive / 168 gold

## Historical pool

- Discovered: 180692
- Ever alive: 33616
- Ever gold: 1243

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
