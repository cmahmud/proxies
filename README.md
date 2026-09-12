# SyndProxy validated proxy pool

## Current pool

- Alive now: 429
- Gold now: 344
- HTTP: 90 alive / 64 gold
- HTTPS: 39 alive / 17 gold
- SOCKS4: 143 alive / 121 gold
- SOCKS5: 157 alive / 142 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49550
- Ever gold: 1586

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
