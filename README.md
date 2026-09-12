# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 449
- HTTP: 116 alive / 90 gold
- HTTPS: 50 alive / 31 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 174 alive / 166 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49299
- Ever gold: 1576

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
