# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 431
- HTTP: 104 alive / 74 gold
- HTTPS: 55 alive / 26 gold
- SOCKS4: 184 alive / 163 gold
- SOCKS5: 181 alive / 168 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49131
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
