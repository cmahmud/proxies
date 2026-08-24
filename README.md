# SyndProxy validated proxy pool

## Current pool

- Alive now: 577
- Gold now: 429
- HTTP: 129 alive / 75 gold
- HTTPS: 86 alive / 24 gold
- SOCKS4: 175 alive / 159 gold
- SOCKS5: 187 alive / 171 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34628
- Ever gold: 1256

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
