# SyndProxy validated proxy pool

## Current pool

- Alive now: 473
- Gold now: 403
- HTTP: 90 alive / 64 gold
- HTTPS: 36 alive / 20 gold
- SOCKS4: 161 alive / 147 gold
- SOCKS5: 186 alive / 172 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48802
- Ever gold: 1567

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
