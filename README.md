# SyndProxy validated proxy pool

## Current pool

- Alive now: 427
- Gold now: 353
- HTTP: 81 alive / 71 gold
- HTTPS: 47 alive / 30 gold
- SOCKS4: 105 alive / 77 gold
- SOCKS5: 194 alive / 175 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48586
- Ever gold: 1557

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
