# SyndProxy validated proxy pool

## Current pool

- Alive now: 549
- Gold now: 386
- HTTP: 117 alive / 54 gold
- HTTPS: 68 alive / 14 gold
- SOCKS4: 170 alive / 155 gold
- SOCKS5: 194 alive / 163 gold

## Historical pool

- Discovered: 178697
- Ever alive: 33381
- Ever gold: 1235

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
