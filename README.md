# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 409
- HTTP: 84 alive / 61 gold
- HTTPS: 67 alive / 16 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 191 alive / 171 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36336
- Ever gold: 1272

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
