# SyndProxy validated proxy pool

## Current pool

- Alive now: 521
- Gold now: 446
- HTTP: 100 alive / 83 gold
- HTTPS: 51 alive / 31 gold
- SOCKS4: 178 alive / 161 gold
- SOCKS5: 192 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49195
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
