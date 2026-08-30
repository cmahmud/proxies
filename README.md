# SyndProxy validated proxy pool

## Current pool

- Alive now: 537
- Gold now: 443
- HTTP: 120 alive / 86 gold
- HTTPS: 71 alive / 38 gold
- SOCKS4: 163 alive / 158 gold
- SOCKS5: 183 alive / 161 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44101
- Ever gold: 1397

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
