# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 412
- HTTP: 86 alive / 57 gold
- HTTPS: 68 alive / 18 gold
- SOCKS4: 170 alive / 163 gold
- SOCKS5: 193 alive / 174 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36282
- Ever gold: 1270

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
