# SyndProxy validated proxy pool

## Current pool

- Alive now: 643
- Gold now: 482
- HTTP: 156 alive / 100 gold
- HTTPS: 122 alive / 43 gold
- SOCKS4: 168 alive / 161 gold
- SOCKS5: 197 alive / 178 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44945
- Ever gold: 1420

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
