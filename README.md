# SyndProxy validated proxy pool

## Current pool

- Alive now: 539
- Gold now: 385
- HTTP: 120 alive / 53 gold
- HTTPS: 50 alive / 10 gold
- SOCKS4: 173 alive / 156 gold
- SOCKS5: 196 alive / 166 gold

## Historical pool

- Discovered: 178697
- Ever alive: 33386
- Ever gold: 1235

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
