# SyndProxy validated proxy pool

## Current pool

- Alive now: 659
- Gold now: 488
- HTTP: 160 alive / 102 gold
- HTTPS: 128 alive / 43 gold
- SOCKS4: 172 alive / 163 gold
- SOCKS5: 199 alive / 180 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44984
- Ever gold: 1421

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
