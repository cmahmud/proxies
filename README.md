# SyndProxy validated proxy pool

## Current pool

- Alive now: 507
- Gold now: 439
- HTTP: 101 alive / 80 gold
- HTTPS: 52 alive / 26 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 184 alive / 172 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49180
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
