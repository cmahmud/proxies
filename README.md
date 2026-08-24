# SyndProxy validated proxy pool

## Current pool

- Alive now: 549
- Gold now: 386
- HTTP: 133 alive / 54 gold
- HTTPS: 43 alive / 12 gold
- SOCKS4: 176 alive / 156 gold
- SOCKS5: 197 alive / 164 gold

## Historical pool

- Discovered: 178697
- Ever alive: 33374
- Ever gold: 1235

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
