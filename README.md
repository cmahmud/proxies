# SyndProxy validated proxy pool

## Current pool

- Alive now: 527
- Gold now: 438
- HTTP: 103 alive / 78 gold
- HTTPS: 54 alive / 27 gold
- SOCKS4: 186 alive / 163 gold
- SOCKS5: 184 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49140
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
