# SyndProxy validated proxy pool

## Current pool

- Alive now: 549
- Gold now: 440
- HTTP: 114 alive / 83 gold
- HTTPS: 65 alive / 30 gold
- SOCKS4: 171 alive / 159 gold
- SOCKS5: 199 alive / 168 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44579
- Ever gold: 1407

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
