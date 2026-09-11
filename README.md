# SyndProxy validated proxy pool

## Current pool

- Alive now: 510
- Gold now: 448
- HTTP: 113 alive / 88 gold
- HTTPS: 44 alive / 27 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 182 alive / 172 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49240
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
