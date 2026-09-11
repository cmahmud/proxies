# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 448
- HTTP: 122 alive / 88 gold
- HTTPS: 42 alive / 29 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 184 alive / 169 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49262
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
