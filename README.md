# SyndProxy validated proxy pool

## Current pool

- Alive now: 427
- Gold now: 345
- HTTP: 89 alive / 64 gold
- HTTPS: 37 alive / 17 gold
- SOCKS4: 142 alive / 121 gold
- SOCKS5: 159 alive / 143 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49551
- Ever gold: 1586

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
