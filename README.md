# SyndProxy validated proxy pool

## Current pool

- Alive now: 510
- Gold now: 442
- HTTP: 102 alive / 81 gold
- HTTPS: 51 alive / 27 gold
- SOCKS4: 172 alive / 164 gold
- SOCKS5: 185 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49178
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
