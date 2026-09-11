# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 445
- HTTP: 116 alive / 87 gold
- HTTPS: 45 alive / 30 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 184 alive / 168 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49248
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
