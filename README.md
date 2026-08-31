# SyndProxy validated proxy pool

## Current pool

- Alive now: 697
- Gold now: 472
- HTTP: 184 alive / 97 gold
- HTTPS: 112 alive / 38 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 229 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45292
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
