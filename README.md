# SyndProxy validated proxy pool

## Current pool

- Alive now: 527
- Gold now: 444
- HTTP: 119 alive / 89 gold
- HTTPS: 54 alive / 29 gold
- SOCKS4: 173 alive / 159 gold
- SOCKS5: 181 alive / 167 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49304
- Ever gold: 1576

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
