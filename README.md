# SyndProxy validated proxy pool

## Current pool

- Alive now: 518
- Gold now: 408
- HTTP: 87 alive / 60 gold
- HTTPS: 59 alive / 16 gold
- SOCKS4: 181 alive / 160 gold
- SOCKS5: 191 alive / 172 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36326
- Ever gold: 1272

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
