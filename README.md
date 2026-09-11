# SyndProxy validated proxy pool

## Current pool

- Alive now: 512
- Gold now: 444
- HTTP: 113 alive / 89 gold
- HTTPS: 44 alive / 26 gold
- SOCKS4: 173 alive / 160 gold
- SOCKS5: 182 alive / 169 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49244
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
