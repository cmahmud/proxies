# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 441
- HTTP: 104 alive / 83 gold
- HTTPS: 53 alive / 28 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 185 alive / 169 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49206
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
