# SyndProxy validated proxy pool

## Current pool

- Alive now: 520
- Gold now: 449
- HTTP: 114 alive / 84 gold
- HTTPS: 49 alive / 28 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 188 alive / 176 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49237
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
