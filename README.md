# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 407
- HTTP: 84 alive / 59 gold
- HTTPS: 66 alive / 16 gold
- SOCKS4: 173 alive / 160 gold
- SOCKS5: 194 alive / 172 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36319
- Ever gold: 1272

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
