# SyndProxy validated proxy pool

## Current pool

- Alive now: 689
- Gold now: 455
- HTTP: 152 alive / 89 gold
- HTTPS: 121 alive / 31 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 241 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45321
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
