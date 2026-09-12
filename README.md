# SyndProxy validated proxy pool

## Current pool

- Alive now: 523
- Gold now: 455
- HTTP: 123 alive / 91 gold
- HTTPS: 51 alive / 32 gold
- SOCKS4: 171 alive / 160 gold
- SOCKS5: 178 alive / 172 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49282
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
