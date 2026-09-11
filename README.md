# SyndProxy validated proxy pool

## Current pool

- Alive now: 532
- Gold now: 437
- HTTP: 105 alive / 78 gold
- HTTPS: 56 alive / 26 gold
- SOCKS4: 188 alive / 163 gold
- SOCKS5: 183 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49136
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
