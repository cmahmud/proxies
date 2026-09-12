# SyndProxy validated proxy pool

## Current pool

- Alive now: 526
- Gold now: 445
- HTTP: 120 alive / 85 gold
- HTTPS: 46 alive / 27 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 184 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49277
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
