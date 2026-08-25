# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 411
- HTTP: 89 alive / 62 gold
- HTTPS: 56 alive / 17 gold
- SOCKS4: 181 alive / 161 gold
- SOCKS5: 191 alive / 171 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36338
- Ever gold: 1272

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
