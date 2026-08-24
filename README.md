# SyndProxy validated proxy pool

## Current pool

- Alive now: 566
- Gold now: 438
- HTTP: 129 alive / 82 gold
- HTTPS: 77 alive / 23 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 189 alive / 172 gold

## Historical pool

- Discovered: 181494
- Ever alive: 33964
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
