# SyndProxy validated proxy pool

## Current pool

- Alive now: 521
- Gold now: 450
- HTTP: 108 alive / 86 gold
- HTTPS: 52 alive / 30 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 184 alive / 172 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49187
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
