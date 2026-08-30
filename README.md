# SyndProxy validated proxy pool

## Current pool

- Alive now: 623
- Gold now: 482
- HTTP: 139 alive / 100 gold
- HTTPS: 117 alive / 45 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 198 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44936
- Ever gold: 1420

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
