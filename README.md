# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 444
- HTTP: 121 alive / 85 gold
- HTTPS: 47 alive / 27 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 183 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49276
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
