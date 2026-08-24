# SyndProxy validated proxy pool

## Current pool

- Alive now: 549
- Gold now: 387
- HTTP: 134 alive / 56 gold
- HTTPS: 41 alive / 12 gold
- SOCKS4: 175 alive / 156 gold
- SOCKS5: 199 alive / 163 gold

## Historical pool

- Discovered: 178697
- Ever alive: 33377
- Ever gold: 1235

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
