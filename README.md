# SyndProxy validated proxy pool

## Current pool

- Alive now: 533
- Gold now: 447
- HTTP: 125 alive / 89 gold
- HTTPS: 51 alive / 29 gold
- SOCKS4: 174 alive / 160 gold
- SOCKS5: 183 alive / 169 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49255
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
