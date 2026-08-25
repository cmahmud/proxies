# SyndProxy validated proxy pool

## Current pool

- Alive now: 516
- Gold now: 407
- HTTP: 85 alive / 59 gold
- HTTPS: 61 alive / 16 gold
- SOCKS4: 175 alive / 160 gold
- SOCKS5: 195 alive / 172 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36321
- Ever gold: 1272

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
