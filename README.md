# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 446
- HTTP: 113 alive / 80 gold
- HTTPS: 47 alive / 30 gold
- SOCKS4: 171 alive / 160 gold
- SOCKS5: 188 alive / 176 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49214
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
