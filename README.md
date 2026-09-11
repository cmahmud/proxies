# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 447
- HTTP: 109 alive / 86 gold
- HTTPS: 44 alive / 27 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 188 alive / 173 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49232
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
