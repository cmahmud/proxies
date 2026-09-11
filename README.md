# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 434
- HTTP: 104 alive / 75 gold
- HTTPS: 50 alive / 28 gold
- SOCKS4: 186 alive / 163 gold
- SOCKS5: 184 alive / 168 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49148
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
