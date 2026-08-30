# SyndProxy validated proxy pool

## Current pool

- Alive now: 608
- Gold now: 462
- HTTP: 130 alive / 94 gold
- HTTPS: 113 alive / 37 gold
- SOCKS4: 166 alive / 159 gold
- SOCKS5: 199 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44821
- Ever gold: 1414

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
