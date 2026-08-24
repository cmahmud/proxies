# SyndProxy validated proxy pool

## Current pool

- Alive now: 533
- Gold now: 402
- HTTP: 118 alive / 65 gold
- HTTPS: 48 alive / 13 gold
- SOCKS4: 175 alive / 159 gold
- SOCKS5: 192 alive / 165 gold

## Historical pool

- Discovered: 177985
- Ever alive: 33328
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
