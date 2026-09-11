# SyndProxy validated proxy pool

## Current pool

- Alive now: 526
- Gold now: 438
- HTTP: 95 alive / 77 gold
- HTTPS: 54 alive / 28 gold
- SOCKS4: 192 alive / 164 gold
- SOCKS5: 185 alive / 169 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49127
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
