# SyndProxy validated proxy pool

## Current pool

- Alive now: 507
- Gold now: 411
- HTTP: 86 alive / 65 gold
- HTTPS: 58 alive / 17 gold
- SOCKS4: 172 alive / 159 gold
- SOCKS5: 191 alive / 170 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36380
- Ever gold: 1273

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
