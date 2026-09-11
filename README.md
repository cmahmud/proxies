# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 439
- HTTP: 104 alive / 78 gold
- HTTPS: 48 alive / 28 gold
- SOCKS4: 185 alive / 162 gold
- SOCKS5: 187 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49167
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
