# SyndProxy validated proxy pool

## Current pool

- Alive now: 543
- Gold now: 444
- HTTP: 123 alive / 87 gold
- HTTPS: 57 alive / 26 gold
- SOCKS4: 180 alive / 160 gold
- SOCKS5: 183 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49263
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
