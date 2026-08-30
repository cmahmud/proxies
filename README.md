# SyndProxy validated proxy pool

## Current pool

- Alive now: 540
- Gold now: 439
- HTTP: 108 alive / 82 gold
- HTTPS: 62 alive / 30 gold
- SOCKS4: 171 alive / 159 gold
- SOCKS5: 199 alive / 168 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44576
- Ever gold: 1407

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
