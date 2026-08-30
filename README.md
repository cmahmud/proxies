# SyndProxy validated proxy pool

## Current pool

- Alive now: 565
- Gold now: 442
- HTTP: 128 alive / 86 gold
- HTTPS: 73 alive / 32 gold
- SOCKS4: 162 alive / 158 gold
- SOCKS5: 202 alive / 166 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44157
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
