# SyndProxy validated proxy pool

## Current pool

- Alive now: 507
- Gold now: 447
- HTTP: 110 alive / 86 gold
- HTTPS: 44 alive / 27 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 184 alive / 173 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49239
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
