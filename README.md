# SyndProxy validated proxy pool

## Current pool

- Alive now: 704
- Gold now: 470
- HTTP: 175 alive / 97 gold
- HTTPS: 122 alive / 35 gold
- SOCKS4: 178 alive / 162 gold
- SOCKS5: 229 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45295
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
