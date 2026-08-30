# SyndProxy validated proxy pool

## Current pool

- Alive now: 571
- Gold now: 443
- HTTP: 131 alive / 91 gold
- HTTPS: 69 alive / 32 gold
- SOCKS4: 166 alive / 158 gold
- SOCKS5: 205 alive / 162 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44246
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
